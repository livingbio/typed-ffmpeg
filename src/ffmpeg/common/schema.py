from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True, kw_only=True)
class FFMpegFilterOptionChoice:
    name: str
    help: str
    value: str | int


@dataclass(frozen=True, kw_only=True)
class FFMpegFilterOption:
    name: str
    alias: tuple[str, ...]
    description: str | None
    typing: str
    default: bool | int | float | str | None
    required: bool
    choices: tuple[FFMpegFilterOptionChoice, ...]


@dataclass(frozen=True, kw_only=True)
class FFMpegIOType:
    name: str
    type: Literal["video", "audio"]


@dataclass(frozen=True, kw_only=True)
class FFMpegFilter:
    id: str
    filter_type: Literal["af", "asrc", "asink", "vf", "vsrc", "vsink", "avsrc", "avf", "vaf"]

    name: str
    description: str
    ref: str

    is_input_dynamic: bool
    is_output_dynamic: bool
    is_support_timeline: bool
    is_support_framesync: bool

    input_stream_typings: tuple[FFMpegIOType, ...] | None
    output_stream_typings: tuple[FFMpegIOType, ...] | None
    formula_input_typings: str | None
    formula_output_typings: str | None

    options: tuple[FFMpegFilterOption, ...]
