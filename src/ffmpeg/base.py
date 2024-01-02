from __future__ import annotations

from abc import ABC, abstractproperty
from typing import TYPE_CHECKING, Any, Mapping

from pydantic import BaseModel, model_validator

from .schema import StreamType

if TYPE_CHECKING:
    from .streams.audio import AudioStream
    from .streams.av import AVStream
    from .streams.video import VideoStream


class Node(BaseModel):
    name: str
    args: list[str] = []
    kwargs: Mapping[str, Any] = {}


class Stream(BaseModel):
    node: Node
    index: int = 0  # the nth child of the node
    selector: StreamType | None = None


class FilterableStream(Stream, ABC):
    node: FilterNode | InputNode

    def filter(self, *streams: "FilterableStream", name: str, **kwargs: str) -> "AVStream":
        return self.filter_multi_output(*streams, name=name, **kwargs).stream(0)

    def filter_multi_output(self, *streams: "FilterableStream", name: str, **kwargs: Any) -> "FilterNode":
        return FilterNode(name=name, kwargs=kwargs, inputs=[self, *streams])

    @abstractproperty
    def video(self) -> "VideoStream":
        raise NotImplementedError("This stream does not have a video component")

    @abstractproperty
    def audio(self) -> "AudioStream":
        raise NotImplementedError("This stream does not have an audio component")

    def output(self, *streams: "FilterableStream", **kwargs: Any) -> "OutputStream":
        return OutputNode(name="output", kwargs=kwargs, inputs=[self, *streams]).stream()


class InputNode(Node):
    def video(self) -> "VideoStream":
        from .streams.video import VideoStream

        return VideoStream(node=self, selector=StreamType.video)

    def audio(self) -> "AudioStream":
        from .streams.audio import AudioStream

        return AudioStream(node=self, selector=StreamType.audio)

    def stream(self) -> "AVStream":
        from .streams.av import AVStream

        return AVStream(node=self)


class FilterNode(Node):
    inputs: list[FilterableStream]
    input_typings: list[StreamType] | None = None
    output_typings: list[StreamType] | None = None

    def stream(self, index: int) -> "AVStream":
        from .streams.av import AVStream

        if self.output_typings is not None:
            assert (
                len(self.output_typings) > index
            ), f"Specified index {index} is out of range for outputs {len(self.output_typings)}"

        return AVStream(node=self, index=index)

    def video(self, index: int) -> "VideoStream":
        from .streams.video import VideoStream

        assert self.output_typings is not None, "Output typings must be specified to use `video`"
        video_outputs = [i for i, k in enumerate(self.output_typings) if k == StreamType.video]
        assert (
            len(video_outputs) > index
        ), f"Specified index {index} is out of range for video outputs {len(video_outputs)}"
        return VideoStream(node=self, index=video_outputs[index])

    def audio(self, index: int) -> "AudioStream":
        from .streams.audio import AudioStream

        assert self.output_typings is not None, "Output typings must be specified to use `audio`"
        audio_outputs = [i for i, k in enumerate(self.output_typings) if k == StreamType.audio]
        assert (
            len(audio_outputs) > index
        ), f"Specified index {index} is out of range for audio outputs {len(audio_outputs)}"
        return AudioStream(node=self, index=audio_outputs[index])

    @model_validator(mode="after")
    def validate_input(self) -> "FilterNode":
        if self.input_typings is None:
            return self

        assert len(self.inputs) == len(
            self.input_typings
        ), f"Expected {len(self.input_typings)} inputs, got {len(self.inputs)}"

        stream: FilterableStream
        expected_type: StreamType

        for i, (stream, expected_type) in enumerate(zip(self.inputs, self.input_typings)):
            if expected_type == StreamType.video:
                assert isinstance(stream, VideoStream), f"Expected input {i} to have video component, got {stream}"
            if expected_type == StreamType.audio:
                assert isinstance(stream, AudioStream), f"Expected input {i} to have audio component, got {stream}"

        return self


class OutputNode(Node):
    inputs: list[FilterableStream]

    def stream(self, index: int = 0) -> "OutputStream":
        return OutputStream(node=self, index=index)


class OutputStream(Stream):
    node: OutputNode | GlobalNode

    def global_args(self, *args: str, **kwargs: str | bool | int | float | None) -> "OutputStream":
        return GlobalNode(name="global_args", input=self, args=list(args), kwargs=kwargs).stream()

    def overwrite_output(self) -> "OutputStream":
        return GlobalNode(name="overwrite_output", input=self, args=["-y"]).stream()


class GlobalNode(Node):
    input: OutputStream

    def stream(self) -> "OutputStream":
        return OutputStream(node=self)


def input(filename: str, **kwargs: str | int | None | float) -> "AVStream":
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
