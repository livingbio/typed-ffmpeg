//! Schema types for manual filter configuration overrides.

use serde::{Deserialize, Serialize};

/// Manual definitions for FFmpeg filters that can't be fully auto-typed.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FFMpegFilterManuallyDefined {
    #[serde(rename = "__class__", default, skip_serializing_if = "Option::is_none")]
    pub class: Option<String>,
    pub name: String,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub formula_typings_input: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub formula_typings_output: Option<String>,
    #[serde(default)]
    pub pre: Vec<(String, String)>,
}
