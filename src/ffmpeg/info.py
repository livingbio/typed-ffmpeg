"""
Module for querying FFmpeg codec and encoder information.

This module provides functionality to query the available FFmpeg codecs,
decoders, and encoders on the system. It parses the output of FFmpeg's
command-line tools to extract information about supported formats and
capabilities.
"""

import logging
import subprocess
from dataclasses import dataclass
from enum import Flag, auto

from .exceptions import FFMpegExecuteError
from .utils.run import command_line

logger = logging.getLogger(__name__)


class CodecFlags(Flag):
    """
    Flag enumeration representing the capabilities of a codec.

    These flags correspond to the character flags in FFmpeg's codec information
    output and indicate what features a codec supports.
    """

    video = auto()  # Codec supports video encoding/decoding
    audio = auto()  # Codec supports audio encoding/decoding
    subtitle = auto()  # Codec supports subtitle processing
    frame_level_multithreading = auto()  # Codec supports frame-level multithreading
    slice_level_multithreading = auto()  # Codec supports slice-level multithreading
    experimental = auto()  # Codec is considered experimental
    draw_horiz_band = auto()  # Codec supports drawing horizontal bands
    direct_rendering_method_1 = auto()  # Codec supports direct rendering method 1


@dataclass(frozen=True)
class Codec:
    """
    Represents an FFmpeg codec with its capabilities and description.

    This immutable dataclass stores information about a codec identified by the
    `ffmpeg -codecs` command, including its name, supported features (as flags),
    and its textual description.

    Attributes:
        name: The codec identifier used in FFmpeg commands
        flags: Bitmap of capabilities supported by the codec
        description: Human-readable description of the codec
    """

    name: str
    flags: CodecFlags
    description: str


def parse_codec_flags(flags: str) -> CodecFlags:
    """
    Parse the FFmpeg codec flags string into a CodecFlags enum.

    This function interprets the character flags from FFmpeg's codec listing
    and converts them to the corresponding CodecFlags enum values.

    Args:
        flags: A string of flag characters from FFmpeg codec information

    Returns:
        A CodecFlags bitmap with the appropriate flags set
    """
    flags_enum = CodecFlags(0)
    if flags[0] == "V":
        flags_enum |= CodecFlags.video
    if flags[0] == "A":
        flags_enum |= CodecFlags.audio
    if flags[0] == "S":
        flags_enum |= CodecFlags.subtitle
    if flags[1] == "F":
        flags_enum |= CodecFlags.frame_level_multithreading
    if flags[2] == "S":
        flags_enum |= CodecFlags.slice_level_multithreading
    if flags[3] == "X":
        flags_enum |= CodecFlags.experimental
    if flags[4] == "B":
        flags_enum |= CodecFlags.draw_horiz_band
    if flags[5] == "D":
        flags_enum |= CodecFlags.direct_rendering_method_1
    return flags_enum


def get_codecs() -> tuple[Codec, ...]:
    """
    Query the system for all available FFmpeg codecs.

    This function calls `ffmpeg -codecs` and parses the output to create
    a tuple of Codec objects representing all codecs available on the system.

    Returns:
        A tuple of Codec objects with information about each codec

    Raises:
        FFMpegExecuteError: If the ffmpeg command fails
    """
    args = ["ffmpeg", "-hide_banner", "-codecs"]
    logger.info("Running ffmpeg command: %s", command_line(args))
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    retcode = p.poll()
    if p.returncode != 0:
        raise FFMpegExecuteError(
            retcode=retcode, cmd=command_line(args), stdout=out, stderr=err
        )

    codecs = out.decode("utf-8")
    codecs_lines = codecs.strip().split("\n")
    # Skip header lines until we find the separator
    for i, line in enumerate(codecs_lines):
        if line.startswith(" ------"):
            codecs_lines = codecs_lines[i + 1 :]
            break
    return tuple(
        Codec(
            name=parts[1],
            flags=parse_codec_flags(parts[0]),
            description=parts[2],
        )
        for line in codecs_lines
        for parts in [line.split(None, 3)]
    )


class CoderFlags(Flag):
    """
    Flag enumeration representing the capabilities of a coder (encoder/decoder).

    These flags correspond to the character flags in FFmpeg's encoder/decoder
    information output and indicate what features a coder supports.
    """

    video = auto()  # Coder supports video processing
    audio = auto()  # Coder supports audio processing
    subtitle = auto()  # Coder supports subtitle processing
    frame_level_multithreading = auto()  # Coder supports frame-level multithreading
    slice_level_multithreading = auto()  # Coder supports slice-level multithreading
    experimental = auto()  # Coder is considered experimental
    draw_horiz_band = auto()  # Coder supports drawing horizontal bands
    direct_rendering_method_1 = auto()  # Coder supports direct rendering method 1


