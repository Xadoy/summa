use std::time::{SystemTime, UNIX_EPOCH};

use summa_core::errors::BuilderError;
use summa_proto::proto;
use tantivy::schema::Schema;
use tantivy::IndexSortByField;

use crate::errors::{Error, SummaServerResult};
use crate::requests::validators;

#[derive(Builder)]
#[builder(build_fn(error = "BuilderError"))]
pub struct CreateIndexRequest {
    pub index_name: String,
    pub index_engine: proto::CreateIndexEngineRequest,
    pub schema: Schema,
    #[builder(default = "tantivy::store::Compressor::None")]
    pub compression: tantivy::store::Compressor,
    #[builder(default = "None")]
    pub blocksize: Option<usize>,
    #[builder(default = "None")]
    pub sort_by_field: Option<IndexSortByField>,
    #[builder(default)]
    pub index_attributes: proto::IndexAttributes,
}

impl TryFrom<proto::CreateIndexRequest> for CreateIndexRequest {
    type Error = Error;

    fn try_from(proto_request: proto::CreateIndexRequest) -> SummaServerResult<Self> {
        let schema = validators::parse_schema(&proto_request.schema)?;
        let mut index_attributes = proto_request.index_attributes.unwrap_or_default();
        validators::parse_default_fields(&schema, &index_attributes.default_fields)?;
        validators::parse_multi_fields(&schema, &index_attributes.multi_fields)?;
        validators::parse_primary_key(&schema, &index_attributes.primary_key)?;

        index_attributes.created_at = SystemTime::now().duration_since(UNIX_EPOCH).expect("cannot retrieve time").as_secs();

        let compression = proto::Compression::from_i32(proto_request.compression)
            .map(proto::Compression::into)
            .unwrap_or(tantivy::store::Compressor::None);

        Ok(CreateIndexRequestBuilder::default()
            .index_name(proto_request.index_name)
            .index_engine(proto::CreateIndexEngineRequest::from_i32(proto_request.index_engine).expect("unknown engine"))
            .schema(schema)
            .compression(compression)
            .blocksize(proto_request.blocksize.map(|blocksize| blocksize as usize))
            .sort_by_field(proto_request.sort_by_field.map(proto::SortByField::into))
            .index_attributes(index_attributes)
            .build()
            .map_err(summa_core::Error::from)?)
    }
}
