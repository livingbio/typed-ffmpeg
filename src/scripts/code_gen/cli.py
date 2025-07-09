"""Code generation CLI for typed-ffmpeg."""

import logging
import os
from dataclasses import asdict, replace
from pathlib import Path

import typer

from ffmpeg.common.cache import load, save
from ffmpeg.common.schema import (
    FFMpegFilter,
    FFMpegFilterOption,
    FFMpegFilterOptionChoice,
    FFMpegFilterOptionType,
    FFMpegIOType,
    FFMpegOption,
    FFMpegOptionType,
    StreamType,
)

from .. import manual, parse_c, parse_docs, parse_help
from .gen import render
from .schema import (
    FFMpegAVOption,
    FFMpegCodec,
    FFMpegDecoder,
    FFMpegDemuxer,
    FFMpegEncoder,
    FFMpegFormat,
    FFMpegMuxer,
    FFMpegOptionChoice,
)

app = typer.Typer()


def gen_filter_info(ffmpeg_filter: FFMpegFilter) -> FFMpegFilter:
    """
    Generate filter info.

    Args:
        ffmpeg_filter: The filter

    Returns:
        The filter info

    """
    filter_doc = parse_docs.cli.extract_docs(ffmpeg_filter.name)

    # NOTE:
    # currently we only use filter_doc's url info
    return replace(ffmpeg_filter, ref=filter_doc.url)


def load_options(rebuild: bool) -> list[FFMpegOption]:
    """
    Load options from the output path.

    Args:
        rebuild: Whether to use the cache

    Returns:
        The option info

    """
    if not rebuild:
        try:
            return load(list[FFMpegOption], "options")
        except Exception as e:
            logging.error(f"Failed to load options from cache: {e}")

    options = [
        FFMpegOption(
            name=i.name,
            type=FFMpegOptionType(i.type.value),
            flags=i.flags,
            help=i.help,
        )
        for i in parse_c.cli.parse_ffmpeg_options()
    ]
    save(options, "options")
    return options


def load_av_option_set(rebuild: bool) -> list[FFMpegAVOption]:
    """
    Load AV options from the output path.

    Args:
        rebuild: Whether to use the cache

    Returns:
        The options

    """
    if not rebuild:
        try:
            return load(list[FFMpegAVOption], "av_option_sets")
        except Exception as e:
            logging.error(f"Failed to load options from cache: {e}")

    options = parse_help.cli.all_av_option_sets()
    output: list[FFMpegAVOption] = []
    for option in options:
        _option = FFMpegAVOption(
            section=option.section,
            name=option.name,
            type=str(option.type),
            flags=str(option.flags),
            help=option.help,
            min=None,
            max=None,
            default=None,
            choices=tuple(
                FFMpegOptionChoice(
                    name=choice.name,
                    help=choice.help,
                    flags=choice.flags,
                    value=choice.value,
                )
                for choice in option.choices
            ),
        )
        output.append(_option)

    save(output, "av_option_sets")
    return output


