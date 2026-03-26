//! Core parsing utilities for FFmpeg help output.

use anyhow::{bail, Context, Result};
use regex::Regex;
use std::collections::BTreeMap;
use std::process::Command;
use std::sync::LazyLock;

use crate::schema::codegen::parse_version;
use crate::schema::parse_help::{HelpAVOption, HelpOption, HelpOptionChoice};

/// Valid FFmpeg option types.
const VALID_OPTION_TYPES: &[&str] = &[
    "boolean",
    "duration",
    "color",
    "flags",
    "dictionary",
    "pix_fmt",
    "int",
    "int64",
    "unsigned",
    "double",
    "float",
    "string",
    "video_rate",
    "image_size",
    "rational",
    "sample_fmt",
    "binary",
    "channel_layout",
    "pixel_format",
    "sample_rate",
];

/// A tree node in the parsed help output.
/// We use `serde_json::Map` since Rust type aliases can't be recursive.
/// This is effectively `BTreeMap<String, SectionTree>`.
#[derive(Debug, Clone, Default)]
pub struct SectionTree(pub BTreeMap<String, SectionTree>);

impl SectionTree {
    pub fn new() -> Self {
        SectionTree(BTreeMap::new())
    }

    pub fn insert(&mut self, key: String, value: SectionTree) {
        self.0.insert(key, value);
    }

    pub fn get(&self, key: &str) -> Option<&SectionTree> {
        self.0.get(key)
    }

    pub fn get_mut(&mut self, key: &str) -> Option<&mut SectionTree> {
        self.0.get_mut(key)
    }

    pub fn keys(&self) -> impl Iterator<Item = &String> {
        self.0.keys()
    }

    pub fn iter(&self) -> impl Iterator<Item = (&String, &SectionTree)> {
        self.0.iter()
    }

    pub fn is_empty(&self) -> bool {
        self.0.is_empty()
    }

    pub fn contains_key(&self, key: &str) -> bool {
        self.0.contains_key(key)
    }
}

impl<'a> IntoIterator for &'a SectionTree {
    type Item = (&'a String, &'a SectionTree);
    type IntoIter = std::collections::btree_map::Iter<'a, String, SectionTree>;

    fn into_iter(self) -> Self::IntoIter {
        self.0.iter()
    }
}

/// Execute an ffmpeg command and return stdout.
pub fn run_ffmpeg_command(args: &[&str], ffmpeg_binary: &str) -> Result<String> {
    let mut cmd_args: Vec<&str> = args.to_vec();
    cmd_args.push("-hide_banner");

    let output = Command::new(ffmpeg_binary)
        .args(&cmd_args)
        .output()
        .with_context(|| format!("Failed to run {ffmpeg_binary}"))?;

    Ok(String::from_utf8_lossy(&output.stdout).to_string())
}

/// Get the FFmpeg version string (major.minor).
pub fn get_ffmpeg_version(ffmpeg_binary: &str) -> Result<String> {
    let output = run_ffmpeg_command(&["-version"], ffmpeg_binary)?;
    let first_line = output.lines().next().unwrap_or("");
    let (major, minor) = parse_version(first_line)?;
    Ok(format!("{major}.{minor}"))
}

/// Count leading indent, with special handling for lines starting with '-'.
fn count_indent(line: &str) -> usize {
    for (i, ch) in line.chars().enumerate() {
        if ch != ' ' {
            if ch == '-' {
                return i + 1;
            } else {
                return i;
            }
        }
    }
    line.len()
}

/// Parse indented help text into a nested tree structure.
pub fn parse_section_tree(text: &str) -> SectionTree {
    let mut output = SectionTree::new();
    let mut paths: Vec<(usize, String)> = Vec::new();

    for line in text.lines() {
        let indent = count_indent(line);
        let trimmed = line.trim();
        if trimmed.is_empty() {
            continue;
        }

        // Remove all paths with indent >= current
        paths.retain(|(ind, _)| *ind < indent);

        // Navigate to insertion point
        let mut insert_node = &mut output;
        for (_, key) in &paths {
            insert_node = insert_node.get_mut(key).unwrap();
        }

        insert_node.insert(trimmed.to_string(), SectionTree::new());
        paths.push((indent, trimmed.to_string()));
    }

    output
}

