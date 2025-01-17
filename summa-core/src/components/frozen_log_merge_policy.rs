use std::fmt::Debug;

use tantivy::merge_policy::{LogMergePolicy, MergeCandidate, MergePolicy};
use tantivy::SegmentMeta;

use super::SummaSegmentAttributes;

#[derive(Debug, Default)]
pub struct FrozenLogMergePolicy(LogMergePolicy);

impl MergePolicy for FrozenLogMergePolicy {
    fn compute_merge_candidates(&self, segments: &[SegmentMeta]) -> Vec<MergeCandidate> {
        let filtered_segments = segments
            .iter()
            .filter(|segment_meta| {
                let segment_attributes = segment_meta.segment_attributes();
                let is_frozen = segment_attributes
                    .as_ref()
                    .map(|segment_attributes| {
                        let parsed_attributes = serde_json::from_value::<SummaSegmentAttributes>(segment_attributes.clone());
                        parsed_attributes.map(|v| v.is_frozen).unwrap_or(false)
                    })
                    .unwrap_or(false);
                !is_frozen
            })
            .cloned()
            .collect::<Vec<SegmentMeta>>();
        self.0.compute_merge_candidates(&filtered_segments)
    }
}
