"""Code generation utilities for typed-ffmpeg."""

import keyword
import pathlib
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


env.filters["stream_name_safe"] = stream_name_safe
env.filters["option_name_safe"] = option_name_safe
env.filters["filter_option_typing"] = filter_option_typing
env.filters["option_typing"] = option_typing
env.filters["input_typings"] = input_typings
env.filters["output_typings"] = output_typings
env.filters["filter_option_typings"] = filter_option_typings


def render(
    *,
    outpath: pathlib.Path,
    **kwargs: Any,
) -> list[pathlib.Path]:
    """
    Render the filter and option documents.

    Args:
        outpath: The output path
        **kwargs: Additional keyword arguments to pass to the template

    Returns:
        The rendered files

    """
    outpath.mkdir(exist_ok=True)
    output = []

    for template_file in template_folder.glob("**/*.*.jinja"):
        template_path = template_file.relative_to(template_folder)

        template = env.get_template(str(template_path))
        code = template.render(**kwargs)

        opath = outpath / str(template_path).replace(".jinja", "")
        opath.parent.mkdir(parents=True, exist_ok=True)

        with opath.open("w") as ofile:
            ofile.write("# NOTE: this file is auto-generated, do not modify\n")
            ofile.write(code)

        output.append(opath)

    return output
