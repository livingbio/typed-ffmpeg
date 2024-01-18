import re
import subprocess
from collections import defaultdict

from code_gen.schema import StreamType

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


def _parse_options(lines: list[str], tree: dict[str, list[str]]) -> list[AVOption]:
    output: list[AVOption] = []
    for line in lines:
        name, type, flags, help = re.findall(r"([\w]+)\s*<([\w]+)>\s*([\w\.]{11})\s*(.*)", line)[0]

        if output and output[-1].description == help:
            output[-1].alias.append(name)
            continue

        if match := re.findall("\(default ([\w]+)\)", help):
            default = match[0]
        else:
            default = None

        if match := re.findall("\(from ([\w]+) to ([\w]+)\)", help):
            min, max = match[0]
        else:
            min = None
            max = None

        choices = []
        for choice in tree.get(line, []):
            _name, _value, _flags, _help = re.findall(r"([\w]+)\s*([\w]+)\s*([\w\.]{11})\s*(.*)", choice)[0]
            choices.append(AVChoice(name=_name, help=_help, value=_value, flags=_flags))

        output.append(
            AVOption(
                alias=[name],
                name=name,
                description=help,
                typing=type,
                flags=flags,
                min=min,
                max=max,
                default=default,
                choices=choices,
            )
        )

    return output


def extract_help_text(filter_name: str):
    text = help_text(filter_name)
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
        for _input in inputs:
            index, name, _type = _parse_io(_input)
            input_types.append((name, _type))
    else:
        input_types = None

    if not is_output_dynamic:
        output_types = []
        for output in outputs:
            index, name, _type = _parse_io(output)
            output_types.append((name, _type))
    else:
        output_types = None

    is_suppoert_timeline = tree[""][-1] == "This filter has support for timeline through the 'enable' option."
    is_support_framesync = "framesync AVOptions:" in tree

    options = tree[f"{filter_name} AVOptions:"]

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
        options=_parse_options(options, tree),
    )
