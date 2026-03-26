//! Cross-version comparison and metadata for deprecation hints.

use anyhow::Result;
use std::collections::{HashMap, HashSet};
use std::path::Path;

use crate::cache;
use crate::schema::codegen::version_cache_key;

/// Diff between two FFmpeg versions.
#[derive(Debug, Default)]
pub struct VersionDelta {
    pub from_version: String,
    pub to_version: String,
    pub filters_added: Vec<String>,
    pub filters_removed: Vec<String>,
    pub codecs_added: Vec<String>,
    pub codecs_removed: Vec<String>,
    pub formats_added: Vec<String>,
    pub formats_removed: Vec<String>,
}

/// Aggregated version info across all available caches.
#[derive(Debug, Default, Clone)]
pub struct VersionMetadata {
    /// Maps filter name → set of major version strings where it exists.
    pub filter_versions: HashMap<String, HashSet<String>>,
    /// Maps codec name → set of major version strings where it exists.
    pub codec_versions: HashMap<String, HashSet<String>>,
    /// Maps format name → set of major version strings where it exists.
    pub format_versions: HashMap<String, HashSet<String>>,
    /// All available version strings, sorted.
    pub available_versions: Vec<String>,
}

/// Load item names from a cache entry, returning None if unavailable.
fn load_names_from_cache(cache_dir: &Path, cache_id: &str) -> Option<HashSet<String>> {
    let items: Option<Vec<serde_json::Value>> = cache::load(cache_dir, cache_id).ok()?;
    items.map(|list| {
        list.iter()
            .filter_map(|v| v.get("name").and_then(|n| n.as_str()).map(String::from))
            .collect()
    })
}

/// Compute the delta between two FFmpeg versions.
pub fn diff_versions(
    cache_dir: &Path,
    from_version: &str,
    to_version: &str,
) -> Result<VersionDelta> {
    let from_key = version_cache_key(from_version);
    let to_key = version_cache_key(to_version);

    fn diff_names(
        cache_dir: &Path,
        prefix: &str,
        from_key: &str,
        to_key: &str,
    ) -> (Vec<String>, Vec<String>) {
        let from_names = load_names_from_cache(cache_dir, &format!("{prefix}_{from_key}"));
        let to_names = load_names_from_cache(cache_dir, &format!("{prefix}_{to_key}"));
        match (from_names, to_names) {
            (Some(from), Some(to)) => {
                let added: Vec<String> = to.difference(&from).cloned().collect();
                let removed: Vec<String> = from.difference(&to).cloned().collect();
                (sorted(added), sorted(removed))
            }
            _ => (Vec::new(), Vec::new()),
        }
    }

    let (filters_added, filters_removed) =
        diff_names(cache_dir, "filters", &from_key, &to_key);
    let (codecs_added, codecs_removed) = diff_names(cache_dir, "codecs", &from_key, &to_key);
    let (formats_added, formats_removed) =
        diff_names(cache_dir, "formats", &from_key, &to_key);

    Ok(VersionDelta {
        from_version: from_version.to_string(),
        to_version: to_version.to_string(),
        filters_added,
        filters_removed,
        codecs_added,
        codecs_removed,
        formats_added,
        formats_removed,
    })
}

fn sorted(mut v: Vec<String>) -> Vec<String> {
    v.sort();
    v
}

/// Build aggregated metadata across all available version caches.
pub fn build_version_metadata(cache_dir: &Path, versions: &[String]) -> VersionMetadata {
    let mut metadata = VersionMetadata {
        available_versions: {
            let mut v = versions.to_vec();
            v.sort();
            v
        },
        ..Default::default()
    };

    for version in versions {
        let vkey = version_cache_key(version);
        let major = version.split('.').next().unwrap_or("0").to_string();

        if let Some(names) = load_names_from_cache(cache_dir, &format!("filters_{vkey}")) {
            for name in names {
                metadata
                    .filter_versions
                    .entry(name)
                    .or_default()
                    .insert(major.clone());
            }
        }

        if let Some(names) = load_names_from_cache(cache_dir, &format!("codecs_{vkey}")) {
            for name in names {
                metadata
                    .codec_versions
                    .entry(name)
                    .or_default()
                    .insert(major.clone());
            }
        }

        if let Some(names) = load_names_from_cache(cache_dir, &format!("formats_{vkey}")) {
            for name in names {
                metadata
                    .format_versions
                    .entry(name)
                    .or_default()
                    .insert(major.clone());
            }
        }
    }

    metadata
}

/// Generate a version availability note for a docstring.
pub fn format_version_note(
    item_name: &str,
    version_map: &HashMap<String, HashSet<String>>,
    all_versions: &[String],
    current_version: &str,
) -> Option<String> {
    let present_in = version_map.get(item_name)?;

    let all_majors: Vec<String> = {
        let mut m: Vec<String> = all_versions
            .iter()
            .map(|v| v.split('.').next().unwrap_or("0").to_string())
            .collect();
        m.sort();
        m.dedup();
        m
    };

    if all_majors.is_empty() {
        return None;
    }

    let current_ver: i32 = current_version.parse().unwrap_or(0);

    if present_in.contains(current_version) {
        // Check if it's new (not in earlier versions)
        let earlier: Vec<&String> = all_majors
            .iter()
            .filter(|v| v.parse::<i32>().unwrap_or(0) < current_ver)
            .collect();
        if !earlier.is_empty() && !earlier.iter().any(|v| present_in.contains(v.as_str())) {
            return Some(format!("New in FFmpeg {current_version}.0."));
        }

        // Check if it's removed in a later version
        let later: Vec<&String> = all_majors
            .iter()
            .filter(|v| v.parse::<i32>().unwrap_or(0) > current_ver)
            .collect();
        let removed_in: Vec<&&String> = later
            .iter()
            .filter(|v| !present_in.contains(v.as_str()))
            .collect();
        if let Some(first_removed) = removed_in.first() {
            return Some(format!("Removed in FFmpeg {}.0.", first_removed));
        }
    } else {
        // Item doesn't exist in current version - check if deprecated
        let earlier: Vec<&String> = all_majors
            .iter()
            .filter(|v| v.parse::<i32>().unwrap_or(0) < current_ver)
            .collect();
        if earlier.iter().any(|v| present_in.contains(v.as_str())) {
            return Some(format!(
                "No longer available in FFmpeg {current_version}.0."
            ));
        }
    }

    None
}
