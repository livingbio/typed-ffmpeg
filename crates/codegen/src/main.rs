//! CLI entry point for typed-ffmpeg-codegen.

use anyhow::Result;
use clap::Parser;
use std::path::PathBuf;

use typed_ffmpeg_codegen::cache;
use typed_ffmpeg_codegen::cli::*;
use typed_ffmpeg_codegen::codegen::version_diff;
use typed_ffmpeg_codegen::parse_help::utils::get_ffmpeg_version;
use typed_ffmpeg_codegen::schema::codegen::{is_supported_version, version_cache_key};

fn main() -> Result<()> {
    let cli = Cli::parse();

    if cli.verbose {
        env_logger::Builder::from_env(env_logger::Env::default().default_filter_or("debug")).init();
    } else {
        env_logger::Builder::from_env(env_logger::Env::default().default_filter_or("warn")).init();
    }

    match cli.command {
        Commands::Generate {
            ffmpeg_binary,
            outpath,
            version_dir,
            rebuild,
            cache_dir,
        } => cmd_generate(ffmpeg_binary, outpath, version_dir, rebuild, cache_dir)?,

        Commands::Reexport { version, outpath } => cmd_reexport(version, outpath)?,

        Commands::Diff {
            from_version,
            to_version,
            cache_dir,
        } => {
            let cache_dir = cache_dir.unwrap_or_else(cache::default_cache_dir);
            let delta = version_diff::diff_versions(&cache_dir, &from_version, &to_version)?;

            println!("\n  FFmpeg {} → {}\n", delta.from_version, delta.to_version);
            print_section("Filters", &delta.filters_added, &delta.filters_removed);
            print_section("Codecs", &delta.codecs_added, &delta.codecs_removed);
            print_section("Formats", &delta.formats_added, &delta.formats_removed);

            let total = delta.filters_added.len()
                + delta.filters_removed.len()
                + delta.codecs_added.len()
                + delta.codecs_removed.len()
                + delta.formats_added.len()
                + delta.formats_removed.len();
            println!("\n  Total changes: {total}");
        }

        Commands::ParseHelp { action } => match action {
            ParseHelpAction::ExtractFilters {
                ffmpeg_binary,
                cache_dir,
            } => {
                let cache_dir = cache_dir.unwrap_or_else(cache::default_cache_dir);
                let version = get_ffmpeg_version(&ffmpeg_binary)?;
                let key = version_cache_key(&version);
                log::info!("Extracting filters for FFmpeg {version}...");
                let filters =
                    typed_ffmpeg_codegen::parse_help::filters::extract(&ffmpeg_binary)?;
                cache::save(&cache_dir, &format!("filters_{key}"), &filters)?;
                println!("Cached {} filters", filters.len());
            }
            ParseHelpAction::ExtractCodecs {
                ffmpeg_binary,
                cache_dir,
            } => {
                let cache_dir = cache_dir.unwrap_or_else(cache::default_cache_dir);
                let version = get_ffmpeg_version(&ffmpeg_binary)?;
                let key = version_cache_key(&version);
                log::info!("Extracting codecs for FFmpeg {version}...");
                let codecs =
                    typed_ffmpeg_codegen::parse_help::codecs::extract(&ffmpeg_binary)?;
                cache::save(&cache_dir, &format!("codecs_{key}"), &codecs)?;
                println!("Cached {} codecs", codecs.len());
            }
            ParseHelpAction::ExtractFormats {
                ffmpeg_binary,
                cache_dir,
            } => {
                let cache_dir = cache_dir.unwrap_or_else(cache::default_cache_dir);
                let version = get_ffmpeg_version(&ffmpeg_binary)?;
                let key = version_cache_key(&version);
                log::info!("Extracting formats for FFmpeg {version}...");
                let formats =
                    typed_ffmpeg_codegen::parse_help::formats::extract(&ffmpeg_binary)?;
                cache::save(&cache_dir, &format!("formats_{key}"), &formats)?;
                println!("Cached {} formats", formats.len());
            }
            ParseHelpAction::ExtractHelp {
                ffmpeg_binary,
                cache_dir,
            } => {
                let cache_dir = cache_dir.unwrap_or_else(cache::default_cache_dir);
                let version = get_ffmpeg_version(&ffmpeg_binary)?;
                let key = version_cache_key(&version);
                log::info!("Extracting full help for FFmpeg {version}...");
                let options =
                    typed_ffmpeg_codegen::parse_help::help::extract(&ffmpeg_binary)?;
                cache::save(&cache_dir, &format!("help_{key}"), &options)?;
                println!("Cached {} options", options.len());
            }
        },

        Commands::ParseC { action } => match action {
            ParseCAction::ParseOptions {
                ffmpeg_source,
                cache_dir,
            } => {
                let cache_dir = cache_dir.unwrap_or_else(cache::default_cache_dir);
                log::info!("Parsing FFmpeg options from C source...");
                let text = typed_ffmpeg_codegen::parse_c::pre_compile::preprocess_ffmpeg_opt(
                    &ffmpeg_source,
                )?;
                let options =
                    typed_ffmpeg_codegen::parse_c::parse_ffmpeg_opt::parse_ffmpeg_opt_c(&text)?;
                cache::save(&cache_dir, "c_options", &options)?;
                println!("Cached {} C options", options.len());
            }
        },

        Commands::ParseDocs { action } => match action {
            ParseDocsAction::Download { cache_dir } => {
                let cache_dir = cache_dir.unwrap_or_else(cache::default_cache_dir);
                cache::ensure_cache_dir(&cache_dir)?;
                let path = cache_dir.join("ffmpeg-filters.html");
                log::info!("Downloading FFmpeg filter docs...");
                typed_ffmpeg_codegen::parse_docs::download::download_ffmpeg_filter_docs(&path)?;
                println!("Downloaded to {}", path.display());
            }
            ParseDocsAction::Process { cache_dir } => {
                let cache_dir = cache_dir.unwrap_or_else(cache::default_cache_dir);
                log::info!("Processing FFmpeg filter docs...");
                let html = typed_ffmpeg_codegen::parse_docs::download::ensure_docs(&cache_dir)?;
                let docs =
                    typed_ffmpeg_codegen::parse_docs::parser::parse_filter_documents(&html)?;
                cache::save(&cache_dir, "filter_docs", &docs)?;
                println!("Processed {} filter documents", docs.len());
            }
        },

        Commands::Manual { action } => match action {
            ManualAction::InitConfig { name, cache_dir } => {
                let cache_dir = cache_dir.unwrap_or_else(cache::default_cache_dir);
                typed_ffmpeg_codegen::manual::init_config(&cache_dir, &name)?;
                println!("Initialized manual config for {name}");
            }
        },
    }

    Ok(())
}

