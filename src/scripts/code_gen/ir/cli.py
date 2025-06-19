from ... import parse_help


from pathlib import Path

import typer

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

    codecs = parse_help.cli.all_codecs()
    render(
        template_folder=Path(__file__).parent / "templates",
        outpath=outpath,
        codecs=codecs,
    )