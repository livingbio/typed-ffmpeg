//! Template rendering engine using Tera.
//!
//! Sets up the Tera environment with custom filters/functions and renders
//! all templates to generate Python source files.

use anyhow::{Context, Result};
use regex::Regex;
use std::collections::{HashMap, HashSet};
use std::path::{Path, PathBuf};
use std::sync::LazyLock;
use tera::{Function, Tera, Value};
use walkdir::WalkDir;

use super::utils;
use super::version_diff;

/// Set of module names that are generated from templates.
fn discover_generated_modules(template_dir: &Path) -> HashSet<String> {
    let mut modules = HashSet::new();
    for entry in WalkDir::new(template_dir).into_iter().filter_map(|e| e.ok()) {
        let path = entry.path();
        if let Some(name) = path.file_name().and_then(|n| n.to_str()) {
            if name.ends_with(".tera") {
                if let Ok(rel) = path.strip_prefix(template_dir) {
                    let s = rel.to_string_lossy();
                    if let Some(base) = s.split('.').next() {
                        modules.insert(base.replace('/', "."));
                    }
                }
            }
        }
    }
    modules
}

// ---- Regex for normalize_help_text ----

static RE_NORMALIZE_1: LazyLock<Regex> = LazyLock::new(|| Regex::new(r#"\\\n\s*""#).unwrap());
static RE_NORMALIZE_2: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"\n\s*").unwrap());
static RE_NORMALIZE_3: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"\s+").unwrap());
static RE_HTML_TAGS: LazyLock<Regex> = LazyLock::new(|| Regex::new(r"<[^>]+>").unwrap());

// ---- Custom Tera Filters ----

/// Register all custom filters with a Tera instance.
fn register_filters(tera: &mut Tera) {
    tera.register_filter("stream_name_safe", tera_stream_name_safe);
    tera.register_filter("option_name_safe", tera_option_name_safe);
    tera.register_filter("normalize_help_text", tera_normalize_help_text);
    tera.register_filter("striptags", tera_striptags);
    tera.register_filter("option_typing", tera_option_typing);
    tera.register_filter("filter_option_typings", tera_filter_option_typings);
    tera.register_filter("filter_option_typing", tera_filter_option_typing);
    tera.register_filter("input_typings", tera_input_typings);
    tera.register_filter("output_typings", tera_output_typings);
    tera.register_filter("indent_all", tera_indent_all);
    tera.register_filter("to_def_repr", tera_to_def_repr);
}

fn tera_stream_name_safe(
    value: &Value,
    _args: &HashMap<String, Value>,
) -> tera::Result<Value> {
    let s = value
        .as_str()
        .ok_or_else(|| tera::Error::msg("stream_name_safe expects a string"))?;
    Ok(Value::String(utils::stream_name_safe(s)))
}

fn tera_option_name_safe(
    value: &Value,
    _args: &HashMap<String, Value>,
) -> tera::Result<Value> {
    let s = value
        .as_str()
        .ok_or_else(|| tera::Error::msg("option_name_safe expects a string"))?;
    Ok(Value::String(utils::option_name_safe(s)))
}

fn tera_normalize_help_text(
    value: &Value,
    _args: &HashMap<String, Value>,
) -> tera::Result<Value> {
    let text = value
        .as_str()
        .ok_or_else(|| tera::Error::msg("normalize_help_text expects a string"))?;
    let normalized = RE_NORMALIZE_1.replace_all(text, " ");
    let normalized = RE_NORMALIZE_2.replace_all(&normalized, " ");
    let normalized = RE_NORMALIZE_3.replace_all(&normalized, " ");
    let normalized = normalized.replace("\\\"", "\"");
    Ok(Value::String(normalized.trim().to_string()))
}

fn tera_striptags(
    value: &Value,
    _args: &HashMap<String, Value>,
) -> tera::Result<Value> {
    let text = value.as_str().unwrap_or("");
    Ok(Value::String(RE_HTML_TAGS.replace_all(text, "").to_string()))
}

