"""Schema definitions for FFmpeg options."""

from dataclasses import dataclass
from enum import Enum


class FFMpegOptionFlag(int, Enum):
    """FFmpeg option flags that define option behavior and characteristics."""

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
class FFMpegOption:
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
