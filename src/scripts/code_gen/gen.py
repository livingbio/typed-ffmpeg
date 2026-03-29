"""Code generation utilities for typed-ffmpeg."""

import keyword
import pathlib
import re
from math import isnan
from pathlib import Path
from typing import Any

import jinja2

from ffmpeg_core.common.schema import (
    FFMpegFilter,
    FFMpegFilterOption,
    FFMpegFilterOptionType,
    FFMpegOption,
    FFMpegOptionType,
)

from .utils import get_relative_import

template_folder = Path(__file__).parent / "templates"

loader = jinja2.FileSystemLoader(template_folder)
env = jinja2.Environment(
    loader=loader,
)


def filter_option_typing(option: FFMpegFilterOption) -> str:
    """
    Get the typing of the filter option.

    Args:
        option: The filter option

    Returns:
        The typing of the filter option

    """
    base_type = None
    if option.type == FFMpegFilterOptionType.boolean:
        base_type = "Boolean"
    elif option.type == FFMpegFilterOptionType.duration:
        base_type = "Duration"
    elif option.type == FFMpegFilterOptionType.color:
        base_type = "Color"
    elif option.type == FFMpegFilterOptionType.flags:
        base_type = "Flags"
    elif option.type == FFMpegFilterOptionType.dictionary:
        base_type = "Dictionary"
    elif option.type == FFMpegFilterOptionType.pix_fmt:
        base_type = "Pix_fmt"
    elif option.type == FFMpegFilterOptionType.int:
        base_type = "Int"
    elif option.type == FFMpegFilterOptionType.int64:
        base_type = "Int64"
    elif option.type == FFMpegFilterOptionType.double:
        base_type = "Double"
    elif option.type == FFMpegFilterOptionType.float:
        base_type = "Float"
    elif option.type == FFMpegFilterOptionType.string:
        base_type = "String"
    elif option.type == FFMpegFilterOptionType.video_rate:
        base_type = "Video_rate"
    elif option.type == FFMpegFilterOptionType.image_size:
        base_type = "Image_size"
    elif option.type == FFMpegFilterOptionType.rational:
        base_type = "Rational"
    elif option.type == FFMpegFilterOptionType.sample_fmt:
        base_type = "Sample_fmt"
    elif option.type == FFMpegFilterOptionType.binary:
        base_type = "Binary"
    elif option.type == FFMpegFilterOptionType.channel_layout:
        base_type = "String"
    elif option.type == FFMpegFilterOptionType.unsigned:
        base_type = "Int"

    assert base_type, f"{option.type} not fit"
    if not option.choices:
        return base_type

    values = ",".join(f'"{i.name}"' for i in option.choices)
    return base_type + f"| Literal[{values}]"


def stream_name_safe(string: str) -> str:
    """
    Convert stream name to safe name.

    Args:
        string: The stream name

    Returns:
        The stream name safe

    """
    opt_name = option_name_safe(string)
    if not opt_name.startswith("_"):
        return "_" + opt_name
    return opt_name


def option_name_safe(string: str) -> str:
    """
    Convert option name to safe name.

    Args:
        string: The option name

    Returns:
        The option name safe

    """
    # Keep the shorthand help option readable.
    if string == "?":
        return "_q"

    safe = string.replace("-", "_")
    safe = re.sub(r"\W", "_", safe)
    if not safe:
        return "_"
    if safe[0].isdigit():
        safe = "_" + safe
    if safe in keyword.kwlist:
        safe = "_" + safe
    return safe


def option_typing(option: FFMpegOption) -> str:
    """
    Get the typing of the option.

    Args:
        option: The option

    Returns:
        The typing of the option

    Raises:
        ValueError: If the option type is unknown.

    """
    match option.type:
        case FFMpegOptionType.OPT_TYPE_FUNC:
            return "Func"
        case FFMpegOptionType.OPT_TYPE_BOOL:
            return "Boolean"
        case FFMpegOptionType.OPT_TYPE_STRING:
            return "String"
        case FFMpegOptionType.OPT_TYPE_INT:
            return "Int"
        case FFMpegOptionType.OPT_TYPE_INT64:
            return "Int64"
        case FFMpegOptionType.OPT_TYPE_FLOAT:
            return "Float"
        case FFMpegOptionType.OPT_TYPE_DOUBLE:
            return "Double"
        case FFMpegOptionType.OPT_TYPE_TIME:
            return "Time"
        case _:
            raise ValueError(f"Unknown option type: {option.type}")


