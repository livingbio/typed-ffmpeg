//! Schema definitions for FFmpeg metadata used across the codegen system.
//!
//! These types mirror the Python dataclass hierarchy and are serde-compatible
//! with the JSON cache format (including `__class__` discriminator tags).

pub mod codegen;
pub mod docs;
pub mod filter;
pub mod manual;
pub mod parse_c;
pub mod parse_help;

// Re-export commonly used types
pub use codegen::*;
pub use filter::*;
pub use parse_c::{FFMpegOption as FFMpegCOption, FFMpegOptionFlag, FFMpegOptionType as COptionType};
pub use parse_help::*;
