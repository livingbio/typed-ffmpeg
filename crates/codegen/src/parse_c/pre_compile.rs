//! Pre-compile FFmpeg source for option extraction.
//!
//! Downloads FFmpeg source, runs configure, and preprocesses ffmpeg_opt.c.

use anyhow::{Context, Result};
use std::path::Path;
use std::process::Command;

/// Run the GCC preprocessor on ffmpeg_opt.c and return the result.
pub fn preprocess_ffmpeg_opt(ffmpeg_source_dir: &Path) -> Result<String> {
    let opt_c = ffmpeg_source_dir.join("fftools").join("ffmpeg_opt.c");
    if !opt_c.exists() {
        anyhow::bail!(
            "ffmpeg_opt.c not found at {}",
            opt_c.display()
        );
    }

    let output = Command::new("gcc")
        .args([
            "-E",
            "-I",
            ffmpeg_source_dir.to_str().unwrap(),
            opt_c.to_str().unwrap(),
        ])
        .output()
        .context("Failed to run gcc -E")?;

    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr);
        anyhow::bail!("gcc preprocessing failed: {stderr}");
    }

    Ok(String::from_utf8_lossy(&output.stdout).to_string())
}
