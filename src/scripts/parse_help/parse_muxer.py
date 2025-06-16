import re
from typing import Literal

from .parse_all_options import parse_all_options
from .parse_codecs import extract_help_text
from .schema import FFMpegAVOption, FFMpegDemuxer, FFMpegMuxer, FFMpegMuxerBase


def parse_help_text(text: str) -> list[FFMpegMuxerBase]:
    """
    Parse the help text for encoders or decoders.

    Args:
        text: The help text to parse from ffmpeg command output

    Returns:
        A list of codec instances (either FFMpegEncoder or FFMpegDecoder objects)
    """
    output: list[FFMpegMuxerBase] = []
    lines = text.splitlines()
    re_pattern = re.compile(r"^\s*([\w\.\s]{2})\s(\w+)\s+(.*)$")

    for line in lines:
        match = re_pattern.findall(line)
        if match:
            flags, name, description = match[0]
            output.append(
                FFMpegMuxerBase(name=name, flags=flags, description=description)
            )
    return output


def extract_muxer_help_text(
    type: Literal["muxers", "demuxers"],
) -> list[FFMpegMuxerBase]:
    """
    Get the help text for all codecs.

    Args:
        type: The type of codec

    Returns:
        A list of codecs
    """
    return parse_help_text(extract_help_text(f"-{type}"))


def extract_codec_option(
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
    codec_options = parse_all_options(extract_help_text("-h", f"{type}={codec}"))
    # NOTE: some filter help text contains duplicate options, so we need to remove them (e.g. encoder=h264_nvenc)
    passed_options = set()
    output = []
    for option in codec_options:
        if option.name in passed_options:
            continue
        passed_options.add(option.name)
        output.append(option)
    return output


def extract_all_muxers() -> list[FFMpegMuxerBase]:
    output: list[FFMpegMuxerBase] = []

    for codec in extract_muxer_help_text("muxers"):
        options = extract_codec_option(codec.name, "muxer")
        output.append(
            FFMpegMuxer(
                name=codec.name,
                flags=codec.flags,
                description=codec.description,
                options=tuple(options),
            )
        )

    for codec in extract_muxer_help_text("demuxers"):
        options = extract_codec_option(codec.name, "demuxer")
        output.append(
            FFMpegDemuxer(
                name=codec.name,
                flags=codec.flags,
                description=codec.description,
                options=tuple(options),
            )
        )

    return output
