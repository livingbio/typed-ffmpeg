
from pathlib import Path

import typer
from ...parse_help import parse_codecs
from .render import render
app = typer.Typer()

@app.command()
def generate(outpath: Path | None = None, rebuild: bool = False) -> None:
    """
    Generate filter and option documents

    Args:
        outpath: The output path
        rebuild: Whether to rebuild the filters and options from scratch, ignoring the cache
    """
    if not outpath:
        outpath = Path(__file__).parent.parent.parent / "ffmpeg"

    codecs = parse_codecs.extract()

    render(
    )
    os.system("pre-commit run -a")


if __name__ == "__main__":
    app()
