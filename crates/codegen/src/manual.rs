//! Manual configuration overrides for complex filters.

use anyhow::Result;
use std::path::Path;

use crate::cache;
use crate::schema::manual::FFMpegFilterManuallyDefined;

/// Load manual configuration for a specific filter.
pub fn load_config(
    cache_dir: &Path,
    filter_name: &str,
) -> Result<Option<FFMpegFilterManuallyDefined>> {
    let id = format!("manual_{filter_name}");
    cache::load(cache_dir, &id)
}

/// Initialize default manual configurations for filters with dynamic I/O.
pub fn init_config(cache_dir: &Path, filter_name: &str) -> Result<()> {
    let config = FFMpegFilterManuallyDefined {
        class: Some("FFMpegFilterManuallyDefined".to_string()),
        name: filter_name.to_string(),
        formula_typings_input: None,
        formula_typings_output: None,
        pre: Vec::new(),
    };
    cache::save(cache_dir, &format!("manual_{filter_name}"), &config)
}
