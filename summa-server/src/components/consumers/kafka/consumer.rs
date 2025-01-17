use std::str;
use std::sync::Arc;
use std::time::Duration;

use futures::StreamExt;
use opentelemetry::{global, Context, KeyValue};
use rdkafka::admin::{AdminClient, AdminOptions, AlterConfig, NewTopic, ResourceSpecifier, TopicReplication};
use rdkafka::config::{ClientConfig, FromClientConfig};
use rdkafka::consumer::{CommitMode, Consumer as KafkaConsumer, StreamConsumer as KafkaStreamConsumer, StreamConsumer};
use rdkafka::error::KafkaError;
use rdkafka::message::BorrowedMessage;
use rdkafka::util::Timeout;
use summa_core::utils::thread_handler::ThreadHandler;
use tokio::sync::Mutex;
use tracing::{info, info_span, instrument, warn, Instrument};

use super::status::{KafkaConsumingError, KafkaConsumingStatus};
use crate::errors::{Error, SummaServerResult};

enum ConsumingState {
    Enabled(ThreadHandler<SummaServerResult<StreamConsumer>>),
    Disabled(StreamConsumer),
}

impl std::fmt::Debug for ConsumingState {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        f.debug_struct("ConsumingState").finish()
    }
}

/// Manages consuming thread
#[derive(Clone, Debug)]
pub struct ConsumerThread {
    consumer_name: String,
    config: crate::configs::consumer::Config,
    kafka_producer_config: ClientConfig,
    consuming_state: Arc<Mutex<Option<ConsumingState>>>,
}

impl ConsumerThread {
    #[instrument]
    pub fn new(consumer_name: &str, config: &crate::configs::consumer::Config) -> SummaServerResult<ConsumerThread> {
        let mut kafka_consumer_config = ClientConfig::new();
        kafka_consumer_config
            .set("broker.address.ttl", "1000")
            .set("bootstrap.servers", config.bootstrap_servers.join(","))
            .set("group.id", &config.group_id)
            .set("enable.partition.eof", "false")
            .set("session.timeout.ms", config.session_timeout_ms.to_string())
            .set("max.poll.interval.ms", config.max_poll_interval_ms.to_string())
            .set("auto.offset.reset", "earliest")
            .set("allow.auto.create.topics", "true");

        let mut kafka_producer_config = ClientConfig::new();
        kafka_producer_config.set("bootstrap.servers", config.bootstrap_servers.join(","));

        let stream_consumer: KafkaStreamConsumer = kafka_consumer_config.create()?;
        stream_consumer.subscribe(&config.topics.iter().map(String::as_str).collect::<Vec<_>>())?;

        Ok(ConsumerThread {
            consumer_name: consumer_name.to_owned(),
            config: config.clone(),
            kafka_producer_config,
            consuming_state: Arc::new(Mutex::new(Some(ConsumingState::Disabled(stream_consumer)))),
        })
    }

    pub fn consumer_name(&self) -> &str {
        &self.consumer_name
    }

