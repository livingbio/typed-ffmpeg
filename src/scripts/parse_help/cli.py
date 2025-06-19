#!/usr/bin/env python3
"""
CLI for parsing FFmpeg filter help information.

This module provides commands to extract and parse filter information from FFmpeg's
help output. It combines information from multiple sources to create comprehensive
filter definitions with proper typing information.
"""

import typer

from ffmpeg.common.schema import FFMpegFilter

from .parse_all_filter import extract as extract_all_filters
from .parse_codecs import extract
from .parse_filter import extract_avfilter_info_from_help
from .parse_formats import extract
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

    for filter_info in extract_all_filters():
        try:
            filter_info_from_help = extract_avfilter_info_from_help(filter_info.name)
        except AssertionError:  # pragma: no cover
            typer.echo(f"Failed to parse filter {filter_info.name}")  #
            continue

        output.append(
            FFMpegFilter(
                name=filter_info.name,
                description=filter_info.description,
                # flags
                is_support_timeline=filter_info.is_support_timeline,
                is_support_slice_threading=filter_info.is_support_slice_threading,
                is_support_command=filter_info.is_support_command,
                # NOTE: is_support_framesync can only be determined by filter_info_from_help
                is_support_framesync=filter_info_from_help.is_support_framesync,
                is_filter_sink=filter_info.is_filter_sink,
                is_filter_source=filter_info.is_filter_source,
                # IO Typing
                is_dynamic_input=filter_info.is_dynamic_input,
                is_dynamic_output=filter_info.is_dynamic_output,
                # stream_typings's name can only be determined by filter_info_from_help
                stream_typings_input=filter_info_from_help.stream_typings_input,
                stream_typings_output=filter_info_from_help.stream_typings_output,
                options=filter_info_from_help.options,
            )
        )

    return output


@app.command()
def all_codecs() -> list[FFMpegCodec]:
    """
    Parse all codecs from FFmpeg help output
    """
    return extract()


@app.command()
def all_formats() -> list[FFMpegFormat]:
    """
    Parse all muxers from FFmpeg help output
    """
    return extract()
