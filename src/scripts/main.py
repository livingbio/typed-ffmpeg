#!/usr/bin/env python3
"""
Main CLI entry point for the typed-ffmpeg scripts package.

This module provides a unified command-line interface for various FFmpeg code generation
and parsing utilities. It combines multiple sub-applications into a single CLI tool with
different subcommands for each functionality area.
"""

import pdb
import sys
from pathlib import Path
from types import TracebackType
from typing import Annotated

import typer

from .code_gen.cli import app as code_gen_app
from .code_gen.cli import generate
from .manual.cli import app as manual_app
from .parse_c.cli import app as parse_c_app
from .parse_docs.cli import app as parse_docs_app
from .parse_help.cli import app as parse_help_app
from .version_utils import SUPPORTED_VERSIONS


def pdb_callback(value: bool) -> None:
    """Enable debugger on exceptions when the --pdb option is used."""
    if value:

        def debugger_hook(
            exctype: type[BaseException],
            value: BaseException,
            traceback: TracebackType | None,
        ) -> None:
            if exctype is KeyboardInterrupt:
                sys.__excepthook__(exctype, value, traceback)
            else:
                pdb.post_mortem(traceback)

        sys.excepthook = debugger_hook


app = typer.Typer(help="Typed-FFmpeg code generation and parsing utilities")


# Add global --pdb option
@app.callback()
def main(
    pdb: bool = typer.Option(False, "--pdb", help="Drop into debugger on exceptions"),
) -> None:
    """Typed-FFmpeg code generation and parsing utilities."""
    pdb_callback(pdb)


@app.command()
def collect(
    version: Annotated[
        str,
        typer.Argument(help=f"Target FFmpeg version ({', '.join(SUPPORTED_VERSIONS)})"),
    ],
    ffmpeg_binary: Annotated[
        str,
        typer.Option(help="Path to the FFmpeg binary for this version"),
    ] = "ffmpeg",
    outpath: Annotated[
        Path | None,
        typer.Option(help="Output path for generated code"),
    ] = None,
) -> None:
    """
    Collect cache data for a specific FFmpeg version.

    Parses the specified FFmpeg binary to extract filter, codec, and format
    definitions, then stores the cache data in the version-specific directory
    under versions/{version}/cache/.

    Example:
        scripts collect v7 --ffmpeg-binary /usr/local/bin/ffmpeg7

    Raises:
        typer.Exit: If the version is not supported.

    """
    if version not in SUPPORTED_VERSIONS:
        typer.echo(
            f"Error: Unsupported version '{version}'. "
            f"Supported: {', '.join(SUPPORTED_VERSIONS)}",
            err=True,
        )
        raise typer.Exit(1)

    typer.echo(f"Collecting data for FFmpeg {version} using binary: {ffmpeg_binary}")
    generate(
        outpath=outpath, rebuild=True, version=version, ffmpeg_binary=ffmpeg_binary
    )
    typer.echo(f"Cache data saved to versions/{version}/cache/")


app.add_typer(parse_help_app, name="parse-help")
app.add_typer(manual_app, name="manual")
app.add_typer(parse_c_app, name="parse-c")
app.add_typer(parse_docs_app, name="parse-docs")
app.add_typer(code_gen_app, name="code-gen")

if __name__ == "__main__":
    app()
