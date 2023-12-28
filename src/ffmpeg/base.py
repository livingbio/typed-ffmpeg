from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from .stream import AudioStream, VideoStream


class Stream(BaseModel):
    node: "FilterNode" | None = None
    label: str | None = None
    selector: str | None = None


class FilterNode(BaseModel):
    streams: list[Stream]
    name: str
    kwargs: dict[str, str | int | float | bool | None] = {}

    def _vs(self, label: str = None, selector: str = None) -> "VideoStream":
        from .stream import VideoStream

        return VideoStream(node=self, label=label, selector=selector)

    def _as(self, label: str = None, selector: str = None) -> "AudioStream":
        from .stream import AudioStream

        return AudioStream(node=self, label=label, selector=selector)
