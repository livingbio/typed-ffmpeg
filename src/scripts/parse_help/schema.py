from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class FFMpegOptionChoice:
    name: str
    help: str


@dataclass(frozen=True, kw_only=True)
class FFMpegOptionValue(FFMpegOptionChoice):
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
