import re
import subprocess
from collections import defaultdict


def help_text(filter_name: str) -> str:
    result = subprocess.run(
        ["ffmpeg", "-h", f"filter={filter_name}", "-hide_banner"], stdout=subprocess.PIPE, text=True
    )
    return result.stdout


def _left_space(line: str) -> int:
    for i in range(len(line)):
        if line[i] != " ":
            return i

    return len(line)


def parse_section_tree(text: str) -> dict[str, list[str]]:
    output: dict[str, list[str]] = defaultdict(list)
    paths: list[tuple[int, str]] = []

    for line in text.split("\n"):
        indent = _left_space(line)
        if not line.strip():
            continue
        paths = [k for k in paths if k[0] < indent]

        if paths:
            parent = paths[-1][1]
        else:
            parent = ""

        line = line.strip()
        output[parent].append(line)
        paths.append((indent, line))

    return output


def extract_help_text(filter_name: str):
    text = help_text(filter_name)

    p = re.compile(
        r"Filter (?P<name>[\w]+)\n"
        r"\s*(?P<description>[\w\s]+)\n"
        r"\s*(?P<is_slice>slice threading supported\n)?"
        r"\s*Inputs:"
    )

    return p.findall(text)
