"""Subtitle stream utilities."""

from ..dag.nodes import FilterableStream


class SubtitleStream(FilterableStream):
    """A stream that contains subtitle data."""