fn print_section(title: &str, added: &[String], removed: &[String]) {
    if added.is_empty() && removed.is_empty() {
        println!("  {title}: no changes");
        return;
    }
    println!("  {title}:");
    for name in added {
        println!("    + {name}");
    }
    for name in removed {
        println!("    - {name}");
    }
}

/// Full generate command matching Python's code_gen/cli.py generate().
fn cmd_generate(
    ffmpeg_binary: String,
    outpath: PathBuf,
    version_dir: bool,
    rebuild: bool,
    cache_dir: Option<PathBuf>,
) -> Result<()> {
    let cache_dir = cache_dir.unwrap_or_else(cache::default_cache_dir);
    cache::ensure_cache_dir(&cache_dir)?;

    let version = get_ffmpeg_version(&ffmpeg_binary)?;
    log::info!("Detected FFmpeg version: {version}");

    if !is_supported_version(&version)? {
        anyhow::bail!("FFmpeg version {version} is not supported (minimum 5.0)");
    }

    let version_key = version_cache_key(&version);
    let major_version = version_key.split('_').next().unwrap_or("0");
    let version_prefix = if version_dir {
        Some(format!("v{major_version}"))
    } else {
        None
    };

    let actual_outpath = if let Some(ref prefix) = version_prefix {
        outpath.join(prefix)
    } else {
        outpath.clone()
    };

    // ---- Load filters (with schema conversion, manual overrides, doc merge) ----
    let filters_id = format!("filters_{version_key}");
    if rebuild || !cache::exists(&cache_dir, &filters_id) {
        log::info!("Extracting filters...");
        let raw_filters =
            typed_ffmpeg_codegen::parse_help::filters::extract(&ffmpeg_binary)?;

        // Load filter docs for URL references
        let filter_docs = load_filter_docs(&cache_dir);

        let mut filters: Vec<serde_json::Value> = Vec::new();
        for f in raw_filters {
            if f.name == "afir" {
                continue; // Known problematic filter
            }

            // Load manual config overrides FIRST (affects filter_type computation)
            let manual_config =
                typed_ffmpeg_codegen::manual::load_config(&cache_dir, &f.name)
                    .ok()
                    .flatten();

            let formula_input = manual_config.as_ref().and_then(|m| m.formula_typings_input.clone());
            let formula_output = manual_config.as_ref().and_then(|m| m.formula_typings_output.clone());
            let pre = manual_config.as_ref().map(|m| m.pre.clone()).unwrap_or_default();

            // Convert parse_help filter to main filter schema (with manual overrides)
            let mut filter_obj = convert_help_filter_to_schema(
                &f,
                formula_input.as_deref(),
                formula_output.as_deref(),
                &pre,
            );

            // Merge documentation URL
            if let Some(docs) = &filter_docs {
                if let Some(doc) = typed_ffmpeg_codegen::parse_docs::parser::find_filter_doc(
                    docs, &f.name,
                ) {
                    filter_obj["ref"] = serde_json::Value::String(doc.url());
                }
            }

            filters.push(filter_obj);
        }

        // Sort by name
        filters.sort_by(|a, b| {
            let an = a.get("name").and_then(|v| v.as_str()).unwrap_or("");
            let bn = b.get("name").and_then(|v| v.as_str()).unwrap_or("");
            an.cmp(bn)
        });

        cache::save(&cache_dir, &filters_id, &filters)?;
    }

    // ---- Load codecs (with __class__ tags for encoder/decoder) ----
    let codecs_id = format!("codecs_{version_key}");
    if rebuild || !cache::exists(&cache_dir, &codecs_id) {
        log::info!("Extracting codecs...");
        let codecs = typed_ffmpeg_codegen::parse_help::codecs::extract(&ffmpeg_binary)?;
        let converted: Vec<serde_json::Value> = codecs
            .into_iter()
            .map(|c| {
                let class = if c.is_encoder {
                    "FFMpegEncoder"
                } else {
                    "FFMpegDecoder"
                };
                let mut obj = serde_json::to_value(&c).unwrap_or_default();
                obj["__class__"] = serde_json::Value::String(class.to_string());
                obj["description"] = obj.get("help").cloned().unwrap_or_default();
                add_code_gen_type_to_options(&mut obj);
                obj
            })
            .collect();
        cache::save(&cache_dir, &codecs_id, &converted)?;
    }

    // ---- Load formats (with __class__ tags for muxer/demuxer) ----
    let formats_id = format!("formats_{version_key}");
    if rebuild || !cache::exists(&cache_dir, &formats_id) {
        log::info!("Extracting formats...");
        let formats = typed_ffmpeg_codegen::parse_help::formats::extract(&ffmpeg_binary)?;
        let converted: Vec<serde_json::Value> = formats
            .into_iter()
            .map(|f| {
                let is_muxer = f.flags.contains('E');
                let class = if is_muxer {
                    "FFMpegMuxer"
                } else {
                    "FFMpegDemuxer"
                };
                let mut obj = serde_json::to_value(&f).unwrap_or_default();
                obj["__class__"] = serde_json::Value::String(class.to_string());
                obj["description"] = obj.get("help").cloned().unwrap_or_default();
                obj["is_muxer"] = serde_json::Value::Bool(is_muxer);
                obj["is_demuxer"] = serde_json::Value::Bool(!is_muxer);
                add_code_gen_type_to_options(&mut obj);
                obj
            })
            .collect();
        cache::save(&cache_dir, &formats_id, &converted)?;
    }

    // ---- Load C options ----
    let options_id = format!("options_{version_key}");
    if rebuild || !cache::exists(&cache_dir, &options_id) {
        log::info!("Extracting C options (if ffmpeg source available)...");
        // C options require ffmpeg source; skip if not available
        // They'll be loaded from cache if already extracted via parse-c command
    }

    // ---- Load AV option sets (from ffmpeg -h full) ----
    let av_opts_id = format!("av_option_sets_{version_key}");
    if rebuild || !cache::exists(&cache_dir, &av_opts_id) {
        log::info!("Extracting AV option sets...");
        let help_options = typed_ffmpeg_codegen::parse_help::help::extract(&ffmpeg_binary)?;
        // Filter to only AV options (those with type field)
        let av_options: Vec<&_> = help_options
            .iter()
            .filter(|o| o.option_type.is_some())
            .collect();
        cache::save(&cache_dir, &av_opts_id, &av_options)?;
    }

    // ---- Load all cached data as JSON values for template rendering ----
    let filters: serde_json::Value =
        cache::load(&cache_dir, &filters_id)?.unwrap_or(serde_json::json!([]));
    let codecs: serde_json::Value =
        cache::load(&cache_dir, &codecs_id)?.unwrap_or(serde_json::json!([]));
    let muxers: serde_json::Value =
        cache::load(&cache_dir, &formats_id)?.unwrap_or(serde_json::json!([]));
    let options: serde_json::Value =
        cache::load(&cache_dir, &options_id)?.unwrap_or(serde_json::json!([]));
    let mut av_option_sets: serde_json::Value =
        cache::load(&cache_dir, &av_opts_id)?.unwrap_or(serde_json::json!([]));
    // Add code_gen_type to each AV option
    if let Some(arr) = av_option_sets.as_array_mut() {
        for opt in arr {
            let type_str = opt
                .get("option_type")
                .or_else(|| opt.get("type"))
                .and_then(|t| t.as_str())
                .unwrap_or("");
            let choices = opt.get("choices").and_then(|c| c.as_array()).cloned().unwrap_or_default();
            let base = match type_str {
                "boolean" => "bool | None",
                "int" | "int64" | "unsigned" => "int | None",
                "float" | "double" => "float | None",
                "sample_rate" => "int | None",
                _ => "str | None",
            };
            let suffix = if type_str != "flags" && !choices.is_empty() {
                let lits: Vec<String> = choices.iter()
                    .filter_map(|c| c.get("name").and_then(|n| n.as_str()))
                    .map(|n| format!("\"{n}\""))
                    .collect();
                format!("| Literal[{}]", lits.join(", "))
            } else { String::new() };
            opt["code_gen_type"] = serde_json::Value::String(format!("{base}{suffix}"));
        }
    }

    // ---- Build version metadata for deprecation hints ----
    let version_metadata = if version_dir {
        let mut available = std::collections::HashSet::new();
        if let Ok(entries) = std::fs::read_dir(&cache_dir) {
            for entry in entries.flatten() {
                let name = entry.file_name().to_string_lossy().to_string();
                if name.starts_with("filters_") && name.ends_with(".json") {
                    let parts: Vec<&str> = name
                        .strip_prefix("filters_")
                        .unwrap()
                        .strip_suffix(".json")
                        .unwrap()
                        .split('_')
                        .collect();
                    if parts.len() == 2 {
                        available.insert(format!("{}.{}", parts[0], parts[1]));
                    }
                }
            }
        }
        if !available.is_empty() {
            let versions: Vec<String> = available.into_iter().collect();
            Some(version_diff::build_version_metadata(&cache_dir, &versions))
        } else {
            None
        }
    } else {
        None
    };

    // ---- Build template context ----
    let mut context = tera::Context::new();
    context.insert("filters", &filters);
    context.insert("codecs", &codecs);
    context.insert("muxers", &muxers);
    context.insert("options", &options);
    context.insert("av_option_sets", &av_option_sets);
    context.insert("ffmpeg_version", &version);
    if let Some(ref prefix) = version_prefix {
        context.insert("version_prefix", prefix);
    }
    // version_metadata is used via format_version_note Tera function
    context.insert(
        "has_version_metadata",
        &version_metadata.is_some(),
    );

    // ---- Determine template directory ----
    let template_dir = find_template_dir()?;

    log::info!(
        "Rendering templates from {} to {}",
        template_dir.display(),
        actual_outpath.display()
    );
    let rendered = typed_ffmpeg_codegen::codegen::gen::render(
        &template_dir,
        &actual_outpath,
        version_prefix.as_deref(),
        &mut context,
        version_metadata,
    )?;

    log::info!(
        "Generated {} files at {}",
        rendered.len(),
        actual_outpath.display()
    );
    Ok(())
}

