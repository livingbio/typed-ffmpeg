#!/usr/bin/env python3
"""
CLI for parsing FFmpeg filter help information.

This module provides commands to extract and parse filter information from FFmpeg's
help output. It combines information from multiple sources to create comprehensive
filter definitions with proper typing information.
"""

import typer

from ffmpeg.common.schema import (
    FFMpegFilter,
    FFMpegFilterOption,
    FFMpegFilterOptionChoice,
    FFMpegFilterOptionType,
)

from . import parse_codecs, parse_filters, parse_formats
from .schema import FFMpegCodec, FFMpegFormat

app = typer.Typer(help="Parse FFmpeg filter help information")


@app.command()
def all_filters() -> list[FFMpegFilter]:
    """
    Parse all filters from FFmpeg help output

    This function combines information from two sources:
    1. The general filter list from 'ffmpeg -filters'
    2. Detailed filter information from 'ffmpeg -h filter=<filter_name>'

    It merges these sources to create comprehensive FFMpegFilter objects that include
    both the high-level filter capabilities and detailed option information for each filter.

    Returns:
        A list of FFMpegFilter objects with complete filter information
    """
    output = []

    for filter_info in parse_filters.extract():
        output.append(
            FFMpegFilter(
                name=filter_info.name,
                description=filter_info.help,
                # flags
                is_support_timeline=False,
                is_support_slice_threading=False,
                is_support_command=False,
                # NOTE: is_support_framesync can only be determined by filter_info_from_help
                is_support_framesync=False,
                is_filter_sink=filter_info.io_flags.endswith("->|"),
                is_filter_source=filter_info.io_flags.startswith("|->"),
                # IO Typing
                is_dynamic_input="N->" in filter_info.io_flags,
                is_dynamic_output="->N" in filter_info.io_flags,
                # stream_typings's name can only be determined by filter_info_from_help
                stream_typings_input=(),
                stream_typings_output=(),
                options=tuple(
                    FFMpegFilterOption(
                        name=option.name,
                        type=FFMpegFilterOptionType(option.type),
                        default=option.default,
                        description=option.help,
                        choices=tuple(
                            FFMpegFilterOptionChoice(
                                name=choice.name,
                                help=choice.help,
                                flags=choice.flags,
                                value=choice.value,
                            )
                            for choice in option.choices
                        ),
                    )
                    for option in filter_info.options
                ),
            )
        )

    return output


@app.command()
def all_codecs() -> list[FFMpegCodec]:
    """
    Parse all codecs from FFmpeg help output
    """
    return parse_codecs.extract()


@app.command()
def all_formats() -> list[FFMpegFormat]:
    """
    Parse all muxers from FFmpeg help output
    """
    return parse_formats.extract()