def input_typings(ffmpeg_filter: FFMpegFilter) -> str:
    """
    Get the input typings of the filter.

    Args:
        ffmpeg_filter: The filter

    Returns:
        The input typings of the filter

    """
    if ffmpeg_filter.formula_typings_input:
        return ffmpeg_filter.formula_typings_input
    return (
        "["
        + ", ".join(
            f"StreamType.{i.type.value}" for i in ffmpeg_filter.stream_typings_input
        )
        + "]"
    )


def output_typings(ffmpeg_filter: FFMpegFilter) -> str:
    """
    Get the output typings of the filter.

    Args:
        ffmpeg_filter: The filter

    Returns:
        The output typings of the filter

    """
    if ffmpeg_filter.formula_typings_output:
        return ffmpeg_filter.formula_typings_output
    return (
        "["
        + ", ".join(
            f"StreamType.{i.type.value}" for i in ffmpeg_filter.stream_typings_output
        )
        + "]"
    )


def default_value(option: FFMpegFilterOption, f: FFMpegFilter) -> str:
    """
    Get the default value of the filter option.

    Args:
        option: The filter option
        f: The filter

    Returns:
        The default value of the filter option

    """
    if option.name in f.pre_dict:
        return f"Auto({repr(f.pre_dict[option.name])})"
    if not isinstance(option.default, float) or not isnan(option.default):
        return f"Default({repr(option.default)})"
    return 'Default("nan")'


def default_typings(option: FFMpegFilterOption, f: FFMpegFilter) -> str:
    """
    Get the default typing of the filter option.

    Args:
        option: The filter option
        f: The filter

    Returns:
        The default typing of the filter option

    """
    if option.choices:
        return f"{filter_option_typing(option)} | Default = {default_value(option, f)}"
    return f"{filter_option_typing(option)} = {default_value(option, f)}"


def filter_option_typings(ffmpeg_filter: FFMpegFilter) -> str:
    """
    Get the typing of the filter options.

    Args:
        ffmpeg_filter: The filter

    Returns:
        The typing of the filter options

    """
    output = []

    for option in ffmpeg_filter.options:
        output.append(
            f"{option_name_safe(option.name)}: {default_typings(option, ffmpeg_filter)}"
        )

    if output:
        return ",".join(output) + ","
    return ""


def normalize_help_text(text: str) -> str:
    r"""
    Normalize help text by replacing newlines and extra spaces.

    This function handles cases where FFmpeg help text contains line breaks,
    such as: 'text ("option1", "option2"\n        "continuation text")'
    The pattern specifically targets the C-style string continuation where
    a backslash-newline-whitespace-quote sequence should be replaced with
    a single space to join the strings properly.

    Args:
        text: The help text to normalize

    Returns:
        The normalized help text with all content on a single line

    """
    # Replace literal backslash-n followed by spaces and quote with space
    # This handles C-style string continuation: "text\n        "more text"
    normalized = re.sub(r'\\\n\s*"', " ", text)
    # Replace newlines and following whitespace with a single space
    normalized = re.sub(r"\n\s*", " ", normalized)
    # Replace multiple spaces with a single space
    normalized = re.sub(r"\s+", " ", normalized)
    # Strip backslash-escapes before quotes (invalid in Python docstrings)
    normalized = normalized.replace('\\"', '"')
    return normalized.strip()


env.filters["stream_name_safe"] = stream_name_safe
env.filters["option_name_safe"] = option_name_safe
env.filters["filter_option_typing"] = filter_option_typing
env.filters["option_typing"] = option_typing
env.filters["input_typings"] = input_typings
env.filters["output_typings"] = output_typings
env.filters["filter_option_typings"] = filter_option_typings
env.filters["normalize_help_text"] = normalize_help_text
env.globals["get_relative_import"] = get_relative_import
env.globals["format_version_note"] = (
    None  # Set at render time when version metadata exists
)

