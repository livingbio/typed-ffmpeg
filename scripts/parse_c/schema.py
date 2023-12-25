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


class AVOption(pydantic.BaseModel):
    name: str
    help: str
    offset: str
    type: str
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
    alias: str | None = None
    deprecated: bool = False

    choices: list[Choice] = []

    @property
    def required(self) -> bool:
        if self.default is None:
            return True
        return False


class AVFilterPad(pydantic.BaseModel):
    name: str
    type: str


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


class AVFilter(pydantic.BaseModel):
    name: str
    description: str

    # preinit: str
    # init: str
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
    input_filter_pad: list[AVFilterPad] = []
    output_filter_pad: list[AVFilterPad] = []

    @property
    def flags_value(self) -> int:
        return parse_av_filter_flags(self.flags)

    @property
    def priv_class_value(self) -> str:
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
                    Choice(name=option.name, help=option.help, value=option.default)
                ]

        # collect alias map
        alias_map = defaultdict(list)
        for option in [k for k in self.options if k.type != "AV_OPT_TYPE_CONST"]:
            alias_map[option.offset].append(option)
            alias_map[option.offset].sort(key=lambda i: i.name)

        assert all(len(v) <= 2 for v in alias_map.values()), f"alias_map should have 1 or 2 items {self}"

        # collect options
        for option in [k for k in self.options if k.unit == None or k.type != "AV_OPT_TYPE_CONST"]:
            if len(alias_map[option.offset]) > 1:
                if alias_map[option.offset][0].name == option.name:
                    continue
                else:
                    alias = alias_map[option.offset][0].name
            else:
                alias = None

            if option.unit == None:
                output.append(
                    Option(
                        name=option.name,
                        alias=alias,
                        help=option.help,
                        type=option.type,
                        default=option.default,
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
                        choices=choices[option.unit],
                        deprecated=option.flag_is_deprecated,
                    )
                )

        return output
