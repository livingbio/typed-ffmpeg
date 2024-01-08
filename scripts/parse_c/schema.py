import enum
import re
from collections import defaultdict
from functools import cached_property
from itertools import groupby

import pydantic


class AVOptionFlags(int, enum.Enum):
    # ref: libavutil/opt.h
    AV_OPT_FLAG_ENCODING_PARAM = 1
    AV_OPT_FLAG_DECODING_PARAM = 2
    AV_OPT_FLAG_AUDIO_PARAM = 8
    AV_OPT_FLAG_VIDEO_PARAM = 16
    AV_OPT_FLAG_SUBTITLE_PARAM = 32
    AV_OPT_FLAG_EXPORT = 64
    AV_OPT_FLAG_READONLY = 128
    AV_OPT_FLAG_BSF_PARAM = 1 << 8
    AV_OPT_FLAG_RUNTIME_PARAM = 1 << 15
    AV_OPT_FLAG_FILTERING_PARAM = 1 << 16
    AV_OPT_FLAG_DEPRECATED = 1 << 17
    AV_OPT_FLAG_CHILD_CONSTS = 1 << 18


class AVOptionType(str, enum.Enum):
    AV_OPT_TYPE_FLAGS = "AV_OPT_TYPE_FLAGS"
    AV_OPT_TYPE_INT = "AV_OPT_TYPE_INT"
    AV_OPT_TYPE_INT64 = "AV_OPT_TYPE_INT64"
    AV_OPT_TYPE_DOUBLE = "AV_OPT_TYPE_DOUBLE"
    AV_OPT_TYPE_FLOAT = "AV_OPT_TYPE_FLOAT"
    AV_OPT_TYPE_STRING = "AV_OPT_TYPE_STRING"
    AV_OPT_TYPE_RATIONAL = "AV_OPT_TYPE_RATIONAL"
    AV_OPT_TYPE_BINARY = "AV_OPT_TYPE_BINARY"
    AV_OPT_TYPE_DICT = "AV_OPT_TYPE_DICT"
    AV_OPT_TYPE_UINT64 = "AV_OPT_TYPE_UINT64"
    AV_OPT_TYPE_CONST = "AV_OPT_TYPE_CONST"
    AV_OPT_TYPE_IMAGE_SIZE = "AV_OPT_TYPE_IMAGE_SIZE"
    AV_OPT_TYPE_PIXEL_FMT = "AV_OPT_TYPE_PIXEL_FMT"
    AV_OPT_TYPE_SAMPLE_FMT = "AV_OPT_TYPE_SAMPLE_FMT"
    AV_OPT_TYPE_VIDEO_RATE = "AV_OPT_TYPE_VIDEO_RATE"
    AV_OPT_TYPE_DURATION = "AV_OPT_TYPE_DURATION"
    AV_OPT_TYPE_COLOR = "AV_OPT_TYPE_COLOR"
    AV_OPT_TYPE_CHANNEL_LAYOUT = "AV_OPT_TYPE_CHANNEL_LAYOUT"
    AV_OPT_TYPE_BOOL = "AV_OPT_TYPE_BOOL"
    AV_OPT_TYPE_CHLAYOUT = "AV_OPT_TYPE_CHLAYOUT"


class OptionDefFlag(int, enum.Enum):
    # fftools/cmdutils.h
    HAS_ARG = 1 << 0
    OPT_BOOL = 1 << 1
    OPT_EXPERT = 1 << 2
    OPT_STRING = 1 << 3
    OPT_VIDEO = 1 << 4
    OPT_AUDIO = 1 << 5
    OPT_INT = 1 << 6
    OPT_FLOAT = 1 << 7
    OPT_SUBTITLE = 1 << 8
    OPT_INT64 = 1 << 9
    OPT_EXIT = 1 << 10
    OPT_DATA = 1 << 11
    OPT_PERFILE = 1 << 12
    OPT_OFFSET = 1 << 13
    OPT_SPEC = 1 << 14
    OPT_TIME = 1 << 15
    OPT_DOUBLE = 1 << 16
    OPT_INPUT = 1 << 17
    OPT_OUTPUT = 1 << 18


