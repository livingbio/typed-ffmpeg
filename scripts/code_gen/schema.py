from pydantic import BaseModel, HttpUrl

from ..parse_c.schema import AVFilterPad, FilterType


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
