from dataclasses import dataclass
from functools import cached_property

from bs4 import BeautifulSoup, Tag


@dataclass(frozen=True, kw_only=True)
class FilterDocument:
    section_index: str
    hash: str
    title: str
    body: str
    filter_names: tuple[str, ...]

    @property
    def url(self) -> str:
        return f"https://ffmpeg.org/ffmpeg-filters.html#{self.hash}"

    @cached_property
    def description(self) -> str:
        from .helpers import convert_html_to_markdown

        return convert_html_to_markdown(self.body)

    @cached_property
    def parameter_descs(self) -> dict[str, str]:
        from .helpers import parse_paremeters

        soup = BeautifulSoup(self.body, "html.parser")
        options_p_tag = soup.find(
            "p", string=lambda text: "options" in text.lower() if text else False
        )

        if options_p_tag:
            options = options_p_tag.find_next("dl")
        else:
            options = soup.find("dl")

        if options:
            assert isinstance(options, Tag)
            return parse_paremeters(options)
        return {}
