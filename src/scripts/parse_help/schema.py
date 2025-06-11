from dataclasses import dataclass


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


@dataclass(frozen=True, kw_only=True)
class FFMpegEncoder:
    name: str
    flags: str
    description: str


@dataclass(frozen=True, kw_only=True)
class FFMpegDecoder:
    name: str
    flags: str
    description: str
