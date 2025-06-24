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
class FFMpegAVOptionIR:
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
class FFMpegOptionSetIR:
    name: str
    help: str
    options: tuple[FFMpegAVOptionIR, ...] = ()

    @property
    def safe_name(self) -> str:
        raise NotImplementedError()


@dataclass(frozen=True, kw_only=True)
class FFMpegCodecIR(FFMpegOptionSetIR):
    is_decoder: bool
    is_encoder: bool


@dataclass(frozen=True, kw_only=True)
class FFMpegFormatIR(FFMpegOptionSetIR):
    is_muxer: bool
    is_demuxer: bool


@dataclass(frozen=True, kw_only=True)
class FFMpegFilterIR(FFMpegOptionSetIR):
    is_dynamic_input: bool
    is_dynamic_output: bool

    stream_typings_input: tuple[Literal["audio", "video"], ...]
    stream_typings_output: tuple[Literal["audio", "video"], ...]

    @property
    def return_typing(self) -> str:
        raise NotImplementedError()
