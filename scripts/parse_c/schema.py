from functools import cached_property
from itertools import groupby

import pydantic


class AVOption(pydantic.BaseModel):
    name: str
    help: str
    # the offset of the field in the struct, it required Macro to get the value
    # offset: int
    type: str
    default: int | float | str
    min: float | str
    max: float | str
    flags: str
    unit: str | None = None


class Choice(pydantic.BaseModel):
    name: str
    help: str
    value: int | str


class Option(pydantic.BaseModel):
    name: str
    help: str
    type: str
    default: int | float | str

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


class AVFilter(pydantic.BaseModel):
    name: str
    description: str

    # preinit: str
    # init: str
    # uninit: str
    # priv_size: str
    # activate: str
    # inputs: str
    # nb_inputs: str
    # outputs: str
    # nb_outputs: str
    # priv_class: str
    # flags: str
    # process_command: str

    options: list[AVOption] = []

    @cached_property
    def parsed_options(self) -> list[Option]:
        output = []

        unit: str | None
        options: list[AVOption]

        for unit, options in groupby(self.options, key=lambda i: i.unit):
            if unit == None:
                output.extend(Option(**i.model_dump()) for i in options)
            else:
                options = list(options)
                option = [k for k in options if k.type != "AV_OPT_TYPE_CONST"]
                assert len(option) == 1
                option = option[0]
                choices = [
                    Choice(name=i.name, help=i.help, value=i.default) for i in options if i.type == "AV_OPT_TYPE_CONST"
                ]
                output.append(
                    Option(
                        name=option.name, help=option.help, type=option.type, default=option.default, choices=choices
                    )
                )

        return output
