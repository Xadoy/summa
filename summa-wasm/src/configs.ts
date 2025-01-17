export class RemoteEngineConfig {
  method: string;
  url_template: string;
  headers_template: Map<string, string> | null;
  chunked_cache_config?: ChunkedCacheConfig;
  constructor(
    method: string,
    url_template: string,
    headers_template: Map<string, string> | null,
    chunked_cache_config?: ChunkedCacheConfig,
  ) {
    this.method = method
    this.url_template = url_template
    this.headers_template = headers_template;
    this.chunked_cache_config = chunked_cache_config;
  }
}

export class ChunkedCacheConfig {
  chunk_size: number;
  cache_size?: number;
  constructor(
    chunk_size: number,
    cache_size?: number
  ) {
    this.chunk_size = chunk_size
    this.cache_size = cache_size
  }
}

export class IndexAttributes {
  created_at: number;
  primary_key?: string;
  default_fields: string[];
  multi_fields: string[];
  default_index_name?: string;
  description?: string;
  default_snippets?: string;
  constructor(
    created_at: number,
    default_fields: string[],
    multi_fields: string[],
    primary_key?: string,
    default_index_name?: string,
    description?: string,
    default_snippets?: string,
  ) {
    this.created_at = created_at
    this.default_fields = default_fields
    this.multi_fields = multi_fields
    this.primary_key = primary_key
    this.default_index_name = default_index_name
    this.description = description
    this.default_snippets = default_snippets
  }
}
