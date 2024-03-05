from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from .serialize import dumps, loads

schema_path = Path(__file__).parent / "../scripts/schemas"
schema_path.mkdir(exist_ok=True)


@dataclass(frozen=True, kw_only=True)
class FFMpegFilterOptionChoice:
    name: str
    help: str
    value: str | int


@dataclass(frozen=True, kw_only=True)
class FFmpegFilterOption:
    name: str
    alias: tuple[str, ...] = ()
    description: str | None = None
    typing: str
    default: bool | int | float | str | None = None
    required: bool = False
    choices: tuple[FFMpegFilterOptionChoice, ...] = ()


@dataclass(frozen=True, kw_only=True)
class FFMpegIOType:
    name: str
    type: Literal["video", "audio"]


@dataclass(frozen=True, kw_only=True)
class FFmpegFilter:
    id: str
    filter_type: Literal["af", "asrc", "asink", "vf", "vsrc", "vsink", "avsrc", "avf", "vaf"] | None = None

    name: str | None = None
    description: str | None = None
    ref: str | None = None

    is_input_dynamic: bool = False
    is_output_dynamic: bool = False
    is_support_timeline: bool = False
    is_support_framesync: bool = False

    input_stream_typings: tuple[FFMpegIOType, ...] | None = None
    output_stream_typings: tuple[FFMpegIOType, ...] | None = None
    formula_input_typings: str | None = None
    formula_output_typings: str | None = None

    options: tuple[FFmpegFilterOption, ...] = ()

    @property
    def is_input_type_mixed(self) -> bool:
        if self.input_types:
            return "video" in self.input_types and "audio" in self.input_types
        return False

    @property
    def input_types(self) -> str | None:
        if self.is_input_dynamic:
            return self.formula_input_typings

        assert self.input_stream_typings
        return str([k.type for k in self.input_stream_typings])

    @property
    def output_types(self) -> str | None:
        if self.is_output_dynamic:
            return self.formula_output_typings

        assert self.output_stream_typings
        return str([k.type for k in self.output_stream_typings])

    @classmethod
    def load(cls, id: str) -> FFmpegFilter:
        path = schema_path / f"{id}.json"

        with path.open() as ifile:
            obj = loads(ifile.read())
            assert isinstance(obj, FFmpegFilter)
            return obj

    def save(self) -> None:
        with (schema_path / f"{self.id}.json").open("w") as ofile:
            ofile.write(dumps(self))
