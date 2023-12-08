from typing import Any

from .stream import Stream


class FilterNode:
    def __init__(self, stream: "Stream", name: str, **kwargs: Any) -> None:
        ...

    def stream(self) -> "Stream":
        raise NotImplementedError()
