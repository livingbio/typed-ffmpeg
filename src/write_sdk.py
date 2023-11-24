import os
import pathlib
import re

from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables from .env file
load_dotenv(override=True)


def extract_python_code(body: str) -> str:
    re_python = re.compile(r"```(.*)```", re.DOTALL | re.MULTILINE)

    match = re_python.findall(body)
    if match:
        if match[0].strip().startswith("python"):
            return match[0].strip()[6:]
        return match[0]

    return body


def process_document(path: pathlib.Path) -> None:
    client = AzureOpenAI(azure_deployment="gpt35")

    SYSTEM_PROMPT = {
        "role": "system",
        "content": f"""
- You are a python and ffmpeg expert
- please write a python wrapper for following ffmpeg filter document with typing
- only return python code
""",
    }

    SAMPLE_PROMPTS = []

    for sample in pathlib.Path("./samples").iterdir():
        sample_input = sample / "input.html"
        sample_output = sample / "output.py"

        SAMPLE_PROMPTS += [{"role": "user", "content": sample_input.read_text()}, {"role": "assistant", "content": sample_output.read_text()}]

    name = path.stem
    body = path.read_text()

    result = client.chat.completions.create(
        messages=[SYSTEM_PROMPT] + SAMPLE_PROMPTS + [{"role": "user", "content": f"{body}"}],
        model="gpt-3.5-turbo",
    )

    os.makedirs("sdk/filters", exist_ok=True)
    with open(f"sdk/filters/{name}.py", "w") as ofile:
        code = extract_python_code(result.choices[0].message.content or "")
        ofile.write(code)


def process_audio_filter() -> None:
    for i in pathlib.Path("./source").glob("*.html"):
        if not i.stem.startswith("8."):
            continue

        print(f"Processing {i}")
        process_document(i)


if __name__ == "__main__":
    process_audio_filter()
