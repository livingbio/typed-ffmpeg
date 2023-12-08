# https://ffmpeg.org/ffmpeg-filters.html

import pathlib
import re
import urllib.request

import typer

app = typer.Typer()

DOCUMENT_PATH = pathlib.Path("./source")


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


if __name__ == "__main__":
    DOCUMENT_PATH.mkdir(exist_ok=True)
    app()
