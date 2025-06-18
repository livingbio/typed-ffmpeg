"""
This module is used to parse the help text of FFmpeg. 

ffmpeg -h full or ffmpeg -h filter=scale

The help text is parsed into a tree structure, and then the tree structure is parsed into a list of FFMpegAVOption objects.

The tree structure is parsed into a list of FFMpegAVOption objects by the following steps:

1. Parse the help text into a tree structure.
2. Parse the tree structure into a list of FFMpegAVOption objects.
"""

import re

from .utils import run_ffmpeg_command, parse_section_tree
from .schema import FFMpegAVOption, FFMpegOptionChoice


def parse(help_text: str) -> dict[str, list[str]]:
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
        A list of FFMpegAVOption objects
    """
    return parse_section_tree(help_text)
    output: list[FFMpegAVOption] = []
    section = None
    last_option: FFMpegAVOption | None = None
    choices: list[FFMpegOptionChoice] = []

    re_option_pattern = re.compile(
        r"(?P<short_name>[\w\-\.\+]+)\s+\<(?P<type>[\w]+)\>\s+(?P<flags>[\w\.]{11})\s*(?P<help>.*)?"
    )
    re_choice_pattern = re.compile(
        r"(?P<short_name>[\w\-\.\+]+)\s+(?P<flags>[\w\.]{11})\s*(?P<help>.*)?"
    )
    re_value_pattern = re.compile(
        r"(?P<short_name>[\w\-\.\+]+)\s+(?P<value>[\w\-]+)\s+(?P<flags>[\w\.]{11})\s*(?P<help>.*)?"
    )

    for line in help_text.split("\n"):
        # Empty line
        if not line.strip():
            if last_option:
                output.append(
                    FFMpegAVOption(
                        section=last_option.section,
                        name=last_option.name.strip().strip("-"),
                        type=last_option.type,
                        flags=last_option.flags,
                        help=last_option.help,
                        choices=tuple(choices),
                    )
                )
                last_option = None
                choices = []
            continue

        # AVOptions section
        if re.findall(r"^[\w\.\s\/]+[\s]+AVOptions:", line):
            section = line
            continue

        if not section:
            continue

        # Choice line
        if line.startswith("     "):
            assert last_option
            if last_option.type == "flags":
                choice = re_choice_pattern.findall(line)
                assert choice, f"No choice found in line: {line}"
                name, flags, help = choice[0]
                choices.append(
                    FFMpegOptionChoice(
                        name=name.strip(),
                        flags=flags,
                        help=help,
                        value=name.strip(),
                    )
                )
            elif last_option.type == "string":
                choice = re_choice_pattern.findall(line)
                assert choice, f"No choice found in line: {line}"
                name, flags, help = choice[0]
                choices.append(
                    FFMpegOptionChoice(
                        name=name.strip(),
                        flags=flags,
                        help=help,
                        value=name.strip(),
                    )
                )
            else:
                v = re_value_pattern.findall(line)
                assert v, f"No value found in line: {line}"
                name, value, flags, help = v[0]
                choices.append(
                    FFMpegOptionChoice(
                        name=name.strip(),
                        flags=flags,
                        value=value,
                        help=help,
                    )
                )

            continue

        # Option line
        if line.startswith("  ") and not line.startswith("   "):
            if last_option:
                output.append(
                    FFMpegAVOption(
                        section=last_option.section,
                        name=last_option.name.strip().strip("-"),
                        type=last_option.type,
                        flags=last_option.flags,
                        help=last_option.help,
                        choices=tuple(choices),
                    )
                )
            last_option = None
            choices = []

            p = re_option_pattern.findall(line)
            assert p, f"No option found in line: {line}"

            last_option = FFMpegAVOption(
                section=section,
                name=p[0][0].strip(),
                type=p[0][1],
                flags=p[0][2],
                help=p[0][3],
            )

    return output


def extract_options_from_help() -> list[FFMpegAVOption]:
    """
    Extract all AVOptions from ffmpeg help text.

    Returns:
        A list of FFMpegAVOption objects
    """
    text = run_ffmpeg_command(["-h", "full"])
    return parse(text)
