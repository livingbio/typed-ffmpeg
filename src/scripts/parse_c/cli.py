#!/usr/bin/env python3
"""
CLI for parsing FFmpeg C source code.

This module provides commands to pre-compile FFmpeg source code and parse
options from the C code, extracting structured information about FFmpeg's
command-line options and their properties.
"""

import typer

from ffmpeg.common.schema import FFMpegOption

from .parse_ffmpeg_opt_c import parse_ffmpeg_opt_c
from .pre_compile import precompile, target_folder

app = typer.Typer(help="Parse FFmpeg C source code")


@app.command()
def pre_compile() -> None:
    """
    Pre-compile the ffmpeg source code
    """
    precompile()


@app.command()
def parse_ffmpeg_options() -> list[FFMpegOption]:
    """
    Parse the ffmpeg options from C code
    """
    precompile()

    ffmpeg_opt_c = target_folder / "fftools/ffmpeg_opt.c"
    return parse_ffmpeg_opt_c(ffmpeg_opt_c.read_text())


if __name__ == "__main__":
    app()
