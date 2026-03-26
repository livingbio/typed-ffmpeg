//! Parse FFmpeg filter information from help output.

use anyhow::{bail, Result};
use regex::Regex;
use std::sync::LazyLock;

use super::utils::{glob, parse_av_option, parse_section_tree, run_ffmpeg_command};
use crate::schema::parse_help::{HelpAVOption, HelpFilter, HelpIOType};

static RE_FILTER_LIST: LazyLock<Regex> = LazyLock::new(|| {
    Regex::new(
        r"^\s*(?P<flag>[\w\.]{2,3})\s+(?P<name>\w+)\s+(?P<io_flags>[\w\|]+\->[\w\|]+)\s+(?P<help>.*)$",
    )
    .unwrap()
});

static RE_FILTER_IO: LazyLock<Regex> = LazyLock::new(|| {
    Regex::new(r"#(?P<index>\d+):\s*(?P<name>\w+)\s*\((?P<type>\w+)\)").unwrap()
});

/// Parse the filter list output from `ffmpeg -filters`.
fn parse_list(text: &str) -> Vec<HelpFilter> {
    let mut output = Vec::new();
    for line in text.lines() {
        if let Some(caps) = RE_FILTER_LIST.captures(line) {
            output.push(HelpFilter {
                name: caps["name"].to_string(),
                flags: caps["flag"].to_string(),
                io_flags: caps["io_flags"].to_string(),
                help: caps["help"].to_string(),
                options: Vec::new(),
                stream_typings_input: Vec::new(),
                stream_typings_output: Vec::new(),
                is_dynamic_input: false,
                is_dynamic_output: false,
                is_framesync: false,
                is_slice_threading: false,
                is_timeline: false,
            });
        }
    }
    output
}

/// Parse IO types from a section tree.
fn parse_io_from_tree(tree: &super::utils::SectionTree) -> Vec<HelpIOType> {
    let mut output = Vec::new();
    for (key, _) in tree {
        if key.starts_with('#') {
            if let Some(caps) = RE_FILTER_IO.captures(key) {
                let stream_type = caps["type"].to_string();
                if stream_type == "audio" || stream_type == "video" {
                    output.push(HelpIOType {
                        name: Some(caps["name"].to_string()),
                        stream_type,
                    });
                }
            }
        }
    }
    output
}

/// Parse the detailed help text for a single filter.
fn parse_filter(text: &str) -> Result<HelpFilter> {
    if text.contains("Unknown filter") {
        bail!("Unknown filter");
    }

    let tree = parse_section_tree(text);

    let is_framesync = !glob(&tree, r"framesync AVOptions").is_empty();
    let is_slice_threading = !glob(&tree, r"slice threading supported").is_empty();
    let is_timeline = !glob(&tree, r"This filter has support for timeline").is_empty();

    let filter_matches = glob(&tree, r"^Filter");
    let (section_key, subtree) = filter_matches
        .first()
        .ok_or_else(|| anyhow::anyhow!("No Filter section found"))?;
    let name = section_key
        .split_whitespace()
        .nth(1)
        .unwrap_or("")
        .to_string();
    let help = subtree
        .keys()
        .next()
        .cloned()
        .unwrap_or_default();

    let mut options: Vec<HelpAVOption> = Vec::new();
    let av_matches = glob(&tree, r".*AVOptions");
    if let Some((section, _)) = av_matches.first() {
        options = parse_av_option(section, &tree)?;
    }

    let input_matches = glob(&tree, "Inputs:");
    let (mut is_dynamic_input, mut input_types) = (false, Vec::new());
    if let Some((_, input_subtree)) = input_matches.first() {
        if !glob(input_subtree, r"dynamic \(depending on the options\)").is_empty() {
            is_dynamic_input = true;
        } else {
            input_types = parse_io_from_tree(input_subtree);
        }
    }

    let output_matches = glob(&tree, "Outputs:");
    let (mut is_dynamic_output, mut output_types) = (false, Vec::new());
    if let Some((_, output_subtree)) = output_matches.first() {
        if !glob(output_subtree, r"dynamic \(depending on the options\)").is_empty() {
            is_dynamic_output = true;
        } else {
            output_types = parse_io_from_tree(output_subtree);
        }
    }

    Ok(HelpFilter {
        name,
        help,
        flags: String::new(),
        io_flags: String::new(),
        options,
        stream_typings_input: input_types,
        stream_typings_output: output_types,
        is_dynamic_input,
        is_dynamic_output,
        is_framesync,
        is_slice_threading,
        is_timeline,
    })
}

/// Extract detailed info for a single filter.
fn extract_filter(filter_name: &str, ffmpeg_binary: &str) -> Result<HelpFilter> {
    let text = run_ffmpeg_command(&["-h", &format!("filter={filter_name}")], ffmpeg_binary)?;
    parse_filter(&text)
}

/// Extract all filter information from the FFmpeg binary.
pub fn extract(ffmpeg_binary: &str) -> Result<Vec<HelpFilter>> {
    let list_text = run_ffmpeg_command(&["-filters"], ffmpeg_binary)?;
    let filter_list = parse_list(&list_text);

    let mut output = Vec::new();
    for list_filter in &filter_list {
        match extract_filter(&list_filter.name, ffmpeg_binary) {
            Ok(mut detailed) => {
                detailed.flags = list_filter.flags.clone();
                detailed.io_flags = list_filter.io_flags.clone();
                output.push(detailed);
            }
            Err(e) => {
                log::warn!("Failed to parse filter {}: {e}", list_filter.name);
            }
        }
    }

    Ok(output)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse_filter_list() {
        let text = r#"Filters:
  T.. = Timeline support
  .S. = Slice threading
  ..C = Command support
 ... abench            A->A       Benchmark part of a filtergraph.
 ..C acompressor       A->A       Audio compressor.
 T.C overlay           VV->V      Overlay a video source on top of the input.
"#;
        let filters = parse_list(text);
        assert_eq!(filters.len(), 3);
        assert_eq!(filters[0].name, "abench");
        assert_eq!(filters[0].io_flags, "A->A");
        assert_eq!(filters[2].name, "overlay");
        assert_eq!(filters[2].io_flags, "VV->V");
    }
}