# Set of modules that are generated from templates (as opposed to hand-written).
# This is derived from the template file names and used by the versioned import
# resolver to decide between relative (generated→generated) and absolute
# (generated→shared core) imports.
GENERATED_MODULES: set[str] = set()
for _tf in template_folder.glob("**/*.*.jinja"):
    _rel = _tf.relative_to(template_folder)
    # Convert path to module name: "streams/video.py.jinja" → "streams.video"
    _mod = str(_rel).split(".")[0].replace("/", ".")
    GENERATED_MODULES.add(_mod)


def render(
    *,
    outpath: pathlib.Path,
    version_prefix: str | None = None,
    **kwargs: Any,
) -> list[pathlib.Path]:
    """
    Render the filter and option documents.

    Args:
        outpath: The output path
        version_prefix: Version subdirectory name (e.g., "v6") for versioned
            output. When set, generated files use absolute imports for shared
            core modules.
        **kwargs: Additional keyword arguments to pass to the template

    Returns:
        The rendered files

    """
    outpath.mkdir(parents=True, exist_ok=True)
    output = []

    # Create a version-aware import function for templates.
    # NOTE: We pass this as a template variable (not env.globals) because
    # Jinja2 caches imported macro modules with the globals from their first
    # render. Passing via template.render() ensures each render gets the
    # correct function regardless of macro caching.
    def versioned_get_relative_import(
        import_path: str, template_path: str, imports: str
    ) -> str:
        return get_relative_import(
            import_path,
            template_path,
            imports,
            version_prefix=version_prefix,
            generated_modules=GENERATED_MODULES,
        )

    # Wire up version note function if metadata is provided
    version_metadata = kwargs.pop("version_metadata", None)
    format_version_note_fn = None
    if version_metadata is not None:
        from .version_diff import format_version_note as _fmt_note

        current_major = version_prefix[1:] if version_prefix else None

        def format_version_note_fn(name: str) -> str | None:  # type: ignore[no-redef]
            return _fmt_note(
                name,
                version_metadata.filter_versions,
                version_metadata.available_versions,
                current_major or "",
            )

    for template_file in template_folder.glob("**/*.*.jinja"):
        template_path = template_file.relative_to(template_folder)

        template = env.get_template(str(template_path))
        code = template.render(
            template_path=template_path,
            get_relative_import=versioned_get_relative_import,
            format_version_note=format_version_note_fn,
            **kwargs,
        )

        opath = outpath / str(template_path).replace(".jinja", "")
        opath.parent.mkdir(parents=True, exist_ok=True)

        # Strip trailing whitespace from each line to satisfy pre-commit hooks
        code = "\n".join(line.rstrip() for line in code.splitlines())

        with opath.open("w") as ofile:
            ofile.write("# NOTE: this file is auto-generated, do not modify\n")
            ofile.write(code)
            if not code.endswith("\n"):
                ofile.write("\n")

        output.append(opath)

    # Generate py.typed marker for type checker discovery
    py_typed = outpath / "py.typed"
    py_typed.touch()
    output.append(py_typed)

    # Generate __init__.py for the version subpackage
    if version_prefix:
        init_py = outpath / "__init__.py"
        if not init_py.exists():
            init_py.write_text(
                f'"""typed-ffmpeg bindings for FFmpeg {version_prefix}."""\n'
            )
            output.append(init_py)

    return output


# ── TypeScript code generation ──────────────────────────────────────────────

template_folder_ts = Path(__file__).parent / "templates_ts"


_TS_RESERVED_WORDS = {
    "break",
    "case",
    "catch",
    "class",
    "const",
    "continue",
    "debugger",
    "default",
    "delete",
    "do",
    "else",
    "enum",
    "export",
    "extends",
    "false",
    "finally",
    "for",
    "function",
    "if",
    "import",
    "in",
    "instanceof",
    "new",
    "null",
    "return",
    "super",
    "switch",
    "this",
    "throw",
    "true",
    "try",
    "typeof",
    "var",
    "void",
    "while",
    "with",
    "yield",
    "let",
    "static",
    "implements",
    "interface",
    "package",
    "private",
    "protected",
    "public",
    "abstract",
    "as",
    "async",
    "await",
    "constructor",
    "declare",
    "from",
    "get",
    "is",
    "module",
    "namespace",
    "of",
    "require",
    "set",
    "type",
    "undefined",
}


