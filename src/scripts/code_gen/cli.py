import logging
import os
from dataclasses import asdict, replace
from pathlib import Path

import typer

from ffmpeg.common.cache import load, save
from ffmpeg.common.schema import FFMpegFilter, FFMpegOption

from ..manual.cli import load_config
from ..parse_c.cli import parse_ffmpeg_options
from ..parse_docs.cli import extract_docs
from ..parse_help.cli import all_codecs, all_filters
from ..parse_help.schema import FFMpegCodec
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
    try:
        return load(list[FFMpegOption], "options")
    except Exception as e:
        logging.error(f"Failed to load options from cache: {e}")

    options = parse_ffmpeg_options()
    save(options, "options")
    return options


def load_filters(outpath: Path, rebuild: bool) -> list[FFMpegFilter]:
    """
    Load filters from the output path

    Args:
        outpath: The output path
        rebuild: Whether to use the cache

    Returns:
        The filters
    """

    if not rebuild:
        try:
            return load(list[FFMpegFilter], "filters")
        except Exception as e:
            logging.error(f"Failed to load filters from cache: {e}")

    ffmpeg_filters = []
    for f in sorted(all_filters(), key=lambda i: i.name):
        if f.name == "afir":
            continue

        manual_config = load_config(f.name)
        if manual_config:
            f = replace(f, **asdict(manual_config))

        try:
            filter_info = gen_filter_info(f)
            save(filter_info, filter_info.name)
            ffmpeg_filters.append(filter_info)
        except ValueError:
            print(f"Failed to generate filter info for {f.name}")

    save(ffmpeg_filters, "filters")

    return ffmpeg_filters


def load_codecs(rebuild: bool) -> list[FFMpegCodec]:
    """
    Load codecs from the output path

    Args:
        rebuild: Whether to use the cache

    Returns:
        The codecs
    """

    if not rebuild:
        try:
            return load(list[FFMpegCodec], "codecs")
        except Exception as e:
            logging.error(f"Failed to load codecs from cache: {e}")

    codecs = all_codecs()
    save(codecs, "codecs")
    return codecs


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

    ffmpeg_filters = load_filters(outpath, rebuild)
    ffmpeg_options = gen_option_info()
    ffmpeg_codecs = load_codecs(rebuild)

    render(
        filters=ffmpeg_filters,
        options=ffmpeg_options,
        codecs=ffmpeg_codecs,
        outpath=outpath,
    )
    os.system("pre-commit run -a")


if __name__ == "__main__":
    app()
