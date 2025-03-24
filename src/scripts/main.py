#!/usr/bin/env python3
"""
Main CLI entry point for the typed-ffmpeg scripts package.

This module provides a unified command-line interface for various FFmpeg code generation
and parsing utilities. It combines multiple sub-applications into a single CLI tool with
different subcommands for each functionality area.
"""

import typer

from .code_gen.cli import app as code_gen_app
from .manual.cli import app as manual_app
from .parse_c.cli import app as parse_c_app
from .parse_docs.cli import app as parse_docs_app
from .parse_help.cli import app as parse_help_app

app = typer.Typer(help="Typed-FFmpeg code generation and parsing utilities")


app.add_typer(parse_help_app, name="parse-help")
app.add_typer(manual_app, name="manual")
app.add_typer(parse_c_app, name="parse-c")
app.add_typer(parse_docs_app, name="parse-docs")
app.add_typer(code_gen_app, name="code-gen")

if __name__ == "__main__":
    app()
