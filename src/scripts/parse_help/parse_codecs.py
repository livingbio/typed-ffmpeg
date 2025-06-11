import re
import subprocess
from typing import TypeVar

from .schema import FFMpegDecoder, FFMpegEncoder

T = TypeVar("T", FFMpegEncoder, FFMpegDecoder)


def extract_help_text(command: str) -> str:
    """
    Get the help text for encoders or decoders.

    Args:
        command (str): The ffmpeg command to run ('-encoders' or '-decoders')

    Returns:
        str: The raw help text output from ffmpeg command
    """
    result = subprocess.run(
        ["ffmpeg", command, "-hide_banner"],
        stdout=subprocess.PIPE,
        text=True,
    )
    return result.stdout


def parse_help_text(text: str, codec_class: type[T]) -> list[T]:
    """
    Parse the help text for encoders or decoders.

    Args:
        text (str): The help text to parse from ffmpeg command output
        codec_class (Type[T]): The class to instantiate (FFMpegEncoder or FFMpegDecoder)

    Returns:
        list[T]: A list of codec instances (either FFMpegEncoder or FFMpegDecoder objects)
    """
    output: list[T] = []
    lines = text.splitlines()
    re_pattern = re.compile(r"^\s*([\w\.]{6})\s(\w+)\s+(.*)$")

    for line in lines:
        match = re_pattern.findall(line)
        if match:
            flags, name, description = match[0]
            output.append(codec_class(name=name, flags=flags, description=description))
    return output


def extract_encoders_help_text() -> str:
    """
    Get the help text for encoders.

    Returns:
        str: The raw help text output from ffmpeg -encoders command
    """
    return extract_help_text("-encoders")


def parse_encoders_help_text(text: str) -> list[FFMpegEncoder]:
    """
    Parse the help text for encoders.

    Args:
        text (str): The help text to parse from ffmpeg -encoders command output

    Returns:
        list[FFMpegEncoder]: A list of FFMpegEncoder instances
    """
    return parse_help_text(text, FFMpegEncoder)


def extract_decoders_help_text() -> str:
    """
    Get the help text for decoders.

    Returns:
        str: The raw help text output from ffmpeg -decoders command
    """
    return extract_help_text("-decoders")


def parse_decoders_help_text(text: str) -> list[FFMpegDecoder]:
    """
    Parse the help text for decoders.

    Args:
        text (str): The help text to parse from ffmpeg -decoders command output

    Returns:
        list[FFMpegDecoder]: A list of FFMpegDecoder instances
    """
    return parse_help_text(text, FFMpegDecoder)
