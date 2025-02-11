import keyword
import pathlib
from math import isnan
from pathlib import Path

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


def filter_option_typing(self: FFMpegFilterOption) -> str:
    base_type = None
    if self.type == FFMpegFilterOptionType.boolean:
        base_type = "Boolean"
    elif self.type == FFMpegFilterOptionType.duration:
        base_type = "Duration"
    elif self.type == FFMpegFilterOptionType.color:
        base_type = "Color"
    elif self.type == FFMpegFilterOptionType.flags:
        base_type = "Flags"
    elif self.type == FFMpegFilterOptionType.dictionary:
        base_type = "Dictionary"
    elif self.type == FFMpegFilterOptionType.pix_fmt:
        base_type = "Pix_fmt"
    elif self.type == FFMpegFilterOptionType.int:
        base_type = "Int"
    elif self.type == FFMpegFilterOptionType.int64:
        base_type = "Int64"
    elif self.type == FFMpegFilterOptionType.double:
        base_type = "Double"
    elif self.type == FFMpegFilterOptionType.float:
        base_type = "Float"
    elif self.type == FFMpegFilterOptionType.string:
        base_type = "String"
    elif self.type == FFMpegFilterOptionType.video_rate:
        base_type = "Video_rate"
    elif self.type == FFMpegFilterOptionType.image_size:
        base_type = "Image_size"
    elif self.type == FFMpegFilterOptionType.rational:
        base_type = "Rational"
    elif self.type == FFMpegFilterOptionType.sample_fmt:
        base_type = "Sample_fmt"
    elif self.type == FFMpegFilterOptionType.binary:
        base_type = "Binary"

    assert base_type, f"{self.type} not fit"
    if not self.choices:
        return base_type

    values = ",".join(f'"{i.name}"' for i in self.choices)
    return base_type + f"| Literal[{values}]"


def stream_name_safe(string: str) -> str:
    opt_name = option_name_safe(string)
    if not opt_name.startswith("_"):
        return "_" + opt_name
    return opt_name


def option_name_safe(string: str) -> str:
    if string in keyword.kwlist:
        return "_" + string
    if string[0].isdigit():
        return "_" + string
    if "-" in string:
        return string.replace("-", "_")

    return string


def option_typing(self: FFMpegOption) -> str:
    if self.type == FFMpegOptionType.OPT_TYPE_FUNC:
        return "Func"
    elif self.type == FFMpegOptionType.OPT_TYPE_BOOL:
        return "Boolean"
    elif self.type == FFMpegOptionType.OPT_TYPE_STRING:
        return "String"
    elif self.type == FFMpegOptionType.OPT_TYPE_INT:
        return "Int"
    elif self.type == FFMpegOptionType.OPT_TYPE_INT64:
        return "Int64"
    elif self.type == FFMpegOptionType.OPT_TYPE_FLOAT:
        return "Float"
    elif self.type == FFMpegOptionType.OPT_TYPE_DOUBLE:
        return "Double"
    elif self.type == FFMpegOptionType.OPT_TYPE_TIME:
        return "Time"


def input_typings(self: FFMpegFilter) -> str:
    if self.formula_typings_input:
        return self.formula_typings_input
    return (
        "["
        + ", ".join(f"StreamType.{i.type.value}" for i in self.stream_typings_input)
        + "]"
    )


def output_typings(self: FFMpegFilter) -> str:
    if self.formula_typings_output:
        return self.formula_typings_output
    return (
        "["
        + ", ".join(f"StreamType.{i.type.value}" for i in self.stream_typings_output)
        + "]"
    )


def default_value(option: FFMpegFilterOption, f: FFMpegFilter) -> str:
    if option.name in f.pre_dict:
        return f"Auto({repr(f.pre_dict[option.name])})"
    if not isinstance(option.default, float) or not isnan(option.default):
        return f"Default({repr(option.default)})"
    return 'Default("nan")'


def default_typings(option: FFMpegFilterOption, f: FFMpegFilter) -> str:
    if option.choices:
        return f"{filter_option_typing(option)} | Default = {default_value(option, f)}"
    return f"{filter_option_typing(option)} = {default_value(option, f)}"


def filter_option_typings(self: FFMpegFilter) -> str:
    output = []

    for option in self.options:
        output.append(
            f"{option_name_safe(option.name)}: {default_typings(option, self)}"
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
    filters: list[FFMpegFilter], options: list[FFMpegOption], outpath: pathlib.Path
) -> list[pathlib.Path]:
    outpath.mkdir(exist_ok=True)
    output = []
    for template_file in template_folder.glob("**/*.py.jinja"):
        template_path = template_file.relative_to(template_folder)

        template = env.get_template(str(template_path))
        code = template.render(filters=filters, options=options)

        opath = outpath / str(template_path).replace(".jinja", "")
        opath.parent.mkdir(parents=True, exist_ok=True)

        with opath.open("w") as ofile:
            ofile.write("# NOTE: this file is auto-generated, do not modify\n")
            ofile.write(code)

        output.append(opath)

    return output
