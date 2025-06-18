"""
This module is used to parse the help text of FFmpeg.

ffmpeg -h full or ffmpeg -h filter=scale

The help text is parsed into a tree structure, and then the tree structure is parsed into a list of FFMpegAVOption objects.

The tree structure is parsed into a list of FFMpegAVOption objects by the following steps:

1. Parse the help text into a tree structure.
2. Parse the tree structure into a list of FFMpegAVOption objects.
"""

import re

from .schema import FFMpegAVOption, FFMpegOption, FFMpegOptionChoice, FFMpegOptionType
from .utils import parse_general_option, parse_section_tree, run_ffmpeg_command, parse_av_option



def parse(help_text: str) -> list[FFMpegOption]:
    """
    Parse all options from ffmpeg help text.

    Example:
    ```
    AVOptions:
    -b                 <int64>      E..VA...... set bitrate (in bits/s) (from 0 to I64_MAX) (default 200000)
    -ab                <int64>      E...A...... set bitrate (in bits/s) (from 0 to INT_MAX) (default 128000)
    -bt                <int>        E..VA...... Set video bitrate tolerance (in bits/s). In 1-pass mode, bitrate tolerance specifies how far ratecontrol is willing to deviate from the target average bitrate value. This is not related to minimum/maximum bitrate. Lowering tolerance too much has an adverse effect on quality. (from 0 to INT_MAX) (default 4000000)
    -flags             <flags>      ED.VAS..... (default 0)
       flush_packets                E.......... reduce the latency by flushing out packets immediately
       ignidx                       .D......... ignore index
       genpts                       .D......... generate pts
    ```

    Args:
        help_text: The help text to parse

    Returns:
        A list of FFMpegOption objects
    """
    tree = parse_section_tree(help_text)
    output: list[FFMpegOption] = []

    for section in tree:
        if "options" in section:
            output.extend(parse_general_option(section, tree))
        elif "AVOptions" in section:
            # FFmpeg's AVOptions
            output.extend(parse_av_option(section, tree))
         

    return output


def extract_options_from_help() -> list[FFMpegOption]:
    """
    Extract all options from ffmpeg help text.

    Returns:
        A list of FFMpegOption objects
    """
    text = run_ffmpeg_command(["-h", "full"])
    return parse(text)
