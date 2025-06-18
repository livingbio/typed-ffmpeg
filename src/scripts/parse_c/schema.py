from enum import Enum

from ffmpeg.common.serialize import serializable


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