/// Implement the reexport command matching Python's reexport().
fn cmd_reexport(version: Option<String>, outpath: PathBuf) -> Result<()> {
    use regex::Regex;

    let version = if let Some(v) = version {
        v
    } else {
        // Find latest version dir
        let mut version_dirs: Vec<String> = Vec::new();
        if let Ok(entries) = std::fs::read_dir(&outpath) {
            for entry in entries.flatten() {
                let name = entry.file_name().to_string_lossy().to_string();
                if entry.path().is_dir()
                    && name.starts_with('v')
                    && name[1..].chars().all(|c| c.is_ascii_digit())
                {
                    version_dirs.push(name);
                }
            }
        }
        version_dirs.sort();
        let last = version_dirs
            .last()
            .ok_or_else(|| {
                anyhow::anyhow!("No version directories found. Run 'generate --version-dir' first.")
            })?
            .clone();
        last[1..].to_string() // "v8" → "8"
    };

    let version_prefix = format!("v{version}");
    let version_dir = outpath.join(&version_prefix);
    if !version_dir.exists() {
        anyhow::bail!("Version directory {} does not exist.", version_dir.display());
    }

    // Only re-export user-facing entry point modules
    let reexport_targets = ["filters.py", "sources.py"];

    let re_func = Regex::new(r"^def\s+([a-zA-Z_]\w*)\s*\(")?;
    let re_class = Regex::new(r"^class\s+([a-zA-Z_]\w*)")?;

    for filename in &reexport_targets {
        let src = version_dir.join(filename);
        if !src.exists() {
            continue;
        }

        let content = std::fs::read_to_string(&src)?;
        let mut names: Vec<String> = Vec::new();

        for line in content.lines() {
            if let Some(caps) = re_func.captures(line) {
                let name = &caps[1];
                if !name.starts_with('_') {
                    names.push(name.to_string());
                }
            } else if let Some(caps) = re_class.captures(line) {
                let name = &caps[1];
                if !name.starts_with('_') {
                    names.push(name.to_string());
                }
            }
        }

        if names.is_empty() {
            continue;
        }
        names.sort();

        let module_name = filename.replace(".py", "").replace('/', ".");
        let reexport_path = outpath.join(filename);

        let mut lines = vec![
            "# NOTE: this file is auto-generated, do not modify".to_string(),
            format!(
                "\"\"\"Re-exports from ffmpeg.{version_prefix}.{module_name} (default version).\"\"\""
            ),
            String::new(),
            format!("from ffmpeg.{version_prefix}.{module_name} import ("),
        ];
        for name in &names {
            lines.push(format!("    {name} as {name},"));
        }
        lines.push(")".to_string());
        lines.push(String::new());
        lines.push("__all__ = [".to_string());
        for name in &names {
            lines.push(format!("    \"{name}\","));
        }
        lines.push("]".to_string());
        lines.push(String::new());

        std::fs::write(&reexport_path, lines.join("\n"))?;
        println!(
            "  Generated {} ({} symbols from {version_prefix})",
            reexport_path.display(),
            names.len()
        );
    }

    Ok(())
}

