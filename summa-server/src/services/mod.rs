//! Services responsible for various aspects a search engine like indices management or aliasing

pub(crate) mod api;
pub(crate) mod gateway;
pub(crate) mod index;
pub(crate) mod metrics;
pub(crate) mod p2p;
pub(crate) mod store;

pub use api::Api;
pub use index::Index;
pub use metrics::Metrics;
pub use p2p::P2p;
pub use store::Store;
