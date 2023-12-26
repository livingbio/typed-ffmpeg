# https://ffmpeg.org/ffmpeg-filters.html


import parse_c.cli
import parse_docs.cli
import typer

app = typer.Typer()


app.add_typer(parse_docs.cli.app, name="parse_docs")
app.add_typer(parse_c.cli.app, name="parse_c")

if __name__ == "__main__":
    app()
