//! JSON-based caching for parsed FFmpeg metadata.
//!
//! Compatible with the Python `ffmpeg_core.common.cache` module.
//! Cache files are stored in `~/.ffmpeg-core/cache/list/`.

use anyhow::{Context, Result};
use serde::{de::DeserializeOwned, Serialize};
use std::fs;
use std::path::{Path, PathBuf};

/// Get the default cache directory path.
pub fn default_cache_dir() -> PathBuf {
    dirs::home_dir()
        .expect("Could not determine home directory")
        .join(".ffmpeg-core")
        .join("cache")
        .join("list")
}

/// Ensure the cache directory exists.
pub fn ensure_cache_dir(cache_dir: &Path) -> Result<()> {
    fs::create_dir_all(cache_dir)
        .with_context(|| format!("Failed to create cache directory: {}", cache_dir.display()))?;
    Ok(())
}

/// Get the path for a cache file with the given ID.
pub fn cache_file_path(cache_dir: &Path, id: &str) -> PathBuf {
    cache_dir.join(format!("{id}.json"))
}

/// Load a cached object from JSON.
pub fn load<T: DeserializeOwned>(cache_dir: &Path, id: &str) -> Result<Option<T>> {
    let path = cache_file_path(cache_dir, id);
    if !path.exists() {
        return Ok(None);
    }
    let raw = fs::read_to_string(&path)
        .with_context(|| format!("Failed to read cache file: {}", path.display()))?;
    let obj: T =
        serde_json::from_str(&raw).with_context(|| format!("Failed to parse cache: {id}"))?;
    Ok(Some(obj))
}

/// Save an object to the JSON cache.
pub fn save<T: Serialize>(cache_dir: &Path, id: &str, obj: &T) -> Result<()> {
    ensure_cache_dir(cache_dir)?;
    let path = cache_file_path(cache_dir, id);
    let raw = serde_json::to_string_pretty(obj)?;
    fs::write(&path, raw)
        .with_context(|| format!("Failed to write cache file: {}", path.display()))?;
    Ok(())
}

/// Check if a cache entry exists.
pub fn exists(cache_dir: &Path, id: &str) -> bool {
    cache_file_path(cache_dir, id).exists()
}
