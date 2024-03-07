import typer

from ...common.schema import FFMpegOption
from .parse_ffmpeg_opt_c import parse_ffmpeg_opt_c

app = typer.Typer()


@app.command()
def parse_ffmpeg_options() -> list[FFMpegOption]:
    ffmpeg_opt_c = "./ffmpeg/fftools/ffmpeg_opt.c"
    return parse_ffmpeg_opt_c(ffmpeg_opt_c.read_text())