class OptionDef(pydantic.BaseModel):
    name: str
    flags: int
    help: str
    argname: str | None = None

    @property
    def is_input_option(self):
        return bool(self.flags & OptionDefFlag.OPT_INPUT)

    @property
    def is_output_option(self):
        return bool(self.flags & OptionDefFlag.OPT_OUTPUT)

    @property
    def typing(self) -> str:
        def base_typing(self) -> str:
            if not self.flags & OptionDefFlag.HAS_ARG:
                # Ref: https://ffmpeg.org/ffmpeg.html#Options
                return "bool"

            if self.flags & OptionDefFlag.OPT_BOOL:
                return "bool"

            if self.flags & OptionDefFlag.OPT_INT:
                return "int"

            if self.flags & OptionDefFlag.OPT_INT64:
                return "int"

            if self.flags & OptionDefFlag.OPT_FLOAT:
                return "float"

            if self.flags & OptionDefFlag.OPT_DOUBLE:
                return "float"

            if self.flags & OptionDefFlag.OPT_STRING:
                return "str"

            if self.flags & OptionDefFlag.OPT_TIME:
                return "str"

            return "str"

        base = base_typing(self)
        if self.flags & OptionDefFlag.OPT_SPEC:
            return base + f" | dict[str, {base}]"
        return base


class AVOption(pydantic.BaseModel):
    name: str
    help: str
    offset: str
    type: AVOptionType
    default: str | None = None
    min: str | None = None
    max: str | None = None
    flags: str | None = None
    unit: str | None = None

    @property
    def flags_value(self) -> int:
        text = self.flags
        if text is None:
            return 0

        text = text.split("=", 1)[-1]
        text = text.replace("\n", "")

        return eval(text)

    @property
    def flag_is_deprecated(self) -> bool:
        return bool(self.flags_value & AVOptionFlags.AV_OPT_FLAG_DEPRECATED)


class Choice(pydantic.BaseModel):
    name: str
    help: str
    value: int | str


class Option(pydantic.BaseModel):
    name: str
    help: str
    type: str
    default: str | None = None
    default_value: str | int | float | None = None
    alias: list[str] = []
    deprecated: bool = False

    choices: list[Choice] = []

    @pydantic.computed_field
    @property
    def required(self) -> bool:
        if self.default is None:
            return True

        if "void" in self.default:
            return True

        # remove whitespace
        default = self.default.replace(" ", "")
        if ".str=0" in default or ".str=NULL" in default:
            return True

        return False


class AVFilterPadType(str, enum.Enum):
    video = "AVMEDIA_TYPE_VIDEO"
    audio = "AVMEDIA_TYPE_AUDIO"


class AVFilterPad(pydantic.BaseModel):
    name: str
    type: AVFilterPadType


class AVClass(pydantic.BaseModel):
    class_name: str
    item_name: str
    option: str
    version: str | None = None
    log_level_offset_offset: str | None = None
    parent_log_context_offset: str | None = None
    child_next: str | None = None
    child_class_next: str | None = None
    category: str | None = None


class AVFilterFlags(int, enum.Enum):
    # ref: libavfilter/avfilter.h
    AVFILTER_FLAG_DYNAMIC_INPUTS = 1 << 0
    AVFILTER_FLAG_DYNAMIC_OUTPUTS = 1 << 1
    AVFILTER_FLAG_SLICE_THREADS = 1 << 2
    AVFILTER_FLAG_METADATA_ONLY = 1 << 3
    AVFILTER_FLAG_HWDEVICE = 1 << 4
    AVFILTER_FLAG_SUPPORT_TIMELINE_GENERIC = 1 << 16
    AVFILTER_FLAG_SUPPORT_TIMELINE_INTERNAL = 1 << 17
    AVFILTER_FLAG_SUPPORT_TIMELINE = AVFILTER_FLAG_SUPPORT_TIMELINE_GENERIC | AVFILTER_FLAG_SUPPORT_TIMELINE_INTERNAL


def parse_av_filter_flags(text: str | None) -> int:
    if text is None:
        return 0

    text = text.replace("\n", "")

    def convert_avfilter_flag(match) -> str:
        return str(AVFilterFlags[match.group(1)].value)

    if "AVFILTER" in text:
        text = re.sub(r"(AVFILTER_FLAG_\w+)", convert_avfilter_flag, text)

    return eval(text)