/// Search a tree for keys matching a regex pattern (recursive).
pub fn glob(tree: &SectionTree, pattern: &str) -> Vec<(String, SectionTree)> {
    let re = Regex::new(pattern).unwrap();
    let mut results = Vec::new();
    glob_inner(tree, &re, &mut results);
    results
}

fn glob_inner(tree: &SectionTree, re: &Regex, results: &mut Vec<(String, SectionTree)>) {
    for (key, value) in tree {
        if re.is_match(key) {
            results.push((key.clone(), value.clone()));
        } else {
            glob_inner(value, re, results);
        }
    }
}

// Regex patterns for parsing options and choices
// Matches: name  value  flags  help
// "name" is everything up to first double-space (replaced lookahead with [^ ]+(?: [^ ]+)*)
static RE_CHOICE_WITH_VALUE: LazyLock<Regex> = LazyLock::new(|| {
    Regex::new(
        r"^(?P<name>[^ ]+(?:\s[^ ]+)*?)\s{2,}(?P<value>[\d\-]+)\s+(?P<flags>[\w\.]{11})(?P<help>\s+.*)?",
    )
    .unwrap()
});

static RE_CHOICE_WITHOUT_VALUE: LazyLock<Regex> = LazyLock::new(|| {
    Regex::new(r"^(?P<name>[^ ]+(?:\s[^ ]+)*?)\s{2,}(?P<flags>[\w\.]{11})(?P<help>\s+.*)?")
        .unwrap()
});

static RE_OPTION: LazyLock<Regex> = LazyLock::new(|| {
    Regex::new(
        r"(?P<name>[\-\w]+)\s+\[?<(?P<type>[\w]+)>\s*\]?\s*(?P<flags>[\w\.]{11})\s*(?P<help>.*)?",
    )
    .unwrap()
});

static RE_MIN_MAX: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"\(from\s+(?P<min>.+?)\s+to\s+(?P<max>.+?)\)").unwrap());

static RE_DEFAULT: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"\(default\s+(?P<default>.+?)\)$").unwrap());

/// Extract min, max, and default values from a help string.
fn extract_min_max_default(help: &str) -> (Option<String>, Option<String>, Option<String>) {
    let (min, max) = if let Some(caps) = RE_MIN_MAX.captures(help) {
        (
            Some(caps["min"].to_string()),
            Some(caps["max"].to_string()),
        )
    } else {
        (None, None)
    };

    let default = RE_DEFAULT
        .captures(help)
        .map(|caps| caps["default"].trim_matches('"').to_string());

    (min, max, default)
}

/// Validate that a string is a valid FFmpeg option type.
fn validate_option_type(value: &str) -> Result<String> {
    if VALID_OPTION_TYPES.contains(&value) {
        Ok(value.to_string())
    } else {
        bail!("Invalid option type: {value}")
    }
}

