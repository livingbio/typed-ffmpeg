from __future__ import annotations

import json
import pathlib

from ...common.schema import FFMpegFilter

schema_path = pathlib.Path(__file__).parent / "schemas"
schema_path.mkdir(exist_ok=True)


class _FFmpegFilter(FFMpegFilter):
    @property
    def is_input_type_mixed(self) -> bool:
        if self.input_types:
            return "video" in self.input_types and "audio" in self.input_types
        return False

    @property
    def input_types(self) -> str | None:
        if self.is_input_dynamic:
            return self.formula_input_typings
        return str([k.type for k in self.input_stream_typings])

    @property
    def output_types(self) -> str | None:
        if self.is_output_dynamic:
            return self.formula_output_typings
        return str([k.type for k in self.output_stream_typings])

    @classmethod
    def load(cls, id: str) -> _FFmpegFilter:
        path = schema_path / f"{id}.json"

        with path.open() as ifile:
            return _FFmpegFilter(**json.load(ifile))

    def save(self) -> None:
        with (schema_path / f"{self.id}.json").open("w") as ofile:
            ofile.write(self.model_dump_json(indent=2))