def load_filters(rebuild: bool) -> list[FFMpegFilter]:
    """
    Load filters from the output path.

    Args:
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
    for f in sorted(parse_help.cli.all_filters(), key=lambda i: i.name):
        if f.name == "afir":
            continue

        # Convert parse_help filter to main filter schema
        converted_filter = FFMpegFilter(
            name=f.name,
            description=f.help,
            # flags
            is_support_timeline=f.is_timeline,
            is_support_slice_threading=f.is_slice_threading,
            is_support_command=False,
            # NOTE: is_support_framesync can only be determined by filter_info_from_help
            is_support_framesync=f.is_framesync,
            is_filter_sink=f.io_flags.endswith("->|"),
            is_filter_source=f.io_flags.startswith("|->"),
            # IO Typing
            is_dynamic_input="N->" in f.io_flags,
            is_dynamic_output="->N" in f.io_flags,
            # stream_typings's name can only be determined by filter_info_from_help
            stream_typings_input=tuple(
                FFMpegIOType(name=i.name, type=StreamType(i.type))
                for i in f.stream_typings_input
            ),
            stream_typings_output=tuple(
                FFMpegIOType(name=i.name, type=StreamType(i.type))
                for i in f.stream_typings_output
            ),
            options=tuple(
                FFMpegFilterOption(
                    name=option.name,
                    type=FFMpegFilterOptionType(option.type),
                    default=option.default,
                    description=option.help,
                    choices=tuple(
                        FFMpegFilterOptionChoice(
                            name=choice.name,
                            help=choice.help,
                            flags=choice.flags,
                            value=choice.value,
                        )
                        for choice in option.choices
                    ),
                )
                for option in f.options
            ),
        )

        manual_config = manual.cli.load_config(converted_filter.name)
        if manual_config:
            converted_filter = replace(converted_filter, **asdict(manual_config))

        try:
            filter_info = gen_filter_info(converted_filter)
            save(filter_info, filter_info.name)
            ffmpeg_filters.append(filter_info)
        except ValueError:
            print(f"Failed to generate filter info for {converted_filter.name}")

    save(ffmpeg_filters, "filters")

    return ffmpeg_filters


def load_codecs(rebuild: bool) -> list[FFMpegCodec]:
    """
    Load codecs from the output path.

    Args:
        rebuild: Whether to use the cache

    Returns:
        The codecs

    Raises:
        ValueError: If a codec is invalid.

    """
    if not rebuild:
        try:
            return load(list[FFMpegCodec], "codecs")
        except Exception as e:
            logging.error(f"Failed to load codecs from cache: {e}")

    codecs: list[FFMpegCodec] = []
    for k in parse_help.cli.all_codecs():
        cls: type[FFMpegDecoder] | type[FFMpegEncoder]
        if k.is_encoder:
            cls = FFMpegEncoder
        elif k.is_decoder:
            cls = FFMpegDecoder
        else:
            raise ValueError(f"Invalid codec: {k.name}")

        codecs.append(
            cls(
                name=k.name,
                flags=k.flags,
                description=k.help,
                options=tuple(
                    FFMpegAVOption(
                        section=i.section,
                        name=i.name,
                        type=str(i.type),
                        flags=str(i.flags),
                        help=i.help,
                        min=i.min,
                        max=i.max,
                        default=i.default,
                        choices=tuple(
                            FFMpegOptionChoice(
                                name=choice.name,
                                help=choice.help,
                                flags=choice.flags,
                                value=choice.value,
                            )
                            for choice in i.choices
                        ),
                    )
                    for i in k.options
                ),
            )
        )

    save(codecs, "codecs")
    return codecs


def load_formats(rebuild: bool) -> list[FFMpegFormat]:
    """
    Load muxers from the output path.

    Args:
        rebuild: Whether to use the cache

    Returns:
        The muxers

    Raises:
        ValueError: If a format is invalid.

    """
    if not rebuild:
        try:
            return load(list[FFMpegFormat], "formats")
        except Exception as e:
            logging.error(f"Failed to load muxers from cache: {e}")

    formats: list[FFMpegFormat] = []
    for k in parse_help.cli.all_formats():
        cls: type[FFMpegDemuxer] | type[FFMpegMuxer]
        if k.is_muxer:
            cls = FFMpegMuxer
        elif k.is_demuxer:
            cls = FFMpegDemuxer
        else:
            raise ValueError(f"Invalid format: {k.name}")

        formats.append(
            cls(
                name=k.name,
                flags=k.flags,
                description=k.help,
                options=tuple(
                    FFMpegAVOption(
                        section=i.section,
                        name=i.name,
                        type=str(i.type),
                        flags=str(i.flags),
                        help=i.help,
                        min=i.min,
                        max=i.max,
                        default=i.default,
                        choices=tuple(
                            FFMpegOptionChoice(
                                name=choice.name,
                                help=choice.help,
                                flags=choice.flags,
                                value=choice.value,
                            )
                            for choice in i.choices
                        ),
                    )
                    for i in k.options
                ),
            )
        )

    save(formats, "formats")
    return formats


@app.command()
def generate(outpath: Path | None = None, rebuild: bool = False) -> None:
    """
    Generate filter and option documents.

    Args:
        outpath: The output path
        rebuild: Whether to rebuild the filters and options from scratch, ignoring the cache

    """
    if not outpath:
        outpath = Path(__file__).parent.parent.parent / "ffmpeg"

    ffmpeg_filters = load_filters(rebuild)
    ffmpeg_options = load_options(rebuild)
    ffmpeg_codecs = load_codecs(rebuild)
    ffmpeg_muxers = load_formats(rebuild)
    ffmpeg_av_option_set = load_av_option_set(rebuild)

    render(
        filters=ffmpeg_filters,
        options=ffmpeg_options,
        codecs=ffmpeg_codecs,
        muxers=ffmpeg_muxers,
        av_option_sets=ffmpeg_av_option_set,
        outpath=outpath,
    )
    os.system("pre-commit run -a")


if __name__ == "__main__":
    app()