/// Convert a parse_help HelpFilter to a JSON value matching FFMpegFilter schema.
fn convert_help_filter_to_schema(
    f: &typed_ffmpeg_codegen::schema::parse_help::HelpFilter,
    formula_input: Option<&str>,
    formula_output: Option<&str>,
    pre: &[(String, String)],
) -> serde_json::Value {
    let stream_typings_input: Vec<serde_json::Value> = f
        .stream_typings_input
        .iter()
        .map(|io| {
            serde_json::json!({
                "__class__": "FFMpegIOType",
                "name": io.name,
                "type": { "__class__": "StreamType", "value": io.stream_type }
            })
        })
        .collect();

    let stream_typings_output: Vec<serde_json::Value> = f
        .stream_typings_output
        .iter()
        .map(|io| {
            serde_json::json!({
                "__class__": "FFMpegIOType",
                "name": io.name,
                "type": { "__class__": "StreamType", "value": io.stream_type }
            })
        })
        .collect();

    let options: Vec<serde_json::Value> = f
        .options
        .iter()
        .map(|opt| {
            let choices: Vec<serde_json::Value> = opt
                .choices
                .iter()
                .map(|c| {
                    serde_json::json!({
                        "__class__": "FFMpegFilterOptionChoice",
                        "name": c.name,
                        "help": c.help,
                        "flags": c.flags,
                        "value": c.value,
                    })
                })
                .collect();
            serde_json::json!({
                "__class__": "FFMpegFilterOption",
                "name": opt.name,
                "type": { "__class__": "FFMpegFilterOptionType", "value": opt.option_type },
                "default": opt.default,
                "description": opt.help,
                "choices": choices,
            })
        })
        .collect();

    let is_filter_sink = f.io_flags.ends_with("->|");
    let is_filter_source = f.io_flags.starts_with("|->");
    let is_dynamic_input = f.io_flags.contains("N->");
    let is_dynamic_output = f.io_flags.contains("->N");

    // Compute filter_type (mirrors Python FFMpegFilter.filter_type property)
    let filter_type = compute_filter_type(
        is_filter_sink,
        is_filter_source,
        is_dynamic_input,
        is_dynamic_output,
        &stream_typings_input,
        &stream_typings_output,
        formula_input,
        formula_output,
    );

    // Compute to_def (mirrors Python FFMpegFilter.to_def property)
    let typings_input = if let Some(fi) = formula_input {
        serde_json::Value::String(fi.to_string())
    } else {
        let arr: Vec<String> = stream_typings_input
            .iter()
            .filter_map(|io| io.get("type").and_then(|t| t.get("value")).and_then(|v| v.as_str()))
            .map(String::from)
            .collect();
        serde_json::to_value(&arr).unwrap_or_default()
    };
    let typings_output = if let Some(fo) = formula_output {
        serde_json::Value::String(fo.to_string())
    } else {
        let arr: Vec<String> = stream_typings_output
            .iter()
            .filter_map(|io| io.get("type").and_then(|t| t.get("value")).and_then(|v| v.as_str()))
            .map(String::from)
            .collect();
        serde_json::to_value(&arr).unwrap_or_default()
    };

    let to_def = serde_json::json!({
        "__class__": "FFMpegFilterDef",
        "name": f.name,
        "typings_input": typings_input,
        "typings_output": typings_output,
    });

    // Compute input_typings set (for template conditionals)
    let input_typings_set = compute_input_typings_set(
        is_filter_source, is_dynamic_input,
        &stream_typings_input, formula_input,
    );

    serde_json::json!({
        "__class__": "FFMpegFilter",
        "name": f.name,
        "description": f.help,
        "is_support_timeline": f.is_timeline,
        "is_support_slice_threading": f.is_slice_threading,
        "is_support_command": false,
        "is_support_framesync": f.is_framesync,
        "is_filter_sink": is_filter_sink,
        "is_filter_source": is_filter_source,
        "is_dynamic_input": is_dynamic_input,
        "is_dynamic_output": is_dynamic_output,
        "stream_typings_input": stream_typings_input,
        "stream_typings_output": stream_typings_output,
        "formula_typings_input": formula_input,
        "formula_typings_output": formula_output,
        "options": options,
        "opt_names": f.options.iter().map(|o| &o.name).collect::<Vec<_>>(),
        "pre": pre,
        "filter_type": { "value": filter_type },
        "to_def": to_def,
        "input_typings": input_typings_set,
    })
}