/// Filter: `{{ option | option_typing }}` — maps FFMpegOption type to Python typing.
fn tera_option_typing(
    value: &Value,
    _args: &HashMap<String, Value>,
) -> tera::Result<Value> {
    // `value` is the full option object; extract `.type` or `.type.value`
    let type_val = value
        .get("type")
        .and_then(|t| {
            // Could be a string or {"__class__": "...", "value": "..."}
            t.as_str()
                .map(String::from)
                .or_else(|| t.get("value").and_then(|v| v.as_str()).map(String::from))
        })
        .unwrap_or_default();

    let result = match type_val.as_str() {
        "OPT_TYPE_FUNC" => "Func",
        "OPT_TYPE_BOOL" => "Boolean",
        "OPT_TYPE_STRING" => "String",
        "OPT_TYPE_INT" => "Int",
        "OPT_TYPE_INT64" => "Int64",
        "OPT_TYPE_FLOAT" => "Float",
        "OPT_TYPE_DOUBLE" => "Double",
        "OPT_TYPE_TIME" => "Time",
        _ => "String",
    };
    Ok(Value::String(result.to_string()))
}

/// Filter: `{{ option | filter_option_typing }}` — maps FFMpegFilterOption type to Python typing.
fn tera_filter_option_typing(
    value: &Value,
    _args: &HashMap<String, Value>,
) -> tera::Result<Value> {
    let type_str = extract_type_value(value);
    let choices = value
        .get("choices")
        .and_then(|v| v.as_array())
        .cloned()
        .unwrap_or_default();

    Ok(Value::String(filter_option_typing_impl(&type_str, &choices)))
}

/// Filter: `{{ f | filter_option_typings }}` — generates complete typed parameter list.
fn tera_filter_option_typings(
    value: &Value,
    _args: &HashMap<String, Value>,
) -> tera::Result<Value> {
    let options = value
        .get("options")
        .and_then(|v| v.as_array())
        .cloned()
        .unwrap_or_default();

    let pre = value.get("pre").and_then(|v| v.as_array()).cloned().unwrap_or_default();
    let pre_dict: HashMap<String, String> = pre
        .iter()
        .filter_map(|pair| {
            let arr = pair.as_array()?;
            Some((arr.first()?.as_str()?.to_string(), arr.get(1)?.as_str()?.to_string()))
        })
        .collect();

    let mut parts = Vec::new();
    for opt in &options {
        let name = opt.get("name").and_then(|v| v.as_str()).unwrap_or("");
        let safe_name = utils::option_name_safe(name);
        let type_str = extract_type_value(opt);
        let choices = opt
            .get("choices")
            .and_then(|v| v.as_array())
            .cloned()
            .unwrap_or_default();
        let typing = filter_option_typing_impl(&type_str, &choices);
        let default = default_value_impl(opt, &pre_dict);

        if choices.is_empty() {
            parts.push(format!("{safe_name}: {typing} = {default}"));
        } else {
            parts.push(format!("{safe_name}: {typing} | Default = {default}"));
        }
    }

    if parts.is_empty() {
        Ok(Value::String(String::new()))
    } else {
        Ok(Value::String(parts.join(",") + ","))
    }
}

/// Filter: `{{ f | input_typings }}` — get input typings string.
fn tera_input_typings(
    value: &Value,
    _args: &HashMap<String, Value>,
) -> tera::Result<Value> {
    if let Some(formula) = value
        .get("formula_typings_input")
        .and_then(|v| v.as_str())
    {
        if !formula.is_empty() {
            return Ok(Value::String(formula.to_string()));
        }
    }
    let items: Vec<String> = value
        .get("stream_typings_input")
        .and_then(|v| v.as_array())
        .map(|arr| {
            arr.iter()
                .filter_map(|io| extract_stream_type(io).map(|t| format!("StreamType.{t}")))
                .collect()
        })
        .unwrap_or_default();
    Ok(Value::String(format!("[{}]", items.join(", "))))
}

/// Filter: `{{ f | output_typings }}` — get output typings string.
fn tera_output_typings(
    value: &Value,
    _args: &HashMap<String, Value>,
) -> tera::Result<Value> {
    if let Some(formula) = value
        .get("formula_typings_output")
        .and_then(|v| v.as_str())
    {
        if !formula.is_empty() {
            return Ok(Value::String(formula.to_string()));
        }
    }
    let items: Vec<String> = value
        .get("stream_typings_output")
        .and_then(|v| v.as_array())
        .map(|arr| {
            arr.iter()
                .filter_map(|io| extract_stream_type(io).map(|t| format!("StreamType.{t}")))
                .collect()
        })
        .unwrap_or_default();
    Ok(Value::String(format!("[{}]", items.join(", "))))
}

