//! Utility functions for code generation (import resolution, naming).

use regex::Regex;
use std::collections::HashSet;
use std::path::Path;
use std::sync::LazyLock;

/// Python reserved keywords that need escaping.
const PYTHON_KEYWORDS: &[&str] = &[
    "False", "None", "True", "and", "as", "assert", "async", "await", "break", "class",
    "continue", "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if",
    "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try",
    "while", "with", "yield",
];

static RE_NON_WORD: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"[^\w]").unwrap());

/// Convert an option name to a safe Python identifier.
pub fn option_name_safe(name: &str) -> String {
    if name == "?" {
        return "_q".to_string();
    }

    let mut safe = name.replace('-', "_");
    safe = RE_NON_WORD.replace_all(&safe, "_").to_string();

    if safe.is_empty() {
        return "_".to_string();
    }

    if safe.starts_with(|c: char| c.is_ascii_digit()) {
        safe = format!("_{safe}");
    }

    if PYTHON_KEYWORDS.contains(&safe.as_str()) {
        safe = format!("_{safe}");
    }

    safe
}

/// Convert a stream name to a safe Python identifier with underscore prefix.
pub fn stream_name_safe(name: &str) -> String {
    let safe = option_name_safe(name);
    if safe.starts_with('_') {
        safe
    } else {
        format!("_{safe}")
    }
}

/// Compute the relative import path between two module paths.
///
/// Mirrors the Python `get_relative_path()` exactly:
/// - Returns `None` if importing from the same file
/// - Special-cases `codecs.schema` and `formats.schema` for same-package imports
/// - Computes relative dotted imports (e.g., `..streams.audio`)
pub fn get_relative_path(import_path: &str, template_path: &str) -> Option<String> {
    // Normalize template path: "streams/audio.py.tera" → "streams/audio"
    let template_path_str = template_path.replace('\\', "/");
    let template_base = template_path_str.split('.').next().unwrap_or("");
    // Convert to Path-like for comparison
    let template_path_obj = Path::new(template_base);
    let import_as_path = import_path.replace('.', "/");
    let import_path_obj = Path::new(&import_as_path);

    if template_path_obj == import_path_obj {
        return None; // self-import
    }

    // Special case: codecs/encoders importing codecs.schema → .schema
    if import_path == "codecs.schema" && template_path_str.starts_with("codecs/") {
        return Some(".schema".to_string());
    }
    if import_path == "formats.schema" && template_path_str.starts_with("formats/") {
        return Some(".schema".to_string());
    }

    let file_parts: Vec<&str> = template_base.split('/').collect();
    let import_parts: Vec<&str> = import_path.split('.').collect();

    // Find first divergence point
    let min_len = file_parts.len().min(import_parts.len());
    let mut diverge_idx = 0;
    for i in 0..min_len {
        if file_parts[i] != import_parts[i] {
            diverge_idx = i;
            break;
        }
        diverge_idx = i + 1;
    }

    // Build relative import: dots for going up + remaining import path
    let back_steps = file_parts.len() - diverge_idx - 1;
    let mut result = ".".to_string();
    for _ in 0..back_steps {
        result.push('.');
    }
    let remaining = &import_parts[diverge_idx..];
    if !remaining.is_empty() {
        result.push_str(&remaining.join("."));
    }

    Some(result)
}

/// Generate a Python import statement.
///
/// Mirrors the Python `get_relative_import()` exactly:
/// - Non-versioned mode: relative imports
/// - Versioned mode: relative for generated modules, absolute (`ffmpeg_core.X`) for shared core
pub fn get_relative_import(
    import_path: &str,
    template_path: &str,
    imports: &str,
    version_prefix: Option<&str>,
    generated_modules: &HashSet<String>,
) -> String {
    let relative_path = match get_relative_path(import_path, template_path) {
        Some(p) => p,
        None => return String::new(), // self-import
    };

    if version_prefix.is_none() {
        // Non-versioned mode: relative imports
        return format!("from {relative_path} import {imports}");
    }

    // Versioned mode
    let is_generated = generated_modules.contains(import_path);

    if is_generated {
        format!("from {relative_path} import {imports}")
    } else {
        // Target is shared core → absolute import from ffmpeg_core
        format!("from ffmpeg_core.{import_path} import {imports}")
    }
}
