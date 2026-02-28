#!/usr/bin/env python3
"""
CLI for parsing FFmpeg filter help information.

This module provides commands to extract and parse filter information from FFmpeg's
help output. It combines information from multiple sources to create comprehensive
filter definitions with proper typing information.
"""

import typer

from . import parse_codecs, parse_filters, parse_formats, parse_help
from .schema import FFMpegAVOption, FFMpegCodec, FFMpegFilter, FFMpegFormat

app = typer.Typer(help="Parse FFmpeg filter help information")


@app.command()
def all_av_option_sets() -> list[FFMpegAVOption]:
    """
    Parse all options from FFmpeg help output.

    Returns:
        List of parsed FFmpeg options.

    """
    return [k for k in parse_help.extract() if isinstance(k, FFMpegAVOption)]


@app.command()
def all_filters() -> list[FFMpegFilter]:
    """
    Parse all filters from FFmpeg help output.

    This function combines information from two sources:
    1. The general filter list from 'ffmpeg -filters'
    2. Detailed filter information from 'ffmpeg -h filter=<filter_name>'

    It merges these sources to create comprehensive filter information objects.

    Returns:
        A list of parse_help FFMpegFilter objects with complete filter information

    """
    return parse_filters.extract()


@app.command()
def all_codecs() -> list[FFMpegCodec]:
    """
    Parse all codecs from FFmpeg help output.

    Returns:
        List of parsed FFmpeg codecs.

    """
    return parse_codecs.extract()


@app.command()
def all_formats() -> list[FFMpegFormat]:
    """
    Parse all muxers from FFmpeg help output.

    Returns:
        List of parsed FFmpeg formats.

    """
    return parse_formats.extract()