/// Filter: `{{ text | indent_all(prefix="    ") }}` — indent ALL lines including first.
/// Tera's built-in `indent` skips the first line; Jinja2's `indent(n, True)` indents all.
fn tera_indent_all(
    value: &Value,
    args: &HashMap<String, Value>,
) -> tera::Result<Value> {
    let text = value.as_str().unwrap_or("");
    let prefix = args
        .get("prefix")
        .and_then(|v| v.as_str())
        .unwrap_or("    ");
    let result: String = text
        .lines()
        .map(|line| {
            if line.trim().is_empty() {
                String::new()
            } else {
                format!("{prefix}{line}")
            }
        })
        .collect::<Vec<_>>()
        .join("\n");
    Ok(Value::String(result))
}

/// Filter: `{{ f.to_def | to_def_repr }}` — render FFMpegFilterDef as Python constructor.
/// Converts JSON `{"name": "x", "typings_input": [...], ...}` to
/// `FFMpegFilterDef(name='x', typings_input=('audio',), typings_output=('video',))`
fn tera_to_def_repr(
    value: &Value,
    _args: &HashMap<String, Value>,
) -> tera::Result<Value> {
    let name = value
        .get("name")
        .and_then(|v| v.as_str())
        .unwrap_or("");

    fn typings_repr(v: &Value) -> String {
        match v {
            Value::String(s) => s.clone(), // formula string passed through directly
            Value::Array(arr) => {
                let items: Vec<String> = arr
                    .iter()
                    .filter_map(|i| i.as_str())
                    .map(|s| format!("'{s}'"))
                    .collect();
                if items.len() == 1 {
                    format!("({},)", items[0])
                } else {
                    format!("({})", items.join(", "))
                }
            }
            _ => "()".to_string(),
        }
    }

    let ti = value.get("typings_input").map(typings_repr).unwrap_or_else(|| "()".to_string());
    let to = value.get("typings_output").map(typings_repr).unwrap_or_else(|| "()".to_string());

    Ok(Value::String(format!(
        "FFMpegFilterDef(name='{name}', typings_input={ti}, typings_output={to})"
    )))
}

// ---- Tera Functions (globals called from templates) ----

/// Register Tera functions (globals).
fn register_functions(
    tera: &mut Tera,
    version_prefix: Option<String>,
    generated_modules: HashSet<String>,
    version_metadata: Option<version_diff::VersionMetadata>,
    current_version: String,
) {
    // get_relative_import(import_path, template_path, imports)
    let vp = version_prefix.clone();
    let gm = generated_modules.clone();
    tera.register_function(
        "get_relative_import",
        move |args: &HashMap<String, Value>| -> tera::Result<Value> {
            let import_path = args
                .get("import_path")
                .and_then(|v| v.as_str())
                .ok_or_else(|| tera::Error::msg("import_path required"))?;
            let template_path = args
                .get("template_path")
                .and_then(|v| v.as_str())
                .ok_or_else(|| tera::Error::msg("template_path required"))?;
            let imports = args
                .get("imports")
                .and_then(|v| v.as_str())
                .unwrap_or("");

            let result = utils::get_relative_import(
                import_path,
                template_path,
                imports,
                vp.as_deref(),
                &gm,
            );
            Ok(Value::String(result))
        },
    );

    // get_relative_path(import_path, template_path)
    tera.register_function(
        "get_relative_path",
        |args: &HashMap<String, Value>| -> tera::Result<Value> {
            let import_path = args
                .get("import_path")
                .and_then(|v| v.as_str())
                .unwrap_or("");
            let template_path = args
                .get("template_path")
                .and_then(|v| v.as_str())
                .unwrap_or("");
            match utils::get_relative_path(import_path, template_path) {
                Some(p) => Ok(Value::String(p)),
                None => Ok(Value::Null),
            }
        },
    );

    // format_version_note(name) -> string or null
    let vm = version_metadata;
    let cv = current_version;
    tera.register_function(
        "format_version_note",
        move |args: &HashMap<String, Value>| -> tera::Result<Value> {
            let name = args
                .get("name")
                .and_then(|v| v.as_str())
                .unwrap_or("");
            match &vm {
                Some(metadata) => {
                    match version_diff::format_version_note(
                        name,
                        &metadata.filter_versions,
                        &metadata.available_versions,
                        &cv,
                    ) {
                        Some(note) => Ok(Value::String(note)),
                        None => Ok(Value::Null),
                    }
                }
                None => Ok(Value::Null),
            }
        },
    );
}

// ---- Helper functions ----

/// Extract the type value from a filter option, handling both string and enum-tagged formats.
fn extract_type_value(obj: &Value) -> String {
    obj.get("type")
        .and_then(|t| {
            t.as_str()
                .map(String::from)
                .or_else(|| t.get("value").and_then(|v| v.as_str()).map(String::from))
        })
        .unwrap_or_default()
}

