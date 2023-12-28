from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from .stream import AudioStream, VideoStream


class Stream(BaseModel):
    node: "Node" | None = None
    label: str | None = None
    selector: str | None = None


class Node(BaseModel):
    name: str
    kwargs: dict[str, str | int | float | bool | None] = {}


class InputNode(Node):
    def _vs(self, label: str = None, selector: str = None) -> "VideoStream":
        from .stream import VideoStream

        return VideoStream(node=self, label=label, selector=selector)

    def _as(self, label: str = None, selector: str = None) -> "AudioStream":
        from .stream import AudioStream

        return AudioStream(node=self, label=label, selector=selector)


class FilterNode(InputNode):
    streams: list[Stream]


class OutputNode(Node):
    streams: list[Stream]


class OutputStream(Stream):
    node: OutputNode | "GlobalNode" | "MergeOutputsNode"


class GlobalNode(Node):
    stream: OutputStream


class MergeOutputsNode(Node):
    streams: list[OutputStream]
