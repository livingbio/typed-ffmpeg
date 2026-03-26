//! Schema types from `parse_help/schema.py`.
//!
//! These represent the raw parsed output from FFmpeg help text,
//! before transformation into codegen types.

use serde::{Deserialize, Serialize};

/// An FFmpeg option from help text output.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HelpOption {
    pub section: String,
    pub name: String,
    #[serde(rename = "type", default, skip_serializing_if = "Option::is_none")]
    pub option_type: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub flags: Option<String>,
    pub help: String,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub argname: Option<String>,
}

/// A choice value for an AV option.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HelpOptionChoice {
    pub name: String,
    pub help: String,
    pub flags: String,
    pub value: String,
}

/// An FFmpeg AV option with additional metadata.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HelpAVOption {
    pub section: String,
    pub name: String,
    #[serde(rename = "type", default, skip_serializing_if = "Option::is_none")]
    pub option_type: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub flags: Option<String>,
    pub help: String,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub argname: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub min: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub max: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub default: Option<String>,
    #[serde(default)]
    pub choices: Vec<HelpOptionChoice>,
}

/// Base class for sets of FFmpeg options.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HelpOptionSet {
    pub name: String,
    pub flags: String,
    pub help: String,
    #[serde(default)]
    pub options: Vec<HelpAVOption>,
}

/// FFmpeg IO type for filter inputs/outputs.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HelpIOType {
    #[serde(default)]
    pub name: Option<String>,
    #[serde(rename = "type")]
    pub stream_type: String, // "audio" or "video"
}

/// A parsed FFmpeg filter from help output.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HelpFilter {
    pub name: String,
    pub flags: String,
    pub help: String,
    pub io_flags: String,
    #[serde(default)]
    pub options: Vec<HelpAVOption>,
    #[serde(default)]
    pub stream_typings_input: Vec<HelpIOType>,
    #[serde(default)]
    pub stream_typings_output: Vec<HelpIOType>,
    #[serde(default)]
    pub is_dynamic_input: bool,
    #[serde(default)]
    pub is_dynamic_output: bool,
    #[serde(default)]
    pub is_framesync: bool,
    #[serde(default)]
    pub is_slice_threading: bool,
    #[serde(default)]
    pub is_timeline: bool,
}

/// A parsed FFmpeg codec from help output.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HelpCodec {
    pub name: String,
    pub flags: String,
    pub help: String,
    #[serde(default)]
    pub options: Vec<HelpAVOption>,
    pub is_encoder: bool,
    pub is_decoder: bool,
}

/// A parsed FFmpeg format from help output.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct HelpFormat {
    pub name: String,
    pub flags: String,
    pub help: String,
    #[serde(default)]
    pub options: Vec<HelpAVOption>,
}
