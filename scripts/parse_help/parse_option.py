import subprocess
from typing import Any


def help_full_text() -> str:
    result = subprocess.run(["ffmpeg", "-h", "full", "-hide_banner"], stdout=subprocess.PIPE, text=True)
    return result.stdout


def process() -> Any:
    text = help_full_text()

    return [k.strip() for k in text.split("\n\n")]
