use async_broadcast::Sender;
use tokio::task::JoinHandle;

use crate::errors::SummaResult;

#[derive(Clone, Debug)]
pub enum ControlMessage {
    Shutdown,
}

/// Holds `JoinHandle` together with its `shutdown_trigger`
#[derive(Debug)]
pub struct ThreadHandler<T> {
    join_handle: JoinHandle<T>,
    shutdown_trigger: Sender<ControlMessage>,
}

impl<T> ThreadHandler<T> {
    pub fn new(join_handle: JoinHandle<T>, shutdown_trigger: Sender<ControlMessage>) -> ThreadHandler<T> {
        ThreadHandler { join_handle, shutdown_trigger }
    }

    pub async fn stop(self) -> SummaResult<T> {
        self.shutdown_trigger.broadcast(ControlMessage::Shutdown).await?;
        Ok(self.join_handle.await?)
    }
}