class FilterType(str, enum.Enum):
    AUDIO_FILTER = "af"
    AUDIO_SOURCE = "asrc"
    AUDIO_SINK = "asink"
    VIDEO_FILTER = "vf"
    VIDEO_SOURCE = "vsrc"
    VIDEO_SINK = "vsink"
    AUDIO_AND_VIDEO_SOURCE = "avsrc"
    AUDIO_AND_VIDEO_FILTER = "avf"
    VIDEO_AND_AUDIO_FILTER = "vaf"


def parse_default(text: str) -> str | float | int | bool | None:
    if text is None:
        return None

    match = re.findall(r"\.([\w]+)\s*=\s*(.*)\]", text)
    if not match:
        return text

    type, value = match[0]
    value = value.strip("'\"")

    try:
        match type:
            case "dbl":
                return float(value)
            case "i64":
                return int(value)
            case "str":
                return value
    except ValueError:
        return value


class AVFilter(pydantic.BaseModel):
    id: str  # the varname of the filter
    name: str
    description: str

    # preinit: str
    init: str | None = None
    init_src: str | None = None
    # uninit: str
    # priv_size: str
    # activate: str
    inputs: str | None = None
    # nb_inputs: str
    outputs: str | None = None
    # nb_outputs: str
    priv_class: str | None = None
    flags: str | None = None
    # process_command: str

    options: list[AVOption] = []
    input_filter_pads: list[AVFilterPad] = []
    output_filter_pads: list[AVFilterPad] = []

    @property
    def type(self) -> FilterType:
        _, type, _ = self.id.split("_", 2)
        return FilterType(type)

    @property
    def init_value(self) -> str:
        return self.init.strip("&")

    @property
    def flags_value(self) -> int:
        return parse_av_filter_flags(self.flags)

    @property
    def priv_class_value(self) -> str | None:
        if self.priv_class is None:
            return None
        return self.priv_class.strip("&")

    @property
    def inputs_value(self) -> str | None:
        # af_lv2.c's inputs is 0
        if self.inputs is None or self.inputs == "((void*)0)" or self.inputs == "0":
            return None

        return self.inputs.strip("()")

    @property
    def outputs_value(self) -> str | None:
        if self.outputs is None or self.outputs == "((void*)0)":
            return None

        return self.outputs.strip("()")

    @property
    def is_dynamic_inputs(self) -> bool:
        return bool(self.flags_value & AVFilterFlags.AVFILTER_FLAG_DYNAMIC_INPUTS)

    @property
    def is_dynamic_outputs(self) -> bool:
        return bool(self.flags_value & AVFilterFlags.AVFILTER_FLAG_DYNAMIC_OUTPUTS)

    @cached_property
    def parsed_options(self) -> list[Option]:
        output = []

        unit: str | None
        options: list[AVOption]

        # collect choices
        choices = {}
        for unit, options in groupby(
            [k for k in self.options if k.unit and k.type == "AV_OPT_TYPE_CONST"], key=lambda i: i.unit
        ):
            for option in options:
                choices[unit] = choices.get(option.unit, []) + [
                    Choice(name=option.name, help=option.help, value=parse_default(option.default))
                ]

        # collect alias map
        alias_map: dict[str, list[AVOption]] = defaultdict(list)
        for option in [k for k in self.options if k.type != "AV_OPT_TYPE_CONST"]:
            alias_map[option.offset].append(option)

        # collect options
        for option in [k for k in self.options if k.unit == None or k.type != "AV_OPT_TYPE_CONST"]:
            if len(alias_map[option.offset]) > 1:
                if alias_map[option.offset][0].name != option.name:
                    continue
                else:
                    alias = [k.name for k in alias_map[option.offset]]
            else:
                alias = [k.name for k in alias_map[option.offset]]

            if option.unit == None:
                output.append(
                    Option(
                        name=option.name,
                        alias=alias,
                        help=option.help,
                        type=option.type,
                        default=option.default,
                        default_value=parse_default(option.default),
                        deprecated=option.flag_is_deprecated,
                    )
                )
            else:
                output.append(
                    Option(
                        name=option.name,
                        alias=alias,
                        help=option.help,
                        type=option.type,
                        default=option.default,
                        default_value=parse_default(option.default),
                        choices=choices.get(option.unit, []),
                        deprecated=option.flag_is_deprecated,
                    )
                )

        return output