def ts_option_name_safe(string: str) -> str:
    """
    Convert option name to TypeScript-safe identifier.

    Returns:
        A TypeScript-safe identifier string.

    """
    safe = option_name_safe(string)
    if safe in _TS_RESERVED_WORDS:
        safe = "_" + safe
    return safe


def ts_stream_name_safe(string: str) -> str:
    """
    Convert stream name to TypeScript-safe identifier.

    Returns:
        A TypeScript-safe identifier string.

    """
    safe = stream_name_safe(string)
    if safe.lstrip("_") in _TS_RESERVED_WORDS:
        safe = "_" + safe
    return safe


def ts_filter_option_typing(option: FFMpegFilterOption) -> str:
    """
    Map FFMpeg filter option type to TypeScript type alias.

    Returns:
        The TypeScript type alias string.

    """
    type_map = {
        FFMpegFilterOptionType.boolean: "FFBoolean",
        FFMpegFilterOptionType.duration: "FFDuration",
        FFMpegFilterOptionType.color: "FFColor",
        FFMpegFilterOptionType.flags: "FFFlags",
        FFMpegFilterOptionType.dictionary: "FFDictionary",
        FFMpegFilterOptionType.pix_fmt: "FFPixFmt",
        FFMpegFilterOptionType.int: "FFInt",
        FFMpegFilterOptionType.int64: "FFInt64",
        FFMpegFilterOptionType.double: "FFDouble",
        FFMpegFilterOptionType.float: "FFFloat",
        FFMpegFilterOptionType.string: "FFString",
        FFMpegFilterOptionType.video_rate: "FFVideoRate",
        FFMpegFilterOptionType.image_size: "FFImageSize",
        FFMpegFilterOptionType.rational: "FFRational",
        FFMpegFilterOptionType.sample_fmt: "FFSampleFmt",
        FFMpegFilterOptionType.binary: "FFBinary",
        FFMpegFilterOptionType.channel_layout: "FFString",
        FFMpegFilterOptionType.unsigned: "FFInt",
    }
    base = type_map.get(option.type, "FFString")
    if not option.choices:
        return base
    values = " | ".join(f'"{i.name}"' for i in option.choices)
    return f"{base} | {values}"


def ts_input_typings(ffmpeg_filter: FFMpegFilter) -> str:
    """
    Generate TypeScript array literal for input typings (pre-evaluated).

    Returns:
        Comma-separated string of "video"/"audio" literals.

    """
    if ffmpeg_filter.formula_typings_input:
        # Pre-evaluate: convert Python formula to static TS array
        # For dynamic inputs, we just return an empty array (handled at runtime)
        return ""
    return ", ".join(
        '"video"' if i.type.value == "video" else '"audio"'
        for i in ffmpeg_filter.stream_typings_input
    )


def ts_output_typings(ffmpeg_filter: FFMpegFilter) -> str:
    """
    Generate TypeScript array literal for output typings (pre-evaluated).

    Returns:
        Comma-separated string of "video"/"audio" literals.

    """
    if ffmpeg_filter.formula_typings_output:
        return ""
    return ", ".join(
        '"video"' if i.type.value == "video" else '"audio"'
        for i in ffmpeg_filter.stream_typings_output
    )


def ts_option_typing(option: FFMpegOption) -> str:
    """
    Map FFMpeg CLI option type to TypeScript type alias.

    Returns:
        The TypeScript type alias string.

    """
    type_map = {
        FFMpegOptionType.OPT_TYPE_FUNC: "FFFunc",
        FFMpegOptionType.OPT_TYPE_BOOL: "FFBoolean",
        FFMpegOptionType.OPT_TYPE_STRING: "FFString",
        FFMpegOptionType.OPT_TYPE_INT: "FFInt",
        FFMpegOptionType.OPT_TYPE_INT64: "FFInt64",
        FFMpegOptionType.OPT_TYPE_FLOAT: "FFFloat",
        FFMpegOptionType.OPT_TYPE_DOUBLE: "FFDouble",
        FFMpegOptionType.OPT_TYPE_TIME: "FFTime",
    }
    return type_map.get(option.type, "FFString")