/// Add `code_gen_type` field to each option in a codec/format JSON object.
/// This mirrors the Python `FFMpegAVOption.code_gen_type` property.
fn add_code_gen_type_to_options(obj: &mut serde_json::Value) {
    if let Some(options) = obj.get_mut("options").and_then(|v| v.as_array_mut()) {
        for opt in options {
            let type_str = opt
                .get("option_type")
                .or_else(|| opt.get("type"))
                .and_then(|t| t.as_str())
                .unwrap_or("");
            let choices = opt
                .get("choices")
                .and_then(|c| c.as_array())
                .cloned()
                .unwrap_or_default();

            let base = match type_str {
                "boolean" => "bool | None",
                "int" | "int64" | "unsigned" => "int | None",
                "float" | "double" => "float | None",
                "sample_rate" => "int | None",
                "string" | "channel_layout" | "flags" | "duration" | "dictionary"
                | "image_size" | "pixel_format" | "sample_fmt" | "binary" | "rational"
                | "color" | "video_rate" | "pix_fmt" => "str | None",
                _ => "str | None",
            };

            let choices_suffix = if type_str != "flags" && !choices.is_empty() {
                let literals: Vec<String> = choices
                    .iter()
                    .filter_map(|c| c.get("name").and_then(|n| n.as_str()))
                    .map(|n| format!("\"{n}\""))
                    .collect();
                format!("| Literal[{}]", literals.join(", "))
            } else {
                String::new()
            };

            opt["code_gen_type"] =
                serde_json::Value::String(format!("{base}{choices_suffix}"));
        }
    }
}

