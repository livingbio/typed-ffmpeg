from __future__ import annotations

from abc import ABC, abstractproperty
from typing import TYPE_CHECKING, Any, Sequence

from pydantic import model_validator

from ..schema import StreamType
from .base import Node, Stream, _DAGContext, empty_dag_context

if TYPE_CHECKING:
    from ..streams.audio import AudioStream
    from ..streams.av import AVStream
    from ..streams.video import VideoStream
    from .input_node import InputNode
    from .output_node import OutputNode, OutputStream


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

    def output(self, *streams: "FilterableStream", filename: str, **kwargs: Any) -> "OutputStream":
        return OutputNode(kwargs=kwargs, inputs=[self, *streams], filename=filename).stream()

    def label(self, context: _DAGContext) -> str:
        if isinstance(self.node, InputNode):
            if self.selector:
                return f"[{context.get_node_label(self.node)}:{self.selector}]"
            else:
                return f"[{context.get_node_label(self.node)}]"
        else:
            if self.selector:
                return f"[{context.get_node_label(self.node)}-{self.index}:{self.selector}]"
            else:
                return f"[{context.get_node_label(self.node)}-{self.index}]"

    @model_validator(mode="after")
    def validate_index(self) -> FilterableStream:
        if isinstance(self.node, InputNode):
            assert self.index is None, "Input streams cannot have an index"
        else:
            assert self.index is not None, "Filter streams must have an index"
        return self


class FilterNode(Node):
    name: str
    inputs: list[FilterableStream]
    input_typings: list[StreamType] | None = None
    output_typings: list[StreamType] | None = None

    @property
    def incoming_streams(self) -> Sequence[Stream]:
        return self.inputs

    def stream(self, index: int) -> "AVStream":
        from ..streams.av import AVStream

        if self.output_typings is not None:
            assert (
                len(self.output_typings) > index
            ), f"Specified index {index} is out of range for outputs {len(self.output_typings)}"

        return AVStream(node=self, index=index)

    def video(self, index: int) -> "VideoStream":
        from ..streams.video import VideoStream

        assert self.output_typings is not None, "Output typings must be specified to use `video`"
        video_outputs = [i for i, k in enumerate(self.output_typings) if k == StreamType.video]
        assert (
            len(video_outputs) > index
        ), f"Specified index {index} is out of range for video outputs {len(video_outputs)}"
        return VideoStream(node=self, index=video_outputs[index])

    def audio(self, index: int) -> "AudioStream":
        from ..streams.audio import AudioStream

        assert self.output_typings is not None, "Output typings must be specified to use `audio`"
        audio_outputs = [i for i, k in enumerate(self.output_typings) if k == StreamType.audio]
        assert (
            len(audio_outputs) > index
        ), f"Specified index {index} is out of range for audio outputs {len(audio_outputs)}"
        return AudioStream(node=self, index=audio_outputs[index])

    @model_validator(mode="after")
    def validate_input(self) -> "FilterNode":
        from ..streams.audio import AudioStream
        from ..streams.video import VideoStream

        if self.input_typings is None:
            return self

        assert len(self.inputs) == len(
            self.input_typings
        ), f"Expected {len(self.input_typings)} inputs, got {len(self.inputs)}"

        stream: FilterableStream
        expected_type: StreamType

        for i, (stream, expected_type) in enumerate(zip(self.inputs, self.input_typings)):
            if expected_type == StreamType.video:
                assert isinstance(
                    stream, VideoStream
                ), f"Expected input {i} to have video component, got {stream.__class__.__name__}"
            if expected_type == StreamType.audio:
                assert isinstance(
                    stream, AudioStream
                ), f"Expected input {i} to have audio component, got {stream.__class__.__name__}"

        return self

    def get_args(self, context: _DAGContext = empty_dag_context) -> list[str]:
        incoming_labels = "".join(k.label(context) for k in self.inputs)
        outputs = context.get_outgoing_streams(self)

        outgoing_labels = ""
        for output in outputs:
            # NOTE: all outgoing streams must be filterable
            assert isinstance(output, FilterableStream)
            outgoing_labels += output.label(context)

        commands = [f"{self.name}="]
        for key, value in self.kwargs.items():
            commands += [f":{key}={value}"]

        return [incoming_labels] + commands + [outgoing_labels]
