use std::collections::HashMap;
use std::default::Default;

use serde::{Deserialize, Serialize};
use summa_proto::proto::IndexEngineConfig;

use crate::errors::{BuilderError, SummaResult, ValidationError};

#[derive(Builder, Clone, Debug, Serialize, Deserialize)]
#[builder(default, build_fn(error = "BuilderError"))]
pub struct Config {
    #[serde(default = "HashMap::new")]
    pub aliases: HashMap<String, String>,
    #[serde(default = "HashMap::new")]
    pub indices: HashMap<String, IndexEngineConfig>,
    #[builder(default = "None")]
    pub autocommit_interval_ms: Option<u64>,
    #[builder(default = "1024 * 1024 * 1024")]
    pub writer_heap_size_bytes: u64,
    #[builder(default = "1")]
    pub writer_threads: u64,
}

impl Default for Config {
    fn default() -> Self {
        Config {
            aliases: HashMap::new(),
            indices: HashMap::new(),
            autocommit_interval_ms: None,
            writer_heap_size_bytes: 1024 * 1024 * 1024,
            writer_threads: 1,
        }
    }
}

impl Config {
    /// Copy aliases for the index
    pub fn get_index_aliases_for_index(&self, index_name: &str) -> Vec<String> {
        self.aliases
            .iter()
            .filter(|(_, v)| *v == index_name)
            .map(|(k, _)| k.clone())
            .collect::<Vec<String>>()
    }

    /// Find index by alias
    pub fn resolve_index_alias(&self, alias: &str) -> Option<String> {
        self.aliases.get(alias).cloned()
    }

    /// Set new alias for index
    pub fn set_index_alias(&mut self, alias: &str, index_name: &str) -> SummaResult<Option<String>> {
        if alias.is_empty() {
            return Err(ValidationError::EmptyArgument("alias".to_owned()).into());
        }
        if index_name.is_empty() {
            return Err(ValidationError::EmptyArgument("index_name".to_owned()).into());
        }
        if !self.indices.contains_key(index_name) {
            return Err(ValidationError::MissingIndex(index_name.to_owned()).into());
        }
        Ok(self.aliases.insert(alias.to_owned(), index_name.to_owned()))
    }

    /// Delete all aliases listed in `index_aliases`
    pub fn delete_index_aliases(&mut self, index_aliases: &Vec<String>) {
        for alias in index_aliases {
            self.aliases.remove(alias);
        }
    }
}