def parse_coder_flags(flags: str) -> CoderFlags:
    """
    Parse the FFmpeg coder flags string into a CoderFlags enum.

    This function interprets the character flags from FFmpeg's encoder/decoder
    listing and converts them to the corresponding CoderFlags enum values.

    Args:
        flags: A string of flag characters from FFmpeg encoder/decoder information

    Returns:
        A CoderFlags bitmap with the appropriate flags set
    """
    flags_enum = CoderFlags(0)
    if flags[0] == "V":
        flags_enum |= CoderFlags.video
    if flags[0] == "A":
        flags_enum |= CoderFlags.audio
    if flags[0] == "S":
        flags_enum |= CoderFlags.subtitle
    if flags[1] == "F":
        flags_enum |= CoderFlags.frame_level_multithreading
    if flags[2] == "S":
        flags_enum |= CoderFlags.slice_level_multithreading
    if flags[3] == "X":
        flags_enum |= CoderFlags.experimental
    if flags[4] == "B":
        flags_enum |= CoderFlags.draw_horiz_band
    if flags[5] == "D":
        flags_enum |= CoderFlags.direct_rendering_method_1
    return flags_enum


@dataclass
class Coder:
    """
    Represents an FFmpeg encoder or decoder with its capabilities and description.

    This dataclass stores information about a coder identified by the
    `ffmpeg -encoders` or `ffmpeg -decoders` command, including its name,
    supported features (as flags), and its textual description.

    Attributes:
        name: The coder identifier used in FFmpeg commands
        flags: Bitmap of capabilities supported by the coder
        description: Human-readable description of the coder
    """

    name: str
    flags: CoderFlags
    description: str


def get_coders(codes: str) -> tuple[Coder, ...]:
    """
    Parse the output of an FFmpeg encoder/decoder listing into Coder objects.

    This function parses the text output from `ffmpeg -encoders` or
    `ffmpeg -decoders` commands and constructs Coder objects for each entry.

    Args:
        codes: String output from the FFmpeg encoders/decoders command

    Returns:
        A tuple of Coder objects representing the available encoders/decoders
    """
    codecs_lines = codes.strip().split("\n")
    # Skip header lines until we find the separator
    for i, line in enumerate(codecs_lines):
        if line.startswith(" ------"):
            codecs_lines = codecs_lines[i + 1 :]
            break
    return tuple(
        Coder(
            name=parts[1],
            flags=parse_coder_flags(parts[0]),
            description=parts[2],
        )
        for line in codecs_lines
        for parts in [line.split(None, 3)]
    )


def get_decoders() -> tuple[Coder, ...]:
    """
    Query the system for all available FFmpeg decoders.

    This function calls `ffmpeg -decoders` and parses the output to create
    a tuple of Coder objects representing all decoders available on the system.

    Returns:
        A tuple of Coder objects with information about each decoder

    Raises:
        FFMpegExecuteError: If the ffmpeg command fails
    """
    args = ["ffmpeg", "-hide_banner", "-decoders"]
    logger.info("Running ffmpeg command: %s", command_line(args))
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    retcode = p.poll()
    if p.returncode != 0:
        raise FFMpegExecuteError(
            retcode=retcode, cmd=command_line(args), stdout=out, stderr=err
        )

    decoders = out.decode("utf-8")
    return get_coders(decoders)


def get_encoders() -> tuple[Coder, ...]:
    """
    Query the system for all available FFmpeg encoders.

    This function calls `ffmpeg -encoders` and parses the output to create
    a tuple of Coder objects representing all encoders available on the system.

    Returns:
        A tuple of Coder objects with information about each encoder

    Raises:
        FFMpegExecuteError: If the ffmpeg command fails
    """
    args = ["ffmpeg", "-hide_banner", "-encoders"]
    logger.info("Running ffmpeg command: %s", command_line(args))
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    retcode = p.poll()
    if p.returncode != 0:
        raise FFMpegExecuteError(
            retcode=retcode, cmd=command_line(args), stdout=out, stderr=err
        )

    encoders = out.decode("utf-8")
    return get_coders(encoders)
