import json
import pathlib
from typing import Literal

from parse_c.schema import AVFilterPad, AVFilterPadType, AVOptionType, FilterType
from pydantic import BaseModel, HttpUrl

schema_path = pathlib.Path(__file__).parent / "schemas"
schema_path.mkdir(exist_ok=True)

TYPING_MAP: dict[AVOptionType, str] = {
    AVOptionType.AV_OPT_TYPE_BOOL: "bool",
    AVOptionType.AV_OPT_TYPE_INT: "int",
    AVOptionType.AV_OPT_TYPE_INT64: "int",
    AVOptionType.AV_OPT_TYPE_FLOAT: "float",
    AVOptionType.AV_OPT_TYPE_DOUBLE: "float",
    AVOptionType.AV_OPT_TYPE_STRING: "str",
    AVOptionType.AV_OPT_TYPE_FLAGS: "str",
    AVOptionType.AV_OPT_TYPE_COLOR: "str",
    AVOptionType.AV_OPT_TYPE_RATIONAL: "float",
    AVOptionType.AV_OPT_TYPE_IMAGE_SIZE: "str",
    AVOptionType.AV_OPT_TYPE_VIDEO_RATE: "str",
    AVOptionType.AV_OPT_TYPE_DURATION: "int",
    AVOptionType.AV_OPT_TYPE_PIXEL_FMT: "str",
    AVOptionType.AV_OPT_TYPE_CHLAYOUT: "str",
    AVOptionType.AV_OPT_TYPE_SAMPLE_FMT: "str",
    AVOptionType.AV_OPT_TYPE_DICT: "str",
    AVOptionType.AV_OPT_TYPE_BINARY: "str",
}


class FFmpegFilterOption(BaseModel):
    name: str
    alias: list[str] = []
    description: str | None = None

    typing: Literal["bool", "int", "float", "str"]
    default: str | int | float | None = None
    required: bool


class FFmpegFilter(BaseModel):
    id: str
    filter_type: FilterType

    name: str
    description: str
    ref: HttpUrl = None

    is_input_dynamic: bool = False
    is_output_dynamic: bool = False

    input_stream_typings: list[AVFilterPad] = []
    output_stream_typings: list[AVFilterPad] = []
    formula_input_typings: str | None = None
    formula_output_typings: str | None = None

    options: list[FFmpegFilterOption] = []

    @property
    def input_types(self) -> list[str]:
        if self.is_input_dynamic:
            return []
        return [("video" if stream.type == AVFilterPadType.video else "audio") for stream in self.input_stream_typings]

    @property
    def output_types(self) -> list[str]:
        if self.is_output_dynamic:
            return []
        return [("video" if stream.type == AVFilterPadType.video else "audio") for stream in self.output_stream_typings]

    @classmethod
    def load(cls, id: str) -> "FFmpegFilter":
        path = schema_path / f"{id}.json"
        with path.open() as ifile:
            return FFmpegFilter(**json.load(ifile))

    def save(self) -> None:
        with (schema_path / f"{self.id}.json").open("w") as ofile:
            ofile.write(self.model_dump_json(indent=2))
