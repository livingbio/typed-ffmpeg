//! Schema types for the code generation layer.
//!
//! These mirror `src/scripts/code_gen/schema.py` - the types used after
//! parse_help data is transformed for code generation purposes.

use regex::Regex;
use serde::{Deserialize, Serialize};
use std::sync::LazyLock;

/// Minimum supported FFmpeg version.
pub const MIN_FFMPEG_VERSION_MAJOR: u32 = 5;
pub const MIN_FFMPEG_VERSION_MINOR: u32 = 0;

/// Convert a version string like "6.0" to a cache key like "6_0".
pub fn version_cache_key(version: &str) -> String {
    version.replace('.', "_")
}

/// Parse major.minor from a version string or ffmpeg -version output.
pub fn parse_version(version_str: &str) -> anyhow::Result<(u32, u32)> {
    static RE: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"(\d+)\.(\d+)").unwrap());

    let caps = RE
        .captures(version_str)
        .ok_or_else(|| anyhow::anyhow!("Cannot parse version from: {version_str:?}"))?;

    Ok((caps[1].parse()?, caps[2].parse()?))
}

/// Check if a version is supported (>= 5.0).
pub fn is_supported_version(version: &str) -> anyhow::Result<bool> {
    let (major, minor) = parse_version(version)?;
    Ok((major, minor) >= (MIN_FFMPEG_VERSION_MAJOR, MIN_FFMPEG_VERSION_MINOR))
}

/// Possible option types for codec/format/filter AV options.
pub type FFMpegOptionType = String;

/// A choice option for FFmpeg parameters.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CodegenOptionChoice {
    #[serde(rename = "__class__", default, skip_serializing_if = "Option::is_none")]
    pub class: Option<String>,
    pub name: String,
    pub help: String,
    pub flags: String,
    pub value: String,
}

/// An FFmpeg AV option with metadata (codegen layer).
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CodegenAVOption {
    #[serde(rename = "__class__", default, skip_serializing_if = "Option::is_none")]
    pub class: Option<String>,
    pub section: String,
    pub name: String,
    #[serde(rename = "type")]
    pub option_type: String,
    pub flags: String,
    pub help: String,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub min: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub max: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub default: Option<String>,
    #[serde(default)]
    pub choices: Vec<CodegenOptionChoice>,
}

impl CodegenAVOption {
    /// Get the Python type annotation for this option.
    pub fn code_gen_type(&self) -> String {
        let base = match self.option_type.as_str() {
            "boolean" => "bool | None",
            "int" | "int64" | "unsigned" => "int | None",
            "float" | "double" => "float | None",
            "sample_rate" => "int | None",
            "string" | "channel_layout" | "flags" | "duration" | "dictionary" | "image_size"
            | "pixel_format" | "sample_fmt" | "binary" | "rational" | "color" | "video_rate"
            | "pix_fmt" => "str | None",
            other => panic!("Invalid option type: {other}"),
        };

        let choices_suffix = if self.option_type != "flags" && !self.choices.is_empty() {
            let literals: Vec<String> = self
                .choices
                .iter()
                .map(|c| format!("\"{}\"", c.name))
                .collect();
            format!("| Literal[{}]", literals.join(", "))
        } else {
            String::new()
        };

        format!("{base}{choices_suffix}")
    }
}

/// Base class for FFmpeg codecs (codegen layer).
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(tag = "__class__")]
pub enum CodegenCodec {
    FFMpegEncoder(CodegenCodecData),
    FFMpegDecoder(CodegenCodecData),
}

/// Codec data shared between encoders and decoders.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CodegenCodecData {
    pub name: String,
    pub flags: String,
    pub description: String,
    #[serde(default)]
    pub options: Vec<CodegenAVOption>,
}

impl CodegenCodec {
    pub fn data(&self) -> &CodegenCodecData {
        match self {
            CodegenCodec::FFMpegEncoder(d) | CodegenCodec::FFMpegDecoder(d) => d,
        }
    }

    pub fn is_encoder(&self) -> bool {
        matches!(self, CodegenCodec::FFMpegEncoder(_))
    }

    pub fn is_decoder(&self) -> bool {
        matches!(self, CodegenCodec::FFMpegDecoder(_))
    }

    /// Get the codec type from flags.
    pub fn codec_type(&self) -> &str {
        match self.data().flags.chars().next() {
            Some('V') => "video",
            Some('A') => "audio",
            Some('S') => "subtitle",
            _ => "unknown",
        }
    }
}

/// Base class for FFmpeg formats (codegen layer).
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(tag = "__class__")]
pub enum CodegenFormat {
    FFMpegMuxer(CodegenFormatData),
    FFMpegDemuxer(CodegenFormatData),
}

/// Format data shared between muxers and demuxers.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CodegenFormatData {
    pub name: String,
    pub flags: String,
    pub description: String,
    #[serde(default)]
    pub options: Vec<CodegenAVOption>,
}

impl CodegenFormat {
    pub fn data(&self) -> &CodegenFormatData {
        match self {
            CodegenFormat::FFMpegMuxer(d) | CodegenFormat::FFMpegDemuxer(d) => d,
        }
    }

    pub fn is_muxer(&self) -> bool {
        matches!(self, CodegenFormat::FFMpegMuxer(_))
    }

    pub fn is_demuxer(&self) -> bool {
        matches!(self, CodegenFormat::FFMpegDemuxer(_))
    }
}
