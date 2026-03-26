//! Parse FFmpeg options from ffmpeg_opt.c source code.

use anyhow::{Context, Result};
use regex::Regex;
use std::sync::LazyLock;

use super::parse_c_structure::parse_c_structure;
use crate::schema::parse_c::{FFMpegOption, FFMpegOptionFlag, FFMpegOptionType};

static RE_OPTIONS_ARRAY: LazyLock<Regex> = LazyLock::new(|| {
    Regex::new(r"(?s)const\s+OptionDef\s+options\[\]\s*=\s*\{(.+?)\n\};").unwrap()
});

/// Parse ffmpeg_opt.c content to extract command-line option definitions.
pub fn parse_ffmpeg_opt_c(text: &str) -> Result<Vec<FFMpegOption>> {
    let caps = RE_OPTIONS_ARRAY
        .captures(text)
        .context("Could not find `const OptionDef options[]` in source")?;

    let array_body = &caps[1];
    let elements = parse_c_structure(array_body);

    let mut options = Vec::new();
    let mut canon_map: std::collections::HashMap<String, String> = std::collections::HashMap::new();

    for elem in &elements {
        if elem.len() < 4 {
            continue;
        }

        let name = elem[0].trim_matches('"').to_string();

        // Parse type - may or may not be present
        let (option_type, flags_str, help_idx) = if elem[1].starts_with("OPT_TYPE_") {
            // New format: name, type, flags, ...
            (
                parse_option_type(&elem[1])?,
                elem[2].clone(),
                if elem.len() > 4 { 4 } else { 3 },
            )
        } else {
            // Old format: name, flags, ... (type defaults to OPT_TYPE_FUNC)
            (FFMpegOptionType::Func, elem[1].clone(), 3)
        };

        let flags = FFMpegOptionFlag::eval_flags_expr(&flags_str)
            .unwrap_or_else(|_| {
                log::warn!("Could not parse flags: {flags_str} for option {name}");
                0
            });

        let help = if help_idx < elem.len() {
            elem[help_idx].trim_matches('"').to_string()
        } else {
            String::new()
        };

        // Check for argname and canon
        let argname = if help_idx + 1 < elem.len() {
            let a = elem[help_idx + 1].trim_matches('"');
            if !a.is_empty() && !a.starts_with('{') && !a.starts_with('.') {
                Some(a.to_string())
            } else {
                None
            }
        } else {
            None
        };

        // Track canon references
        if flags & FFMpegOptionFlag::OPT_HAS_CANON != 0 {
            // This option has a canonical form - we'll resolve it after
            for inner in elem {
                if inner.contains(".name_canon") {
                    if let Some(canon_name) = inner.split('"').nth(1) {
                        canon_map.insert(name.clone(), canon_name.to_string());
                    }
                }
            }
        }

        options.push(FFMpegOption {
            class: Some("FFMpegOption".to_string()),
            name,
            option_type,
            flags,
            help,
            argname,
            canon: None,
        });
    }

    // Resolve canon references
    for opt in &mut options {
        if let Some(canon) = canon_map.get(&opt.name) {
            opt.canon = Some(canon.clone());
        }
    }

    Ok(options)
}

fn parse_option_type(s: &str) -> Result<FFMpegOptionType> {
    match s.trim() {
        "OPT_TYPE_FUNC" => Ok(FFMpegOptionType::Func),
        "OPT_TYPE_BOOL" => Ok(FFMpegOptionType::Bool),
        "OPT_TYPE_STRING" => Ok(FFMpegOptionType::String),
        "OPT_TYPE_INT" => Ok(FFMpegOptionType::Int),
        "OPT_TYPE_INT64" => Ok(FFMpegOptionType::Int64),
        "OPT_TYPE_FLOAT" => Ok(FFMpegOptionType::Float),
        "OPT_TYPE_DOUBLE" => Ok(FFMpegOptionType::Double),
        "OPT_TYPE_TIME" => Ok(FFMpegOptionType::Time),
        other => anyhow::bail!("Unknown option type: {other}"),
    }
}
