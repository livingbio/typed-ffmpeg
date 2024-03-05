import enum
import json
import pathlib

from parse_c.schema import Choice, FilterType
from pydantic import BaseModel, HttpUrl

schema_path = pathlib.Path(__file__).parent / "schemas"
schema_path.mkdir(exist_ok=True)


class StreamType(str, enum.Enum):
    video = "video"
    audio = "audio"

    def __repr__(self):
        return f"StreamType.{self.value}"


class FFmpegFilterOption(BaseModel):
    name: str
    alias: list[str] = []
    description: str | None = None

    typing: str
    default: bool | int | float | str | None = None
    required: bool = False
    choices: list[Choice] = []

    @property
    def _typing(self) -> str:
        if self.choices:
            return f"{self.typing} | Literal[" + ", ".join(repr(k.name) for k in self.choices) + "]"
        return self.typing

    @property
    def _default(self) -> str | int | float | None:
        if self.choices:
            if v := [k for k in self.choices if k.value == self.default]:
                return v[0].name
        return self.default


class FFMpegIOType(BaseModel):
    name: str
    type: StreamType


class FFmpegFilter(BaseModel):
    id: str
    filter_type: FilterType = None

    name: str = None
    description: str = None
    ref: HttpUrl = None

    is_input_dynamic: bool = False
    is_output_dynamic: bool = False
    is_support_timeline: bool = False
    is_support_framesync: bool = False

    input_stream_typings: list[FFMpegIOType] | None = None
    output_stream_typings: list[FFMpegIOType] | None = None
    formula_input_typings: str | None = None
    formula_output_typings: str | None = None

    options: list[FFmpegFilterOption] = []

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
    def load(cls, id: str) -> "FFmpegFilter":
        path = schema_path / f"{id}.json"

        with path.open() as ifile:
            return FFmpegFilter(**json.load(ifile))

    def save(self) -> None:
        with (schema_path / f"{self.id}.json").open("w") as ofile:
            ofile.write(self.model_dump_json(indent=2))
