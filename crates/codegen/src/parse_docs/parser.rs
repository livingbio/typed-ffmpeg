//! Parse FFmpeg filter documentation HTML into structured data.

use anyhow::Result;
use regex::Regex;
use std::sync::LazyLock;

use crate::schema::docs::FilterDocument;

// Matches: <h3 class="section"><a href="#toc-aap">8.1 aap</a></h3>
// Hash extracted from href="#toc-xxx" → "toc-xxx"
static RE_SECTION: LazyLock<Regex> = LazyLock::new(|| {
    Regex::new(r#"<h[34][^>]*><a\s+href="(?:#?)([^"]+)"[^>]*>(\d+(?:\.\d+)*)\s+(.+?)</a></h[34]>"#).unwrap()
});

/// Parse the HTML docs into FilterDocument objects.
pub fn parse_filter_documents(html: &str) -> Result<Vec<FilterDocument>> {
    let mut documents = Vec::new();
    let section_starts: Vec<_> = RE_SECTION.find_iter(html).collect();

    for (i, section_match) in section_starts.iter().enumerate() {
        let caps = RE_SECTION.captures(section_match.as_str()).unwrap();
        let raw_hash = caps[1].to_string();
        let section_index = caps[2].to_string();
        let title_raw = caps[3].to_string();

        // Convert hash: "toc-aap" → "aap", "toc-acrossfade-1" → "acrossfade"
        let hash = raw_hash
            .strip_prefix("toc-")
            .unwrap_or(&raw_hash)
            .trim_end_matches("-1")
            .to_string();

        // Extract body between this section and the next
        let start = section_match.end();
        let end = if i + 1 < section_starts.len() {
            section_starts[i + 1].start()
        } else {
            html.len()
        };
        let body = html[start..end].to_string();

        // Extract filter names from title (e.g., "acrossfade, crossfade")
        let title = format!("{section_index} {title_raw}");
        let filter_names: Vec<String> = title_raw
            .split(',')
            .map(|s| {
                // Remove any HTML tags (e.g., <code>aap</code>)
                let stripped = RE_HTML_TAGS.replace_all(s.trim(), "");
                stripped.to_lowercase()
            })
            .filter(|s| !s.is_empty())
            .collect();

        if !filter_names.is_empty() {
            documents.push(FilterDocument {
                section_index,
                hash,
                title,
                body,
                filter_names,
            });
        }
    }

    Ok(documents)
}

static RE_HTML_TAGS: LazyLock<Regex> =
    LazyLock::new(|| Regex::new(r"<[^>]+>").unwrap());

/// Find documentation for a specific filter.
pub fn find_filter_doc<'a>(
    docs: &'a [FilterDocument],
    filter_name: &str,
) -> Option<&'a FilterDocument> {
    docs.iter()
        .find(|doc| doc.filter_names.contains(&filter_name.to_lowercase()))
}
