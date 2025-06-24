from dataclasses import dataclass
from typing import Literal

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
class FFMpegOptionChoiceIR:
    name: str
    help: str
    flags: str
    value: str


@dataclass(frozen=True, kw_only=True)
class FFMpegOptionIR:
    name: str
    help: str
    type: FFMpegOptionType
    default: str | None
    choices: tuple[FFMpegOptionChoiceIR, ...] = ()

    @property
    def safe_name(self) -> str:
        raise NotImplementedError()
    @property
    def typing(self) -> str:
        raise NotImplementedError()


@dataclass(frozen=True, kw_only=True)
class FFMpegCodecIR:
    name: str
    options: tuple[FFMpegOptionIR, ...] = ()
    help: str

    is_decoder: bool
    is_encoder: bool

    @property
    def safe_name(self) -> str:
        raise NotImplementedError()
