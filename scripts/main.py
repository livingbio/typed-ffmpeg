# https://ffmpeg.org/ffmpeg-filters.html

import pathlib
import re
import urllib.request

import typer
from app.settings import settings
from devtools import sprint
from parse_c.parse_c import parse_all_filter_names, parse_c
from parse_c.schema import AVFilter
from utils.code_gen import generate_class
from utils.parser import FilterDocument, parse_filter_document
from utils.signature import Filter, parse_schema

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


@app.command()
def code_gen() -> None:
    filters = []
    for f in settings.schemas_path.glob("*.json"):
        filter = Filter.load(f)
        filters.append(filter)

    code = generate_class(filters)

    with (settings.source_path / "stream.py").open("w") as ofile:
        ofile.write(code)


@app.command()
def generate_schema(path: pathlib.Path) -> None:
    info = FilterDocument.load(path)

    if all((settings.schemas_path / f"{filter_name}.json").exists() for filter_name in info.filter_names):
        return None

    filters = parse_schema(info)

    for filter in filters:
        filter.save()


@app.command()
def split_documents(should_generate_schema: bool = False) -> None:
    # split documents into individual files for easier processing

    section_pattern = re.compile(
        r'(?P<body><h3 class="section"><a href="(.*?)">(?P<name>.*?)</a></h3>(.*?))<span',
        re.MULTILINE | re.DOTALL,
    )

    def extract_filter(html: str) -> list[tuple[str, str]]:
        return [(m.group("name"), m.group("body")) for m in section_pattern.finditer(html)]

    infos: list[FilterDocument] = []
    with (DOCUMENT_PATH / "ffmpeg-filters.html").open() as ifile:
        for name, body in extract_filter(ifile.read()):
            info = parse_filter_document(body)

            if not info.section_index.startswith("8.") and not info.section_index.startswith("11."):
                continue

            print(f"Processing {info.title}...")
            info.save()

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


@app.command()
def parse_filters(root: pathlib.Path, allfilter_c: pathlib.Path) -> None:
    all_filter_names = set(k[1] for k in parse_all_filter_names(allfilter_c))

    total = 0
    parsed_filters: list[AVFilter] = []
    for path in root.glob("*.c"):
        filters = parse_c(path)

        if len(filters) == 0:
            sprint(f"Processing {path}... {len(filters)} filters", sprint.red)
        else:
            sprint(f"Processing {path}... {len(filters)} filters " + ",".join(k.name for k in filters), sprint.green)
            total += len(filters)
            parsed_filters.extend(filters)

    print(f"Total filters: {total} / {len(all_filter_names)}")
    parsed_filter_names = {f.name for f in parsed_filters}

    print(f"not exists filters {parsed_filter_names - all_filter_names}")
    print(f"not found filters {all_filter_names - parsed_filter_names}")


if __name__ == "__main__":
    app()
