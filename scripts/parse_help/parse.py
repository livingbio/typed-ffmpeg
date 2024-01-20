import re
import subprocess
from collections import defaultdict

from code_gen.schema import FFMpegIOType, StreamType

from .schema import AVChoice, AVFilter, AVOption


def help_text(filter_name: str) -> str:
    result = subprocess.run(
        ["ffmpeg", "-h", f"filter={filter_name}", "-hide_banner"], stdout=subprocess.PIPE, text=True
    )
    return result.stdout


def _left_space(line: str) -> int:
    for i in range(len(line)):
        if line[i] != " ":
            return i

    return len(line)


def parse_section_tree(text: str) -> dict[str, list[str]]:
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
    index, name, _type = re.findall(r"#([\d]+): ([\w]+) (.+)", line)[0]
    return int(index), name, StreamType(_type.strip("()"))


def _parse_default(default: str, type: str) -> int | float | bool | str:
    try:
        match (type):
            case "boolean":
                assert default in ("true", "false")
                return default == "true"
            case "duration":
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
                return int(default)
            case "int64":
                return int(default)
            case "double":
                return float(default)
            case "float":
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
    except ValueError:
        return default


def _parse_options(lines: list[str], tree: dict[str, list[str]]) -> list[AVOption]:
    output: list[AVOption] = []
    for line in lines:
        name, type, flags, help = re.findall(r"([\-\w]+)\s+<([\w]+)>\s+([\w\.]{11})(\s+.*)?", line)[0]
        if name[0] == "-":
            continue

        if output and help.strip() and output[-1].description.strip() == help.strip():
            output[-1].alias.append(name)
            continue

        if match := re.findall(r"\(default ([^\)]+)\)", help):
            default = match[0]
        else:
            default = None

        if match := re.findall(r"\(from ([^\)]+) to ([^\)]+)\)", help):
            min, max = match[0]
        else:
            min = None
            max = None

        choices = []
        for choice in tree.get(line, []):
            _name, _value, _flags, _help = re.findall(r"([\w]+)\s+([\s\-\w]+)\s+([\w\.]{11})(\s+.*)?", choice)[0]
            if not _value.strip():
                _value = _name

            choices.append(AVChoice(name=_name, help=_help.strip(), value=_value.strip(), flags=_flags.strip()))

        default = _parse_default(default, type)

        output.append(
            AVOption(
                alias=[name],
                name=name,
                description=help.strip(),
                typing=type,
                flags=flags,
                min=min,
                max=max,
                default=default,
                choices=choices,
            )
        )

    return output


def _remove_repeat_options(options: list[AVOption]) -> list[AVOption]:
    names = set()
    output = []
    for option in options:
        if option.name in names:
            continue

        names.add(option.name)
        output.append(option)

    return output


def extract_avfilter_info_from_help(filter_name: str) -> AVFilter:
    text = help_text(filter_name)

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

    is_suppoert_timeline = tree[""][-1] == "This filter has support for timeline through the 'enable' option."
    is_support_framesync = "framesync AVOptions:" in tree

    options = []
    for item in tree[""]:
        if "AVOptions:" in item:
            options.extend(_parse_options(tree[item], tree))

    options = _remove_repeat_options(options)

    return AVFilter(
        name=filter_name,
        description=description,
        is_slice_threading_supported=slice_threading_supported,
        is_support_framesync=is_support_framesync,
        is_dynamic_inputs=is_input_dynamic,
        is_dynamic_outputs=is_output_dynamic,
        is_support_timeline=is_suppoert_timeline,
        input_types=input_types,
        output_types=output_types,
        options=options,
    )


def extract(filter_name: str) -> AVFilter:
    # try:
    #     return AVFilter.load(filter_name)
    # except IOError:
    filter = extract_avfilter_info_from_help(filter_name=filter_name)
    filter.save()
    return filter
