# https://ffmpeg.org/ffmpeg-filters.html

import pathlib
import re
import urllib.request

import pydantic
import typer
import yaml
from bs4 import BeautifulSoup

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


class Filter(pydantic.BaseModel):
    name: str
    source: str
    description: str
    ref: pydantic.HttpUrl
    parameters: list[dict[str, str]] = []


class FilterDocument(pydantic.BaseModel):
    section_index: str
    hash: str
    title: str
    path: pathlib.Path
    filter_names: list[str]
    refs: list[pathlib.Path] = []

    @property
    def url(self) -> str:
        return f"https://ffmpeg.org/ffmpeg-filters.html#{self.hash}"


def parse_filter_document(body: str) -> FilterDocument:
    soup = BeautifulSoup(body, "html.parser")
    h3 = soup.find("h3")
    title = h3.text
    index, filter_namestr = title.split(" ", 1)
    filter_names = map(str, filter_namestr.split(","))
    ref = h3.a["href"].replace("#toc-", "")

    # check cross reference
    refs: set[str] = set()
    for a in soup.find_all("a"):
        href = a.get("href")
        if href.startswith("#"):
            refs.add(href[1:])

    if ref in refs:
        refs.remove(ref)

    return FilterDocument(refs=[DOCUMENT_PATH / f"{ref}.html" for ref in refs], section_index=index, hash=ref, title=title, path=DOCUMENT_PATH / f"{ref}.html", filter_names=filter_names)


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
def generate_signature(path: pathlib.Path) -> None:
    body = path.read_text()
    path.stem

    info = parse_filter_document(body)
    soup = BeautifulSoup(body, "html.parser")

    # extract parameters
    options = soup.find("dl")

    if options:
        parameters = parse_paremeters(options)
    else:
        parameters = []

    for dl_tag in soup.find_all("dl"):
        dl_tag.decompose()

    for filter_name in info.filter_names:
        filter_name = filter_name.strip()
        filter = Filter(name=filter_name, source=body, description=soup.text.strip(), ref=info.url, parameters=parameters)

        with open(f"source/{filter_name}.yml", "w") as ofile:
            yaml.dump(filter.model_dump(mode="json"), ofile)


@app.command()
def split_documents() -> None:
    # split documents into individual files for easier processing

    section_pattern = re.compile(r'(?P<body><h3 class="section"><a href="(.*?)">(?P<name>.*?)</a></h3>(.*?))<span', re.MULTILINE | re.DOTALL)

    def extract_filter(html: str) -> list[tuple[str, str]]:
        return [(m.group("name"), m.group("body")) for m in section_pattern.finditer(html)]

    with (DOCUMENT_PATH / "ffmpeg-filters.html").open() as ifile:
        for name, body in extract_filter(ifile.read()):
            info = parse_filter_document(body)

            if not info.section_index.startswith("8.") and not info.section_index.startswith("11."):
                continue

            with info.path.open("w") as ofile:
                ofile.write(body)

    return None


if __name__ == "__main__":
    DOCUMENT_PATH.mkdir(exist_ok=True)
    app()
