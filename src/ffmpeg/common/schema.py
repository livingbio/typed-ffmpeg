from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class StreamType(str, Enum):
    video = "video"
    audio = "audio"


class FFMpegFilterOptionTyping(str, Enum):
    boolean = "boolean"
    duration = "duration"
    color = "color"
    flags = "flags"
    dictionary = "dictionary"
    pix_fmt = "pix_fmt"
    int = "int"
    int64 = "int64"
    double = "double"
    float = "float"
    string = "string"
    video_rate = "video_rate"
    image_size = "image_size"
    rational = "rational"
    sample_fmt = "sample_fmt"
    binary = "binary"


class FFMpegFilterType(str, Enum):
    af = "af"
    asrc = "asrc"
    asink = "asink"
    vf = "vf"
    vsrc = "vsrc"
    vsink = "vsink"
    avsrc = "avsrc"
    avf = "avf"
    vaf = "vaf"


@dataclass(frozen=True, kw_only=True)
class FFMpegFilterOptionChoice:
    name: str
    help: str
    value: str | int
    flags: str | None = None


@dataclass(frozen=True, kw_only=True)
class FFMpegFilterOption:
    name: str
    alias: tuple[str, ...] = ()
    description: str
    typing: FFMpegFilterOptionTyping
    min: str | None = None
    max: str | None = None
    default: bool | int | float | str | None = None
    required: bool = False
    choices: tuple[FFMpegFilterOptionChoice, ...] = ()
    flags: str | None = None


@dataclass(frozen=True, kw_only=True)
class FFMpegIOType:
    name: str | None = None
    type: StreamType


@dataclass(frozen=True, kw_only=True)
class FFMpegFilter:
    id: str | None = None
    filter_type: FFMpegFilterType | None = None

    name: str
    description: str
    ref: str | None = None

    # Flags
    is_support_slice_threading: bool | None = None
    is_support_timeline: bool | None = None
    is_support_framesync: bool | None = None
    is_support_command: bool | None = None
    is_filter_sink: bool | None = None
    is_filter_source: bool | None = None

    # IO Typing
    is_dynamic_input: bool = False
    is_dynamic_ouptut: bool = False
    stream_typings_input: tuple[FFMpegIOType, ...] = ()
    stream_typings_output: tuple[FFMpegIOType, ...] = ()
    forumla_typings_input: str | None = None
    formula_typings_output: str | None = None

    options: tuple[FFMpegFilterOption, ...] = ()

    @property
    def is_input_type_mixed(self) -> bool:
        if self.input_types:
            return "video" in self.input_types and "audio" in self.input_types
        return False

    @property
    def input_types(self) -> str | None:
        if self.is_dynamic_input:
            return self.forumla_typings_input

        assert self.stream_typings_input
        return str([k.type for k in self.stream_typings_input])

    @property
    def output_types(self) -> str | None:
        if self.is_dynamic_ouptut:
            return self.formula_typings_output

        assert self.stream_typings_output
        return str([k.type for k in self.stream_typings_output])
