import re
import subprocess
from collections import OrderedDict
from collections.abc import Sequence
from typing import Any
from .schema import FFMpegAVOption, FFMpegOption, FFMpegOptionChoice, FFMpegOptionType

def run_ffmpeg_command(args: Sequence[str]) -> str:
    """
    Execute an ffmpeg command with the provided arguments and return its standard output as a string.

    Args:
        args: The command line arguments to pass to ffmpeg (excluding the 'ffmpeg' executable itself).

    Returns:
        The standard output produced by the ffmpeg command.

    Example:
        >>> run_ffmpeg_command(["-version"])
        'ffmpeg version ...'
    """
    result = subprocess.run(
        ["ffmpeg", *args, "-hide_banner"],
        stdout=subprocess.PIPE,
        text=True,
    )
    return result.stdout


def _count_indent(line: str) -> int:
    """
    Calculate the number of leading spaces in a string, with special handling for lines starting with '-'.

    Args:
        line: The string to analyze.

    Returns:
        The number of leading spaces, or the index after '-' if the first non-space character is '-'.

    Example:
        >>> _left_space('    -foo')
        5
        >>> _left_space('  bar')
        2
    """
    for i in range(len(line)):
        if line[i] != " ":
            if line[i] == "-":
                return i + 1
            else:
                return i

    return len(line)


def parse_section_tree(text: str) -> dict[str, dict[str, dict[str, None]]]:
    """
    Parse indented help text into a nested tree structure, preserving section hierarchy.

    Args:
        text: The help text to parse, typically from ffmpeg's help output.

    Returns:
        A nested ordered dictionary representing the section hierarchy, where each key is a section or option name.

    Example:
        Input text:
            Section1
              Option1
                SubOption1
            Section2
              Option2
        Output:
            OrderedDict({
                'Section1': OrderedDict({
                    'Option1': OrderedDict({
                        'SubOption1': OrderedDict()
                    })
                }),
                'Section2': OrderedDict({
                    'Option2': OrderedDict()
                })
            })
    """
    output: OrderedDict[str, Any] = OrderedDict()
    paths: list[tuple[int, str]] = []

    for i, line in enumerate(text.split("\n")):
        indent = _count_indent(line)
        if not line.strip():
            continue
        paths = [k for k in paths if k[0] < indent]

        line = line.strip()

        insert_node = output
        for p in paths:
            if p[1] not in insert_node:
                insert_node[p[1]] = OrderedDict()

            insert_node = insert_node[p[1]]

        insert_node[line] = OrderedDict()
        paths.append((indent, line))

    return output

re_choice_pattern = re.compile(
    r"^(?P<name>(?:(?!  ).)+)\s+(?P<value>[\d\-]+)?\s+(?P<flags>[\w\.]{11})(?P<help>\s+.*)?"
)
re_option_pattern = re.compile(
    r"(?P<name>[\-\w]+)\s+\<(?P<type>[\w]+)\>\s+(?P<flags>[\w\.]{11})\s*(?P<help>.*)?"
)

def parse_av_option(section: str, tree: dict[str, dict[str, dict[str, None]]]) -> list[FFMpegAVOption]:
    """
    Parse a section of AVOptions from a tree structure into a list of FFMpegAVOption objects.

    Args:
        section: The section name to parse (e.g., 'AVOptions').
        tree: The tree structure as produced by parse_section_tree().

    Returns:
        A list of FFMpegAVOption objects, each representing an option with its possible choices.

    Raises:
        AssertionError: If the expected option or choice format is not matched.
    """
    output: list[FFMpegAVOption] = []
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
        output.append(FFMpegAVOption(
                section=section,
                name=match.group("name").strip("-"),
                type=FFMpegOptionType(match.group("type")),
                flags=match.group("flags"),
                help=match.group("help"),
                choices=tuple(choices),
            )
        )
    return output

def parse_general_option(section: str, tree: dict[str, dict[str, dict[str, None]]]) -> list[FFMpegOption]:
    """
    Parse a section of general options from a tree structure into a list of FFMpegOption objects.

    Args:
        section: The section name to parse (e.g., 'Main options').
        tree: The tree structure as produced by parse_section_tree().

    Returns:
        A list of FFMpegOption objects, each representing a general ffmpeg option.

    Raises:
        AssertionError: If a general option is found to have choices (which is not expected).
    """
    output: list[FFMpegOption] = []
    
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
    return output