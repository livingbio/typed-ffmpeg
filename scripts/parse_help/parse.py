import subprocess


def help_text(filter_name: str) -> str:
    result = subprocess.run(
        ["ffmpeg", "-h", f"filter={filter_name}", "-hide_banner"], stdout=subprocess.PIPE, text=True
    )
    return result.stdout


def extract(text: str, key: str) -> str:
    ...


def extract_help_text(filter_name: str):
    text = help_text(filter_name)
    lines = text.split("\n")

    assert f"Filter {filter_name}" in lines[0]
    lines[1]

    "slice threading supported" in lines[2]
