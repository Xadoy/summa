use std::future::Future;

use async_broadcast::Receiver;
use futures_util::StreamExt;
use iroh_rpc_types::store::StoreAddr;
use summa_core::utils::thread_handler::ControlMessage;
use tracing::{info, info_span, instrument, Instrument};

use crate::errors::SummaServerResult;

const MAX_CHUNK_SIZE: u64 = 1024 * 1024;

#[derive(Clone)]
pub struct Store {
    config: crate::configs::store::Config,
    store: iroh_store::Store,
    rpc_addr: StoreAddr,
    content_loader: iroh_unixfs::content_loader::FullLoader,
}

impl Store {
    pub async fn new(config: crate::configs::store::Config, content_loader: iroh_unixfs::content_loader::FullLoader) -> SummaServerResult<Store> {
        let rpc_addr: StoreAddr = format!("irpc://{}", config.endpoint).parse()?;
        let iroh_store_config = iroh_store::Config::with_rpc_addr(config.path.clone(), rpc_addr.clone());
        let store = if config.path.exists() {
            info!(action = "open_store", path = ?config.path);
            iroh_store::Store::open(iroh_store_config).await?
        } else {
            info!(action = "create_store", path = ?config.path);
            tokio::fs::create_dir_all(&config.path).await?;
            iroh_store::Store::create(iroh_store_config).await?
        };

        Ok(Store {
            config,
            store,
            rpc_addr,
            content_loader,
        })
    }

    pub fn rpc_addr(&self) -> &StoreAddr {
        &self.rpc_addr
    }

    pub fn content_loader(&self) -> &iroh_unixfs::content_loader::FullLoader {
        &self.content_loader
    }

    #[instrument("lifecycle", skip_all)]
    pub async fn prepare_serving_future(&self, mut terminator: Receiver<ControlMessage>) -> SummaServerResult<impl Future<Output = SummaServerResult<()>>> {
        let rpc_addr = format!("irpc://{}", self.config.endpoint).parse()?;
        let store_task = tokio::spawn(iroh_store::rpc::new(rpc_addr, self.store.clone()));

        info!(action = "binded", endpoint = ?self.config.endpoint);
        Ok(async move {
            let signal_result = terminator.recv().await;
            info!(action = "sigterm_received", received = ?signal_result);
            store_task.abort();
            if let Err(e) = store_task.await {
                if !e.is_cancelled() {
                    info!(action = "terminated", error = ?e);
                    return Ok(());
                }
            }
            info!(action = "terminated");
            Ok(())
        }
        .instrument(info_span!(parent: None, "lifecycle")))
    }

    pub async fn put(&self, files: Vec<summa_core::components::ComponentFile>, delete_files: bool) -> SummaServerResult<String> {
        info!(files = ?files);
        let mut entries = vec![];
        for file in files.iter() {
            entries.push(iroh_unixfs::builder::Entry::File(
                iroh_unixfs::builder::FileBuilder::new()
                    .name(file.path().file_name().expect("should have name").to_string_lossy().to_string())
                    .chunker(iroh_unixfs::chunker::Chunker::Fixed(iroh_unixfs::chunker::Fixed {
                        chunk_size: self.config.default_chunk_size as usize,
                    }))
                    .content_reader(tokio::fs::File::open(file.path()).await?)
                    .build()
                    .await?,
            ))
        }
        let root_directory = iroh_unixfs::builder::Entry::Directory(iroh_unixfs::builder::Directory::basic("".to_string(), entries));
        let mut blocks = root_directory.encode().await?;

        let mut chunk = Vec::new();
        let mut chunk_size = 0u64;
        let mut cid = None;

        while let Some(block) = blocks.next().await {
            let block = block?;
            let block_size = block.data().len() as u64 + block.links().len() as u64 * 128;
            cid = Some(*block.cid());
            if chunk_size + block_size > MAX_CHUNK_SIZE {
                let store = self.store.clone();
                let current_chunk = std::mem::take(&mut chunk);
                tokio::task::spawn_blocking(move || store.put_many(current_chunk)).await??;
                chunk_size = 0;
            }
            chunk.push(block.into_parts());
            chunk_size += block_size;
        }
        let store = self.store.clone();
        tokio::task::spawn_blocking(move || store.put_many(chunk)).await??;

        if delete_files {
            for file in files.iter() {
                tokio::fs::remove_file(file.path()).await?;
            }
        }
        Ok(cid.expect("no files found").to_string())
    }
}
