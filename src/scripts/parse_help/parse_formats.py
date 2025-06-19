import re
from typing import Literal

from .schema import FFMpegAVOption, FFMpegDemuxer, FFMpegFormat, FFMpegMuxer
from .utils import parse_av_option, parse_section_tree, run_ffmpeg_command


def _parse_list(text: str) -> list[FFMpegFormat]:
    """
    Parse the help text for formats (muxers or demuxers).

    Args:
        text: The help text to parse from ffmpeg command output

    Returns:
        A list of format instances

    Example:
        ```
        File formats:
         D. = Demuxing supported
         .E = Muxing supported
         --
         D  3dostr          3DO STR
         E 3g2             3GP2 (3GPP2 file format)
         E 3gp             3GP (3GPP file format)
         D  4xm             4X Technologies
         E a64             a64 - video for Commodore 64
         D  aa              Audible AA format files
         D  aac             raw ADTS AAC (Advanced Audio Coding)
        ```
    """
    output: list[FFMpegFormat] = []
    lines = text.splitlines()
    re_pattern = re.compile(r"^\s*([\w]+)\s(\w+)\s+(.*)$")

    for line in lines:
        match = re_pattern.findall(line)
        if match:
            flags, name, description = match[0]
            output.append(FFMpegFormat(name=name, flags=flags, help=description))
    return output


def _extract_list(
    type: Literal["muxers", "demuxers", "formats"],
) -> list[FFMpegFormat]:
    """
    Get the help text for all formats.

    Args:
        type: The type of format

    Returns:
        A list of formats
    """
    return _parse_list(run_ffmpeg_command([f"-{type}"]))



def _parse_format(text: str) -> list[FFMpegAVOption]:
    """
    Parse the help text for a format option.

    Args:
        text: The help text to parse

    Returns:
        A list of format options

    Example:
        ```
        Muxer mp4 [MP4 (MPEG-4 Part 14)]:
        Common extensions: mp4.
        MIME type: video/mp4.
        Default video codec: h264.
        Default audio codec: aac.
        mp4 muxer AVOptions:
          -movflags         <flags>      E........... MOV muxer flags (default 0)
             rtphint                     E........... Add RTP hint tracks
             empty_moov                   E........... Make the initial moov atom empty
             separate_moof                E........... Write separate moof/mdat atoms for each track
             frag_keyframe                E........... Fragment at video keyframes
             frag_custom                  E........... Enable custom fragmenting
        ```
    """
    tree = parse_section_tree(text)
    for section in tree:
        if "AVOptions" in section:
            return parse_av_option(section, tree)
    return []

def _extract_format(
    format: str,
    type: Literal["muxer", "demuxer"],
) -> list[FFMpegAVOption]:
    """
    Get the help text for a format option.

    Args:
        format: The format name
        type: The type of format

    Returns:
        A list of format options
    """
    return _parse_format(run_ffmpeg_command([f"-{type}={format}"]))

def extract() -> list[FFMpegFormat]:
    """
    Extract all format information including muxers and demuxers with their options.

    Returns:
        A list of format instances (muxers and demuxers) with their associated options
    """
    output: list[FFMpegFormat] = []

    for codec in _extract_list("muxers"):
        options = _extract_format(codec.name, "muxer")
        output.append(
            FFMpegMuxer(
                name=codec.name,
                flags=codec.flags,
                help=codec.help,
                options=tuple(options),
            )
        )

    for codec in _extract_list("demuxers"):
        options = _extract_format(codec.name, "demuxer")
        output.append(
            FFMpegDemuxer(
                name=codec.name,
                flags=codec.flags,
                help=codec.help,
                options=tuple(options),
            )
        )

    return output
