#!/usr/bin/env python3
"""
Main CLI entry point for the typed-ffmpeg scripts package.

This module provides a unified command-line interface for various FFmpeg code generation
and parsing utilities. It combines multiple sub-applications into a single CLI tool with
different subcommands for each functionality area.
"""

import pdb
import sys
from types import TracebackType

import typer

from .code_gen.cli import app as code_gen_app
from .manual.cli import app as manual_app
from .parse_c.cli import app as parse_c_app
from .parse_docs.cli import app as parse_docs_app
from .parse_help.cli import app as parse_help_app


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


app.add_typer(parse_help_app, name="parse-help")
app.add_typer(manual_app, name="manual")
app.add_typer(parse_c_app, name="parse-c")
app.add_typer(parse_docs_app, name="parse-docs")
app.add_typer(code_gen_app, name="code-gen")

if __name__ == "__main__":
    app()
