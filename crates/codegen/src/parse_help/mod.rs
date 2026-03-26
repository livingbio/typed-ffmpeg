//! Parse FFmpeg metadata from help output.
//!
//! This module extracts filter, codec, format, and option information
//! by running `ffmpeg` with various help flags and parsing the output.

pub mod codecs;
pub mod filters;
pub mod formats;
pub mod help;
pub mod utils;
