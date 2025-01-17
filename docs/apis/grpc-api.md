---
title: GRPC
parent: APIs
---
## GRPC API

- [consumer_service.proto](#consumer_service-proto)
    - [ConsumerApi](#summa-proto-ConsumerApi)
  
    - [Consumer](#summa-proto-Consumer)
    - [CreateConsumerRequest](#summa-proto-CreateConsumerRequest)
    - [CreateConsumerResponse](#summa-proto-CreateConsumerResponse)
    - [DeleteConsumerRequest](#summa-proto-DeleteConsumerRequest)
    - [DeleteConsumerResponse](#summa-proto-DeleteConsumerResponse)
    - [GetConsumerRequest](#summa-proto-GetConsumerRequest)
    - [GetConsumerResponse](#summa-proto-GetConsumerResponse)
    - [GetConsumersRequest](#summa-proto-GetConsumersRequest)
    - [GetConsumersResponse](#summa-proto-GetConsumersResponse)
  
- [index_service.proto](#index_service-proto)
    - [IndexApi](#summa-proto-IndexApi)
  
    - [AttachFileEngineRequest](#summa-proto-AttachFileEngineRequest)
    - [AttachIndexRequest](#summa-proto-AttachIndexRequest)
    - [AttachIndexResponse](#summa-proto-AttachIndexResponse)
    - [AttachIpfsEngineRequest](#summa-proto-AttachIpfsEngineRequest)
    - [AttachRemoteEngineRequest](#summa-proto-AttachRemoteEngineRequest)
    - [ChunkedCacheConfig](#summa-proto-ChunkedCacheConfig)
    - [CommitIndexRequest](#summa-proto-CommitIndexRequest)
    - [CommitIndexResponse](#summa-proto-CommitIndexResponse)
    - [CreateIndexRequest](#summa-proto-CreateIndexRequest)
    - [CreateIndexResponse](#summa-proto-CreateIndexResponse)
    - [DeleteDocumentRequest](#summa-proto-DeleteDocumentRequest)
    - [DeleteDocumentResponse](#summa-proto-DeleteDocumentResponse)
    - [DeleteIndexRequest](#summa-proto-DeleteIndexRequest)
    - [DeleteIndexResponse](#summa-proto-DeleteIndexResponse)
    - [FileEngineConfig](#summa-proto-FileEngineConfig)
    - [GetIndexRequest](#summa-proto-GetIndexRequest)
    - [GetIndexResponse](#summa-proto-GetIndexResponse)
    - [GetIndicesAliasesRequest](#summa-proto-GetIndicesAliasesRequest)
    - [GetIndicesAliasesResponse](#summa-proto-GetIndicesAliasesResponse)
    - [GetIndicesAliasesResponse.IndicesAliasesEntry](#summa-proto-GetIndicesAliasesResponse-IndicesAliasesEntry)
    - [GetIndicesRequest](#summa-proto-GetIndicesRequest)
    - [GetIndicesResponse](#summa-proto-GetIndicesResponse)
    - [IndexAttributes](#summa-proto-IndexAttributes)
    - [IndexDescription](#summa-proto-IndexDescription)
    - [IndexDocumentOperation](#summa-proto-IndexDocumentOperation)
    - [IndexDocumentRequest](#summa-proto-IndexDocumentRequest)
    - [IndexDocumentResponse](#summa-proto-IndexDocumentResponse)
    - [IndexDocumentStreamRequest](#summa-proto-IndexDocumentStreamRequest)
    - [IndexDocumentStreamResponse](#summa-proto-IndexDocumentStreamResponse)
    - [IndexEngineConfig](#summa-proto-IndexEngineConfig)
    - [IndexOperation](#summa-proto-IndexOperation)
    - [IpfsEngineConfig](#summa-proto-IpfsEngineConfig)
    - [MemoryEngineConfig](#summa-proto-MemoryEngineConfig)
    - [MergeSegmentsRequest](#summa-proto-MergeSegmentsRequest)
    - [MergeSegmentsResponse](#summa-proto-MergeSegmentsResponse)
    - [MigrateIndexRequest](#summa-proto-MigrateIndexRequest)
    - [MigrateIndexResponse](#summa-proto-MigrateIndexResponse)
    - [PrimaryKey](#summa-proto-PrimaryKey)
    - [RemoteEngineConfig](#summa-proto-RemoteEngineConfig)
    - [RemoteEngineConfig.HeadersTemplateEntry](#summa-proto-RemoteEngineConfig-HeadersTemplateEntry)
    - [SetIndexAliasRequest](#summa-proto-SetIndexAliasRequest)
    - [SetIndexAliasResponse](#summa-proto-SetIndexAliasResponse)
    - [SortByField](#summa-proto-SortByField)
    - [VacuumIndexRequest](#summa-proto-VacuumIndexRequest)
    - [VacuumIndexResponse](#summa-proto-VacuumIndexResponse)
    - [WarmupIndexRequest](#summa-proto-WarmupIndexRequest)
    - [WarmupIndexResponse](#summa-proto-WarmupIndexResponse)
  
    - [CommitMode](#summa-proto-CommitMode)
    - [Compression](#summa-proto-Compression)
    - [CreateIndexEngineRequest](#summa-proto-CreateIndexEngineRequest)
  
- [query.proto](#query-proto)
    - [Aggregation](#summa-proto-Aggregation)
    - [AggregationCollector](#summa-proto-AggregationCollector)
    - [AggregationCollector.AggregationsEntry](#summa-proto-AggregationCollector-AggregationsEntry)
    - [AggregationCollectorOutput](#summa-proto-AggregationCollectorOutput)
    - [AggregationCollectorOutput.AggregationResultsEntry](#summa-proto-AggregationCollectorOutput-AggregationResultsEntry)
    - [AggregationResult](#summa-proto-AggregationResult)
    - [AllQuery](#summa-proto-AllQuery)
    - [AverageAggregation](#summa-proto-AverageAggregation)
    - [BooleanQuery](#summa-proto-BooleanQuery)
    - [BooleanSubquery](#summa-proto-BooleanSubquery)
    - [BoostQuery](#summa-proto-BoostQuery)
    - [BucketAggregation](#summa-proto-BucketAggregation)
    - [BucketAggregation.SubAggregationEntry](#summa-proto-BucketAggregation-SubAggregationEntry)
    - [BucketEntry](#summa-proto-BucketEntry)
    - [BucketEntry.SubAggregationEntry](#summa-proto-BucketEntry-SubAggregationEntry)
    - [BucketResult](#summa-proto-BucketResult)
    - [Collector](#summa-proto-Collector)
    - [CollectorOutput](#summa-proto-CollectorOutput)
    - [CountCollector](#summa-proto-CountCollector)
    - [CountCollectorOutput](#summa-proto-CountCollectorOutput)
    - [CustomOrder](#summa-proto-CustomOrder)
    - [DisjunctionMaxQuery](#summa-proto-DisjunctionMaxQuery)
    - [EmptyQuery](#summa-proto-EmptyQuery)
    - [FacetCollector](#summa-proto-FacetCollector)
    - [FacetCollectorOutput](#summa-proto-FacetCollectorOutput)
    - [FacetCollectorOutput.FacetCountsEntry](#summa-proto-FacetCollectorOutput-FacetCountsEntry)
    - [Highlight](#summa-proto-Highlight)
    - [HistogramAggregation](#summa-proto-HistogramAggregation)
    - [HistogramBounds](#summa-proto-HistogramBounds)
    - [HistogramResult](#summa-proto-HistogramResult)
    - [Key](#summa-proto-Key)
    - [MatchQuery](#summa-proto-MatchQuery)
    - [MetricAggregation](#summa-proto-MetricAggregation)
    - [MetricResult](#summa-proto-MetricResult)
    - [MoreLikeThisQuery](#summa-proto-MoreLikeThisQuery)
    - [PhraseQuery](#summa-proto-PhraseQuery)
    - [Query](#summa-proto-Query)
    - [RandomDocument](#summa-proto-RandomDocument)
    - [Range](#summa-proto-Range)
    - [RangeAggregation](#summa-proto-RangeAggregation)
    - [RangeAggregationRange](#summa-proto-RangeAggregationRange)
    - [RangeBucketEntry](#summa-proto-RangeBucketEntry)
    - [RangeBucketEntry.SubAggregationEntry](#summa-proto-RangeBucketEntry-SubAggregationEntry)
    - [RangeQuery](#summa-proto-RangeQuery)
    - [RangeResult](#summa-proto-RangeResult)
    - [RegexQuery](#summa-proto-RegexQuery)
    - [ReservoirSamplingCollector](#summa-proto-ReservoirSamplingCollector)
    - [ReservoirSamplingCollectorOutput](#summa-proto-ReservoirSamplingCollectorOutput)
    - [Score](#summa-proto-Score)
    - [ScoredDocument](#summa-proto-ScoredDocument)
    - [ScoredDocument.SnippetsEntry](#summa-proto-ScoredDocument-SnippetsEntry)
    - [Scorer](#summa-proto-Scorer)
    - [SearchResponse](#summa-proto-SearchResponse)
    - [SingleMetricResult](#summa-proto-SingleMetricResult)
    - [Snippet](#summa-proto-Snippet)
    - [StatsAggregation](#summa-proto-StatsAggregation)
    - [StatsResult](#summa-proto-StatsResult)
    - [TermQuery](#summa-proto-TermQuery)
    - [TermsAggregation](#summa-proto-TermsAggregation)
    - [TermsResult](#summa-proto-TermsResult)
    - [TopDocsCollector](#summa-proto-TopDocsCollector)
    - [TopDocsCollector.SnippetsEntry](#summa-proto-TopDocsCollector-SnippetsEntry)
    - [TopDocsCollectorOutput](#summa-proto-TopDocsCollectorOutput)
  
    - [Occur](#summa-proto-Occur)
  
- [reflection_service.proto](#reflection_service-proto)
    - [ReflectionApi](#summa-proto-ReflectionApi)
  
    - [GetTopTermsRequest](#summa-proto-GetTopTermsRequest)
    - [GetTopTermsResponse](#summa-proto-GetTopTermsResponse)
    - [GetTopTermsResponse.PerSegmentEntry](#summa-proto-GetTopTermsResponse-PerSegmentEntry)
    - [SegmentTerms](#summa-proto-SegmentTerms)
    - [TermInfo](#summa-proto-TermInfo)
  
- [search_service.proto](#search_service-proto)
    - [SearchApi](#summa-proto-SearchApi)
  
    - [IndexQuery](#summa-proto-IndexQuery)
    - [SearchRequest](#summa-proto-SearchRequest)
    - [SearchRequest.TagsEntry](#summa-proto-SearchRequest-TagsEntry)
  
- [utils.proto](#utils-proto)
    - [Empty](#summa-proto-Empty)
  
    - [Order](#summa-proto-Order)
  



<a name="consumer_service-proto"></a>

## consumer_service.proto



<a name="summa-proto-Consumer"></a>

### Consumer
Extra structures


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| consumer_name | [string](#string) |  |  |
| index_name | [string](#string) |  |  |






<a name="summa-proto-CreateConsumerRequest"></a>

### CreateConsumerRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| bootstrap_servers | [string](#string) | repeated |  |
| group_id | [string](#string) |  |  |
| index_name | [string](#string) |  |  |
| consumer_name | [string](#string) |  |  |
| topics | [string](#string) | repeated |  |






<a name="summa-proto-CreateConsumerResponse"></a>

### CreateConsumerResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| consumer | [Consumer](#summa-proto-Consumer) |  |  |






<a name="summa-proto-DeleteConsumerRequest"></a>

### DeleteConsumerRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| consumer_name | [string](#string) |  |  |






<a name="summa-proto-DeleteConsumerResponse"></a>

### DeleteConsumerResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| consumer_name | [string](#string) |  |  |






<a name="summa-proto-GetConsumerRequest"></a>

### GetConsumerRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index_alias | [string](#string) |  |  |
| consumer_name | [string](#string) |  |  |






<a name="summa-proto-GetConsumerResponse"></a>

### GetConsumerResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| consumer | [Consumer](#summa-proto-Consumer) |  |  |






<a name="summa-proto-GetConsumersRequest"></a>

### GetConsumersRequest







<a name="summa-proto-GetConsumersResponse"></a>

### GetConsumersResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| consumers | [Consumer](#summa-proto-Consumer) | repeated |  |





 <!-- end messages -->

 <!-- end enums -->

 <!-- end HasExtensions -->


<a name="summa-proto-ConsumerApi"></a>

### ConsumerApi
Manages ingestion data from Kafka

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| create_consumer | [CreateConsumerRequest](#summa-proto-CreateConsumerRequest) | [CreateConsumerResponse](#summa-proto-CreateConsumerResponse) | Create a new consumer |
| get_consumer | [GetConsumerRequest](#summa-proto-GetConsumerRequest) | [GetConsumerResponse](#summa-proto-GetConsumerResponse) | Get a single consumer |
| get_consumers | [GetConsumersRequest](#summa-proto-GetConsumersRequest) | [GetConsumersResponse](#summa-proto-GetConsumersResponse) | Get a list of all consumers |
| delete_consumer | [DeleteConsumerRequest](#summa-proto-DeleteConsumerRequest) | [DeleteConsumerResponse](#summa-proto-DeleteConsumerResponse) | Remove a consumer |

 <!-- end services -->



<a name="index_service-proto"></a>

## index_service.proto



<a name="summa-proto-AttachFileEngineRequest"></a>

### AttachFileEngineRequest
Attach file engine request






<a name="summa-proto-AttachIndexRequest"></a>

### AttachIndexRequest
Attach index request


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index_name | [string](#string) |  |  |
| attach_file_engine_request | [AttachFileEngineRequest](#summa-proto-AttachFileEngineRequest) |  |  |
| attach_remote_engine_request | [AttachRemoteEngineRequest](#summa-proto-AttachRemoteEngineRequest) |  |  |
| attach_ipfs_engine_request | [AttachIpfsEngineRequest](#summa-proto-AttachIpfsEngineRequest) |  |  |






<a name="summa-proto-AttachIndexResponse"></a>

### AttachIndexResponse
Attach index response


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index | [IndexDescription](#summa-proto-IndexDescription) |  |  |






<a name="summa-proto-AttachIpfsEngineRequest"></a>

### AttachIpfsEngineRequest
Attach file engine request


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| cid | [string](#string) |  |  |






<a name="summa-proto-AttachRemoteEngineRequest"></a>

### AttachRemoteEngineRequest
Attach remote engine request






<a name="summa-proto-ChunkedCacheConfig"></a>

### ChunkedCacheConfig



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| chunk_size | [uint64](#uint64) |  |  |
| cache_size | [uint64](#uint64) | optional |  |






<a name="summa-proto-CommitIndexRequest"></a>

### CommitIndexRequest
Commit index request


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index_alias | [string](#string) |  |  |
| commit_mode | [CommitMode](#summa-proto-CommitMode) |  |  |






<a name="summa-proto-CommitIndexResponse"></a>

### CommitIndexResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| elapsed_secs | [double](#double) | optional |  |






<a name="summa-proto-CreateIndexRequest"></a>

### CreateIndexRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index_name | [string](#string) |  |  |
| index_engine | [CreateIndexEngineRequest](#summa-proto-CreateIndexEngineRequest) |  |  |
| schema | [string](#string) |  |  |
| compression | [Compression](#summa-proto-Compression) |  |  |
| blocksize | [uint32](#uint32) | optional |  |
| sort_by_field | [SortByField](#summa-proto-SortByField) | optional |  |
| index_attributes | [IndexAttributes](#summa-proto-IndexAttributes) |  |  |






<a name="summa-proto-CreateIndexResponse"></a>

### CreateIndexResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index | [IndexDescription](#summa-proto-IndexDescription) |  |  |






<a name="summa-proto-DeleteDocumentRequest"></a>

### DeleteDocumentRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index_alias | [string](#string) |  |  |
| primary_key | [PrimaryKey](#summa-proto-PrimaryKey) |  |  |






<a name="summa-proto-DeleteDocumentResponse"></a>

### DeleteDocumentResponse







<a name="summa-proto-DeleteIndexRequest"></a>

### DeleteIndexRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index_name | [string](#string) |  |  |






<a name="summa-proto-DeleteIndexResponse"></a>

### DeleteIndexResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index_name | [string](#string) |  |  |






<a name="summa-proto-FileEngineConfig"></a>

### FileEngineConfig



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| path | [string](#string) |  |  |






<a name="summa-proto-GetIndexRequest"></a>

### GetIndexRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index_alias | [string](#string) |  |  |






<a name="summa-proto-GetIndexResponse"></a>

### GetIndexResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index | [IndexDescription](#summa-proto-IndexDescription) |  |  |






<a name="summa-proto-GetIndicesAliasesRequest"></a>

### GetIndicesAliasesRequest







<a name="summa-proto-GetIndicesAliasesResponse"></a>

### GetIndicesAliasesResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| indices_aliases | [GetIndicesAliasesResponse.IndicesAliasesEntry](#summa-proto-GetIndicesAliasesResponse-IndicesAliasesEntry) | repeated |  |






<a name="summa-proto-GetIndicesAliasesResponse-IndicesAliasesEntry"></a>

### GetIndicesAliasesResponse.IndicesAliasesEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [string](#string) |  |  |






<a name="summa-proto-GetIndicesRequest"></a>

### GetIndicesRequest







<a name="summa-proto-GetIndicesResponse"></a>

### GetIndicesResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| indices | [IndexDescription](#summa-proto-IndexDescription) | repeated |  |






<a name="summa-proto-IndexAttributes"></a>

### IndexAttributes



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| created_at | [uint64](#uint64) |  |  |
| primary_key | [string](#string) | optional |  |
| default_fields | [string](#string) | repeated |  |
| multi_fields | [string](#string) | repeated |  |
| default_index_name | [string](#string) | optional |  |
| description | [string](#string) | optional |  |
| default_snippets | [string](#string) | repeated |  |






<a name="summa-proto-IndexDescription"></a>

### IndexDescription



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index_name | [string](#string) |  |  |
| index_aliases | [string](#string) | repeated |  |
| index_engine | [IndexEngineConfig](#summa-proto-IndexEngineConfig) |  |  |
| num_docs | [uint64](#uint64) |  |  |
| compression | [Compression](#summa-proto-Compression) |  |  |






<a name="summa-proto-IndexDocumentOperation"></a>

### IndexDocumentOperation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| document | [bytes](#bytes) |  |  |






<a name="summa-proto-IndexDocumentRequest"></a>

### IndexDocumentRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index_alias | [string](#string) |  |  |
| document | [bytes](#bytes) |  |  |






<a name="summa-proto-IndexDocumentResponse"></a>

### IndexDocumentResponse







<a name="summa-proto-IndexDocumentStreamRequest"></a>

### IndexDocumentStreamRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index_alias | [string](#string) |  |  |
| documents | [bytes](#bytes) | repeated |  |






<a name="summa-proto-IndexDocumentStreamResponse"></a>

### IndexDocumentStreamResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| success_docs | [uint64](#uint64) |  |  |
| failed_docs | [uint64](#uint64) |  |  |
| elapsed_secs | [double](#double) |  |  |






<a name="summa-proto-IndexEngineConfig"></a>

### IndexEngineConfig



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| file | [FileEngineConfig](#summa-proto-FileEngineConfig) |  |  |
| memory | [MemoryEngineConfig](#summa-proto-MemoryEngineConfig) |  |  |
| remote | [RemoteEngineConfig](#summa-proto-RemoteEngineConfig) |  |  |
| ipfs | [IpfsEngineConfig](#summa-proto-IpfsEngineConfig) |  |  |






<a name="summa-proto-IndexOperation"></a>

### IndexOperation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index_document | [IndexDocumentOperation](#summa-proto-IndexDocumentOperation) |  |  |






<a name="summa-proto-IpfsEngineConfig"></a>

### IpfsEngineConfig



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| cid | [string](#string) |  |  |
| chunked_cache_config | [ChunkedCacheConfig](#summa-proto-ChunkedCacheConfig) |  |  |
| path | [string](#string) |  |  |






<a name="summa-proto-MemoryEngineConfig"></a>

### MemoryEngineConfig



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| schema | [string](#string) |  |  |






<a name="summa-proto-MergeSegmentsRequest"></a>

### MergeSegmentsRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index_alias | [string](#string) |  |  |
| segment_ids | [string](#string) | repeated |  |






<a name="summa-proto-MergeSegmentsResponse"></a>

### MergeSegmentsResponse







<a name="summa-proto-MigrateIndexRequest"></a>

### MigrateIndexRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| source_index_name | [string](#string) |  |  |
| target_index_name | [string](#string) |  |  |
| target_index_engine | [CreateIndexEngineRequest](#summa-proto-CreateIndexEngineRequest) |  |  |






<a name="summa-proto-MigrateIndexResponse"></a>

### MigrateIndexResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index | [IndexDescription](#summa-proto-IndexDescription) |  |  |






<a name="summa-proto-PrimaryKey"></a>

### PrimaryKey
Possible primary keys


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| str | [string](#string) |  |  |
| i64 | [int64](#int64) |  |  |






<a name="summa-proto-RemoteEngineConfig"></a>

### RemoteEngineConfig



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| method | [string](#string) |  |  |
| url_template | [string](#string) |  |  |
| headers_template | [RemoteEngineConfig.HeadersTemplateEntry](#summa-proto-RemoteEngineConfig-HeadersTemplateEntry) | repeated |  |
| chunked_cache_config | [ChunkedCacheConfig](#summa-proto-ChunkedCacheConfig) |  |  |






<a name="summa-proto-RemoteEngineConfig-HeadersTemplateEntry"></a>

### RemoteEngineConfig.HeadersTemplateEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [string](#string) |  |  |






<a name="summa-proto-SetIndexAliasRequest"></a>

### SetIndexAliasRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index_alias | [string](#string) |  |  |
| index_name | [string](#string) |  |  |






<a name="summa-proto-SetIndexAliasResponse"></a>

### SetIndexAliasResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| old_index_name | [string](#string) | optional | If set, equals to the previous alias of the index |






<a name="summa-proto-SortByField"></a>

### SortByField



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| field | [string](#string) |  |  |
| order | [Order](#summa-proto-Order) |  |  |






<a name="summa-proto-VacuumIndexRequest"></a>

### VacuumIndexRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index_alias | [string](#string) |  |  |






<a name="summa-proto-VacuumIndexResponse"></a>

### VacuumIndexResponse
repeated string deleted_files = 1;






<a name="summa-proto-WarmupIndexRequest"></a>

### WarmupIndexRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index_alias | [string](#string) |  |  |
| is_full | [bool](#bool) |  | If set to false, only term dictionaries will be warmed, otherwise the entire index will be read. |






<a name="summa-proto-WarmupIndexResponse"></a>

### WarmupIndexResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| elapsed_secs | [double](#double) |  | Time spent in warming operation |





 <!-- end messages -->


<a name="summa-proto-CommitMode"></a>

### CommitMode
Commit mode

| Name | Number | Description |
| ---- | ------ | ----------- |
| Async | 0 | Returns immediately and then commits in the background |
| Sync | 1 | Waits until the end of commit |



<a name="summa-proto-Compression"></a>

### Compression


| Name | Number | Description |
| ---- | ------ | ----------- |
| None | 0 |  |
| Brotli | 1 |  |
| Lz4 | 2 |  |
| Snappy | 3 |  |
| Zstd | 4 |  |



<a name="summa-proto-CreateIndexEngineRequest"></a>

### CreateIndexEngineRequest


| Name | Number | Description |
| ---- | ------ | ----------- |
| File | 0 |  |
| Memory | 1 |  |
| Ipfs | 2 |  |


 <!-- end enums -->

 <!-- end HasExtensions -->


<a name="summa-proto-IndexApi"></a>

### IndexApi
Manages indices

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| attach_index | [AttachIndexRequest](#summa-proto-AttachIndexRequest) | [AttachIndexResponse](#summa-proto-AttachIndexResponse) | Attaches index to Summa server. Attaching allows to incorporate and start using of downloaded or network indices |
| commit_index | [CommitIndexRequest](#summa-proto-CommitIndexRequest) | [CommitIndexResponse](#summa-proto-CommitIndexResponse) | Committing all collected writes to the index |
| create_index | [CreateIndexRequest](#summa-proto-CreateIndexRequest) | [CreateIndexResponse](#summa-proto-CreateIndexResponse) | Creates new index from scratch |
| migrate_index | [MigrateIndexRequest](#summa-proto-MigrateIndexRequest) | [MigrateIndexResponse](#summa-proto-MigrateIndexResponse) | Creates new index from scratch |
| delete_document | [DeleteDocumentRequest](#summa-proto-DeleteDocumentRequest) | [DeleteDocumentResponse](#summa-proto-DeleteDocumentResponse) | Deletes single document from the index by its primary key (therefore, index must have primary key) |
| delete_index | [DeleteIndexRequest](#summa-proto-DeleteIndexRequest) | [DeleteIndexResponse](#summa-proto-DeleteIndexResponse) | Deletes index and physically removes file in the case of `FileEngine` |
| get_indices_aliases | [GetIndicesAliasesRequest](#summa-proto-GetIndicesAliasesRequest) | [GetIndicesAliasesResponse](#summa-proto-GetIndicesAliasesResponse) | Gets all existing index aliases |
| get_index | [GetIndexRequest](#summa-proto-GetIndexRequest) | [GetIndexResponse](#summa-proto-GetIndexResponse) | Gets index description |
| get_indices | [GetIndicesRequest](#summa-proto-GetIndicesRequest) | [GetIndicesResponse](#summa-proto-GetIndicesResponse) | Gets all existing index descriptions |
| index_document_stream | [IndexDocumentStreamRequest](#summa-proto-IndexDocumentStreamRequest) stream | [IndexDocumentStreamResponse](#summa-proto-IndexDocumentStreamResponse) | Adds document to the index in a streaming way |
| index_document | [IndexDocumentRequest](#summa-proto-IndexDocumentRequest) | [IndexDocumentResponse](#summa-proto-IndexDocumentResponse) | Adds document to the index |
| merge_segments | [MergeSegmentsRequest](#summa-proto-MergeSegmentsRequest) | [MergeSegmentsResponse](#summa-proto-MergeSegmentsResponse) | Merges multiple segments into a single one. Used for service purposes |
| set_index_alias | [SetIndexAliasRequest](#summa-proto-SetIndexAliasRequest) | [SetIndexAliasResponse](#summa-proto-SetIndexAliasResponse) | Sets or replaces existing index alias |
| vacuum_index | [VacuumIndexRequest](#summa-proto-VacuumIndexRequest) | [VacuumIndexResponse](#summa-proto-VacuumIndexResponse) | Removes deletions from all segments |
| warmup_index | [WarmupIndexRequest](#summa-proto-WarmupIndexRequest) | [WarmupIndexResponse](#summa-proto-WarmupIndexResponse) | Loads all hot parts of the index into the memory |

 <!-- end services -->



<a name="query-proto"></a>

## query.proto



<a name="summa-proto-Aggregation"></a>

### Aggregation
Aggregation


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| bucket | [BucketAggregation](#summa-proto-BucketAggregation) |  |  |
| metric | [MetricAggregation](#summa-proto-MetricAggregation) |  |  |






<a name="summa-proto-AggregationCollector"></a>

### AggregationCollector



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| aggregations | [AggregationCollector.AggregationsEntry](#summa-proto-AggregationCollector-AggregationsEntry) | repeated |  |






<a name="summa-proto-AggregationCollector-AggregationsEntry"></a>

### AggregationCollector.AggregationsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [Aggregation](#summa-proto-Aggregation) |  |  |






<a name="summa-proto-AggregationCollectorOutput"></a>

### AggregationCollectorOutput



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| aggregation_results | [AggregationCollectorOutput.AggregationResultsEntry](#summa-proto-AggregationCollectorOutput-AggregationResultsEntry) | repeated |  |






<a name="summa-proto-AggregationCollectorOutput-AggregationResultsEntry"></a>

### AggregationCollectorOutput.AggregationResultsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [AggregationResult](#summa-proto-AggregationResult) |  |  |






<a name="summa-proto-AggregationResult"></a>

### AggregationResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| bucket | [BucketResult](#summa-proto-BucketResult) |  |  |
| metric | [MetricResult](#summa-proto-MetricResult) |  |  |






<a name="summa-proto-AllQuery"></a>

### AllQuery







<a name="summa-proto-AverageAggregation"></a>

### AverageAggregation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| field | [string](#string) |  |  |






<a name="summa-proto-BooleanQuery"></a>

### BooleanQuery



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| subqueries | [BooleanSubquery](#summa-proto-BooleanSubquery) | repeated |  |






<a name="summa-proto-BooleanSubquery"></a>

### BooleanSubquery



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| occur | [Occur](#summa-proto-Occur) |  |  |
| query | [Query](#summa-proto-Query) |  |  |






<a name="summa-proto-BoostQuery"></a>

### BoostQuery



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| query | [Query](#summa-proto-Query) |  |  |
| score | [string](#string) |  |  |






<a name="summa-proto-BucketAggregation"></a>

### BucketAggregation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| range | [RangeAggregation](#summa-proto-RangeAggregation) |  |  |
| histogram | [HistogramAggregation](#summa-proto-HistogramAggregation) |  |  |
| terms | [TermsAggregation](#summa-proto-TermsAggregation) |  |  |
| sub_aggregation | [BucketAggregation.SubAggregationEntry](#summa-proto-BucketAggregation-SubAggregationEntry) | repeated |  |






<a name="summa-proto-BucketAggregation-SubAggregationEntry"></a>

### BucketAggregation.SubAggregationEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [Aggregation](#summa-proto-Aggregation) |  |  |






<a name="summa-proto-BucketEntry"></a>

### BucketEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [Key](#summa-proto-Key) |  |  |
| doc_count | [uint64](#uint64) |  |  |
| sub_aggregation | [BucketEntry.SubAggregationEntry](#summa-proto-BucketEntry-SubAggregationEntry) | repeated |  |






<a name="summa-proto-BucketEntry-SubAggregationEntry"></a>

### BucketEntry.SubAggregationEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [AggregationResult](#summa-proto-AggregationResult) |  |  |






<a name="summa-proto-BucketResult"></a>

### BucketResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| range | [RangeResult](#summa-proto-RangeResult) |  |  |
| histogram | [HistogramResult](#summa-proto-HistogramResult) |  |  |
| terms | [TermsResult](#summa-proto-TermsResult) |  |  |






<a name="summa-proto-Collector"></a>

### Collector



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| top_docs | [TopDocsCollector](#summa-proto-TopDocsCollector) |  |  |
| reservoir_sampling | [ReservoirSamplingCollector](#summa-proto-ReservoirSamplingCollector) |  |  |
| count | [CountCollector](#summa-proto-CountCollector) |  |  |
| facet | [FacetCollector](#summa-proto-FacetCollector) |  |  |
| aggregation | [AggregationCollector](#summa-proto-AggregationCollector) |  |  |






<a name="summa-proto-CollectorOutput"></a>

### CollectorOutput



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| top_docs | [TopDocsCollectorOutput](#summa-proto-TopDocsCollectorOutput) |  |  |
| reservoir_sampling | [ReservoirSamplingCollectorOutput](#summa-proto-ReservoirSamplingCollectorOutput) |  |  |
| count | [CountCollectorOutput](#summa-proto-CountCollectorOutput) |  |  |
| facet | [FacetCollectorOutput](#summa-proto-FacetCollectorOutput) |  |  |
| aggregation | [AggregationCollectorOutput](#summa-proto-AggregationCollectorOutput) |  |  |






<a name="summa-proto-CountCollector"></a>

### CountCollector







<a name="summa-proto-CountCollectorOutput"></a>

### CountCollectorOutput



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| count | [uint32](#uint32) |  |  |






<a name="summa-proto-CustomOrder"></a>

### CustomOrder



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [Empty](#summa-proto-Empty) |  |  |
| count | [Empty](#summa-proto-Empty) |  |  |
| sub_aggregation | [string](#string) |  |  |
| order | [Order](#summa-proto-Order) |  |  |






<a name="summa-proto-DisjunctionMaxQuery"></a>

### DisjunctionMaxQuery



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| disjuncts | [Query](#summa-proto-Query) | repeated |  |
| tie_breaker | [string](#string) |  |  |






<a name="summa-proto-EmptyQuery"></a>

### EmptyQuery







<a name="summa-proto-FacetCollector"></a>

### FacetCollector



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| field | [string](#string) |  |  |
| facets | [string](#string) | repeated |  |






<a name="summa-proto-FacetCollectorOutput"></a>

### FacetCollectorOutput



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| facet_counts | [FacetCollectorOutput.FacetCountsEntry](#summa-proto-FacetCollectorOutput-FacetCountsEntry) | repeated |  |






<a name="summa-proto-FacetCollectorOutput-FacetCountsEntry"></a>

### FacetCollectorOutput.FacetCountsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [uint64](#uint64) |  |  |






<a name="summa-proto-Highlight"></a>

### Highlight



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| from | [uint32](#uint32) |  |  |
| to | [uint32](#uint32) |  |  |






<a name="summa-proto-HistogramAggregation"></a>

### HistogramAggregation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| field | [string](#string) |  |  |
| interval | [double](#double) |  |  |
| offset | [double](#double) | optional |  |
| min_doc_count | [uint64](#uint64) | optional |  |
| hard_bounds | [HistogramBounds](#summa-proto-HistogramBounds) | optional |  |
| extended_bounds | [HistogramBounds](#summa-proto-HistogramBounds) | optional |  |






<a name="summa-proto-HistogramBounds"></a>

### HistogramBounds



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| min | [double](#double) |  |  |
| max | [double](#double) |  |  |






<a name="summa-proto-HistogramResult"></a>

### HistogramResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| buckets | [BucketEntry](#summa-proto-BucketEntry) | repeated |  |






<a name="summa-proto-Key"></a>

### Key



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| str | [string](#string) |  |  |
| f64 | [double](#double) |  |  |






<a name="summa-proto-MatchQuery"></a>

### MatchQuery



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | [string](#string) |  |  |






<a name="summa-proto-MetricAggregation"></a>

### MetricAggregation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| average | [AverageAggregation](#summa-proto-AverageAggregation) |  |  |
| stats | [StatsAggregation](#summa-proto-StatsAggregation) |  |  |






<a name="summa-proto-MetricResult"></a>

### MetricResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| single_metric | [SingleMetricResult](#summa-proto-SingleMetricResult) |  |  |
| stats | [StatsResult](#summa-proto-StatsResult) |  |  |






<a name="summa-proto-MoreLikeThisQuery"></a>

### MoreLikeThisQuery



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| document | [string](#string) |  |  |
| min_doc_frequency | [uint64](#uint64) | optional |  |
| max_doc_frequency | [uint64](#uint64) | optional |  |
| min_term_frequency | [uint64](#uint64) | optional |  |
| max_query_terms | [uint64](#uint64) | optional |  |
| min_word_length | [uint64](#uint64) | optional |  |
| max_word_length | [uint64](#uint64) | optional |  |
| boost | [string](#string) | optional |  |
| stop_words | [string](#string) | repeated |  |






<a name="summa-proto-PhraseQuery"></a>

### PhraseQuery



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| field | [string](#string) |  |  |
| value | [string](#string) |  |  |
| slop | [uint32](#uint32) |  |  |






<a name="summa-proto-Query"></a>

### Query
Recursive query DSL


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| boolean | [BooleanQuery](#summa-proto-BooleanQuery) |  |  |
| match | [MatchQuery](#summa-proto-MatchQuery) |  |  |
| regex | [RegexQuery](#summa-proto-RegexQuery) |  |  |
| term | [TermQuery](#summa-proto-TermQuery) |  |  |
| phrase | [PhraseQuery](#summa-proto-PhraseQuery) |  |  |
| range | [RangeQuery](#summa-proto-RangeQuery) |  |  |
| all | [AllQuery](#summa-proto-AllQuery) |  |  |
| more_like_this | [MoreLikeThisQuery](#summa-proto-MoreLikeThisQuery) |  |  |
| boost | [BoostQuery](#summa-proto-BoostQuery) |  |  |
| disjunction_max | [DisjunctionMaxQuery](#summa-proto-DisjunctionMaxQuery) |  |  |
| empty | [EmptyQuery](#summa-proto-EmptyQuery) |  |  |






<a name="summa-proto-RandomDocument"></a>

### RandomDocument



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| document | [string](#string) |  |  |
| score | [Score](#summa-proto-Score) |  |  |
| index_alias | [string](#string) |  |  |






<a name="summa-proto-Range"></a>

### Range



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| left | [string](#string) |  |  |
| right | [string](#string) |  |  |
| including_left | [bool](#bool) |  |  |
| including_right | [bool](#bool) |  |  |






<a name="summa-proto-RangeAggregation"></a>

### RangeAggregation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| field | [string](#string) |  |  |
| ranges | [RangeAggregationRange](#summa-proto-RangeAggregationRange) | repeated |  |






<a name="summa-proto-RangeAggregationRange"></a>

### RangeAggregationRange



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| from | [double](#double) | optional |  |
| to | [double](#double) | optional |  |
| key | [string](#string) | optional |  |






<a name="summa-proto-RangeBucketEntry"></a>

### RangeBucketEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [Key](#summa-proto-Key) |  |  |
| doc_count | [uint64](#uint64) |  |  |
| sub_aggregation | [RangeBucketEntry.SubAggregationEntry](#summa-proto-RangeBucketEntry-SubAggregationEntry) | repeated |  |
| from | [double](#double) | optional |  |
| to | [double](#double) | optional |  |






<a name="summa-proto-RangeBucketEntry-SubAggregationEntry"></a>

### RangeBucketEntry.SubAggregationEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [AggregationResult](#summa-proto-AggregationResult) |  |  |






<a name="summa-proto-RangeQuery"></a>

### RangeQuery



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| field | [string](#string) |  |  |
| value | [Range](#summa-proto-Range) |  |  |






<a name="summa-proto-RangeResult"></a>

### RangeResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| buckets | [RangeBucketEntry](#summa-proto-RangeBucketEntry) | repeated |  |






<a name="summa-proto-RegexQuery"></a>

### RegexQuery



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| field | [string](#string) |  |  |
| value | [string](#string) |  |  |






<a name="summa-proto-ReservoirSamplingCollector"></a>

### ReservoirSamplingCollector



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| limit | [uint32](#uint32) |  |  |
| fields | [string](#string) | repeated |  |






<a name="summa-proto-ReservoirSamplingCollectorOutput"></a>

### ReservoirSamplingCollectorOutput



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| random_documents | [RandomDocument](#summa-proto-RandomDocument) | repeated |  |






<a name="summa-proto-Score"></a>

### Score



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| f64_score | [double](#double) |  |  |
| u64_score | [uint64](#uint64) |  |  |






<a name="summa-proto-ScoredDocument"></a>

### ScoredDocument



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| document | [string](#string) |  |  |
| score | [Score](#summa-proto-Score) |  |  |
| position | [uint32](#uint32) |  |  |
| snippets | [ScoredDocument.SnippetsEntry](#summa-proto-ScoredDocument-SnippetsEntry) | repeated |  |
| index_alias | [string](#string) |  |  |






<a name="summa-proto-ScoredDocument-SnippetsEntry"></a>

### ScoredDocument.SnippetsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [Snippet](#summa-proto-Snippet) |  |  |






<a name="summa-proto-Scorer"></a>

### Scorer



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| eval_expr | [string](#string) |  |  |
| order_by | [string](#string) |  |  |






<a name="summa-proto-SearchResponse"></a>

### SearchResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| collector_outputs | [CollectorOutput](#summa-proto-CollectorOutput) | repeated | An array of collector outputs |
| elapsed_secs | [double](#double) |  | Time spent inside of `search` handler |






<a name="summa-proto-SingleMetricResult"></a>

### SingleMetricResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| value | [double](#double) | optional |  |






<a name="summa-proto-Snippet"></a>

### Snippet



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| fragment | [bytes](#bytes) |  |  |
| highlights | [Highlight](#summa-proto-Highlight) | repeated |  |
| html | [string](#string) |  |  |






<a name="summa-proto-StatsAggregation"></a>

### StatsAggregation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| field | [string](#string) |  |  |






<a name="summa-proto-StatsResult"></a>

### StatsResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| count | [uint64](#uint64) |  |  |
| sum | [double](#double) |  |  |
| standard_deviation | [double](#double) | optional |  |
| min | [double](#double) | optional |  |
| max | [double](#double) | optional |  |
| avg | [double](#double) | optional |  |






<a name="summa-proto-TermQuery"></a>

### TermQuery



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| field | [string](#string) |  |  |
| value | [string](#string) |  |  |






<a name="summa-proto-TermsAggregation"></a>

### TermsAggregation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| field | [string](#string) |  |  |
| size | [uint32](#uint32) | optional |  |
| split_size | [uint32](#uint32) | optional |  |
| segment_size | [uint32](#uint32) | optional |  |
| show_term_doc_count_error | [bool](#bool) | optional |  |
| min_doc_count | [uint64](#uint64) | optional |  |
| order | [CustomOrder](#summa-proto-CustomOrder) | optional |  |






<a name="summa-proto-TermsResult"></a>

### TermsResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| buckets | [BucketEntry](#summa-proto-BucketEntry) | repeated |  |
| sum_other_doc_count | [uint64](#uint64) |  |  |
| doc_count_error_upper_bound | [uint64](#uint64) | optional |  |






<a name="summa-proto-TopDocsCollector"></a>

### TopDocsCollector



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| limit | [uint32](#uint32) |  |  |
| offset | [uint32](#uint32) |  |  |
| scorer | [Scorer](#summa-proto-Scorer) | optional |  |
| snippets | [TopDocsCollector.SnippetsEntry](#summa-proto-TopDocsCollector-SnippetsEntry) | repeated |  |
| explain | [bool](#bool) |  |  |
| fields | [string](#string) | repeated |  |






<a name="summa-proto-TopDocsCollector-SnippetsEntry"></a>

### TopDocsCollector.SnippetsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [uint32](#uint32) |  |  |






<a name="summa-proto-TopDocsCollectorOutput"></a>

### TopDocsCollectorOutput



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| scored_documents | [ScoredDocument](#summa-proto-ScoredDocument) | repeated |  |
| has_next | [bool](#bool) |  |  |





 <!-- end messages -->


<a name="summa-proto-Occur"></a>

### Occur


| Name | Number | Description |
| ---- | ------ | ----------- |
| should | 0 |  |
| must | 1 |  |
| must_not | 2 |  |


 <!-- end enums -->

 <!-- end HasExtensions -->

 <!-- end services -->



<a name="reflection_service-proto"></a>

## reflection_service.proto



<a name="summa-proto-GetTopTermsRequest"></a>

### GetTopTermsRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index_alias | [string](#string) |  |  |
| field_name | [string](#string) |  |  |
| top_k | [uint32](#uint32) |  |  |






<a name="summa-proto-GetTopTermsResponse"></a>

### GetTopTermsResponse



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| per_segment | [GetTopTermsResponse.PerSegmentEntry](#summa-proto-GetTopTermsResponse-PerSegmentEntry) | repeated |  |






<a name="summa-proto-GetTopTermsResponse-PerSegmentEntry"></a>

### GetTopTermsResponse.PerSegmentEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [SegmentTerms](#summa-proto-SegmentTerms) |  |  |






<a name="summa-proto-SegmentTerms"></a>

### SegmentTerms



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| term_infos | [TermInfo](#summa-proto-TermInfo) | repeated |  |






<a name="summa-proto-TermInfo"></a>

### TermInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [bytes](#bytes) |  |  |
| doc_freq | [uint32](#uint32) |  |  |





 <!-- end messages -->

 <!-- end enums -->

 <!-- end HasExtensions -->


<a name="summa-proto-ReflectionApi"></a>

### ReflectionApi
Analyzes indices

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| get_top_terms | [GetTopTermsRequest](#summa-proto-GetTopTermsRequest) | [GetTopTermsResponse](#summa-proto-GetTopTermsResponse) |  |

 <!-- end services -->



<a name="search_service-proto"></a>

## search_service.proto



<a name="summa-proto-IndexQuery"></a>

### IndexQuery



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index_alias | [string](#string) |  | The index name or alias |
| query | [Query](#summa-proto-Query) |  | Query DSL. Use `MatchQuery` to pass a free-form query |
| collectors | [Collector](#summa-proto-Collector) | repeated | Every collector is responsible of processing and storing documents and/or their derivatives (like counters) to return them to the caller |






<a name="summa-proto-SearchRequest"></a>

### SearchRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index_queries | [IndexQuery](#summa-proto-IndexQuery) | repeated |  |
| tags | [SearchRequest.TagsEntry](#summa-proto-SearchRequest-TagsEntry) | repeated |  |






<a name="summa-proto-SearchRequest-TagsEntry"></a>

### SearchRequest.TagsEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [string](#string) |  |  |





 <!-- end messages -->

 <!-- end enums -->

 <!-- end HasExtensions -->


<a name="summa-proto-SearchApi"></a>

### SearchApi
Searches documents in the stored indices

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| search | [SearchRequest](#summa-proto-SearchRequest) | [SearchResponse](#summa-proto-SearchResponse) |  |

 <!-- end services -->



<a name="utils-proto"></a>

## utils.proto



<a name="summa-proto-Empty"></a>

### Empty






 <!-- end messages -->


<a name="summa-proto-Order"></a>

### Order


| Name | Number | Description |
| ---- | ------ | ----------- |
| Asc | 0 |  |
| Desc | 1 |  |


 <!-- end enums -->

 <!-- end HasExtensions -->

 <!-- end services -->


