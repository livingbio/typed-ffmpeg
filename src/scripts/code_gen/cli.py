import os
from dataclasses import asdict, replace
from pathlib import Path

import typer

from ffmpeg.common.schema import FFMpegFilter, FFMpegOption

from ..manual.cli import load_config
from ..parse_c.cli import parse_ffmpeg_options
from ..parse_docs.cli import extract_docs
from ..parse_help.cli import all_filters
from .gen import render

app = typer.Typer()


def gen_filter_info(ffmpeg_filter: FFMpegFilter) -> FFMpegFilter:
    """
    Generate filter info

    Args:
        ffmpeg_filter: The filter

    Returns:
        The filter info
    """
    filter_doc = extract_docs(ffmpeg_filter.name)

    # NOTE:
    # currently we only use filter_doc's url info
    return replace(ffmpeg_filter, ref=filter_doc.url)


def gen_option_info() -> list[FFMpegOption]:
    """
    Generate option info

    Returns:
        The option info
    """
    return parse_ffmpeg_options()


@app.command()
def generate(outpath: Path = None) -> None:
    """
    Generate filter and option documents

    Args:
        outpath: The output path
    """
    if not outpath:
        outpath = Path(__file__).parent.parent.parent / "ffmpeg"

    ffmpeg_filters = []

    for f in sorted(all_filters(), key=lambda i: i.name):
        if f.name == "afir":
            continue

        manual_config = load_config(f.name)
        if manual_config:
            f = replace(f, **asdict(manual_config))

        try:
            ffmpeg_filters.append(gen_filter_info(f))
        except ValueError:
            print(f"Failed to generate filter info for {f.name}")
    ffmpeg_options = gen_option_info()

    render(ffmpeg_filters, ffmpeg_options, outpath)
    os.system("pre-commit run -a")


if __name__ == "__main__":
    app()
