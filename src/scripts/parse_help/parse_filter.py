import re
import subprocess
from collections import defaultdict
from dataclasses import replace

from ffmpeg.common.schema import (
    FFMpegFilter,
    FFMpegFilterOption,
    FFMpegFilterOptionChoice,
    FFMpegFilterOptionType,
    FFMpegIOType,
    StreamType,
)


def extract_filter_help_text(filter_name: str) -> str:
    """
    Get the help text for a filter.

    Args:
        filter_name: The name of the filter.

    Returns:
        The help text.
    """

    result = subprocess.run(
        ["ffmpeg", "-h", f"filter={filter_name}", "-hide_banner"],
        stdout=subprocess.PIPE,
        text=True,
    )
    return result.stdout


def _left_space(line: str) -> int:
    """
    Get the number of leading spaces in a string.

    Args:
        line: The string to check.

    Returns:
        The number of leading spaces.
    """
    for i in range(len(line)):
        if line[i] != " ":
            return i

    return len(line)


def parse_section_tree(text: str) -> dict[str, list[str]]:
    """
    Parse the help text into a tree structure.

    Args:
        text: The help text.

    Returns:
        The tree structure.
    """
    output: dict[str, list[str]] = defaultdict(list)
    paths: list[tuple[int, str]] = []

    for line in text.split("\n"):
        indent = _left_space(line)
        if not line.strip():
            continue
        paths = [k for k in paths if k[0] < indent]

        if paths:
            parent = paths[-1][1]
        else:
            parent = ""

        line = line.strip()
        output[parent].append(line)
        paths.append((indent, line))

    return output


def _parse_io(line: str) -> tuple[int, str, StreamType]:
    """
    Parse an input/output line from the help text.

    Args:
        line: The line to parse.

    Returns:
        The index, name, and type.
    """
    index, name, _type = re.findall(r"#([\d]+): ([\w]+) (.+)", line)[0]
    return int(index), name, StreamType(_type.strip("()"))


def _parse_default(default: str | None, type: str) -> int | float | bool | str | None:
    """
    Parse the default value for an option.

    Args:
        default: The default value.
        type: The type of the option.

    Returns:
        The parsed default value.
    """
    if default is not None:
        default = default.strip('"')

    try:
        match type:
            case "boolean":
                assert default in ("true", "false"), (
                    f"Invalid default value for boolean: {default}"
                )
                return default == "true"
            case "duration":
                assert default is not None
                return float(default)
            case "color":
                return default
            case "flags":
                return default
            case "dictionary":
                return default
            case "pix_fmt":
                return default
            case "int":
                assert default is not None
                return int(default)
            case "int64":
                assert default is not None
                return int(default)
            case "double":
                assert default is not None
                return float(default)
            case "float":
                assert default is not None
                return float(default)
            case "string":
                return default
            case "video_rate":
                return default
            case "image_size":
                return default
            case "rational":
                return default
            case "sample_fmt":
                return default
            case "binary":
                return default

    except (ValueError, AssertionError):
        pass

    return default


def _parse_option_line(line: str) -> tuple[str, str, str, str]:
    """
    Parse a line of option text.

    Args:
        line: The line to parse.

    Returns:
        The name, type, flags, and help.
    """
    return re.findall(r"([\-\w]+)\s+<([\w]+)>\s+([\w\.]{11})(\s+.*)?", line)[0]


def _parse_default_line(line: str) -> str | None:
    """
    Parse a default line.

    Args:
        line: The line to parse.

    Returns:
        The default value.
    """
    if match := re.findall(r"\(default ([^\)]+)\)", line):
        return match[0]
    return None


def _parse_min_max_line(line: str) -> tuple[str | None, str | None]:
    """
    Parse a min/max line.

    Args:
        line: The line to parse.

    Returns:
        The min and max values.
    """
    if match := re.findall(r"\(from ([^\)]+) to ([^\)]+)\)", line):
        return match[0]
    return None, None


