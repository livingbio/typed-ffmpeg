import typer
from ..cache import save
from ffmpeg.common.schema import FFMpegOption, FFMpegOptionList

from .parse_ffmpeg_opt_c import parse_ffmpeg_opt_c
from .pre_compile import precompile, target_folder

app = typer.Typer()


@app.command()
def pre_compile() -> None:
    precompile()


@app.command()
def parse_ffmpeg_options() -> list[FFMpegOption]:
    precompile()

    ffmpeg_opt_c = target_folder / "fftools/ffmpeg_opt.c"
    r =  parse_ffmpeg_opt_c(ffmpeg_opt_c.read_text())
    option_list = FFMpegOptionList(options=r)

    save(option_list, "list")
    return r


if __name__ == "__main__":
    app()
