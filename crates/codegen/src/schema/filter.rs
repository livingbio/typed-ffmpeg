//! Core FFmpeg filter schema types from `ffmpeg_core.common.schema`.
//!
//! These are the authoritative data models for FFMpegFilter, FFMpegFilterOption,
//! and related types. The JSON serialization must match the Python `Serializable`
//! format with `__class__` discriminator tags.

use serde::{Deserialize, Serialize};
use std::collections::HashMap;

/// Stream types in FFmpeg.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub enum StreamType {
    #[serde(rename = "audio")]
    Audio,
    #[serde(rename = "video")]
    Video,
}

/// Data types for FFmpeg filter options.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub enum FFMpegFilterOptionType {
    #[serde(rename = "boolean")]
    Boolean,
    #[serde(rename = "duration")]
    Duration,
    #[serde(rename = "color")]
    Color,
    #[serde(rename = "flags")]
    Flags,
    #[serde(rename = "dictionary")]
    Dictionary,
    #[serde(rename = "pix_fmt")]
    PixFmt,
    #[serde(rename = "int")]
    Int,
    #[serde(rename = "int64")]
    Int64,
    #[serde(rename = "double")]
    Double,
    #[serde(rename = "float")]
    Float,
    #[serde(rename = "string")]
    String,
    #[serde(rename = "video_rate")]
    VideoRate,
    #[serde(rename = "image_size")]
    ImageSize,
    #[serde(rename = "rational")]
    Rational,
    #[serde(rename = "sample_fmt")]
    SampleFmt,
    #[serde(rename = "binary")]
    Binary,
    #[serde(rename = "channel_layout")]
    ChannelLayout,
    #[serde(rename = "unsigned")]
    Unsigned,
}

/// FFmpeg filter type classification.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub enum FFMpegFilterType {
    #[serde(rename = "af")]
    Af,
    #[serde(rename = "asrc")]
    Asrc,
    #[serde(rename = "asink")]
    Asink,
    #[serde(rename = "vf")]
    Vf,
    #[serde(rename = "vsrc")]
    Vsrc,
    #[serde(rename = "vsink")]
    Vsink,
    #[serde(rename = "avsrc")]
    Avsrc,
    #[serde(rename = "avf")]
    Avf,
    #[serde(rename = "vaf")]
    Vaf,
}

/// A single choice for an FFmpeg filter option.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FFMpegFilterOptionChoice {
    #[serde(rename = "__class__", default, skip_serializing_if = "Option::is_none")]
    pub class: Option<String>,
    pub name: String,
    pub help: String,
    #[serde(default)]
    pub value: serde_json::Value,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub flags: Option<String>,
}

/// A configurable option for an FFmpeg filter.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FFMpegFilterOption {
    #[serde(rename = "__class__", default, skip_serializing_if = "Option::is_none")]
    pub class: Option<String>,
    pub name: String,
    #[serde(default)]
    pub alias: Vec<String>,
    #[serde(default)]
    pub description: String,
    #[serde(rename = "type")]
    pub option_type: FFMpegFilterOptionType,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub min: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub max: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub default: Option<serde_json::Value>,
    #[serde(default)]
    pub required: bool,
    #[serde(default)]
    pub choices: Vec<FFMpegFilterOptionChoice>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub flags: Option<String>,
}

/// Input/output stream type for a filter.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FFMpegIOType {
    #[serde(rename = "__class__", default, skip_serializing_if = "Option::is_none")]
    pub class: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub name: Option<String>,
    #[serde(rename = "type")]
    pub stream_type: StreamType,
}

/// Comprehensive representation of an FFmpeg filter.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FFMpegFilter {
    #[serde(rename = "__class__", default, skip_serializing_if = "Option::is_none")]
    pub class: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub id: Option<String>,
    pub name: String,
    #[serde(default)]
    pub description: String,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub r#ref: Option<String>,

    // Flags
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub is_support_slice_threading: Option<bool>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub is_support_timeline: Option<bool>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub is_support_framesync: Option<bool>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub is_support_command: Option<bool>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub is_filter_sink: Option<bool>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub is_filter_source: Option<bool>,

    // IO Typing
    #[serde(default)]
    pub is_dynamic_input: bool,
    #[serde(default)]
    pub is_dynamic_output: bool,
    #[serde(default)]
    pub stream_typings_input: Vec<FFMpegIOType>,
    #[serde(default)]
    pub stream_typings_output: Vec<FFMpegIOType>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub formula_typings_input: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub formula_typings_output: Option<String>,

    #[serde(default)]
    pub pre: Vec<(String, String)>,
    #[serde(default)]
    pub options: Vec<FFMpegFilterOption>,
}