/// Compute filter type classification from filter properties.
fn compute_filter_type(
    is_sink: bool,
    is_source: bool,
    is_dynamic_input: bool,
    _is_dynamic_output: bool,
    stream_typings_input: &[serde_json::Value],
    stream_typings_output: &[serde_json::Value],
    formula_input: Option<&str>,
    formula_output: Option<&str>,
) -> String {
    let input_types = compute_input_typings_set(is_source, is_dynamic_input, stream_typings_input, formula_input);
    let output_types = compute_output_typings_set(is_sink, _is_dynamic_output, stream_typings_output, formula_output);

    let has_video_in = input_types.iter().any(|t| t.as_str() == Some("video"));
    let has_audio_in = input_types.iter().any(|t| t.as_str() == Some("audio"));
    let has_video_out = output_types.iter().any(|t| t.as_str() == Some("video"));
    let has_audio_out = output_types.iter().any(|t| t.as_str() == Some("audio"));

    if is_sink {
        if has_video_in { return "vsink".into(); }
        if has_audio_in { return "asink".into(); }
    } else if is_source {
        if has_video_out && has_audio_out { return "avsrc".into(); }
        if has_video_out { return "vsrc".into(); }
        if has_audio_out { return "asrc".into(); }
        // Dynamic output source with no formula: infer from formula strings if available
        if let Some(fo) = formula_output {
            if fo.contains("audio") && !fo.contains("video") { return "asrc".into(); }
            if fo.contains("video") && !fo.contains("audio") { return "vsrc".into(); }
            return "avsrc".into();
        }
        // No formula at all: can't determine, default to vsrc
        return "vsrc".into();
    }

    if input_types.is_empty() {
        if has_video_out { return "vf".into(); }
        if has_audio_out { return "af".into(); }
        return "vf".into();
    }

    if has_video_in && !has_audio_in {
        if has_audio_out { return "vaf".into(); }
        // Dynamic output with no formula: infer from input type
        return "vf".into();
    }
    if has_audio_in && !has_video_in {
        if has_audio_out && !has_video_out { return "af".into(); }
        if has_video_out { return "avf".into(); }
        // Dynamic output with no formula: infer from input type
        return "af".into();
    }
    if has_video_in && has_audio_in {
        return "avf".into();
    }

    "vf".into()
}

