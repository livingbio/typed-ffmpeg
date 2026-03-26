//! Download FFmpeg documentation HTML.

use anyhow::{Context, Result};
use std::fs;
use std::path::Path;

const FFMPEG_FILTERS_URL: &str = "https://ffmpeg.org/ffmpeg-filters.html";

/// Download the FFmpeg filters documentation HTML.
pub fn download_ffmpeg_filter_docs(output_path: &Path) -> Result<()> {
    let client = reqwest::blocking::Client::new();
    let response = client
        .get(FFMPEG_FILTERS_URL)
        .send()
        .context("Failed to download FFmpeg filter docs")?;

    let body = response.text().context("Failed to read response body")?;
    fs::write(output_path, &body)
        .with_context(|| format!("Failed to write to {}", output_path.display()))?;

    Ok(())
}

/// Load previously downloaded docs, or download if not present.
pub fn ensure_docs(cache_path: &Path) -> Result<String> {
    let docs_file = cache_path.join("ffmpeg-filters.html");
    if !docs_file.exists() {
        download_ffmpeg_filter_docs(&docs_file)?;
    }
    fs::read_to_string(&docs_file).context("Failed to read cached docs")
}