/// Extract stream type string from an IO type object.
fn extract_stream_type(io: &Value) -> Option<String> {
    io.get("type").and_then(|t| {
        t.as_str()
            .map(String::from)
            .or_else(|| t.get("value").and_then(|v| v.as_str()).map(String::from))
    })
}

/// Map FFMpegFilterOptionType to Python typing string.
fn filter_option_typing_impl(type_str: &str, choices: &[Value]) -> String {
    let base = match type_str {
        "boolean" => "Boolean",
        "duration" => "Duration",
        "color" => "Color",
        "flags" => "Flags",
        "dictionary" => "Dictionary",
        "pix_fmt" => "Pix_fmt",
        "int" => "Int",
        "int64" => "Int64",
        "double" => "Double",
        "float" => "Float",
        "string" => "String",
        "video_rate" => "Video_rate",
        "image_size" => "Image_size",
        "rational" => "Rational",
        "sample_fmt" => "Sample_fmt",
        "binary" => "Binary",
        "channel_layout" => "String",
        "unsigned" => "Int",
        _ => "String",
    };

    if choices.is_empty() {
        return base.to_string();
    }

    let values: Vec<String> = choices
        .iter()
        .filter_map(|c| c.get("name").and_then(|n| n.as_str()))
        .map(|n| format!("\"{n}\""))
        .collect();

    format!("{base}| Literal[{vals}]", vals = values.join(","))
}

/// Get default value for a filter option.
fn default_value_impl(option: &Value, pre_dict: &HashMap<String, String>) -> String {
    let name = option.get("name").and_then(|v| v.as_str()).unwrap_or("");

    if let Some(pre_val) = pre_dict.get(name) {
        return format!("Auto({pre_val:?})");
    }

    let default = option.get("default");
    match default {
        Some(Value::Null) | None => "Default(None)".to_string(),
        Some(Value::Number(n)) => {
            if let Some(f) = n.as_f64() {
                if f.is_nan() {
                    return "Default(\"nan\")".to_string();
                }
            }
            format!("Default({n})")
        }
        Some(Value::Bool(b)) => format!("Default({b})"),
        Some(Value::String(s)) => format!("Default({s:?})"),
        Some(other) => format!("Default({other})"),
    }
}

/// Render all templates to generate Python source files.
pub fn render(
    template_dir: &Path,
    outpath: &Path,
    version_prefix: Option<&str>,
    context: &mut tera::Context,
    version_metadata: Option<version_diff::VersionMetadata>,
) -> Result<Vec<PathBuf>> {
    // Load ALL .tera files (including _components.tera which has only one dot)
    let glob_pattern = format!("{}/**/*.tera", template_dir.display());
    let mut tera = Tera::new(&glob_pattern).context("Failed to load Tera templates")?;

    let generated_modules = discover_generated_modules(template_dir);

    // Register filters and functions
    register_filters(&mut tera);

    let current_major = version_prefix
        .map(|p| p.trim_start_matches('v').to_string())
        .unwrap_or_default();
    register_functions(
        &mut tera,
        version_prefix.map(String::from),
        generated_modules,
        version_metadata,
        current_major,
    );

    std::fs::create_dir_all(outpath)?;
    let mut output = Vec::new();

    for template_name in tera.get_template_names().collect::<Vec<_>>() {
        let template_name = template_name.to_string();

        // Skip macro-only templates (not renderable output)
        if template_name.starts_with('_') {
            continue;
        }

        context.insert("template_path", &template_name);

        let rendered = tera
            .render(&template_name, context)
            .with_context(|| format!("Failed to render template: {template_name}"))?;

        let out_rel = template_name.strip_suffix(".tera").unwrap_or(&template_name);
        let out_file = outpath.join(out_rel);

        if let Some(parent) = out_file.parent() {
            std::fs::create_dir_all(parent)?;
        }

        let content = format!("# NOTE: this file is auto-generated, do not modify\n{rendered}");
        std::fs::write(&out_file, content)?;
        output.push(out_file);
    }

    // py.typed marker
    let py_typed = outpath.join("py.typed");
    std::fs::write(&py_typed, "")?;
    output.push(py_typed);

    // __init__.py for version subpackage
    if let Some(prefix) = version_prefix {
        let init_py = outpath.join("__init__.py");
        if !init_py.exists() {
            std::fs::write(
                &init_py,
                format!("\"\"\"typed-ffmpeg bindings for FFmpeg {prefix}.\"\"\"\n"),
            )?;
            output.push(init_py);
        }
    }

    Ok(output)
}
