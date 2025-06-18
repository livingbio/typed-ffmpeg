import subprocess
from collections import OrderedDict
from collections.abc import Sequence
from typing import Any


def run_ffmpeg_command(args: Sequence[str]) -> str:
    """
    Run an ffmpeg command and return its output.

    Args:
        args: The command line arguments to pass to ffmpeg (excluding 'ffmpeg' itself)

    Returns:
        The command output as a string
    """
    result = subprocess.run(
        ["ffmpeg", *args, "-hide_banner"],
        stdout=subprocess.PIPE,
        text=True,
    )
    return result.stdout


def _left_space(line: str) -> int:
    """
    Get the number of leading spaces in a string.

    Args:
        line: The string to check.

    Returns:
        The number of leading spaces.
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
    Parse the help text into a tree structure.

    Args:
        text: The help text.

    Returns:
        The tree structure.
    """
    output: OrderedDict[str, Any] = OrderedDict()
    paths: list[tuple[int, str]] = []

    for i, line in enumerate(text.split("\n")):
        indent = _left_space(line)
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
