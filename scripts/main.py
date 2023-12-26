# https://ffmpeg.org/ffmpeg-filters.html


import sys
from pathlib import Path

import code_gen.cli
import parse_c.cli
import parse_docs.cli
import typer

app = typer.Typer()


app.add_typer(parse_docs.cli.app, name="parse-docs")
app.add_typer(parse_c.cli.app, name="parse-c")
app.add_typer(code_gen.cli.app, name="code-gen")

if __name__ == "__main__":
    sys.path.append(Path(__file__).parent)
    app()
