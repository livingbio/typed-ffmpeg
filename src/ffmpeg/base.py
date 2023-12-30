from typing import TYPE_CHECKING, Any, Mapping

from pydantic import BaseModel

if TYPE_CHECKING:
    from .stream import AudioStream, VideoStream


class Default(BaseModel):
    value: str | int | float | bool | None


class Node(BaseModel):
    name: str
    args: list[str] = []
    kwargs: Mapping[str, Default | str | int | float | bool | None] = {}


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

    def stream(self, label: str | int | None = None) -> "FilterableStream":
        return FilterableStream(node=self, label=label)


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

    def overwrite_output(self) -> "OutputStream":
        return GlobalNode(name="overwrite_output", input=self, args=["-y"]).stream()


class GlobalNode(Node):
    input: OutputStream

    def stream(self, label: str | int | None = None) -> "OutputStream":
        return OutputStream(node=self, label=label)


def input(filename: str, **kwargs: str | int | None | float) -> FilterableStream:
    """Input file URL (ffmpeg ``-i`` option)

    Any supplied kwargs are passed to ffmpeg verbatim (e.g. ``t=20``,
    ``f='mp4'``, ``acodec='pcm'``, etc.).

    To tell ffmpeg to read from stdin, use ``pipe:`` as the filename.

    Official documentation: `Main options <https://ffmpeg.org/ffmpeg.html#Main-options>`__
    """
    kwargs["filename"] = filename
    fmt = kwargs.pop("f", None)
    if fmt:
        if "format" in kwargs:
            raise ValueError("Can't specify both `format` and `f` kwargs")
        kwargs["format"] = fmt
    return InputNode(name=input.__name__, kwargs=kwargs).stream()


input("a.mp4").video.crop(x="10", y="20").output(filename="b.mp4").global_args("y").overwrite_output()
