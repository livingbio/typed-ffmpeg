import re
from typing import Literal

from .schema import FFMpegAVOption, FFMpegDemuxer, FFMpegFormat, FFMpegMuxer
from .utils import parse_all_options, run_ffmpeg_command


def parse_help_text(text: str) -> list[FFMpegFormat]:
    """
    Parse the help text for encoders or decoders.

    Args:
        text: The help text to parse from ffmpeg command output

    Returns:
        A list of codec instances (either FFMpegEncoder or FFMpegDecoder objects)
    """
    output: list[FFMpegFormat] = []
    lines = text.splitlines()
    re_pattern = re.compile(r"^\s*([\w\.\s]{2})\s(\w+)\s+(.*)$")

    for line in lines:
        match = re_pattern.findall(line)
        if match:
            flags, name, description = match[0]
            output.append(FFMpegFormat(name=name, flags=flags, help=description))
    return output


def extract_format_help_text(
    type: Literal["muxers", "demuxers", "formats"],
) -> list[FFMpegFormat]:
    """
    Get the help text for all codecs.

    Args:
        type: The type of codec

    Returns:
        A list of codecs
    """
    return parse_help_text(run_ffmpeg_command([f"-{type}"]))


def extract_format_option(
    codec: str, type: Literal["muxer", "demuxer"]
) -> list[FFMpegAVOption]:
    """
    Get the help text for a codec option.

    Args:
        codec: The codec name
        type: The type of codec

    Returns:
        A list of codec options
    """
    codec_options = parse_all_options(run_ffmpeg_command(["-h", f"{type}={codec}"]))
    # NOTE: some filter help text contains duplicate options, so we need to remove them (e.g. encoder=h264_nvenc)
    passed_options = set()
    output = []
    for option in codec_options:
        if option.name in passed_options:
            continue
        passed_options.add(option.name)
        output.append(option)
    return output


def extract_all_formats() -> list[FFMpegFormat]:
    """
    Extract all formats.

    Returns:
        A list of formats
    """
    output: list[FFMpegFormat] = []

    for codec in extract_format_help_text("muxers"):
        options = extract_format_option(codec.name, "muxer")
        output.append(
            FFMpegMuxer(
                name=codec.name,
                flags=codec.flags,
                help=codec.help,
                options=tuple(options),
            )
        )

    for codec in extract_format_help_text("demuxers"):
        options = extract_format_option(codec.name, "demuxer")
        output.append(
            FFMpegDemuxer(
                name=codec.name,
                flags=codec.flags,
                help=codec.help,
                options=tuple(options),
            )
        )

    return output
