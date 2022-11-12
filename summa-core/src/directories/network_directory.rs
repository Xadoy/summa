use std::collections::HashMap;
use std::fmt::{Debug, Formatter};
use std::path::PathBuf;
use std::{io, ops::Range, path::Path, sync::Arc, usize};

use parking_lot::RwLock;
use tantivy::directory::DirectoryClone;
use tantivy::{
    directory::{error::OpenReadError, FileHandle, OwnedBytes},
    AsyncIoResult, Directory, HasLen,
};

use super::ExternalRequestGenerator;
use crate::directories::ExternalRequest;
use crate::errors::SummaResult;

pub struct NetworkDirectory<TExternalRequest: ExternalRequest> {
    file_lengths: Arc<RwLock<HashMap<PathBuf, u64>>>,
    external_request_generator: Box<dyn ExternalRequestGenerator<TExternalRequest>>,
}

impl<TExternalRequest: ExternalRequest> Debug for NetworkDirectory<TExternalRequest> {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        "NetworkDirectory".fmt(f)
    }
}

impl<TExternalRequest: ExternalRequest> NetworkDirectory<TExternalRequest> {
    pub fn open(
        external_request_generator: Box<dyn ExternalRequestGenerator<TExternalRequest>>,
        file_lengths: Arc<RwLock<HashMap<PathBuf, u64>>>,
    ) -> NetworkDirectory<TExternalRequest> {
        NetworkDirectory {
            file_lengths,
            external_request_generator,
        }
    }
}

impl<TExternalRequest: ExternalRequest + 'static> DirectoryClone for NetworkDirectory<TExternalRequest> {
    fn box_clone(&self) -> Box<dyn Directory> {
        Box::new(NetworkDirectory {
            file_lengths: self.file_lengths.clone(),
            external_request_generator: self.external_request_generator.box_clone(),
        })
    }
}

impl<TExternalRequest: ExternalRequest + 'static> Directory for NetworkDirectory<TExternalRequest> {
    fn get_file_handle(&self, file_name: &Path) -> Result<Arc<dyn FileHandle>, OpenReadError> {
        let file_name_str = file_name.to_string_lossy();
        Ok(Arc::new(NetworkFile::new(
            file_name_str.to_string(),
            self.file_lengths.read().get(file_name).cloned(),
            self.external_request_generator.box_clone(),
        )?))
    }

    fn exists(&self, path: &Path) -> Result<bool, OpenReadError> {
        Ok(self.get_file_handle(path)?.len() > 0)
    }

    fn atomic_read(&self, path: &Path) -> Result<Vec<u8>, OpenReadError> {
        let file_handle = self.get_file_handle(path)?;
        Ok(file_handle
            .read_bytes(0..file_handle.len())
            .map_err(|e| OpenReadError::wrap_io_error(e, path.to_path_buf()))?
            .to_vec())
    }

    super::read_only_directory!();
}

#[derive(Debug)]
struct NetworkFile<TExternalRequest: ExternalRequest> {
    file_name: String,
    file_length: Option<u64>,
    request_generator: Box<dyn ExternalRequestGenerator<TExternalRequest>>,
}

impl<TExternalRequest: ExternalRequest> NetworkFile<TExternalRequest> {
    pub fn new(
        file_name: String,
        file_length: Option<u64>,
        request_generator: Box<dyn ExternalRequestGenerator<TExternalRequest>>,
    ) -> Result<NetworkFile<TExternalRequest>, OpenReadError> {
        Ok(NetworkFile {
            file_name,
            file_length,
            request_generator,
        })
    }

    pub fn internal_length(&self) -> SummaResult<u64> {
        Ok(match self.file_length {
            Some(file_length) => file_length,
            None => {
                let external_response = self.request_generator.generate_length_request(&self.file_name)?.request()?;
                external_response
                    .headers
                    .iter()
                    .find_map(|header| {
                        if header.name == "content-length" {
                            Some(header.value.parse::<u64>().unwrap())
                        } else {
                            None
                        }
                    })
                    .unwrap()
            }
        })
    }
}

#[async_trait]
impl<TExternalRequest: ExternalRequest + Debug + 'static> FileHandle for NetworkFile<TExternalRequest> {
    fn read_bytes(&self, byte_range: Range<usize>) -> io::Result<OwnedBytes> {
        let request_response = self.request_generator.generate_range_request(&self.file_name, byte_range)?.request()?;
        Ok(OwnedBytes::new(request_response.data))
    }

    async fn read_bytes_async(&self, byte_range: Range<usize>) -> AsyncIoResult<OwnedBytes> {
        let request = self.request_generator.generate_range_request(&self.file_name, byte_range)?;
        let request_fut = request.request_async();
        Ok(OwnedBytes::new(request_fut.await?.data))
    }
}

impl<TExternalRequest: ExternalRequest> HasLen for NetworkFile<TExternalRequest> {
    fn len(&self) -> usize {
        self.internal_length().unwrap_or(0) as usize
    }
}