fn compute_input_typings_set(
    is_source: bool,
    is_dynamic: bool,
    stream_typings: &[serde_json::Value],
    formula: Option<&str>,
) -> Vec<serde_json::Value> {
    if is_source { return vec![]; }
    if !is_dynamic {
        return stream_typings
            .iter()
            .filter_map(|io| io.get("type").and_then(|t| t.get("value")).cloned())
            .collect();
    }
    if let Some(f) = formula {
        let mut set = vec![];
        if f.contains("video") { set.push(serde_json::json!("video")); }
        if f.contains("audio") { set.push(serde_json::json!("audio")); }
        if set.is_empty() { set.push(serde_json::json!("video")); }
        return set;
    }
    vec![serde_json::json!("video")]
}

fn compute_output_typings_set(
    is_sink: bool,
    is_dynamic: bool,
    stream_typings: &[serde_json::Value],
    formula: Option<&str>,
) -> Vec<serde_json::Value> {
    if is_sink { return vec![]; }
    if !is_dynamic {
        return stream_typings
            .iter()
            .filter_map(|io| io.get("type").and_then(|t| t.get("value")).cloned())
            .collect();
    }
    if let Some(f) = formula {
        let mut set = vec![];
        if f.contains("video") { set.push(serde_json::json!("video")); }
        if f.contains("audio") { set.push(serde_json::json!("audio")); }
        return set;
    }
    vec![]
}

