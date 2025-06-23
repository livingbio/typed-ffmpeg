from typing import cast
from ..code_gen.schema import FFMpegCodecIR, FFMpegOptionIR, FFMpegOptionChoiceIR
from .schema import FFMpegAVOption, FFMpegOptionSet, FFMpegOptionChoice, FFMpegOptionType, FFMpegOption, FFMpegDecoder, FFMpegEncoder

def convert(obj: FFMpegOptionSet | FFMpegOption | FFMpegOptionChoice) -> FFMpegCodecIR | FFMpegOptionIR | FFMpegOptionChoiceIR:
    match obj:
        case FFMpegEncoder():
            return FFMpegCodecIR(
                name=obj.name,
                help=obj.help,
                options=cast(tuple[FFMpegOptionIR, ...], tuple(convert(option) for option in obj.options)),
                is_decoder=False,
                is_encoder=True,
            )
        case FFMpegDecoder():
            return FFMpegCodecIR(
                name=obj.name,
                help=obj.help,
                options=cast(tuple[FFMpegOptionIR, ...], tuple(convert(option) for option in obj.options)),
                is_decoder=True,
                is_encoder=False,
            )
        case FFMpegAVOption():
            return FFMpegOptionIR(
                name=obj.name,
                help=obj.help,
                type=obj.type,
                default=obj.default,
                choices=cast(tuple[FFMpegOptionChoiceIR, ...], tuple(convert(choice) for choice in obj.choices)),
            )
        
    raise NotImplementedError()