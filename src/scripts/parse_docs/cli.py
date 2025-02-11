import re
import urllib.request
from functools import lru_cache
from pathlib import Path

import typer

from ..cache import cache_path, save
from .helpers import parse_filter_document
from .schema import FilterDocument

app = typer.Typer()


@app.command()
def download_ffmpeg_filter_documents() -> Path:
    document_path = cache_path / "docs"
    document_path.mkdir(exist_ok=True)

    # download ffmpeg filter documents
    filter_path = document_path / "ffmpeg-filters.html"

    if filter_path.exists():  # pragma: no cover
        typer.echo("Filter documents already downloaded")
        return filter_path

    typer.echo("Downloading filter documents...")
    url = "https://ffmpeg.org/ffmpeg-filters.html"
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode("utf-8")

    with filter_path.open("w") as ofile:
        ofile.write(text)

    return filter_path


@lru_cache
@app.command()
def process_docs() -> list[FilterDocument]:
    # split documents into individual files for easier processing
    section_pattern = re.compile(
        r'(?P<body><h3 class="section"><a href="(.*?)">(?P<name>.*?)</a></h3>(.*?))<span',
        re.MULTILINE | re.DOTALL,
    )

    def extract_filter(html: str) -> list[tuple[str, str]]:
        return [
            (m.group("name"), m.group("body")) for m in section_pattern.finditer(html)
        ]

    infos: list[FilterDocument] = []
    with (download_ffmpeg_filter_documents()).open() as ifile:
        for name, body in extract_filter(ifile.read()):
            info = parse_filter_document(body)

            print(f"Processing {info.title}...")
            save(info, info.hash)
            infos.append(info)

    return infos


@app.command()
def extract_docs(filter_name: str) -> FilterDocument:
    for doc in process_docs():
        if filter_name in doc.filter_names:
            return doc

    raise ValueError(f"Unknown filter {filter_name}")
