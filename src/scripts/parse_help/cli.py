#!/usr/bin/env python3
"""
CLI for parsing FFmpeg filter help information.

This module provides commands to extract and parse filter information from FFmpeg's
help output. It combines information from multiple sources to create comprehensive
filter definitions with proper typing information.
"""

import typer

from . import parse_codecs, parse_filters, parse_formats
from .schema import FFMpegCodec, FFMpegFilter, FFMpegFormat

app = typer.Typer(help="Parse FFmpeg filter help information")


@app.command()
def all_filters() -> list[FFMpegFilter]:
    """
    Parse all filters from FFmpeg help output
    """
    return parse_filters.extract()


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
