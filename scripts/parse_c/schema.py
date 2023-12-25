import enum
from functools import cached_property
from itertools import groupby

import pydantic


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


class Choice(pydantic.BaseModel):
    name: str
    help: str
    value: int | str


class Option(pydantic.BaseModel):
    name: str
    help: str
    type: str
    default: int | float | str | None = None

    choices: list[Choice] = []


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
    flags: int
    # process_command: str

    options: list[AVOption] = []
    input_filter_pad: AVFilterPad | None = None
    output_filter_pad: AVFilterPad | None = None

    @property
    def priv_class_value(self) -> str:
        return self.priv_class.strip("&")

    @property
    def inputs_value(self) -> str | None:
        if self.inputs is None or self.inputs == "((void*)0)":
            return None

        return self.inputs.strip("()")

    @property
    def outputs_value(self) -> str | None:
        if self.outputs is None or self.outputs == "(void*)0":
            return None

        return self.outputs.strip("()")

    @property
    def is_dynamic_inputs(self) -> bool:
        return bool(self.flags & AVFilterFlags.AVFILTER_FLAG_DYNAMIC_INPUTS)

    @property
    def is_dynamic_outputs(self) -> bool:
        return bool(self.flags & AVFilterFlags.AVFILTER_FLAG_DYNAMIC_OUTPUTS)

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

        # collect options
        for option in [k for k in self.options if k.unit == None or k.type != "AV_OPT_TYPE_CONST"]:
            if option.unit == None:
                output.append(Option(name=option.name, help=option.help, type=option.type, default=option.default))
            else:
                output.append(
                    Option(
                        name=option.name,
                        help=option.help,
                        type=option.type,
                        default=option.default,
                        choices=choices[option.unit],
                    )
                )

        return output
