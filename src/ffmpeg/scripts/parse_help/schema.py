import json
import pathlib
from enum import Enum
from typing import Literal

from pydantic import BaseModel

from ..code_gen.schema import FFMpegIOType

schema_path = pathlib.Path(__file__).parent / "helps"
schema_path.mkdir(exist_ok=True)


class Flag(str, Enum):
    # from opt.c
    AV_OPT_FLAG_ENCODING_PARAM = "E"
    AV_OPT_FLAG_DECODING_PARAM = "D"
    AV_OPT_FLAG_FILTERING_PARAM = "F"
    AV_OPT_FLAG_VIDEO_PARAM = "V"
    AV_OPT_FLAG_AUDIO_PARAM = "A"
    AV_OPT_FLAG_SUBTITLE_PARAM = "S"
    AV_OPT_FLAG_EXPORT = "X"
    AV_OPT_FLAG_READONLY = "R"
    AV_OPT_FLAG_BSF_PARAM = "B"
    AV_OPT_FLAG_RUNTIME_PARAM = "T"
    AV_OPT_FLAG_DEPRECATED = "P"


class AVChoice(BaseModel):
    name: str
    help: str
    value: int | str
    flags: str = None


class AVOption(BaseModel):
    name: str
    alias: list[str] = []
    description: str | None = None

    typing: Literal[
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
    ]
    min: str | None = None
    max: str | None = None
    default: bool | int | float | str | None = None
    choices: list[AVChoice] = []
    flags: str = None


class AVFilter(BaseModel):
    name: str
    description: str

    is_slice_threading_supported: bool = False
    is_support_timeline: bool = False
    is_support_framesync: bool = False

    is_dynamic_inputs: bool = False
    is_dynamic_outputs: bool = False
    input_types: list[FFMpegIOType] | None = None
    output_types: list[FFMpegIOType] | None = None

    options: list[AVOption] = []

    @classmethod
    def load(cls, id: str) -> "AVFilter":
        path = schema_path / f"{id}.json"

        with path.open() as ifile:
            return AVFilter(**json.load(ifile))

    def save(self) -> None:
        with (schema_path / f"{self.name}.json").open("w") as ofile:
            ofile.write(self.model_dump_json(indent=2))
