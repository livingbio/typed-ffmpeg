import subprocess
from typing import Any


def help_full_text() -> str:
    result = subprocess.run(["ffmpeg", "-h", "full", "-hide_banner"], stdout=subprocess.PIPE, text=True)
    return result.stdout


def process() -> Any:
    text = help_full_text()

    # split the text into sections
    sections = [k.strip() for k in text.split("\n\n")]

    output = {}
    for section in sections:
        lines = section.split("\n")

        if not lines[0].endswith(":"):
            continue

        section_name = lines[0][:-1]
        output[section_name] = lines[1:]

    return output
