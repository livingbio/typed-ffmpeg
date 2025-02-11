from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Literal


class StreamType(str, Enum):
    """
    The type of a stream. (audio or video)
    """

    audio = "audio"
    """it is an audio stream"""
    video = "video"
    """it is a video stream"""


class FFMpegFilterOptionType(str, Enum):
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
    type: FFMpegFilterOptionType
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
class FFMpegFilterDef:
    name: str

    typings_input: str | tuple[Literal["video", "audio"], ...] = ()
    typings_output: str | tuple[Literal["video", "audio"], ...] = ()


@dataclass(frozen=True, kw_only=True)
class FFMpegFilter:
    id: str | None = None

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
    is_dynamic_output: bool = False
    stream_typings_input: tuple[FFMpegIOType, ...] = ()
    stream_typings_output: tuple[FFMpegIOType, ...] = ()
    formula_typings_input: str | None = None
    formula_typings_output: str | None = None

    pre: tuple[tuple[str, str], ...] = ()
    options: tuple[FFMpegFilterOption, ...] = ()

    @property
    def pre_dict(self) -> dict[str, str]:
        return dict(self.pre)

    @property
    def to_def(self) -> FFMpegFilterDef:
        return FFMpegFilterDef(
            name=self.name,
            typings_input=self.formula_typings_input
            or tuple(k.type.value for k in self.stream_typings_input),
            typings_output=self.formula_typings_output
            or tuple(k.type.value for k in self.stream_typings_output),
        )

    @property
    def input_typings(self) -> set[StreamType]:
        if self.is_filter_source:
            return set()
        if not self.is_dynamic_input:
            return {i.type for i in self.stream_typings_input}
        else:
            assert self.formula_typings_input, f"{self.name} has no input"
            if "video" not in self.formula_typings_input:
                assert "audio" in self.formula_typings_input, (
                    f"{self.name} has no video input"
                )
                return {StreamType.audio}
            elif "audio" not in self.formula_typings_input:
                assert "video" in self.formula_typings_input, (
                    f"{self.name} has no audio input"
                )
                return {StreamType.video}
            assert (
                "video" in self.formula_typings_input
                and "audio" in self.formula_typings_input
            ), f"{self.name} has no video or audio input"
            return {StreamType.video, StreamType.audio}

    @property
    def output_typings(self) -> set[StreamType]:
        if self.is_filter_sink:
            return set()
        if not self.is_dynamic_output:
            return {i.type for i in self.stream_typings_output}
        else:
            assert self.formula_typings_output, f"{self.name} has no output"
            if "video" not in self.formula_typings_output:
                assert "audio" in self.formula_typings_output, (
                    f"{self.name} has no video output"
                )
                return {StreamType.audio}
            elif "audio" not in self.formula_typings_output:
                assert "video" in self.formula_typings_output, (
                    f"{self.name} has no audio output"
                )
                return {StreamType.video}
            assert (
                "video" in self.formula_typings_output
                and "audio" in self.formula_typings_output
            ), f"{self.name} has no video or audio output"
            return {StreamType.video, StreamType.audio}

    @property
    def filter_type(self) -> FFMpegFilterType:
        if self.is_filter_sink:
            assert len(self.input_typings) == 1
            if {StreamType.video} == self.input_typings:
                return FFMpegFilterType.vsink
            if {StreamType.audio} == self.input_typings:
                return FFMpegFilterType.asink
        elif self.is_filter_source:
            if {StreamType.video, StreamType.audio} == self.output_typings:
                return FFMpegFilterType.avsrc
            if {StreamType.video} == self.output_typings:
                return FFMpegFilterType.vsrc
            if {StreamType.audio} == self.output_typings:
                return FFMpegFilterType.asrc

        assert self.input_typings

        if self.input_typings == {StreamType.video}:
            if StreamType.audio in self.output_typings:
                return FFMpegFilterType.vaf
            if self.output_typings == {StreamType.video}:
                return FFMpegFilterType.vf

        if self.input_typings == {StreamType.audio}:
            if self.output_typings == {StreamType.audio}:
                return FFMpegFilterType.af
            if StreamType.video in self.output_typings:
                return FFMpegFilterType.avf

        if self.input_typings == {StreamType.video, StreamType.audio}:
            return FFMpegFilterType.avf

        raise ValueError(f"Unknown filter type for {self.name}")


