//! Schema types for parsed FFmpeg documentation.

use serde::{Deserialize, Serialize};

/// A parsed filter documentation section.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct FilterDocument {
    /// Section index (e.g., "8.8").
    pub section_index: String,
    /// Anchor hash for linking.
    pub hash: String,
    /// Section title (e.g., "8.8 acue").
    pub title: String,
    /// Raw HTML body of the documentation.
    pub body: String,
    /// Filter names covered by this section.
    pub filter_names: Vec<String>,
}

impl FilterDocument {
    /// Get the documentation URL.
    pub fn url(&self) -> String {
        format!("https://ffmpeg.org/ffmpeg-filters.html#{}", self.hash)
    }
}
