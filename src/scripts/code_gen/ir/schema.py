from dataclasses import dataclass
from typing import Literal
from abc import ABC, abstractmethod

FFMpegOptionType = Literal["boolean", "duration", "color", "flags", "dictionary", "pix_fmt", "int", "int64", "double", "float", "string", "video_rate", "image_size", "rational", "sample_fmt", "binary", "channel_layout", "pixel_format", "sample_rate"]


@dataclass(frozen=True, kw_only=True)
class FFMpegOptionChoice:
    name: str
    help: str
    flags: str
    value: str


@dataclass(frozen=True, kw_only=True)
class FFMpegOption:
    name: str
    help: str
    type: FFMpegOptionType
    default: str
    choices: tuple[FFMpegOptionChoice, ...] = ()

    @abstractmethod
    def safe_name(self) -> str:
        ...

    @abstractmethod
    def typing(self) -> str:
        ...

@dataclass(frozen=True, kw_only=True)
class FFMpegCodec(ABC):
    name: str
    options: tuple[FFMpegOption, ...] = ()
    help: str

    is_decoder: bool
    is_encoder: bool

    @abstractmethod
    def safe_name(self) -> str:
        ...
    