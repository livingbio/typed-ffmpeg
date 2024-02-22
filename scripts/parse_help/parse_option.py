import subprocess


def help_full_text() -> str:
    result = subprocess.run(["ffmpeg", "-h", "full", "-hide_banner"], stdout=subprocess.PIPE, text=True)
    return result.stdout
