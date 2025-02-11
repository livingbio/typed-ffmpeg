import logging
import subprocess
from dataclasses import dataclass
from enum import Flag, auto

from .exceptions import FFMpegExecuteError
from .utils.run import command_line

logger = logging.getLogger(__name__)


class CodecFlags(Flag):
    video = auto()
    audio = auto()
    subtitle = auto()
    frame_level_multithreading = auto()
    slice_level_multithreading = auto()
    experimental = auto()
    draw_horiz_band = auto()
    direct_rendering_method_1 = auto()


@dataclass(frozen=True)
class Codec:
    name: str
    flags: CodecFlags
    description: str


def parse_codec_flags(flags: str) -> CodecFlags:
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
    video = auto()
    audio = auto()
    subtitle = auto()
    frame_level_multithreading = auto()
    slice_level_multithreading = auto()
    experimental = auto()
    draw_horiz_band = auto()
    direct_rendering_method_1 = auto()


def parse_coder_flags(flags: str) -> CoderFlags:
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
    name: str
    flags: CoderFlags
    description: str


def get_coders(codes: str) -> tuple[Coder, ...]:
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
