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
    name = path.stem

    ref_pattern = re.compile(r"#toc\-([\w]+)")

    ref = ref_pattern.findall(body)[0]
    soup = BeautifulSoup(body, "html.parser")
    options = soup.find("dl")

    h3 = soup.find("h3")
    index, section_name = h3.text.split(" ", 1)

    if options:
        parameters = parse_paremeters(options)
    else:
        parameters = []

    for dl_tag in soup.find_all("dl"):
        dl_tag.decompose()

    # check cross reference
    for h3 in soup.find_all("h3"):
        h3.decompose()

    if '<a href="#' in str(soup):
        print(f"Cross reference found in {name}")

    for filter_name in section_name.split(","):
        filter_name = filter_name.strip()
        filter = Filter(name=filter_name, source=body, description=soup.text.strip(), ref=f"https://ffmpeg.org/ffmpeg-filters.html#{ref}", parameters=parameters)

        with open(f"source/{index} {filter_name}.yml", "w") as ofile:
            yaml.dump(filter.model_dump(mode="json"), ofile)


@app.command()
def split_documents() -> None:
    # split documents into individual files for easier processing

    section_pattern = re.compile(r'(?P<body><h3 class="section"><a href="(.*?)">(?P<name>.*?)</a></h3>(.*?))<span', re.MULTILINE | re.DOTALL)

    def extract_filter(html: str) -> list[tuple[str, str]]:
        return [(m.group("name"), m.group("body")) for m in section_pattern.finditer(html)]

    with (DOCUMENT_PATH / "ffmpeg-filters.html").open() as ifile:
        for name, body in extract_filter(ifile.read()):
            soup = BeautifulSoup(body, "html.parser")
            h3 = soup.find("h3")
            title = h3.text
            ref = h3.a["href"].replace("#toc-", "")

            if not title.startswith("8.") and not title.startswith("11."):
                continue

            with open(f"source/{ref}.html", "w") as ofile:
                ofile.write(body)

    return None


if __name__ == "__main__":
    DOCUMENT_PATH.mkdir(exist_ok=True)
    app()
