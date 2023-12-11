import pathlib
from functools import cached_property

import pydantic
from bs4 import BeautifulSoup

from .settings import settings


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


class FilterDocument(pydantic.BaseModel):
    section_index: str
    hash: str
    title: str
    body: str
    path: pathlib.Path
    filter_names: list[str]
    refs: list[pathlib.Path] = []

    @property
    def url(self) -> str:
        return f"https://ffmpeg.org/ffmpeg-filters.html#{self.hash}"

    @cached_property
    def description(self) -> str:
        soup = BeautifulSoup(self.body, "html.parser")
        for dl_tag in soup.find_all("dl"):
            dl_tag.decompose()
        return soup.text.strip()

    @cached_property
    def parameters(self) -> list[dict[str, str]]:
        soup = BeautifulSoup(self.body, "html.parser")
        options = soup.find("dl")

        if options:
            return parse_paremeters(options)
        return []


def parse_filter_document(body: str) -> FilterDocument:
    soup = BeautifulSoup(body, "html.parser")
    h3 = soup.find("h3")
    title = h3.text
    index, filter_namestr = title.split(" ", 1)
    filter_names = map(lambda i: i.strip(), filter_namestr.split(","))
    ref = h3.a["href"].replace("#toc-", "").replace("-1", "")

    # check cross reference
    refs: set[str] = set()
    for a in soup.find_all("a"):
        href = a.get("href")
        if href.startswith("#") and not href.startswith("#toc-"):
            refs.add(href[1:])

    return FilterDocument(
        refs=[settings.sections_path / f"{ref}.html" for ref in refs],
        section_index=index,
        hash=ref,
        title=title,
        body=body,
        path=settings.sections_path / f"{ref}.html",
        filter_names=filter_names,
    )
