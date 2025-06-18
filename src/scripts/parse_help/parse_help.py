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
from .utils import parse_section_tree, run_ffmpeg_command

re_option_pattern = re.compile(
    r"(?P<name>[\-\w]+)\s+\<(?P<type>[\w]+)\>\s+(?P<flags>[\w\.]{11})\s*(?P<help>.*)?"
)
re_choice_pattern = re.compile(
    r"^(?P<name>(?:(?!  ).)+)\s+(?P<value>[\d\-]+)?\s+(?P<flags>[\w\.]{11})(?P<help>\s+.*)?"
)


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
            # FFMpeg's general options
            for option in tree[section]:
                assert not tree[section][option], (
                    f"General options should not have choice: {section}.{option}"
                )
                parts = option.split("  ")
                if " " in parts[0].strip():
                    name, argname = parts[0].strip().split(" ", 1)
                else:
                    name = parts[0].strip()
                    argname = None

                help = parts[-1].strip()

                output.append(
                    FFMpegOption(
                        section=section,
                        name=name.strip("-"),
                        argname=argname,
                        help=help,
                    )
                )
        elif "AVOptions" in section:
            # FFmpeg's AVOptions
            for option in tree[section]:
                choices: list[FFMpegOptionChoice] = []
                for choice in tree[section][option]:
                    match = re_choice_pattern.match(choice)
                    assert match, f"No choice found in line: {choice}"

                    choices.append(
                        FFMpegOptionChoice(
                            name=match.group("name").strip("-"),
                            value=match.group("value"),
                            flags=match.group("flags"),
                            help=match.group("help"),
                        )
                    )

                match = re_option_pattern.match(option)
                assert match, f"No option found in line: {option}"
                output.append(
                    FFMpegAVOption(
                        section=section,
                        name=match.group("name").strip("-"),
                        type=FFMpegOptionType(match.group("type")),
                        flags=match.group("flags"),
                        help=match.group("help"),
                        choices=tuple(choices),
                    )
                )

    return output


def extract_options_from_help() -> list[FFMpegOption]:
    """
    Extract all options from ffmpeg help text.

    Returns:
        A list of FFMpegOption objects
    """
    text = run_ffmpeg_command(["-h", "full"])
    return parse(text)
