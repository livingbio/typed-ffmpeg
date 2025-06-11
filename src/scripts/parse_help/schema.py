from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True, kw_only=True)
class FFMpegOptionChoice:
    name: str
    help: str
    flags: str
    value: str


@dataclass(frozen=True, kw_only=True)
class FFMpegAVOption:
    section: str
    name: str
    type: str
    flags: str
    help: str
    min: str | None = None
    max: str | None = None
    default: str | None = None
    choices: tuple[FFMpegOptionChoice, ...] = ()


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
class FFMpegCodec:
    name: str
    flags: str
    description: str
    options: tuple[FFMpegAVOption, ...] = ()

    @property
    def codec_type(self) -> Literal["video", "audio", "subtitle"]:
        match self.flags[0]:
            case "V":
                return "video"
            case "A":
                return "audio"
            case "S":
                return "subtitle"
            case _:
                raise ValueError(f"Invalid stream type: {self.flags[0]}")


@dataclass(frozen=True, kw_only=True)
class FFMpegEncoder(FFMpegCodec):
    pass


@dataclass(frozen=True, kw_only=True)
class FFMpegDecoder(FFMpegCodec):
    pass