/// Parse a section of AVOptions from a tree structure.
pub fn parse_av_option(section: &str, tree: &SectionTree) -> Result<Vec<HelpAVOption>> {
    let section_tree = tree.get(section).context("Section not found")?;
    let mut output = Vec::new();
    let mut seen = std::collections::HashSet::new();
    // Track help text (everything after the name) → option name to deduplicate aliases
    // e.g., "c1" and "curve1" with identical type+flags+help text — keep the longer name
    let mut seen_help_text: std::collections::HashMap<String, String> = std::collections::HashMap::new();

    for (option_key, choice_tree) in section_tree {
        // Parse choices
        let mut choices = Vec::new();
        for (choice_key, _) in choice_tree {
            let caps = RE_CHOICE_WITH_VALUE
                .captures(choice_key)
                .or_else(|| RE_CHOICE_WITHOUT_VALUE.captures(choice_key));

            let caps = match caps {
                Some(c) => c,
                None => bail!("No choice found in line: {choice_key}"),
            };

            let name = caps.name("name").unwrap().as_str().trim().to_string();
            let value = caps
                .name("value")
                .map(|m| m.as_str().trim().to_string())
                .unwrap_or_else(|| name.clone());
            let flags = caps.name("flags").unwrap().as_str().trim().to_string();
            let help = caps
                .name("help")
                .map(|m| m.as_str().trim().to_string())
                .unwrap_or_default();

            choices.push(HelpOptionChoice {
                name,
                value,
                flags,
                help,
            });
        }

        // Skip duplicate options (same text after name — catches aliases like c1/curve1)
        // When two options have identical type+flags+help, keep the LONGER name (canonical form)
        if let Some((name_part, rest)) = option_key.split_once(' ') {
            let rest_trimmed = rest.trim().to_string();
            if let Some(existing_name) = seen_help_text.get(&rest_trimmed) {
                let existing_name: &String = existing_name;
                if name_part.len() > existing_name.len() {
                    // Current name is longer (canonical) — replace the short alias
                    let idx = output.iter().position(|o: &HelpAVOption| o.name == existing_name.trim_start_matches('-'));
                    if let Some(idx) = idx {
                        output.remove(idx);
                    }
                    seen_help_text.insert(rest_trimmed, name_part.to_string());
                    // Fall through to add this option
                } else {
                    continue; // Current name is shorter (alias) — skip
                }
            } else {
                seen_help_text.insert(rest_trimmed, name_part.to_string());
            }
        }

        let caps = match RE_OPTION.captures(option_key) {
            Some(c) => c,
            None => bail!("No option found in line: {option_key}"),
        };

        let name = caps["name"].trim_start_matches('-').to_string();
        let option_type = validate_option_type(&caps["type"])?;
        let flags = caps["flags"].to_string();
        let help = caps
            .name("help")
            .map(|m| m.as_str().trim().to_string())
            .unwrap_or_default();

        let (min, max, default) = extract_min_max_default(&help);

        // Skip duplicate normalized names
        let normalize_name = name.replace('-', "_");
        if seen.contains(&normalize_name) {
            continue;
        }
        seen.insert(normalize_name);

        output.push(HelpAVOption {
            section: section.to_string(),
            name,
            option_type: Some(option_type),
            flags: Some(flags),
            help,
            argname: None,
            min,
            max,
            default,
            choices,
        });
    }

    Ok(output)
}

/// Parse a section of general options from a tree structure.
pub fn parse_general_option(section: &str, tree: &SectionTree) -> Result<Vec<HelpOption>> {
    let section_tree = tree.get(section).context("Section not found")?;
    let mut output = Vec::new();

    for (option_key, subtree) in section_tree {
        if !subtree.is_empty() {
            bail!("General options should not have choices: {section}.{option_key}");
        }

        let parts: Vec<&str> = option_key.splitn(2, "  ").collect();
        let first = parts[0].trim();
        let (name, argname) = if first.contains(' ') {
            let mut split = first.splitn(2, ' ');
            let n = split.next().unwrap();
            let a = split.next().map(|s| s.to_string());
            (n, a)
        } else {
            (first, None)
        };

        let help = parts.last().unwrap_or(&"").trim().to_string();

        output.push(HelpOption {
            section: section.to_string(),
            name: name.trim_start_matches('-').to_string(),
            option_type: None,
            flags: None,
            help,
            argname,
        });
    }

    Ok(output)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_re_option_matches() {
        let line = "delta             <float>      ..F.A....T. set the filter delta (from 0 to 1) (default 0.001)";
        let m = RE_OPTION.captures(line);
        assert!(m.is_some(), "RE_OPTION should match: {line}");
        let m = m.unwrap();
        assert_eq!(&m["name"], "delta");
        assert_eq!(&m["type"], "float");
    }
}

