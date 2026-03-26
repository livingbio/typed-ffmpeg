//! Convert HTML to Markdown for docstrings.

use scraper::{Html, Selector};

/// Convert HTML content to a simplified Markdown representation.
pub fn convert_html_to_markdown(html: &str) -> String {
    let document = Html::parse_fragment(html);

    // Simple approach: extract text content with basic formatting
    let mut result = String::new();

    // Get all text content
    let selector = Selector::parse("p, li, dt, dd, h1, h2, h3, h4, h5, h6, pre").unwrap();
    for element in document.select(&selector) {
        let tag = element.value().name();
        let text: String = element.text().collect::<Vec<_>>().join(" ");
        let text = text.trim();

        if text.is_empty() {
            continue;
        }

        match tag {
            "h1" | "h2" | "h3" | "h4" | "h5" | "h6" => {
                result.push_str(&format!("\n## {text}\n\n"));
            }
            "li" => {
                result.push_str(&format!("- {text}\n"));
            }
            "dt" => {
                result.push_str(&format!("\n**{text}**\n"));
            }
            "dd" => {
                result.push_str(&format!("  {text}\n"));
            }
            "pre" => {
                result.push_str(&format!("\n```\n{text}\n```\n\n"));
            }
            _ => {
                result.push_str(text);
                result.push_str("\n\n");
            }
        }
    }

    result.trim().to_string()
}