    #[instrument(skip_all, fields(consumer_name = ?self.consumer_name))]
    pub async fn start<TProcessor>(&self, processor: TProcessor)
    where
        TProcessor: Fn(Result<BorrowedMessage<'_>, KafkaError>) -> Result<KafkaConsumingStatus, KafkaConsumingError> + 'static + Send + Sync,
    {
        let mut consuming = self.consuming_state.lock().await;
        *consuming = match consuming.take() {
            Some(ConsumingState::Disabled(stream_consumer)) => {
                info!(action = "start");
                let (shutdown_trigger, mut shutdown_tripwire) = async_broadcast::broadcast(1);
                let consumer_name = self.consumer_name.clone();
                let context = Context::current();
                let stream_processor = {
                    async move {
                        let stream = stream_consumer.stream();
                        let meter = global::meter("summa");
                        let counter = meter.u64_counter("consume").with_description("Number of consumed events").init();
                        let mut terminatable_stream = stream.take_until(shutdown_tripwire.recv());
                        info!(action = "started");
                        loop {
                            match terminatable_stream.next().await {
                                Some(message) => {
                                    match processor(message) {
                                        Ok(_) => counter.add(
                                            &context,
                                            1,
                                            &[KeyValue::new("status", "ok"), KeyValue::new("consumer_name", consumer_name.clone())],
                                        ),
                                        Err(error) => {
                                            warn!(action = "error", error = ?error);
                                            counter.add(
                                                &context,
                                                1,
                                                &[KeyValue::new("status", "error"), KeyValue::new("consumer_name", consumer_name.clone())],
                                            );
                                        }
                                    };
                                }
                                None => {
                                    info!(action = "stopped");
                                    drop(terminatable_stream);
                                    break Ok(stream_consumer);
                                }
                            }
                        }
                    }
                }
                .instrument(info_span!(parent: None, "consumer", consumer_name = ?self.consumer_name));
                Some(ConsumingState::Enabled(ThreadHandler::new(tokio::spawn(stream_processor), shutdown_trigger)))
            }
            old => old,
        }
    }

    #[instrument(skip(self))]
    pub async fn stop(&self) -> SummaServerResult<()> {
        let mut consuming = self.consuming_state.lock().await;
        *consuming = match consuming.take() {
            Some(ConsumingState::Enabled(thread_handler)) => {
                info!(action = "stopping");
                Some(ConsumingState::Disabled(thread_handler.stop().await??))
            }
            old => old,
        };
        Ok(())
    }

    #[instrument(skip(self))]
    pub async fn commit(&self) -> SummaServerResult<()> {
        let mut consuming = self.consuming_state.lock().await;
        *consuming = match consuming.take() {
            Some(ConsumingState::Disabled(stream_consumer)) => {
                info!(action = "committing_consumer_state", position = ?stream_consumer.position());
                let stream_consumer = tokio::task::spawn_blocking(move || {
                    stream_consumer.commit_consumer_state(CommitMode::Sync)?;
                    Ok::<StreamConsumer, Error>(stream_consumer)
                })
                .await?;
                Some(ConsumingState::Disabled(stream_consumer?))
            }
            old => old,
        };
        Ok(())
    }

    #[instrument(skip(self))]
    async fn create_topics(&self) -> SummaServerResult<()> {
        let admin_client = AdminClient::from_config(&self.kafka_producer_config)?;
        let admin_options = AdminOptions::new().operation_timeout(Some(Timeout::Never));
        let new_topics: Vec<_> = self
            .config
            .topics
            .iter()
            .map(|topic_name| NewTopic::new(topic_name.as_str(), 1, TopicReplication::Fixed(1)))
            .collect();
        let alter_topics: Vec<_> = self
            .config
            .topics
            .iter()
            .map(|topic_name| {
                AlterConfig::new(ResourceSpecifier::Topic(topic_name.as_str()))
                    .set("retention.ms", "14400000")
                    .set("retention.bytes", "1073741824")
                    .set("max.message.bytes", "134217728")
            })
            .collect();
        let response = admin_client.create_topics(&new_topics, &admin_options).await?;
        info!(action = "create_topics", topics = ?new_topics, response = ?response);
        let response = admin_client.alter_configs(&alter_topics, &admin_options).await?;
        info!(action = "alter_configs", topics = ?new_topics, response = ?response);
        Ok(())
    }

    #[instrument(skip(self))]
    async fn delete_topics(&self) -> SummaServerResult<()> {
        let admin_client = AdminClient::from_config(&self.kafka_producer_config)?;
        let topics: Vec<_> = self.config.topics.iter().map(String::as_str).collect();
        let response = admin_client
            .delete_topics(
                &topics,
                &AdminOptions::new()
                    .operation_timeout(Some(Timeout::Never))
                    .request_timeout(Some(Timeout::After(Duration::from_secs(600)))),
            )
            .await?;
        info!(action = "delete_topics", topics = ?topics, response = ?response);
        Ok(())
    }

    #[instrument]
    pub async fn on_create(&self) -> SummaServerResult<()> {
        if self.config.create_topics {
            return self.create_topics().await;
        }
        Ok(())
    }

    #[instrument(skip(self), fields(consumer_name = ?self.consumer_name))]
    pub async fn on_delete(&self) -> SummaServerResult<()> {
        if self.config.delete_topics {
            return self.delete_topics().await;
        }
        Ok(())
    }

    pub fn config(&self) -> &crate::configs::consumer::Config {
        &self.config
    }
}
