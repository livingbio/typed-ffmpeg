"""
Schema definitions for FFmpeg filters and options.

This module defines the core data structures and enumerations used to represent
FFmpeg filters, their options, and stream types. These schemas are used throughout
the typed-ffmpeg library to provide type-safe interfaces to FFmpeg functionality.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Literal

from .serialize import Serializable, serializable


@serializable
class StreamType(str, Enum):
    """
    Enumeration of possible stream types in FFmpeg.

    This enum defines the fundamental types of media streams that can be
    processed by FFmpeg filters. Each stream in FFmpeg is either an audio
    stream or a video stream, and filters are designed to work with
    specific stream types.
    """

    audio = "audio"
    """Represents an audio stream containing sound data"""

    video = "video"
    """Represents a video stream containing visual frame data"""


@serializable
class FFMpegFilterOptionType(str, Enum):
    """
    Enumeration of possible data types for FFmpeg filter options.

    This enum defines the various data types that can be used for options
    in FFmpeg filters. Each type corresponds to a specific kind of value
    that can be passed to a filter parameter.
    """

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


@serializable
class FFMpegFilterType(str, Enum):
    """
    Enumeration of FFmpeg filter types based on input/output stream types.

    This enum categorizes filters according to what types of streams they
    process and produce. The naming convention follows FFmpeg's internal
    categorization of filters.
    """

    af = "af"
    """Audio filter: processes audio and outputs audio"""

    asrc = "asrc"
    """Audio source: generates audio without input"""

    asink = "asink"
    """Audio sink: consumes audio without producing output"""

    vf = "vf"
    """Video filter: processes video and outputs video"""

    vsrc = "vsrc"
    """Video source: generates video without input"""

    vsink = "vsink"
    """Video sink: consumes video without producing output"""

    avsrc = "avsrc"
    """Audio-video source: generates both audio and video without input"""

    avf = "avf"
    """Audio-video filter: processes and outputs both audio and video"""

    vaf = "vaf"
    """Video-to-audio filter: processes video and outputs audio"""


@dataclass(frozen=True, kw_only=True)
class FFMpegFilterOptionChoice(Serializable):
    """
    Represents a single choice for an FFmpeg filter option with enumerated values.

    Some FFmpeg filter options accept only specific enumerated values. This class
    represents one such value along with its description and internal representation.
    """

    name: str
    """The name of the choice as it appears in FFmpeg documentation"""

    help: str
    """Description of what this choice does"""

    value: str | int
    """The actual value to pass to FFmpeg when this choice is selected"""

    flags: str | None = None
    """Optional flags associated with this choice"""


@dataclass(frozen=True, kw_only=True)
class FFMpegFilterOption(Serializable):
    """
    Represents a configurable option for an FFmpeg filter.

    This class defines the metadata for a single option that can be passed to
    an FFmpeg filter, including its type, constraints, and default value.
    """

    name: str
    """The primary name of the option as used in FFmpeg"""

    alias: tuple[str, ...] = ()
    """Alternative names that can be used for this option"""

    description: str
    """Human-readable description of what the option does"""

    type: FFMpegFilterOptionType
    """The data type of the option (boolean, int, string, etc.)"""

    min: str | None = None
    """Minimum allowed value for numeric options"""

    max: str | None = None
    """Maximum allowed value for numeric options"""

    default: bool | int | float | str | None = None
    """Default value used by FFmpeg if the option is not specified"""

    required: bool = False
    """Whether the option must be provided or can be omitted"""

    choices: tuple[FFMpegFilterOptionChoice, ...] = ()
    """Enumerated values that this option accepts, if applicable"""

    flags: str | None = None
    """Optional flags that modify the behavior of this option"""


@dataclass(frozen=True, kw_only=True)
class FFMpegIOType(Serializable):
    """
    Defines the type information for a filter's input or output stream.

    This class associates a name with a stream type (audio or video) for
    a specific input or output of an FFmpeg filter.
    """

    name: str | None = None
    """Optional name for this input/output stream"""

    type: StreamType
    """The type of the stream (audio or video)"""


@dataclass(frozen=True, kw_only=True)
class FFMpegFilterDef(Serializable):
    """
    Defines the basic structure of an FFmpeg filter.

    This class provides a simplified representation of an FFmpeg filter,
    focusing on its name and the types of its inputs and outputs.
    """

    name: str
    """The name of the filter as used in FFmpeg"""

    typings_input: str | tuple[Literal["video", "audio"], ...] = ()
    """
    The types of input streams this filter accepts.
    Can be a tuple of stream types or a string expression that evaluates to a tuple.
    """

    typings_output: str | tuple[Literal["video", "audio"], ...] = ()
    """
    The types of output streams this filter produces.
    Can be a tuple of stream types or a string expression that evaluates to a tuple.
    """


@dataclass(frozen=True, kw_only=True)
class FFMpegFilter(Serializable):
    """
    Comprehensive representation of an FFmpeg filter with all its metadata.

    This class contains the complete definition of an FFmpeg filter, including
    its name, description, capabilities, input/output specifications, and options.
    It serves as the central schema for representing filters in typed-ffmpeg.
    """

    id: str | None = None
    """Optional unique identifier for the filter"""

    name: str
    """The name of the filter as used in FFmpeg commands"""

    description: str
    """Human-readable description of what the filter does"""

    ref: str | None = None
    """Optional reference to documentation or source code"""

    # Flags
    is_support_slice_threading: bool | None = None
    """Whether the filter supports slice-based multithreading"""

    is_support_timeline: bool | None = None
    """Whether the filter supports timeline editing features"""

    is_support_framesync: bool | None = None
    """Whether the filter supports frame synchronization"""

    is_support_command: bool | None = None
    """Whether the filter supports runtime commands"""

    is_filter_sink: bool | None = None
    """Whether the filter is a sink (consumes input without producing output)"""

    is_filter_source: bool | None = None
    """Whether the filter is a source (produces output without requiring input)"""

    # IO Typing
    is_dynamic_input: bool = False
    """Whether the filter can accept a variable number of inputs"""

    is_dynamic_output: bool = False
    """Whether the filter can produce a variable number of outputs"""

    stream_typings_input: tuple[FFMpegIOType, ...] = ()
    """The types of input streams this filter accepts"""

    stream_typings_output: tuple[FFMpegIOType, ...] = ()
    """The types of output streams this filter produces"""

    formula_typings_input: str | None = None
    """Optional formula to dynamically determine input types"""

    formula_typings_output: str | None = None
    """Optional formula to dynamically determine output types"""

    pre: tuple[tuple[str, str], ...] = ()
    """Pre-defined parameter pairs for the filter"""

    options: tuple[FFMpegFilterOption, ...] = ()
    """The configurable options this filter accepts"""

    @property
    def pre_dict(self) -> dict[str, str]:
        """
        Convert the pre-defined parameter pairs to a dictionary.

        Returns:
            A dictionary mapping parameter names to their values
        """
        return dict(self.pre)

    @property
    def to_def(self) -> FFMpegFilterDef:
        """
        Convert this comprehensive filter definition to a simplified FFMpegFilterDef.

        This creates a simplified representation of the filter focusing only on
        its name and input/output types, which is useful for filter node creation.

        Returns:
            A simplified FFMpegFilterDef representation of this filter
        """
        return FFMpegFilterDef(
            name=self.name,
            typings_input=self.formula_typings_input
            or tuple(k.type.value for k in self.stream_typings_input),
            typings_output=self.formula_typings_output
            or tuple(k.type.value for k in self.stream_typings_output),
        )

    @property
    def input_typings(self) -> set[StreamType]:
        """
        Determine the set of input stream types this filter accepts.

        This property analyzes the filter's input specifications to determine
        what types of streams (audio, video, or both) it can accept as input.

        Returns:
            A set of StreamType values representing accepted input types

        Raises:
            AssertionError: If a dynamic input filter has no input formula
        """
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
        """
        Determine the set of output stream types this filter produces.

        This property analyzes the filter's output specifications to determine
        what types of streams (audio, video, or both) it can produce as output.

        Returns:
            A set of StreamType values representing produced output types

        Raises:
            AssertionError: If a dynamic output filter has no output formula
        """
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
        """
        Determine the FFmpeg filter type based on input and output stream types.

        This property analyzes the filter's input and output specifications to
        determine which category of filter it belongs to according to FFmpeg's
        classification system (audio filter, video filter, source, sink, etc.).

        Returns:
            The appropriate FFMpegFilterType for this filter

        Raises:
            ValueError: If the filter's input/output configuration doesn't match
                       any known filter type
            AssertionError: If a sink filter has multiple input types or
                           if a filter has no input types
        """
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


@serializable
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


@serializable
class FFMpegOptionType(str, Enum):
    """
    Enumeration of FFmpeg option data types.

    This enum defines the various data types that can be used for FFmpeg
    command-line options. These types correspond to the internal option
    types defined in FFmpeg's libavutil/opt.h header.
    """

    OPT_TYPE_FUNC = "OPT_TYPE_FUNC"
    """Function option type, typically used for callback functions"""

    OPT_TYPE_BOOL = "OPT_TYPE_BOOL"
    """Boolean option type (true/false)"""

    OPT_TYPE_STRING = "OPT_TYPE_STRING"
    """String option type"""

    OPT_TYPE_INT = "OPT_TYPE_INT"
    """Integer option type"""

    OPT_TYPE_INT64 = "OPT_TYPE_INT64"
    """64-bit integer option type"""

    OPT_TYPE_FLOAT = "OPT_TYPE_FLOAT"
    """Floating-point option type"""

    OPT_TYPE_DOUBLE = "OPT_TYPE_DOUBLE"
    """Double-precision floating-point option type"""

    OPT_TYPE_TIME = "OPT_TYPE_TIME"
    """Time value option type (e.g., duration in seconds)"""


@dataclass(frozen=True, kw_only=True)
class FFMpegOption(Serializable):
    """
    Represents a command-line option for FFmpeg.

    This class defines the metadata for a single option that can be passed
    to the FFmpeg command line, including its type, help text, and flags
    that determine its behavior.
    """

    name: str
    """The name of the option as used in FFmpeg commands"""

    type: FFMpegOptionType
    """The data type of the option (boolean, int, string, etc.)"""

    flags: int
    """Bitmap of FFMpegOptionFlag values that define the option's behavior"""

    help: str
    """Human-readable description of what the option does"""

    argname: str | None = None
    """Optional name for the option's argument in help text"""

    canon: str | None = None
    """For alternative option forms, the name of the canonical option"""

    @property
    def is_input_option(self) -> bool:
        """
        Check if this option applies to input files.

        Returns:
            True if this option is meant to be used with input files
        """
        return bool(self.flags & FFMpegOptionFlag.OPT_INPUT)

    @property
    def is_output_option(self) -> bool:
        """
        Check if this option applies to output files.

        Returns:
            True if this option is meant to be used with output files
        """
        return bool(self.flags & FFMpegOptionFlag.OPT_OUTPUT)

    @property
    def is_global_option(self) -> bool:
        """
        Check if this option applies globally rather than to specific files.

        Returns:
            True if this option is a global option that doesn't apply to
            specific input or output files
        """
        return (
            not self.is_input_option
            and not self.is_output_option
            and not (self.flags & FFMpegOptionFlag.OPT_EXIT)
        )

    @property
    def is_support_stream_specifier(self) -> bool:
        """
        Check if this option supports stream specifiers.

        Stream specifiers allow options to be applied to specific streams
        within a file, using syntax like "-c:v" for video codec.

        Returns:
            True if this option can be used with stream specifiers
        """
        return bool(self.flags & FFMpegOptionFlag.OPT_SPEC)
