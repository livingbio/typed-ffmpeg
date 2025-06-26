"""Schema definitions for parsing FFmpeg filter documentation."""

from dataclasses import dataclass
from functools import cached_property

from bs4 import BeautifulSoup, Tag


@dataclass(frozen=True, kw_only=True)
class FilterDocument:
    """A filter document."""

    section_index: str
    """
    The section index of the filter document (e.g. "8.8")
    """
    hash: str
    """
    The hash of the filter
    """
    title: str
    """
    The title of the filter document (e.g. "8.8 acue")
    """
    body: str
    """
    The body of the filter document
    """
    filter_names: tuple[str, ...]
    """
    The names of the filter (e.g. "acue")
    """

    @property
    def url(self) -> str:
        """
        The URL of the filter document.

        Returns:
            The URL of the filter document

        """
        return f"https://ffmpeg.org/ffmpeg-filters.html#{self.hash}"

    @cached_property
    def description(self) -> str:
        """
        The description of the filter document in Markdown.

        Returns:
            The description of the filter document

        """
        from .helpers import convert_html_to_markdown

        return convert_html_to_markdown(self.body)

    @cached_property
    def parameter_descs(self) -> dict[str, str]:
        """
        The parameter descriptions of the filter document in Markdown.

        Returns:
            The parameter descriptions of the filter document

        """
        from .helpers import parse_parameters

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
            return parse_parameters(options)
        return {}
