//! Schema types from `parse_c/schema.py`.
//!
//! Represents FFmpeg command-line options parsed from C source code.

use serde::{Deserialize, Serialize};

/// FFmpeg option flags that define option behavior.
/// These are bitmask flags from FFmpeg's cmdutils.h.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct FFMpegOptionFlag;

impl FFMpegOptionFlag {
    pub const OPT_FUNC_ARG: u32 = 1 << 0;
    pub const OPT_EXIT: u32 = 1 << 1;
    pub const OPT_EXPERT: u32 = 1 << 2;
    pub const OPT_VIDEO: u32 = 1 << 3;
    pub const OPT_AUDIO: u32 = 1 << 4;
    pub const OPT_SUBTITLE: u32 = 1 << 5;
    pub const OPT_DATA: u32 = 1 << 6;
    pub const OPT_PERFILE: u32 = 1 << 7;
    pub const OPT_FLAG_OFFSET: u32 = 1 << 8;
    pub const OPT_OFFSET: u32 = Self::OPT_FLAG_OFFSET | Self::OPT_PERFILE;
    pub const OPT_FLAG_SPEC: u32 = 1 << 9;
    pub const OPT_SPEC: u32 = Self::OPT_FLAG_SPEC | Self::OPT_OFFSET;
    pub const OPT_FLAG_PERSTREAM: u32 = 1 << 10;
    pub const OPT_PERSTREAM: u32 = Self::OPT_FLAG_PERSTREAM | Self::OPT_SPEC;
    pub const OPT_INPUT: u32 = 1 << 11;
    pub const OPT_OUTPUT: u32 = 1 << 12;
    pub const OPT_HAS_ALT: u32 = 1 << 13;
    pub const OPT_HAS_CANON: u32 = 1 << 14;

    /// Evaluate a flag expression like "OPT_VIDEO | OPT_INPUT | OPT_PERFILE".
    pub fn eval_flags_expr(expr: &str) -> anyhow::Result<u32> {
        let mut result: u32 = 0;
        for part in expr.split('|') {
            let part = part.trim();
            let value = match part {
                "OPT_FUNC_ARG" => Self::OPT_FUNC_ARG,
                "OPT_EXIT" => Self::OPT_EXIT,
                "OPT_EXPERT" => Self::OPT_EXPERT,
                "OPT_VIDEO" => Self::OPT_VIDEO,
                "OPT_AUDIO" => Self::OPT_AUDIO,
                "OPT_SUBTITLE" => Self::OPT_SUBTITLE,
                "OPT_DATA" => Self::OPT_DATA,
                "OPT_PERFILE" => Self::OPT_PERFILE,
                "OPT_FLAG_OFFSET" => Self::OPT_FLAG_OFFSET,
                "OPT_OFFSET" => Self::OPT_OFFSET,
                "OPT_FLAG_SPEC" => Self::OPT_FLAG_SPEC,
                "OPT_SPEC" => Self::OPT_SPEC,
                "OPT_FLAG_PERSTREAM" => Self::OPT_FLAG_PERSTREAM,
                "OPT_PERSTREAM" => Self::OPT_PERSTREAM,
                "OPT_INPUT" => Self::OPT_INPUT,
                "OPT_OUTPUT" => Self::OPT_OUTPUT,
                "OPT_HAS_ALT" => Self::OPT_HAS_ALT,
                "OPT_HAS_CANON" => Self::OPT_HAS_CANON,
                _ => anyhow::bail!("Unknown flag constant: {part}"),
            };
            result |= value;
        }
        Ok(result)
    }
}

/// FFmpeg option data types from C source.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
pub enum FFMpegOptionType {
    #[serde(rename = "OPT_TYPE_FUNC")]
    Func,
    #[serde(rename = "OPT_TYPE_BOOL")]
    Bool,
    #[serde(rename = "OPT_TYPE_STRING")]
    String,
    #[serde(rename = "OPT_TYPE_INT")]
    Int,
    #[serde(rename = "OPT_TYPE_INT64")]
    Int64,
    #[serde(rename = "OPT_TYPE_FLOAT")]
    Float,
    #[serde(rename = "OPT_TYPE_DOUBLE")]
    Double,
    #[serde(rename = "OPT_TYPE_TIME")]
    Time,
}

/// A command-line option for FFmpeg parsed from C source.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FFMpegOption {
    #[serde(rename = "__class__", default, skip_serializing_if = "Option::is_none")]
    pub class: Option<String>,
    pub name: String,
    #[serde(rename = "type")]
    pub option_type: FFMpegOptionType,
    pub flags: u32,
    pub help: String,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub argname: Option<String>,
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub canon: Option<String>,
}

impl FFMpegOption {
    pub fn is_input_option(&self) -> bool {
        self.flags & FFMpegOptionFlag::OPT_INPUT != 0
    }

    pub fn is_output_option(&self) -> bool {
        self.flags & FFMpegOptionFlag::OPT_OUTPUT != 0
    }

    pub fn is_global_option(&self) -> bool {
        !self.is_input_option()
            && !self.is_output_option()
            && (self.flags & FFMpegOptionFlag::OPT_EXIT == 0)
    }

    pub fn is_support_stream_specifier(&self) -> bool {
        self.flags & FFMpegOptionFlag::OPT_SPEC != 0
    }
}
