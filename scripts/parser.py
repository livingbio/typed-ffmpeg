import pathlib

import pydantic
from bs4 import BeautifulSoup

from .settings import settings

DOCUMENT_PATH = settings.document_path


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
        if href.startswith("#") and not href.startswith("#toc-"):
            refs.add(href[1:])

    return FilterDocument(refs=[DOCUMENT_PATH / f"{ref}.html" for ref in refs], section_index=index, hash=ref, title=title, path=DOCUMENT_PATH / f"{ref}.html", filter_names=filter_names)
