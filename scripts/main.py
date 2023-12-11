# https://ffmpeg.org/ffmpeg-filters.html

import pathlib
import re
import urllib.request

import pydantic
import typer
from bs4 import BeautifulSoup
from utils.parser import FilterDocument, parse_filter_document
from utils.settings import settings
from utils.signature import parse_schema

app = typer.Typer()

DOCUMENT_PATH = settings.document_path


@app.command()
def download_ffmpeg_filter_documents() -> None:
    # download ffmpeg filter documents
    url = "https://ffmpeg.org/ffmpeg-filters.html"
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode("utf-8")

    with (DOCUMENT_PATH / "ffmpeg-filters.html").open("w") as ofile:
        ofile.write(text)


class Filter(pydantic.BaseModel):
    name: str
    source: str
    description: str
    ref: pydantic.HttpUrl
    parameters: list[dict[str, str]] = []


def parse_paremeters(soup: BeautifulSoup) -> list[dict[str, str]]:
    parameters = []
    current_params = []

    for element in soup.find_all(["dt", "dd"], recursive=False):
        if element.name == "dt" and element.samp:
            current_params.append(element.samp.get_text())
        elif element.name == "dd" and current_params:
            description = str(element)
            for param in current_params:
                parameters.append({"name": param, "description": description})
            current_params = []

    return parameters


@app.command()
def generate_schema(path: pathlib.Path) -> None:
    info = parse_filter_document(path.read_text())
    filters = parse_schema(info)

    for filter in filters:
        with open(settings.schemas_path / f"{filter.name}.json", "w") as ofile:
            ofile.write(filter.model_dump_json())


@app.command()
def split_documents(should_generate_schema: bool = False) -> None:
    # split documents into individual files for easier processing

    section_pattern = re.compile(r'(?P<body><h3 class="section"><a href="(.*?)">(?P<name>.*?)</a></h3>(.*?))<span', re.MULTILINE | re.DOTALL)

    def extract_filter(html: str) -> list[tuple[str, str]]:
        return [(m.group("name"), m.group("body")) for m in section_pattern.finditer(html)]

    infos: list[FilterDocument] = []
    with (DOCUMENT_PATH / "ffmpeg-filters.html").open() as ifile:
        for name, body in extract_filter(ifile.read()):
            info = parse_filter_document(body)

            if not info.section_index.startswith("8.") and not info.section_index.startswith("11."):
                continue

            print(f"Processing {info.title}...")

            with info.path.open("w") as ofile:
                ofile.write(body)

            if should_generate_schema:
                generate_schema(info.path)

            infos.append(info)

    for info in infos:
        # if len(info.refs) >= 1:
        #     print(f"WARNING: {name} has multiple references: {info.refs}")

        for ref in info.refs:
            if not ref.exists():
                print(f"WARNING: {info.title} has missing reference: {ref}")

    return None


if __name__ == "__main__":
    app()
