#!/usr/bin/env python3
"""
CLI for parsing FFmpeg C source code.

This module provides commands to pre-compile FFmpeg source code and parse
options from the C code, extracting structured information about FFmpeg's
command-line options and their properties.
"""

from pathlib import Path

import typer

from ffmpeg.common.schema import FFMpegOption

from .parse_ffmpeg_opt_c import parse_ffmpeg_opt_c
from .pre_compile import precompile, target_folder
from .xsd_to_dataclasses import generate_dataclasses, parse_xsd_file

app = typer.Typer(help="Parse FFmpeg C source code")


@app.command()
def pre_compile() -> None:
    """Pre-compile the ffmpeg source code."""
    precompile()


@app.command()
def parse_ffmpeg_options() -> list[FFMpegOption]:
    """
    Parse the ffmpeg options from C code.

    Returns:
        List of parsed FFmpeg options.

    """
    precompile()

    ffmpeg_opt_c = target_folder / "fftools/ffmpeg_opt.c"
    return parse_ffmpeg_opt_c(ffmpeg_opt_c.read_text())


@app.command()
def parse_ffprobe_xsd(xsd_file: Path, output_file: Path) -> None:
    """Parse the ffprobe XSD file."""
    root, ns = parse_xsd_file(str(xsd_file))
    output, _ = generate_dataclasses(root, ns)
    output_file.write_text(output)


if __name__ == "__main__":
    app()
