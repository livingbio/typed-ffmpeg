# https://ffmpeg.org/ffmpeg-filters.html


import typer

from .code_gen.cli import app as code_gen_app
from .parse_c.cli import app as parse_c_app
from .parse_docs.cli import app as parse_docs_app

app = typer.Typer()

app.add_typer(parse_docs_app, name="parse-docs")
app.add_typer(parse_c_app, name="parse-c")
app.add_typer(code_gen_app, name="code-gen")
