import re
import subprocess
from typing import Literal

from .parse_all_options import parse_all_options
from .schema import FFMpegAVOption, FFMpegCodec, FFMpegDecoder, FFMpegEncoder


def extract_help_text(*command: str) -> str:
    """
    Get the help text for encoders or decoders.

    Args:
        command: The ffmpeg command to run ('-encoders' or '-decoders')

    Returns:
        The raw help text output from ffmpeg command
    """
    result = subprocess.run(
        ["ffmpeg", *command, "-hide_banner"],
        stdout=subprocess.PIPE,
        text=True,
    )
    return result.stdout


def parse_help_text(text: str) -> list[FFMpegCodec]:
    """
    Parse the help text for encoders or decoders.

    Args:
        text: The help text to parse from ffmpeg command output

    Returns:
        A list of codec instances (either FFMpegEncoder or FFMpegDecoder objects)
    """
    output: list[FFMpegCodec] = []
    lines = text.splitlines()
    re_pattern = re.compile(r"^\s*([\w\.]{6})\s(\w+)\s+(.*)$")

    for line in lines:
        match = re_pattern.findall(line)
        if match:
            flags, name, description = match[0]
            output.append(FFMpegCodec(name=name, flags=flags, description=description))
    return output


def extract_codecs_help_text(
    type: Literal["encoders", "decoders", "codecs"],
) -> list[FFMpegCodec]:
    """
    Get the help text for all codecs.

    Args:
        type: The type of codec

    Returns:
        A list of codecs
    """
    return parse_help_text(extract_help_text(f"-{type}"))


def extract_codec_option(
    codec: str, type: Literal["encoder", "decoder"]
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


def extract_all_codecs() -> list[FFMpegCodec]:
    output: list[FFMpegCodec] = []

    for codec in extract_codecs_help_text("encoders"):
        options = extract_codec_option(codec.name, "encoder")
        output.append(
            FFMpegEncoder(
                name=codec.name,
                flags=codec.flags,
                description=codec.description,
                options=tuple(options),
            )
        )

    for codec in extract_codecs_help_text("decoders"):
        options = extract_codec_option(codec.name, "decoder")
        output.append(
            FFMpegDecoder(
                name=codec.name,
                flags=codec.flags,
                description=codec.description,
                options=tuple(options),
            )
        )

    return output