def _parse_choices(lines: list[str]) -> list[FFMpegFilterOptionChoice]:
    """
    Parse the choices for an option.

    Args:
        lines: The lines to parse.

    Returns:
        The parsed choices.
    """
    output: list[FFMpegFilterOptionChoice] = []
    for line in lines:
        match: list[tuple[str, str, str, str]] = re.findall(
            r"([\w]+)\s+([\s\-\w]+)\s+([\w\.]{11})(\s+.*)?", line
        )
        assert match
        name, value, flags, help = match[0]
        if not value.strip():
            value = name

        output.append(
            FFMpegFilterOptionChoice(
                name=name, help=help.strip(), value=value.strip(), flags=flags.strip()
            )
        )

    return output


def _parse_options(
    lines: list[str], tree: dict[str, list[str]]
) -> list[FFMpegFilterOption]:
    """
    Parse the options for a filter.

    Args:
        lines: The lines to parse.
        tree: The tree structure.

    Returns:
        The parsed options.
    """

    output: list[FFMpegFilterOption] = []

    for line in lines:
        name, type, flags, help = _parse_option_line(line)

        if name[0] == "-":
            continue

        if output and help.strip() and output[-1].description.strip() == help.strip():
            output[-1] = replace(output[-1], alias=output[-1].alias + (name,))
            continue

        default_line = _parse_default_line(help)
        min, max = _parse_min_max_line(help)

        choices = _parse_choices(tree.get(line, []))
        default = _parse_default(default_line, type)

        output.append(
            FFMpegFilterOption(
                alias=(name,),
                name=name,
                description=help.strip(),
                type=FFMpegFilterOptionType(type),
                flags=flags,
                min=min,
                max=max,
                default=default,
                choices=tuple(choices),
            )
        )

    return output


def _remove_duplicate(options: list[FFMpegFilterOption]) -> list[FFMpegFilterOption]:
    """
    Remove duplicate options.

    Args:
        options: The options to check.

    Returns:
        The options with duplicates removed.
    """
    output = []
    seen = set()
    for option in options:
        if option.name not in seen:
            output.append(option)
            seen.add(option.name)

    return output


def extract_avfilter_info_from_help(filter_name: str) -> FFMpegFilter:
    text = extract_filter_help_text(filter_name)

    if "Unknown filter" in text:
        raise ValueError(f"Unknown filter {filter_name}")

    tree = parse_section_tree(text)

    assert filter_name in tree[""][0]
    description = tree[f"Filter {filter_name}"][0]

    slice_threading_supported = tree[description][0] == "slice threading supported"
    inputs = tree["Inputs:"]
    outputs = tree["Outputs:"]

    is_input_dynamic = inputs[0] == "dynamic (depending on the options)"
    is_output_dynamic = outputs[0] == "dynamic (depending on the options)"

    if not is_input_dynamic:
        input_types = []
        if inputs[0] != "none (source filter)":
            for _input in inputs:
                index, name, _type = _parse_io(_input)
                input_types.append(FFMpegIOType(name=name, type=_type))
    else:
        input_types = None

    if not is_output_dynamic:
        output_types = []
        if outputs[0] != "none (sink filter)":
            for output in outputs:
                index, name, _type = _parse_io(output)
                output_types.append(FFMpegIOType(name=name, type=_type))
    else:
        output_types = None

    is_suppoert_timeline = (
        tree[""][-1]
        == "This filter has support for timeline through the 'enable' option."
    )
    is_support_framesync = "framesync AVOptions:" in tree

    options = []
    for item in tree[""]:
        if "AVOptions:" in item:
            options.extend(_parse_options(tree[item], tree))

    if is_suppoert_timeline:
        options.append(
            FFMpegFilterOption(
                name="enable",
                description="timeline editing",
                type=FFMpegFilterOptionType.string,
            )
        )

    return FFMpegFilter(
        name=filter_name,
        description=description,
        # flags
        is_support_slice_threading=slice_threading_supported,
        is_support_timeline=is_suppoert_timeline,
        is_support_framesync=is_support_framesync,
        # IO Typing
        is_dynamic_input=is_input_dynamic,
        is_dynamic_output=is_output_dynamic,
        stream_typings_input=tuple(input_types) if input_types else (),
        stream_typings_output=tuple(output_types) if output_types else (),
        options=tuple(_remove_duplicate(options)),
    )
