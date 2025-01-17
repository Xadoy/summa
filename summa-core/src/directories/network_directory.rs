use std::fmt::{Debug, Formatter};
use std::{io, ops::Range, path::Path, sync::Arc, usize};

use tantivy::directory::DirectoryClone;
use tantivy::{
    directory::{error::OpenReadError, FileHandle, OwnedBytes},
    Directory, HasLen,
};

use super::ExternalRequestGenerator;
use crate::components::{DefaultTracker, Tracker, TrackerEvent};
use crate::directories::{ExternalRequest, Noop};
use crate::errors::ValidationError::InvalidHttpHeader;
use crate::errors::{SummaResult, ValidationError};

pub struct NetworkDirectory<TExternalRequest: ExternalRequest> {
    external_request_generator: Box<dyn ExternalRequestGenerator<TExternalRequest>>,
}

impl<TExternalRequest: ExternalRequest> Debug for NetworkDirectory<TExternalRequest> {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        "NetworkDirectory".fmt(f)
    }
}

impl<TExternalRequest: ExternalRequest> NetworkDirectory<TExternalRequest> {
    pub fn open(external_request_generator: Box<dyn ExternalRequestGenerator<TExternalRequest>>) -> NetworkDirectory<TExternalRequest> {
        NetworkDirectory { external_request_generator }
    }

    pub fn get_network_file_handle(&self, file_name: &Path) -> NetworkFile<TExternalRequest> {
        let file_name_str = file_name.to_string_lossy();
        NetworkFile::new(file_name_str.to_string(), self.external_request_generator.box_clone())
    }
}

impl<TExternalRequest: ExternalRequest + 'static> DirectoryClone for NetworkDirectory<TExternalRequest> {
    fn box_clone(&self) -> Box<dyn Directory> {
        Box::new(NetworkDirectory {
            external_request_generator: self.external_request_generator.box_clone(),
        })
    }
}

#[async_trait]
impl<TExternalRequest: ExternalRequest + 'static> Directory for NetworkDirectory<TExternalRequest> {
    fn get_file_handle(&self, file_name: &Path) -> Result<Arc<dyn FileHandle>, OpenReadError> {
        Ok(Arc::new(self.get_network_file_handle(file_name)))
    }

    fn exists(&self, path: &Path) -> Result<bool, OpenReadError> {
        Ok(self.get_file_handle(path)?.len() > 0)
    }

    fn atomic_read(&self, path: &Path) -> Result<Vec<u8>, OpenReadError> {
        let file_handle = self.get_network_file_handle(path);
        Ok(file_handle
            .do_read_bytes(None)
            .map_err(|e| OpenReadError::wrap_io_error(e, path.to_path_buf()))?
            .to_vec())
    }

    async fn atomic_read_async(&self, path: &Path) -> Result<Vec<u8>, OpenReadError> {
        let file_handle = self.get_network_file_handle(path);
        Ok(file_handle
            .do_read_bytes_async(None, DefaultTracker::default())
            .await
            .map_err(|e| OpenReadError::wrap_io_error(e, path.to_path_buf()))?
            .to_vec())
    }

    super::read_only_directory!();
}

#[derive(Debug)]
pub struct NetworkFile<TExternalRequest: ExternalRequest> {
    file_name: String,
    request_generator: Box<dyn ExternalRequestGenerator<TExternalRequest>>,
}

impl<TExternalRequest: ExternalRequest> NetworkFile<TExternalRequest> {
    pub fn new(file_name: String, request_generator: Box<dyn ExternalRequestGenerator<TExternalRequest>>) -> NetworkFile<TExternalRequest> {
        NetworkFile { file_name, request_generator }
    }

    pub fn file_name(&self) -> &str {
        &self.file_name
    }

    pub fn url(&self) -> io::Result<String> {
        Ok(self.request_generator.generate_length_request(&self.file_name)?.url().to_string())
    }

    fn do_read_bytes(&self, byte_range: Option<Range<usize>>) -> io::Result<OwnedBytes> {
        let request_response = self.request_generator.generate_range_request(&self.file_name, byte_range)?.request()?;
        Ok(OwnedBytes::new(request_response.data))
    }

    pub async fn do_read_bytes_async(&self, byte_range: Option<Range<usize>>, tracker: impl Tracker) -> io::Result<OwnedBytes> {
        let request = self.request_generator.generate_range_request(&self.file_name, byte_range)?;
        let url = request.url().to_string();
        tracker.send_event(TrackerEvent::start_reading_file(&url));
        let request_fut = request.request_async();
        tracker.send_event(TrackerEvent::finish_reading_file(&url));
        Ok(OwnedBytes::new(request_fut.await?.data))
    }

    pub fn internal_length(&self) -> SummaResult<u64> {
        let external_response = self.request_generator.generate_length_request(&self.file_name)?.request()?;
        Ok(external_response
            .headers
            .iter()
            .find_map(|header| {
                if header.name == "content-length" {
                    Some(
                        header
                            .value
                            .parse::<u64>()
                            .map_err(|_| InvalidHttpHeader(header.name.clone(), header.value.clone())),
                    )
                } else {
                    None
                }
            })
            .ok_or_else(|| ValidationError::MissingHeader("content_range".to_string()))??)
    }
}

#[async_trait]
impl<TExternalRequest: ExternalRequest + Debug + 'static> FileHandle for NetworkFile<TExternalRequest> {
    fn read_bytes(&self, byte_range: Range<usize>) -> io::Result<OwnedBytes> {
        self.do_read_bytes(Some(byte_range))
    }

    async fn read_bytes_async(&self, byte_range: Range<usize>) -> io::Result<OwnedBytes> {
        self.do_read_bytes_async(Some(byte_range), DefaultTracker::default()).await
    }
}

impl<TExternalRequest: ExternalRequest> HasLen for NetworkFile<TExternalRequest> {
    fn len(&self) -> usize {
        self.internal_length().unwrap_or_default() as usize
    }
}
