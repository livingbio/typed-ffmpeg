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


@app.command()
def split_documents() -> None:
    # split documents into individual files for easier processing

    section_pattern = re.compile(r'(?P<body><h3 class="section"><a href="(.*?)">(?P<name>.*?)</a></h3>(.*?))<span', re.MULTILINE | re.DOTALL)
    ref_pattern = re.compile(r"#toc\-([\w]+)")

    def extract_filter(html: str) -> list[tuple[str, str]]:
        return [(m.group("name"), m.group("body")) for m in section_pattern.finditer(html)]

    with (DOCUMENT_PATH / "ffmpeg-filters.html").open() as ifile:
        for name, body in extract_filter(ifile.read()):
            with open(f"source/{name}.html", "w") as ofile:
                ofile.write(body)

            ref = ref_pattern.findall(body)[0]
            soup = BeautifulSoup(body, "html.parser")
            options = soup.find("dl")
            index, section_name = name.split(" ", 1)

            parameters = []
            if options:
                for dt, dd in zip(options.find_all("dt", recursive=False), options.find_all("dd", recursive=False)):
                    parameters.append({"name": dt.text.strip(), "description": str(dd)})

            for dl_tag in soup.find_all("dl"):
                dl_tag.decompose()

            for filter_name in section_name.split(","):
                filter_name = filter_name.strip()
                filter = Filter(name=filter_name, source=body, description=soup.text.strip(), ref=f"https://ffmpeg.org/ffmpeg-filters.html#{ref}", parameters=parameters)

                with open(f"source/{index} {filter_name}.yml", "w") as ofile:
                    yaml.dump(filter.model_dump(mode="json"), ofile)

    return None


if __name__ == "__main__":
    DOCUMENT_PATH.mkdir(exist_ok=True)
    app()
