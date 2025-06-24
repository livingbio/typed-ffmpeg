from .. import context
from .schema import (
    PythonFFMpegCodec,
    PythonFFMpegFormat,
    PythonFFMpegOption,
    PythonFFMpegOptionChoice,
)


def all_codecs() -> list[PythonFFMpegCodec]:
    return [
        PythonFFMpegCodec(
            name=codec.name,
            options=tuple(
                PythonFFMpegOption(
                    name=option.name,
                    type=option.type,
                    default=option.default,
                    help=option.help,
                    choices=tuple(
                        PythonFFMpegOptionChoice(
                            name=choice.name,
                            help=choice.help,
                            flags=choice.flags,
                            value=choice.value,
                        )
                        for choice in option.choices
                    ),
                )
                for option in codec.options
            ),
            help=codec.help,
            is_decoder=codec.is_decoder,
            is_encoder=codec.is_encoder,
        )
        for codec in context.all_codecs()
    ]


def all_formats() -> list[PythonFFMpegFormat]:
    return [
        PythonFFMpegFormat(
            name=format.name,
            options=tuple(
                PythonFFMpegOption(
                    name=option.name,
                    type=option.type,
                    default=option.default,
                    help=option.help,
                    choices=tuple(
                        PythonFFMpegOptionChoice(
                            name=choice.name,
                            help=choice.help,
                            flags=choice.flags,
                            value=choice.value,
                        )
                        for choice in option.choices
                    ),
                )
                for option in format.options
            ),
            help=format.help,
            is_muxer=format.is_muxer,
            is_demuxer=format.is_demuxer,
        )
        for format in context.all_formats()
    ]
