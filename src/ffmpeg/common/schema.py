from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from ..dag.serialize import dumps, loads

schema_path = Path(__file__).parent / "../scripts/schemas"
schema_path.mkdir(exist_ok=True)


@dataclass(frozen=True, kw_only=True)
class FFMpegFilterOptionChoice:
    name: str
    help: str
    value: str | int


@dataclass(frozen=True, kw_only=True)
class FFMpegFilterOption:
    name: str
    alias: tuple[str, ...]
    description: str | None
    typing: str
    default: bool | int | float | str | None
    required: bool
    choices: tuple[FFMpegFilterOptionChoice, ...]


class FFMpegIOType:
    name: str
    type: Literal["video", "audio"]


@dataclass(frozen=True, kw_only=True)
class FFMpegFilter:
    id: str
    filter_type: Literal["af", "asrc", "asink", "vf", "vsrc", "vsink", "avsrc", "avf", "vaf"]

    name: str
    description: str
    ref: str

    is_input_dynamic: bool
    is_output_dynamic: bool
    is_support_timeline: bool
    is_support_framesync: bool

    input_stream_typings: tuple[FFMpegIOType, ...] | None
    output_stream_typings: tuple[FFMpegIOType, ...] | None
    formula_input_typings: str | None
    formula_output_typings: str | None

    options: tuple[FFMpegFilterOption, ...]

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
    def load(cls, id: str) -> FFMpegFilter:
        path = schema_path / f"{id}.json"

        with path.open() as ifile:
            obj = loads(ifile.read())
            assert isinstance(obj, FFMpegFilter)
            return obj

    def save(self) -> None:
        with (schema_path / f"{self.id}.json").open("w") as ofile:
            ofile.write(dumps(self))
