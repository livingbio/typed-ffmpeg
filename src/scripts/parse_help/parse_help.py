"""
A module for parsing FFmpeg help text output into structured option data.

This module processes the output of commands like `ffmpeg -h full` or `ffmpeg -h filter=scale`
into a structured format. It handles both general FFmpeg options and AVOptions.

The parsing process follows these steps:
1. The help text is parsed into a hierarchical tree structure
2. The tree is then traversed to extract individual options
3. Options are converted into strongly-typed FFMpegOption objects
"""

import re

from .schema import FFMpegAVOption, FFMpegOption, FFMpegOptionChoice, FFMpegOptionType
from .utils import parse_general_option, parse_section_tree, run_ffmpeg_command, parse_av_option



def parse(help_text: str) -> list[FFMpegOption]:
    """
    Parse FFmpeg help text into a structured list of options.

    Processes both general FFmpeg options and AVOptions from the help text.
    The function handles complex option hierarchies, including nested flags
    and their associated values.

    Example input:
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
    Extract and parse all options from FFmpeg's full help output.
    
    Executes `ffmpeg -h full` and processes its output to create a comprehensive
    list of all available FFmpeg options, including both general options and AVOptions.
    """
    text = run_ffmpeg_command(["-h", "full"])
    return parse(text)
