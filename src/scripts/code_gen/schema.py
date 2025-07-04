"""Schema definitions for code generation."""

from collections.abc import Iterable
from dataclasses import dataclass
from typing import Literal

from ffmpeg.common.serialize import Serializable

FFMpegOptionType = Literal[
    "boolean",
    "duration",
    "color",
    "flags",
    "dictionary",
    "pix_fmt",
    "int",
    "int64",
    "double",
    "float",
    "string",
    "video_rate",
    "image_size",
    "rational",
    "sample_fmt",
    "binary",
    "channel_layout",
    "pixel_format",
    "sample_rate",
]


@dataclass(frozen=True, kw_only=True)
class FFMpegOptionChoice(Serializable):
    """A choice option for FFmpeg parameters."""

    name: str
    help: str
    flags: str
    value: str


@dataclass(frozen=True, kw_only=True)
class FFMpegAVOption(Serializable):
    """An FFmpeg AV option with metadata."""

    section: str
    name: str
    type: str
    flags: str
    help: str
    min: str | None = None
    max: str | None = None
    default: str | None = None
    choices: tuple[FFMpegOptionChoice, ...] = ()

    @property
    def code_gen_type(self) -> str:
        """
        Get the code generation type for this option.

        Returns:
            The type string for code generation.

        Raises:
            ValueError: If the option type is invalid.

        """

        def handle_choices() -> str:
            if self.type != "flags":
                # NOTE: flags not supported for now
                if self.choices:
                    return "| Literal[{}]".format(
                        ", ".join(f'"{choice.name}"' for choice in self.choices)
                    )
            return ""

        def handle_type() -> str:
            match self.type:
                case "boolean":
                    return "bool | None"
                case "int":
                    return "int | None"
                case "int64":
                    return "int | None"
                case "float":
                    return "float | None"
                case "double":
                    return "float | None"
                case "string":
                    return "str | None"
                case "channel_layout":
                    return "str | None"
                case "flags":
                    return "str | None"
                case "duration":
                    return "str | None"
                case "dictionary":
                    return "str | None"
                case "image_size":
                    return "str | None"
                case "pixel_format":
                    return "str | None"
                case "sample_rate":
                    return "int | None"
                case "sample_fmt":
                    return "str | None"
                case "binary":
                    return "str | None"
                case "rational":
                    return "str | None"
                case "color":
                    return "str | None"
                case "video_rate":
                    return "str | None"
                case "pix_fmt":
                    return "str | None"
                case _:
                    raise ValueError(f"Invalid option type: {self.type}")

        return f"{handle_type()}{handle_choices()}"


# NOTE: note the flags format for -encoders/-decoders vs -codecs are different
# the following code follows the -encoders/-decoders format
# Encoders:
#  V..... = Video
#  A..... = Audio
#  S..... = Subtitle
#  .F.... = Frame-level multithreading
#  ..S... = Slice-level multithreading
#  ...X.. = Codec is experimental
#  ....B. = Supports draw_horiz_band
#  .....D = Supports direct rendering method 1
#  ------
#  V....D a64multi             Multicolor charset for Commodore 64 (codec a64_multi)
#  V....D a64multi5            Multicolor charset for Commodore 64, extended with 5th color (colram) (codec a64_multi5)


@dataclass(frozen=True, kw_only=True)
class FFMpegCodec(Serializable):
    """Base class for FFmpeg codecs."""

    name: str
    flags: str
    description: str
    options: tuple[FFMpegAVOption, ...] = ()

    def filtered_options(self) -> Iterable[FFMpegAVOption]:
        """
        Get the filtered options for this codec.

        Returns:
            An iterable of filtered options.

        """
        return self.options

    @property
    def codec_type(self) -> Literal["video", "audio", "subtitle"]:
        """
        Get the type of this codec.

        Returns:
            The codec type.

        Raises:
            ValueError: If the stream type is invalid.

        """
        match self.flags[0]:
            case "V":
                return "video"
            case "A":
                return "audio"
            case "S":
                return "subtitle"
            case _:
                raise ValueError(f"Invalid stream type: {self.flags[0]}")

    @property
    def is_encoder(self) -> bool:
        """
        Check if this codec is an encoder.

        Returns:
            True if this is an encoder, False otherwise.

        """
        return isinstance(self, FFMpegEncoder)

    @property
    def is_decoder(self) -> bool:
        """
        Check if this codec is a decoder.

        Returns:
            True if this is a decoder, False otherwise.

        """
        return isinstance(self, FFMpegDecoder)


@dataclass(frozen=True, kw_only=True)
class FFMpegEncoder(FFMpegCodec):
    """An FFmpeg encoder."""

    pass


@dataclass(frozen=True, kw_only=True)
class FFMpegDecoder(FFMpegCodec):
    """An FFmpeg decoder."""

    pass


@dataclass(frozen=True, kw_only=True)
class FFMpegFormat(Serializable):
    """Base class for FFmpeg formats."""

    name: str
    flags: str
    description: str
    options: tuple[FFMpegAVOption, ...] = ()

    @property
    def is_muxer(self) -> bool:
        """
        Check if this format is a muxer.

        Returns:
            True if this is a muxer, False otherwise.

        """
        return isinstance(self, FFMpegMuxer)

    @property
    def is_demuxer(self) -> bool:
        """
        Check if this format is a demuxer.

        Returns:
            True if this is a demuxer, False otherwise.

        """
        return isinstance(self, FFMpegDemuxer)


@dataclass(frozen=True, kw_only=True)
class FFMpegDemuxer(FFMpegFormat):
    """An FFmpeg demuxer."""

    pass


@dataclass(frozen=True, kw_only=True)
class FFMpegMuxer(FFMpegFormat):
    """An FFmpeg muxer."""

    pass
