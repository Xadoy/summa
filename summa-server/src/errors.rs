use std::convert::From;
use std::path::PathBuf;

use tracing::warn;

#[derive(thiserror::Error, Debug)]
pub enum ValidationError {
    #[error("aliased_error: {0}")]
    Aliased(String),
    #[error("existing_consumer_error: {0}")]
    ExistingConsumer(String),
    #[error("existing_index_error: {0}")]
    ExistingIndex(String),
    #[error("invalid_argument: {0}")]
    InvalidArgument(String),
    #[error("invalid_header_name: {0}")]
    InvalidHeaderName(#[from] hyper::header::InvalidHeaderName),
    #[error("invalid_header_value: {0}")]
    InvalidHeaderValue(#[from] hyper::header::InvalidHeaderValue),
    #[error("invalid_schema_error: {0}")]
    InvalidSchema(String),
    #[error("missing_consumer_error: {0}")]
    MissingConsumer(String),
    #[error("missing_index_error: {0}")]
    MissingIndex(String),
    #[error("missing_default_field_error: {0}")]
    MissingDefaultField(String),
    #[error("missing_field_error: {0}")]
    MissingField(String),
    #[error("missing_multi_field_error: {0}")]
    MissingMultiField(String),
    #[error("missing_primary_key_error: {0:?}")]
    MissingPrimaryKey(Option<String>),
}

#[derive(thiserror::Error, Debug)]
pub enum Error {
    #[error("addr_parse_error: {0}")]
    AddrParse(#[from] std::net::AddrParseError),
    #[error("anyhow_error: {0}")]
    Anyhow(#[from] anyhow::Error),
    #[error("clap_matches_error: {0}")]
    ClapMatches(#[from] clap::parser::MatchesError),
    #[error("summa_core: {0}")]
    Core(#[from] summa_core::Error),
    #[error("hyper_error: {0}")]
    Hyper(#[from] hyper::Error),
    #[error("hyper_http_error: {0}")]
    HyperHttp(#[from] hyper::http::Error),
    #[error("internal_error")]
    Internal,
    #[error("{0:?}")]
    IO((std::io::Error, Option<PathBuf>)),
    #[error("json_error: {0}")]
    Json(#[from] serde_json::Error),
    #[error("lock_error: {0}")]
    Lock(#[from] tokio::sync::TryLockError),
    #[error("tantivy_error: {0}")]
    Tantivy(#[from] tantivy::TantivyError),
    #[error("tonic_error: {0}")]
    Tonic(#[from] tonic::transport::Error),
    #[error("upstream_http_status_error: {0}")]
    UpstreamHttpStatus(hyper::StatusCode, String),
    #[error("utf8_error: {0}")]
    Utf8(#[from] std::str::Utf8Error),
    #[error("{0}")]
    Validation(#[from] ValidationError),
    #[error("{0}")]
    Kafka(#[from] rdkafka::error::KafkaError),
    #[error("{0}")]
    Yaml(#[from] serde_yaml::Error),
}

impl From<std::io::Error> for Error {
    fn from(error: std::io::Error) -> Self {
        Error::IO((error, None))
    }
}

impl From<Error> for summa_core::Error {
    fn from(error: Error) -> Self {
        summa_core::Error::External(format!("{error:?}"))
    }
}

impl From<tokio::task::JoinError> for Error {
    fn from(_error: tokio::task::JoinError) -> Self {
        Error::Internal
    }
}

impl From<Error> for tonic::Status {
    fn from(error: Error) -> Self {
        warn!(action = "error", error = ?error);
        tonic::Status::new(
            match error {
                Error::IO((ref io_error, _)) => match io_error.kind() {
                    std::io::ErrorKind::PermissionDenied => tonic::Code::PermissionDenied,
                    _ => tonic::Code::Internal,
                },
                Error::Validation(ValidationError::MissingIndex(_)) => tonic::Code::NotFound,
                Error::Validation(_) => tonic::Code::InvalidArgument,
                Error::Lock(_) => tonic::Code::FailedPrecondition,
                _ => tonic::Code::Internal,
            },
            format!("{error}"),
        )
    }
}

impl From<ValidationError> for tonic::Status {
    fn from(error: ValidationError) -> Self {
        tonic::Status::from(Error::Validation(error))
    }
}

pub type SummaServerResult<T> = Result<T, Error>;
