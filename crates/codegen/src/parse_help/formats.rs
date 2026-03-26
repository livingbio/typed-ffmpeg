//! Parse FFmpeg format information from help output.

use anyhow::Result;
use regex::Regex;
use std::sync::LazyLock;

use super::utils::{parse_av_option, parse_section_tree, run_ffmpeg_command};
use crate::schema::parse_help::{HelpAVOption, HelpFormat};

static RE_FORMAT_LIST: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"^\s*(?P<flag>[DE]+)\s*(?P<name>\w+)\s+(?P<help>.*)$").unwrap());

/// Parse the format list output.
fn parse_list(text: &str) -> Vec<HelpFormat> {
    let mut output = Vec::new();
    for line in text.lines() {
        if let Some(caps) = RE_FORMAT_LIST.captures(line) {
            output.push(HelpFormat {
                name: caps["name"].to_string(),
                flags: caps["flag"].to_string(),
                help: caps["help"].to_string(),
                options: Vec::new(),
            });
        }
    }
    output
}

/// Parse format options from detailed help text.
fn parse_format(text: &str) -> Result<Vec<HelpAVOption>> {
    let tree = parse_section_tree(text);
    for section in tree.keys() {
        if section.contains("AVOptions") {
            return parse_av_option(section, &tree);
        }
    }
    Ok(Vec::new())
}

/// Extract format options for a specific format.
fn extract_format(
    format: &str,
    format_type: &str,
    ffmpeg_binary: &str,
) -> Result<Vec<HelpAVOption>> {
    let text = run_ffmpeg_command(&["-h", &format!("{format_type}={format}")], ffmpeg_binary)?;
    parse_format(&text)
}

/// Extract all format information (muxers and demuxers).
pub fn extract(ffmpeg_binary: &str) -> Result<Vec<HelpFormat>> {
    let mut output = Vec::new();

    // Muxers
    let text = run_ffmpeg_command(&["-muxers"], ffmpeg_binary)?;
    for fmt in parse_list(&text) {
        let options = extract_format(&fmt.name, "muxer", ffmpeg_binary)?;
        output.push(HelpFormat {
            name: fmt.name,
            flags: fmt.flags,
            help: fmt.help,
            options,
        });
    }

    // Demuxers
    let text = run_ffmpeg_command(&["-demuxers"], ffmpeg_binary)?;
    for fmt in parse_list(&text) {
        let options = extract_format(&fmt.name, "demuxer", ffmpeg_binary)?;
        output.push(HelpFormat {
            name: fmt.name,
            flags: fmt.flags,
            help: fmt.help,
            options,
        });
    }

    Ok(output)
}
