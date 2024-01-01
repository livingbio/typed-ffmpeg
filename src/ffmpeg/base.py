from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Iterable, Mapping

from pydantic import BaseModel

from .schema import Default

if TYPE_CHECKING:
    from .stream import AudioStream, VideoStream


def convert_kwargs_to_cmd_line_args(kwargs: Mapping[str, str | int | float | bool | None]) -> list[str]:
    """Helper function to build command line arguments out of dict."""
    args = []
    for k in sorted(kwargs.keys()):
        v = kwargs[k]
        if isinstance(v, Iterable) and not isinstance(v, str):
            for value in v:
                args.append(f"-{k}")
                if value is not None:
                    args.append("{}".format(value))
            continue
        args.append(f"-{k}")
        if v is not None:
            args.append(f"{v}")
    return args


class Node(BaseModel, ABC):
    name: str
    args: list[str] = []
    kwargs: Mapping[str, Default | str | int | float | bool | None] = {}

    @abstractmethod
    def compile(self) -> list[str]:
        ...


class Stream(BaseModel, ABC):
    node: Node
    label: str | int | None = None
    selector: str | None = None

    @abstractmethod
    def compile(self) -> list[str]:
        # compile current and upstream nodes into a single ffmpeg command
        ...


class FilterableStream(Stream):
    node: FilterNode | InputNode

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

    def compile(self) -> list[str]:
        raise NotImplementedError


class InputNode(Node):
    def video(self, label: str | int | None = None) -> "VideoStream":
        from .stream import VideoStream

        return VideoStream(node=self, label=label, selector="v")

    def audio(self, label: str | int | None = None) -> "AudioStream":
        from .stream import AudioStream

        return AudioStream(node=self, label=label, selector="a")

    def stream(self, label: str | int | None = None) -> "FilterableStream":
        return FilterableStream(node=self, label=label)

    def compile(self) -> list[str]:
        raise NotImplemented

    #     return convert_kwargs_to_cmd_line_args(self.kwargs)


class FilterNode(InputNode):
    inputs: list[FilterableStream]
    formula_input_typings: str | None = None
    formula_output_typings: str | None = None
    input_typings: list[str] = []
    output_typings: list[str] = []

    def stream(self, label: str | int | None = None) -> "FilterableStream":
        return FilterableStream(node=self, label=label)

    def compile(self) -> list[str]:
        return super().compile()


class OutputNode(Node):
    inputs: list[FilterableStream]

    def stream(self, label: str | int | None = None) -> "OutputStream":
        return OutputStream(node=self, label=label)

    def compile(self) -> list[str]:
        raise NotImplementedError


class OutputStream(Stream):
    node: OutputNode | GlobalNode

    def global_args(self, *args: str, **kwargs: str | bool | int | float | None) -> "OutputStream":
        return GlobalNode(name="global_args", input=self, args=list(args), kwargs=kwargs).stream()

    def overwrite_output(self) -> "OutputStream":
        return GlobalNode(name="overwrite_output", input=self, args=["-y"]).stream()

    def run(self) -> None:
        ...

    def compile(self) -> list[str]:
        return self.node.compile()


class GlobalNode(Node):
    input: OutputStream

    def stream(self, label: str | int | None = None) -> "OutputStream":
        return OutputStream(node=self, label=label)

    def compile(self) -> list[str]:
        return self.input.compile() + self.args


def input(filename: str, **kwargs: str | int | None | float) -> FilterableStream:
    """Input file URL (ffmpeg ``-i`` option)

    Any supplied kwargs are passed to ffmpeg verbatim (e.g. ``t=20``,
    ``f='mp4'``, ``acodec='pcm'``, etc.).

    To tell ffmpeg to read from stdin, use ``pipe:`` as the filename.

    Official documentation: `Main options <https://ffmpeg.org/ffmpeg.html#Main-options>`__
    """
    kwargs["i"] = filename
    fmt = kwargs.pop("f", None)
    if fmt:
        if "format" in kwargs:
            raise ValueError("Can't specify both `format` and `f` kwargs")
        kwargs["format"] = fmt
    return InputNode(name=input.__name__, kwargs=kwargs).stream()
