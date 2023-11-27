from typing import Any, List, Literal, Optional, Union  # noqa: F401


class FilterNode:
    def __init__(self, stream: "Stream", name: str, **kwargs: Any) -> None:
        ...

    def stream(self) -> "Stream":
        raise NotImplementedError()


class Stream:
    pass
