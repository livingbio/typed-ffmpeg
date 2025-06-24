from typing import Any, cast

from ..code_gen.schema import FFMpegCodecIR, FFMpegFormatIR, FFMpegOptionChoiceIR, FFMpegAVOptionIR
from .schema import (
    FFMpegAVOption,
    FFMpegCodec,
    FFMpegDecoder,
    FFMpegDemuxer,
    FFMpegEncoder,
    FFMpegFormat,
    FFMpegMuxer,
    FFMpegOption,
    FFMpegOptionChoice,
    FFMpegOptionSet,
)
from . import parse_codecs, parse_formats, parse_filters

def convert(obj: Any) -> Any:
   match obj:
      case FFMpegCodec():
          return FFMpegCodecIR(
        name=obj.name,
        help=obj.help,
        options=tuple(convert(option) for option in obj.options),
        is_decoder=isinstance(obj, FFMpegDecoder),
        is_encoder=isinstance(obj, FFMpegEncoder),
    )
      case FFMpegFormat():
         return FFMpegFormatIR(
        name=obj.name,
        help=obj.help,
        options=tuple(convert(option) for option in obj.options),
        is_muxer=isinstance(obj, FFMpegMuxer),
        is_demuxer=isinstance(obj, FFMpegDemuxer),
    )
      case FFMpegAVOption():
         return FFMpegAVOptionIR(
        name=obj.name,
        help=obj.help,
        type=obj.type,
        choices=tuple(convert(choice) for choice in obj.choices),
        default=obj.default,
    )
      case FFMpegOptionChoice():
         return FFMpegOptionChoiceIR(
        name=obj.name,
        help=obj.help,
        flags=obj.flags,
        value=obj.value,
    )
      case _:
         raise ValueError(f"Unknown object: {obj}")

def all_codecs() -> list[FFMpegCodecIR]:
    return cast(list[FFMpegCodecIR], [
        convert(codec)
        for codec in parse_codecs.extract()
    ])

def all_formats() -> list[FFMpegFormatIR]:
    return cast(list[FFMpegFormatIR], [
        convert(format)
        for format in parse_formats.extract()
    ])