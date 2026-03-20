"""Code generation utilities for typed-ffmpeg."""

import keyword
import pathlib
import re
from math import isnan
from pathlib import Path
from typing import Any

import jinja2

from ffmpeg.common.schema import (
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
    if string in keyword.kwlist:
        return "_" + string
    if string[0].isdigit():
        return "_" + string
    if "-" in string:
        return string.replace("-", "_")

    return string


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

    # Create a version-aware import function for templates
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

    # Temporarily override globals for template rendering
    env.globals["get_relative_import"] = versioned_get_relative_import

    # Wire up version note function if metadata is provided
    version_metadata = kwargs.pop("version_metadata", None)
    if version_metadata is not None:
        from .version_diff import format_version_note as _fmt_note

        current_major = version_prefix[1:] if version_prefix else None

        def _version_note_for_filter(name: str) -> str | None:
            return _fmt_note(
                name,
                version_metadata.filter_versions,
                version_metadata.available_versions,
                current_major or "",
            )

        env.globals["format_version_note"] = _version_note_for_filter
    else:
        env.globals["format_version_note"] = None

    try:
        for template_file in template_folder.glob("**/*.*.jinja"):
            template_path = template_file.relative_to(template_folder)

            template = env.get_template(str(template_path))
            code = template.render(template_path=template_path, **kwargs)

            opath = outpath / str(template_path).replace(".jinja", "")
            opath.parent.mkdir(parents=True, exist_ok=True)

            with opath.open("w") as ofile:
                ofile.write("# NOTE: this file is auto-generated, do not modify\n")
                ofile.write(code)

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

    finally:
        # Restore the original non-versioned import function
        env.globals["get_relative_import"] = get_relative_import

    return output
