import json
import pathlib

from pydantic import BaseModel, HttpUrl

from ..parse_c.schema import AVFilterPad, FilterType

schema_path = pathlib.Path(__file__).parent / "schemas"
schema_path.mkdir(exist_ok=True)


class FFmpegFilterOption(BaseModel):
    name: str
    description: str

    typing: str
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

    options: list[FFmpegFilterOption] = []

    @classmethod
    def load(cls, path: pathlib.Path) -> "FFmpegFilter":
        with path.open() as ifile:
            return FFmpegFilter(**json.load(ifile))

    def save(self) -> None:
        with (schema_path / f"{self.id}.json").open("w") as ofile:
            ofile.write(self.model_dump_json())
