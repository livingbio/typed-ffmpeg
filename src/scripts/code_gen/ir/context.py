from typing import Any
from ...parse_help.parse_codecs import extract
from ...parse_help import schema as help_schema
from . import schema

def convert_codecs(codecs: list[help_schema.FFMpegCodec]) -> list[schema.FFMpegCodec]:
    return [
        schema.FFMpegCodec(
            name=codec.name,
            options=codec.options,
        ) for codec in codecs
    ]

def prepare_context() -> dict[str, Any]:
    return {
        "codecs": extract(),
    }