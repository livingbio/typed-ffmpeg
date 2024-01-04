import pathlib
import re
import urllib.request

import typer
from bs4 import BeautifulSoup

from .schema import FilterDocument, parse_filter_document

app = typer.Typer()

document_path = pathlib.Path(__file__).parent / "source"
document_path.mkdir(exist_ok=True)


def extract_html_tags(file_path: pathlib.Path) -> set[str]:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        soup = BeautifulSoup(content, "html.parser")
        tags = {tag.name for tag in soup.find_all(True)}
        return tags

    except Exception as e:
        print(f"An error occurred: {e}")
        return set()


@app.command()
def download_ffmpeg_filter_documents() -> None:
    # download ffmpeg filter documents
    url = "https://ffmpeg.org/ffmpeg-filters.html"
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode("utf-8")

    with (document_path / "ffmpeg-filters.html").open("w") as ofile:
        ofile.write(text)


@app.command()
def scan_documents() -> None:
    documents = split_documents()

    tags = set()
    for document in documents:
        tags |= extract_html_tags(document.path)

    print(tags)


@app.command()
def split_documents() -> list[FilterDocument]:
    # split documents into individual files for easier processing

    section_pattern = re.compile(
        r'(?P<body><h3 class="section"><a href="(.*?)">(?P<name>.*?)</a></h3>(.*?))<span',
        re.MULTILINE | re.DOTALL,
    )

    def extract_filter(html: str) -> list[tuple[str, str]]:
        return [(m.group("name"), m.group("body")) for m in section_pattern.finditer(html)]

    infos: list[FilterDocument] = []
    with (document_path / "ffmpeg-filters.html").open() as ifile:
        for name, body in extract_filter(ifile.read()):
            info = parse_filter_document(body)

            print(f"Processing {info.title}...")
            info.save()
            infos.append(info)

    for info in infos:
        # if len(info.refs) >= 1:
        #     print(f"WARNING: {name} has multiple references: {info.refs}")

        for ref in info.refs:
            if not ref.exists():
                print(f"WARNING: {info.title} has missing reference: {ref}")

    return infos


if __name__ == "__main__":
    app()
