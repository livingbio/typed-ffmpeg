# https://ffmpeg.org/ffmpeg-filters.html

import pathlib
import re
import urllib.request

import typer
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables from .env file
load_dotenv(override=True)

app = typer.Typer()

DOCUMENT_PATH = pathlib.Path("./source")
SDK_PATH = pathlib.Path("./sdk/filters")


@app.command()
def download_ffmpeg_filter_documents() -> None:
    # download ffmpeg filter documents
    url = "https://ffmpeg.org/ffmpeg-filters.html"
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode("utf-8")

    with (DOCUMENT_PATH / "ffmpeg-filters.html").open("w") as ofile:
        ofile.write(text)


@app.command()
def split_documents() -> None:
    # split documents into individual files for easier processing

    pattern = re.compile(r'(?P<body><h3 class="section"><a href="(.*?)">(?P<name>.*?)</a></h3>(.*?))<span', re.MULTILINE | re.DOTALL)

    def extract_filter(html: str) -> list[tuple[str, str]]:
        return [(m.group("name"), m.group("body")) for m in pattern.finditer(html)]

    with (DOCUMENT_PATH / "ffmpeg-filters.html").open() as ifile:
        for name, body in extract_filter(ifile.read()):
            with open(f"source/{name}.html", "w") as ofile:
                ofile.write(body)

    return None


def extract_python_code(body: str) -> str:
    re_python = re.compile(r"```(.*)```", re.DOTALL | re.MULTILINE)

    match = re_python.findall(body)
    if match:
        if match[0].strip().startswith("python"):
            return match[0].strip()[6:]
        return match[0]

    return body


@app.command()
def process_filter(path: pathlib.Path) -> None:
    client = AzureOpenAI(azure_deployment="gpt35")

    SYSTEM_PROMPT = {
        "role": "system",
        "content": """
- You are a python and ffmpeg expert
- please write a python wrapper for following ffmpeg filter document with typing
- only return python code
""",
    }

    SAMPLE_PROMPTS = []

    for sample in pathlib.Path("./samples").iterdir():
        if not sample.is_dir():
            continue

        sample_input = sample / "input.html"
        sample_output = sample / "output.py"

        SAMPLE_PROMPTS += [
            {
                "role": "user",
                "content": f"""
- please generate {sample_input.stem} filter python code with typing
```
{sample_input.read_text()}
```""",
            },
            {"role": "assistant", "content": sample_output.read_text()},
        ]

    filter_names = [k.strip() for k in path.stem.split(" ", 1)[1].split(",")]
    for filter_name in filter_names:
        result = client.chat.completions.create(
            messages=[SYSTEM_PROMPT]
            + SAMPLE_PROMPTS
            + [
                {
                    "role": "user",
                    "content": f"""
- pleaes generate {filter_name} filter python code with typing
{path.read_text()}
""",
                }
            ],
            model="gpt-3.5-turbo",
        )

        with (SDK_PATH / f"{filter_name}.py").open("w") as ofile:
            code = extract_python_code(result.choices[0].message.content or "")
            ofile.write(code)


if __name__ == "__main__":
    DOCUMENT_PATH.mkdir(exist_ok=True)
    SDK_PATH.mkdir(exist_ok=True, parents=True)
    app()
