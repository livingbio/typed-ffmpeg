from pathlib import Path

import typer

from ...common.schema import FFMpegOption
from .parse_ffmpeg_opt_c import parse_ffmpeg_opt_c
from .pre_compile import precompile, source_folder

app = typer.Typer()


@app.command()
def pre_compile() -> None:
    folder = (Path(__file__).parent.parent.parent.parent.parent / "ffmpeg").resolve()
    precompile(folder)


@app.command()
def parse_ffmpeg_options() -> list[FFMpegOption]:
    ffmpeg_opt_c = source_folder / "fftools/ffmpeg_opt.c"
    return parse_ffmpeg_opt_c(ffmpeg_opt_c.read_text())


if __name__ == "__main__":
    app()
