from typing import TYPE_CHECKING, Any

from pydantic import BaseModel

if TYPE_CHECKING:
    from .stream import AudioStream, VideoStream


class Node(BaseModel):
    name: str
    args: list[str] = []
    kwargs: dict[str, str | int | float | bool | None] = {}


class Stream(BaseModel):
    node: Node
    label: str | int | None = None
    selector: str | None = None


class FilterableStream(Stream):
    node: "FilterNode" | "InputNode"

    def filter(self, *streams: "FilterableStream", name: str, **kwargs: str) -> "FilterableStream":
        return self.filter_multi_output(*streams, name=name, **kwargs).stream()

    def filter_multi_output(self, *streams: "FilterableStream", name: str, **kwargs: Any) -> "FilterNode":
        return FilterNode(name=name, kwargs=kwargs, inputs=[self, *streams])

    @property
    def video(self) -> VideoStream:
        return self.node.video(label=self.label)

    @property
    def audio(self) -> AudioStream:
        return self.node.audio(label=self.label)

    def output(self, *streams: "FilterableStream", **kwargs: Any) -> "OutputStream":
        return OutputNode(name="output", kwargs=kwargs, inputs=[self, *streams]).stream()


class InputNode(Node):
    def video(self, label: str | int | None = None) -> "VideoStream":
        from .stream import VideoStream

        return VideoStream(node=self, label=label, selector="v")

    def audio(self, label: str | int | None = None) -> "AudioStream":
        from .stream import AudioStream

        return AudioStream(node=self, label=label, selector="a")

    def stream(self, label: str | int | None = None) -> "Stream":
        return Stream(node=self, label=label)


class FilterNode(InputNode):
    inputs: list[FilterableStream]

    def stream(self, label: str | int | None = None) -> "FilterableStream":
        return FilterableStream(node=self, label=label)


class OutputNode(Node):
    inputs: list[FilterableStream]

    def stream(self, label: str | int | None = None) -> "OutputStream":
        return OutputStream(node=self, label=label)


class OutputStream(Stream):
    node: OutputNode | "GlobalNode"

    def global_args(self, *args: str, **kwargs: str | bool | int | float | None) -> "OutputStream":
        return GlobalNode(name="global_args", input=self, args=list(args), kwargs=kwargs).stream()


class GlobalNode(Node):
    input: OutputStream

    def stream(self, label: str | int | None = None) -> "OutputStream":
        return OutputStream(node=self, label=label)
