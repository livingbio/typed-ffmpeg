from enum import Enum

from code_gen.schema import StreamType
from pydantic import BaseModel


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

    typing: str
    min: str | None = None
    max: str | None = None
    default: str | None = None
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
    input_types: list[tuple[str, StreamType]] | None = None
    output_types: list[tuple[str, StreamType]] | None = None

    options: list[AVOption] = []
