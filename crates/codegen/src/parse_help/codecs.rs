//! Parse FFmpeg codec information from help output.

use anyhow::Result;
use regex::Regex;
use std::sync::LazyLock;

use super::utils::{parse_av_option, parse_section_tree, run_ffmpeg_command};
use crate::schema::parse_help::{HelpAVOption, HelpCodec};

static RE_CODEC_LIST: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"^\s*([\w\.]{6})\s(\w+)\s+(.*)$").unwrap());

/// Parse the codec list output.
fn parse_list(text: &str) -> Vec<HelpCodec> {
    let mut output = Vec::new();
    for line in text.lines() {
        if let Some(caps) = RE_CODEC_LIST.captures(line) {
            output.push(HelpCodec {
                name: caps[2].to_string(),
                flags: caps[1].to_string(),
                help: caps[3].to_string(),
                options: Vec::new(),
                is_encoder: false,
                is_decoder: false,
            });
        }
    }
    output
}

/// Parse codec options from detailed help text.
fn parse_codec(text: &str) -> Result<Vec<HelpAVOption>> {
    let tree = parse_section_tree(text);
    for section in tree.keys() {
        if section.contains("AVOptions") {
            return parse_av_option(section, &tree);
        }
    }
    Ok(Vec::new())
}

/// Extract codec options for a specific codec.
fn extract_codec(codec: &str, codec_type: &str, ffmpeg_binary: &str) -> Result<Vec<HelpAVOption>> {
    let text = run_ffmpeg_command(&["-h", &format!("{codec_type}={codec}")], ffmpeg_binary)?;
    parse_codec(&text)
}

/// Extract all codec information (encoders and decoders).
pub fn extract(ffmpeg_binary: &str) -> Result<Vec<HelpCodec>> {
    let mut output = Vec::new();

    // Encoders
    let text = run_ffmpeg_command(&["-encoders"], ffmpeg_binary)?;
    for codec in parse_list(&text) {
        let options = extract_codec(&codec.name, "encoder", ffmpeg_binary)?;
        output.push(HelpCodec {
            name: codec.name,
            flags: codec.flags,
            help: codec.help,
            options,
            is_encoder: true,
            is_decoder: false,
        });
    }

    // Decoders
    let text = run_ffmpeg_command(&["-decoders"], ffmpeg_binary)?;
    for codec in parse_list(&text) {
        let options = extract_codec(&codec.name, "decoder", ffmpeg_binary)?;
        output.push(HelpCodec {
            name: codec.name,
            flags: codec.flags,
            help: codec.help,
            options,
            is_encoder: false,
            is_decoder: true,
        });
    }

    Ok(output)
}