class FFMpegOptionFlag(int, Enum):
    OPT_FUNC_ARG = 1 << 0
    """
    The OPT_TYPE_FUNC option takes an argument.
    Must not be used with other option types, as for those it holds:
    - OPT_TYPE_BOOL do not take an argument
    - all other types do
    """

    OPT_EXIT = 1 << 1
    """
    Program will immediately exit after processing this option
    """

    OPT_EXPERT = 1 << 2
    """
    Option is intended for advanced users. Only affects help output.
    """

    OPT_VIDEO = 1 << 3
    OPT_AUDIO = 1 << 4
    OPT_SUBTITLE = 1 << 5
    OPT_DATA = 1 << 6

    OPT_PERFILE = 1 << 7
    """
    The option is per-file (currently ffmpeg-only). At least one of OPT_INPUT or OPT_OUTPUT must be set when this flag is in use.
    """

    OPT_FLAG_OFFSET = 1 << 8
    """
    Option is specified as an offset in a passed optctx.
    Always use as OPT_OFFSET in option definitions.
    """

    OPT_OFFSET = OPT_FLAG_OFFSET | OPT_PERFILE
    """
    Option is to be stored in a SpecifierOptList.
    Always use as OPT_SPEC in option definitions.
    """
    OPT_FLAG_SPEC = 1 << 9
    """
    Option is to be stored in a SpecifierOptList.
    Always use as OPT_SPEC in option definitions.
    """

    OPT_SPEC = OPT_FLAG_SPEC | OPT_OFFSET
    """
    Option applies per-stream (implies OPT_SPEC).
    """
    OPT_FLAG_PERSTREAM = 1 << 10
    """
    Option applies per-stream (implies OPT_SPEC).
    """
    OPT_PERSTREAM = OPT_FLAG_PERSTREAM | OPT_SPEC

    OPT_INPUT = 1 << 11
    """
    ffmpeg-only - specifies whether an OPT_PERFILE option applies to input, output, or both.
    """
    OPT_OUTPUT = 1 << 12
    """
    ffmpeg-only - specifies whether an OPT_PERFILE option applies to input, output, or both.
    """

    OPT_HAS_ALT = 1 << 13
    """
    This option is a "canonical" form, to which one or more alternatives exist. These alternatives are listed in u1.names_alt.
    """
    OPT_HAS_CANON = 1 << 14
    """
    This option is an alternative form of some other option, whose name is stored in u1.name_canon
    """


class FFMpegOptionType(str, Enum):
    OPT_TYPE_FUNC = "OPT_TYPE_FUNC"
    OPT_TYPE_BOOL = "OPT_TYPE_BOOL"
    OPT_TYPE_STRING = "OPT_TYPE_STRING"
    OPT_TYPE_INT = "OPT_TYPE_INT"
    OPT_TYPE_INT64 = "OPT_TYPE_INT64"
    OPT_TYPE_FLOAT = "OPT_TYPE_FLOAT"
    OPT_TYPE_DOUBLE = "OPT_TYPE_DOUBLE"
    OPT_TYPE_TIME = "OPT_TYPE_TIME"


@dataclass(frozen=True, kw_only=True)
class FFMpegOption:
    name: str
    type: FFMpegOptionType
    flags: int
    help: str
    argname: str | None = None
    canon: str | None = None

    @property
    def is_input_option(self) -> bool:
        return bool(self.flags & FFMpegOptionFlag.OPT_INPUT)

    @property
    def is_output_option(self) -> bool:
        return bool(self.flags & FFMpegOptionFlag.OPT_OUTPUT)

    @property
    def is_global_option(self) -> bool:
        return (
            not self.is_input_option
            and not self.is_output_option
            and not (self.flags & FFMpegOptionFlag.OPT_EXIT)
        )

    @property
    def is_support_stream_specifier(self) -> bool:
        return bool(self.flags & FFMpegOptionFlag.OPT_SPEC)