impl FFMpegFilter {
    /// Convert pre-defined parameter pairs to a HashMap.
    pub fn pre_dict(&self) -> HashMap<String, String> {
        self.pre.iter().cloned().collect()
    }

    /// Determine the set of input stream types.
    pub fn input_typings(&self) -> std::collections::HashSet<StreamType> {
        if self.is_filter_source.unwrap_or(false) {
            return std::collections::HashSet::new();
        }
        if !self.is_dynamic_input {
            return self.stream_typings_input.iter().map(|io| io.stream_type).collect();
        }
        if let Some(ref formula) = self.formula_typings_input {
            let mut set = std::collections::HashSet::new();
            if formula.contains("video") {
                set.insert(StreamType::Video);
            }
            if formula.contains("audio") {
                set.insert(StreamType::Audio);
            }
            if set.is_empty() {
                set.insert(StreamType::Video); // fallback
            }
            set
        } else {
            let mut set = std::collections::HashSet::new();
            set.insert(StreamType::Video); // fallback
            set
        }
    }

    /// Determine the set of output stream types.
    pub fn output_typings(&self) -> std::collections::HashSet<StreamType> {
        if self.is_filter_sink.unwrap_or(false) {
            return std::collections::HashSet::new();
        }
        if !self.is_dynamic_output {
            return self.stream_typings_output.iter().map(|io| io.stream_type).collect();
        }
        if let Some(ref formula) = self.formula_typings_output {
            let mut set = std::collections::HashSet::new();
            if formula.contains("video") {
                set.insert(StreamType::Video);
            }
            if formula.contains("audio") {
                set.insert(StreamType::Audio);
            }
            set
        } else {
            std::collections::HashSet::new()
        }
    }

    /// Determine the filter type classification.
    pub fn filter_type(&self) -> FFMpegFilterType {
        let inputs = self.input_typings();
        let outputs = self.output_typings();

        if self.is_filter_sink.unwrap_or(false) {
            if inputs.contains(&StreamType::Video) {
                return FFMpegFilterType::Vsink;
            }
            if inputs.contains(&StreamType::Audio) {
                return FFMpegFilterType::Asink;
            }
        } else if self.is_filter_source.unwrap_or(false) {
            if outputs.contains(&StreamType::Video) && outputs.contains(&StreamType::Audio) {
                return FFMpegFilterType::Avsrc;
            }
            if outputs.contains(&StreamType::Video) {
                return FFMpegFilterType::Vsrc;
            }
            if outputs.contains(&StreamType::Audio) {
                return FFMpegFilterType::Asrc;
            }
        }

        if inputs.is_empty() {
            if outputs.contains(&StreamType::Video) {
                return FFMpegFilterType::Vf;
            }
            if outputs.contains(&StreamType::Audio) {
                return FFMpegFilterType::Af;
            }
            return FFMpegFilterType::Vf; // default fallback
        }

        let has_video_in = inputs.contains(&StreamType::Video);
        let has_audio_in = inputs.contains(&StreamType::Audio);
        let has_video_out = outputs.contains(&StreamType::Video);
        let has_audio_out = outputs.contains(&StreamType::Audio);

        if has_video_in && !has_audio_in {
            if has_audio_out {
                return FFMpegFilterType::Vaf;
            }
            if has_video_out {
                return FFMpegFilterType::Vf;
            }
        }

        if has_audio_in && !has_video_in {
            if has_audio_out && !has_video_out {
                return FFMpegFilterType::Af;
            }
            if has_video_out {
                return FFMpegFilterType::Avf;
            }
        }

        if has_video_in && has_audio_in {
            return FFMpegFilterType::Avf;
        }

        FFMpegFilterType::Vf // fallback
    }
}