/// Load filter docs from cache, returning None if unavailable.
fn load_filter_docs(
    cache_dir: &std::path::Path,
) -> Option<Vec<typed_ffmpeg_codegen::schema::docs::FilterDocument>> {
    // Try loading cached docs first
    if let Ok(Some(docs)) = cache::load::<Vec<typed_ffmpeg_codegen::schema::docs::FilterDocument>>(cache_dir, "filter_docs") {
        return Some(docs);
    }

    // Try downloading and parsing
    log::info!("Downloading FFmpeg filter documentation...");
    let html = match typed_ffmpeg_codegen::parse_docs::download::ensure_docs(cache_dir) {
        Ok(h) => h,
        Err(e) => {
            log::warn!("Could not download filter docs: {e}. Doc URLs will be empty.");
            return None;
        }
    };
    match typed_ffmpeg_codegen::parse_docs::parser::parse_filter_documents(&html) {
        Ok(docs) => {
            // Cache for next time
            let _ = cache::save(cache_dir, "filter_docs", &docs);
            log::info!("Parsed {} filter documents", docs.len());
            Some(docs)
        }
        Err(e) => {
            log::warn!("Could not parse filter docs: {e}");
            None
        }
    }
}

/// Find the template directory (next to binary or via CARGO_MANIFEST_DIR).
fn find_template_dir() -> Result<PathBuf> {
    // Check next to binary first (release mode)
    if let Ok(exe) = std::env::current_exe() {
        let next_to_bin = exe.parent().unwrap().join("templates");
        if next_to_bin.exists() {
            return Ok(next_to_bin);
        }
    }

    // Dev mode: relative to manifest dir
    let manifest = PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("templates");
    if manifest.exists() {
        return Ok(manifest);
    }

    anyhow::bail!("Could not find templates directory")
}
