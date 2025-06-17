import subprocess
from collections.abc import Sequence


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
