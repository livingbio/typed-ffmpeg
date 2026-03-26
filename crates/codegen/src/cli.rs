//! CLI definitions using clap.

use clap::{Parser, Subcommand};
use std::path::PathBuf;

#[derive(Parser)]
#[command(name = "typed-ffmpeg-codegen")]
#[command(about = "Code generation tool for typed-ffmpeg Python bindings")]
pub struct Cli {
    #[command(subcommand)]
    pub command: Commands,

    /// Enable verbose logging
    #[arg(long, global = true)]
    pub verbose: bool,
}

#[derive(Subcommand)]
pub enum Commands {
    /// Generate Python bindings
    Generate {
        /// Path to FFmpeg binary
        #[arg(long, default_value = "ffmpeg")]
        ffmpeg_binary: String,

        /// Output directory for generated files
        #[arg(long)]
        outpath: PathBuf,

        /// Generate into a version subdirectory (e.g., v7)
        #[arg(long)]
        version_dir: bool,

        /// Force rebuild, ignoring cache
        #[arg(long)]
        rebuild: bool,

        /// Custom cache directory
        #[arg(long)]
        cache_dir: Option<PathBuf>,
    },

    /// Create re-export modules at root level
    Reexport {
        /// FFmpeg version to re-export
        #[arg(long)]
        version: Option<String>,

        /// Output directory
        #[arg(long)]
        outpath: PathBuf,
    },

    /// Show differences between FFmpeg versions
    Diff {
        /// Source version
        from_version: String,

        /// Target version
        to_version: String,

        /// Custom cache directory
        #[arg(long)]
        cache_dir: Option<PathBuf>,
    },

    /// Parse FFmpeg help output
    ParseHelp {
        #[command(subcommand)]
        action: ParseHelpAction,
    },

    /// Parse FFmpeg C source
    ParseC {
        #[command(subcommand)]
        action: ParseCAction,
    },

    /// Parse FFmpeg documentation
    ParseDocs {
        #[command(subcommand)]
        action: ParseDocsAction,
    },

    /// Manage manual filter configurations
    Manual {
        #[command(subcommand)]
        action: ManualAction,
    },
}

#[derive(Subcommand)]
pub enum ParseHelpAction {
    /// Extract filter metadata
    ExtractFilters {
        #[arg(long, default_value = "ffmpeg")]
        ffmpeg_binary: String,
        #[arg(long)]
        cache_dir: Option<PathBuf>,
    },
    /// Extract codec metadata
    ExtractCodecs {
        #[arg(long, default_value = "ffmpeg")]
        ffmpeg_binary: String,
        #[arg(long)]
        cache_dir: Option<PathBuf>,
    },
    /// Extract format metadata
    ExtractFormats {
        #[arg(long, default_value = "ffmpeg")]
        ffmpeg_binary: String,
        #[arg(long)]
        cache_dir: Option<PathBuf>,
    },
    /// Extract all help options
    ExtractHelp {
        #[arg(long, default_value = "ffmpeg")]
        ffmpeg_binary: String,
        #[arg(long)]
        cache_dir: Option<PathBuf>,
    },
}

#[derive(Subcommand)]
pub enum ParseCAction {
    /// Parse FFmpeg options from C source
    ParseOptions {
        /// Path to FFmpeg source directory
        #[arg(long)]
        ffmpeg_source: PathBuf,
        #[arg(long)]
        cache_dir: Option<PathBuf>,
    },
}

#[derive(Subcommand)]
pub enum ParseDocsAction {
    /// Download FFmpeg filter documentation
    Download {
        #[arg(long)]
        cache_dir: Option<PathBuf>,
    },
    /// Process downloaded documentation
    Process {
        #[arg(long)]
        cache_dir: Option<PathBuf>,
    },
}

#[derive(Subcommand)]
pub enum ManualAction {
    /// Initialize manual config for a filter
    InitConfig {
        /// Filter name
        name: String,
        #[arg(long)]
        cache_dir: Option<PathBuf>,
    },
}