def ts_av_option_type(option: Any) -> str:
    """
    Map FFMpeg AV option type to TypeScript type.

    Returns:
        The TypeScript type string.

    """
    type_map = {
        "boolean": "boolean | null",
        "int": "number | null",
        "int64": "number | null",
        "unsigned": "number | null",
        "float": "number | null",
        "double": "number | null",
        "string": "string | null",
        "channel_layout": "string | null",
        "flags": "string | null",
        "duration": "string | null",
        "dictionary": "string | null",
        "image_size": "string | null",
        "pixel_format": "string | null",
        "sample_rate": "number | null",
        "sample_fmt": "string | null",
        "binary": "string | null",
        "rational": "string | null",
        "color": "string | null",
        "video_rate": "string | null",
        "pix_fmt": "string | null",
    }
    base = type_map.get(option.type, "string | null")
    if option.choices and option.type != "flags":
        literals = " | ".join(f'"{c.name}"' for c in option.choices)
        return f"{base} | {literals}"
    return base


def render_ts(
    *,
    outpath: pathlib.Path,
    **kwargs: Any,
) -> list[pathlib.Path]:
    """
    Render TypeScript templates.

    Args:
        outpath: The output path for generated .ts files
        **kwargs: Context variables (filters, options, codecs, etc.)

    Returns:
        List of generated file paths

    """
    loader_ts = jinja2.FileSystemLoader(template_folder_ts)
    env_ts = jinja2.Environment(loader=loader_ts)

    # Register TS-specific Jinja2 filters
    env_ts.filters["stream_name_safe"] = ts_stream_name_safe
    env_ts.filters["option_name_safe"] = ts_option_name_safe
    env_ts.filters["filter_option_typing"] = ts_filter_option_typing
    env_ts.filters["option_typing"] = ts_option_typing
    env_ts.filters["input_typings_ts"] = ts_input_typings
    env_ts.filters["output_typings_ts"] = ts_output_typings
    env_ts.filters["normalize_help_text"] = normalize_help_text
    env_ts.filters["striptags"] = lambda s: re.sub(r"<[^>]+>", "", s) if s else ""
    env_ts.filters["ts_av_option_type"] = ts_av_option_type

    # Wire up version note function (None by default)
    version_metadata = kwargs.pop("version_metadata", None)
    format_version_note_fn = None
    if version_metadata is not None:
        from .version_diff import format_version_note as _fmt_note

        ffmpeg_version = kwargs.get("ffmpeg_version", "")
        current_major = ffmpeg_version.split(".")[0] if ffmpeg_version else ""

        def format_version_note_fn(name: str) -> str | None:  # type: ignore[no-redef]
            return _fmt_note(
                name,
                version_metadata.filter_versions,
                version_metadata.available_versions,
                current_major,
            )

    outpath.mkdir(parents=True, exist_ok=True)
    output = []

    for template_file in template_folder_ts.glob("**/*.*.jinja"):
        template_path = template_file.relative_to(template_folder_ts)

        # Skip macro-only templates (starting with _)
        if template_path.name.startswith("_"):
            continue

        template = env_ts.get_template(str(template_path))
        code = template.render(
            template_path=template_path,
            format_version_note=format_version_note_fn,
            **kwargs,
        )

        opath = outpath / str(template_path).replace(".jinja", "")
        opath.parent.mkdir(parents=True, exist_ok=True)

        # Strip trailing whitespace
        code = "\n".join(line.rstrip() for line in code.splitlines())

        with opath.open("w") as ofile:
            ofile.write("// NOTE: this file is auto-generated, do not modify\n")
            ofile.write(code)
            if not code.endswith("\n"):
                ofile.write("\n")

        output.append(opath)

    return output
