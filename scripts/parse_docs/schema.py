import pathlib
from functools import cached_property

import pydantic
from bs4 import BeautifulSoup

from .helpers import convert_html_to_markdown

sections_path = pathlib.Path(__file__).parent / "sections"
sections_path.mkdir(exist_ok=True)


def parse_paremeters(soup: BeautifulSoup) -> dict[str, str]:
    parameters = []
    current_params = []

    for element in soup.find_all(["dt", "dd"], recursive=False):
        if element.name == "dt" and element.samp:
            current_params.append(element.samp.get_text())
        elif element.name == "dd" and current_params:
            description = str(element)
            for param in current_params:
                param = param.strip().replace(" ", ",")
                for p in param.split(","):
                    p = p.strip()
                    parameters.append({"name": p, "description": description})
            current_params = []

    return {k["name"]: k["description"] for k in parameters}


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
        return convert_html_to_markdown(self.body)

    @cached_property
    def parameter_descs(self) -> dict[str, str]:
        soup = BeautifulSoup(self.body, "html.parser")
        options_p_tag = soup.find("p", string=lambda text: "options" in text.lower() if text else False)

        if options_p_tag:
            options = options_p_tag.find_next("dl")
        else:
            options = soup.find("dl")

        if options:
            return parse_paremeters(options)
        return {}

    def save(self) -> None:
        with self.path.open("w") as ofile:
            ofile.write(self.body)

    @classmethod
    def load(self, path: pathlib.Path) -> "FilterDocument":
        with path.open() as ifile:
            body = ifile.read()
            return parse_filter_document(body)


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
        refs=[sections_path / f"{ref}.html" for ref in refs],
        section_index=index,
        hash=ref,
        title=title,
        body=body,
        path=sections_path / f"{ref}.html",
        filter_names=filter_names,
    )
