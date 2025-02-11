from __future__ import annotations

import logging
import os.path
from dataclasses import dataclass, replace
from pathlib import Path
from typing import TYPE_CHECKING, Any

from ..exceptions import FFMpegTypeError, FFMpegValueError
from ..schema import Default, StreamType
from ..utils.escaping import escape
from ..utils.lazy_eval.schema import LazyValue
from ..utils.typing import override
from .global_runnable.runnable import GlobalRunable
from .io.output_args import OutputArgs
from .schema import Node, Stream

if TYPE_CHECKING:
    from ..streams.audio import AudioStream
    from ..streams.av import AVStream
    from ..streams.video import VideoStream
    from .context import DAGContext


logger = logging.getLogger(__name__)


@dataclass(frozen=True, kw_only=True)
class FilterNode(Node):
    """
    A filter node that can be used to apply filters to streams
    """

    name: str
    """
    The name of the filter
    """

    inputs: tuple[FilterableStream, ...] = ()
    """
    The input streams
    """

    input_typings: tuple[StreamType, ...] = ()
    """
    The input typings
    """

    output_typings: tuple[StreamType, ...] = ()
    """
    The output typings
    """

    @override
    def repr(self) -> str:
        return self.name

    def video(self, index: int) -> VideoStream:
        """
        Return the video stream at the specified index

        Args:
            index: the index of the video stream

        Returns:
            the video stream at the specified index
        """
        from ..streams.video import VideoStream

        video_outputs = [
            i for i, k in enumerate(self.output_typings) if k == StreamType.video
        ]
        if not len(video_outputs) > index:
            raise FFMpegValueError(
                f"Specified index {index} is out of range for video outputs {len(video_outputs)}"
            )
        return VideoStream(node=self, index=video_outputs[index])

    def audio(self, index: int) -> AudioStream:
        """
        Return the audio stream at the specified index

        Args:
            index: the index of the audio stream

        Returns:
            the audio stream at the specified index
        """
        from ..streams.audio import AudioStream

        audio_outputs = [
            i for i, k in enumerate(self.output_typings) if k == StreamType.audio
        ]
        if not len(audio_outputs) > index:
            raise FFMpegValueError(
                f"Specified index {index} is out of range for audio outputs {len(audio_outputs)}"
            )

        return AudioStream(node=self, index=audio_outputs[index])

    def __post_init__(self) -> None:
        from ..streams.audio import AudioStream
        from ..streams.video import VideoStream

        super().__post_init__()

        if len(self.inputs) != len(self.input_typings):
            raise FFMpegValueError(
                f"Expected {len(self.input_typings)} inputs, got {len(self.inputs)}"
            )

        stream: FilterableStream
        expected_type: StreamType

        for i, (stream, expected_type) in enumerate(
            zip(self.inputs, self.input_typings)
        ):
            if expected_type == StreamType.video:
                if not isinstance(stream, VideoStream):
                    raise FFMpegTypeError(
                        f"Expected input {i} to have video component, got {stream.__class__.__name__}"
                    )
            if expected_type == StreamType.audio:
                if not isinstance(stream, AudioStream):
                    raise FFMpegTypeError(
                        f"Expected input {i} to have audio component, got {stream.__class__.__name__}"
                    )

    @override
    def get_args(self, context: DAGContext = None) -> list[str]:
        from .context import DAGContext

        if not context:
            context = DAGContext.build(self)

        incoming_labels = "".join(f"[{k.label(context)}]" for k in self.inputs)
        outputs = context.get_outgoing_streams(self)

        outgoing_labels = ""
        for output in sorted(outputs, key=lambda stream: stream.index or 0):
            # NOTE: all outgoing streams must be filterable
            assert isinstance(output, FilterableStream)
            outgoing_labels += f"[{output.label(context)}]"

        commands = []
        for key, value in self.kwargs:
            assert not isinstance(value, LazyValue), (
                f"LazyValue should have been evaluated: {key}={value}"
            )

            # Note: the -nooption syntax cannot be used for boolean AVOptions, use -option 0/-option 1.
            if isinstance(value, bool):
                value = str(int(value))

            if not isinstance(value, Default):
                commands += [f"{key}={escape(value)}"]

        if commands:
            return (
                [incoming_labels]
                + [f"{self.name}="]
                + [escape(":".join(commands), "\\'[],;")]
                + [outgoing_labels]
            )
        return [incoming_labels] + [f"{self.name}"] + [outgoing_labels]


@dataclass(frozen=True, kw_only=True)
class FilterableStream(Stream, OutputArgs):
    """
    A stream that can be used as input to a filter
    """

    node: FilterNode | InputNode

    @override
    def _output_node(
        self, *streams: FilterableStream, filename: str | Path, **kwargs: Any
    ) -> OutputNode:
        """
        Output the streams to a file URL

        Args:
            *streams: the other streams to output
            filename: the filename to output to
            **kwargs: the arguments for the output

        Returns:
            the output stream
        """
        return OutputNode(
            inputs=(self, *streams),
            filename=str(filename),
            kwargs=tuple(kwargs.items()),
        )

    def vfilter(
        self,
        *streams: FilterableStream,
        name: str,
        input_typings: tuple[StreamType, ...] = (StreamType.video,),
        **kwargs: Any,
    ) -> VideoStream:
        """
        Apply a custom video filter which has only one output to this stream

        Args:
            *streams (FilterableStream): the streams to apply the filter to
            name: the name of the filter
            input_typings: the input typings
            **kwargs: the arguments for the filter

        Returns:
            the output stream
        """
        return self.filter_multi_output(
            *streams,
            name=name,
            input_typings=input_typings,
            output_typings=(StreamType.video,),
            **kwargs,
        ).video(0)

    def afilter(
        self,
        *streams: FilterableStream,
        name: str,
        input_typings: tuple[StreamType, ...] = (StreamType.audio,),
        **kwargs: Any,
    ) -> AudioStream:
        """
        Apply a custom audio filter which has only one output to this stream

        Args:
            *streams (FilterableStream): the streams to apply the filter to
            name: the name of the filter
            input_typings: the input typings
            **kwargs: the arguments for the filter

        Returns:
            the output stream
        """
        return self.filter_multi_output(
            *streams,
            name=name,
            input_typings=input_typings,
            output_typings=(StreamType.audio,),
            **kwargs,
        ).audio(0)

    def filter_multi_output(
        self,
        *streams: FilterableStream,
        name: str,
        input_typings: tuple[StreamType, ...] = (),
        output_typings: tuple[StreamType, ...] = (),
        **kwargs: Any,
    ) -> FilterNode:
        """
        Apply a custom filter which has multiple outputs to this stream

        Args:
            *streams (FilterableStream): the streams to apply the filter to
            name: the name of the filter
            input_typings: the input typings
            output_typings: the output typings
            **kwargs: the arguments for the filter

        Returns:
            the FilterNode
        """
        return FilterNode(
            name=name,
            kwargs=tuple(kwargs.items()),
            inputs=(self, *streams),
            input_typings=input_typings,
            output_typings=output_typings,
        )

    def label(self, context: DAGContext = None) -> str:
        """
        Return the label for this stream

        Args:
            context: the DAG context

        Returns:
            the label for this stream
        """
        from ..streams.audio import AudioStream
        from ..streams.av import AVStream
        from ..streams.video import VideoStream
        from .context import DAGContext

        if not context:
            context = DAGContext.build(self.node)

        if isinstance(self.node, InputNode):
            if isinstance(self, AVStream):
                return f"{context.get_node_label(self.node)}"
            elif isinstance(self, VideoStream):
                return f"{context.get_node_label(self.node)}:v"
            elif isinstance(self, AudioStream):
                return f"{context.get_node_label(self.node)}:a"
            raise FFMpegValueError(
                f"Unknown stream type: {self.__class__.__name__}"
            )  # pragma: no cover

        if isinstance(self.node, FilterNode):
            if len(self.node.output_typings) > 1:
                return f"{context.get_node_label(self.node)}#{self.index}"
            return f"{context.get_node_label(self.node)}"
        raise FFMpegValueError(
            f"Unknown node type: {self.node.__class__.__name__}"
        )  # pragma: no cover

    def __post_init__(self) -> None:
        if isinstance(self.node, InputNode):
            assert self.index is None, "Input streams cannot have an index"
        else:
            assert self.index is not None, "Filter streams must have an index"


@dataclass(frozen=True, kw_only=True)
class InputNode(Node):
    """
    A node that can be used to read from files
    """

    filename: str
    """
    The filename to read from
    """

    inputs: tuple[()] = ()

    @override
    def repr(self) -> str:
        return os.path.basename(self.filename)

    @property
    def video(self) -> VideoStream:
        """
        Return the video stream of this node

        Returns:
            the video stream
        """
        from ..streams.video import VideoStream

        return VideoStream(node=self)

    @property
    def audio(self) -> AudioStream:
        """
        Return the audio stream of this node

        Returns:
            the audio stream
        """
        from ..streams.audio import AudioStream

        return AudioStream(node=self)

    def stream(self) -> AVStream:
        """
        Return the output stream of this node

        Returns:
            the output stream
        """
        from ..streams.av import AVStream

        return AVStream(node=self)

    @override
    def get_args(self, context: DAGContext = None) -> list[str]:
        commands = []
        for key, value in self.kwargs:
            if isinstance(value, bool):
                if value is True:
                    commands += [f"-{key}"]
                elif value is False:
                    commands += [f"-no{key}"]
            else:
                commands += [f"-{key}", str(value)]
        commands += ["-i", self.filename]
        return commands


@dataclass(frozen=True, kw_only=True)
class OutputNode(Node):
    filename: str
    """
    The filename to output to
    """
    inputs: tuple[FilterableStream, ...]

    @override
    def repr(self) -> str:
        return os.path.basename(self.filename)

    def stream(self) -> OutputStream:
        """
        Return the output stream of this node

        Returns:
            the output stream
        """
        return OutputStream(node=self)

    @override
    def get_args(self, context: DAGContext = None) -> list[str]:
        # !handle mapping
        commands = []

        if context and (
            any(isinstance(k.node, FilterNode) for k in self.inputs)
            or len([k for k in context.all_nodes if isinstance(k, OutputNode)]) > 1
        ):
            for input in self.inputs:
                if isinstance(input.node, InputNode):
                    commands += ["-map", input.label(context)]
                else:
                    commands += ["-map", f"[{input.label(context)}]"]

        for key, value in self.kwargs:
            if isinstance(value, bool):
                if value is True:
                    commands += [f"-{key}"]
                elif value is False:
                    commands += [f"-no{key}"]
            else:
                commands += [f"-{key}", str(value)]
        commands += [self.filename]
        return commands


@dataclass(frozen=True, kw_only=True)
class OutputStream(Stream, GlobalRunable):
    node: OutputNode

    @override
    def _global_node(self, *streams: OutputStream, **kwargs: Any) -> GlobalNode:
        """
        Add extra global command-line argument

        Args:
            **kwargs: the extra arguments

        Returns:
            the output stream
        """
        return GlobalNode(inputs=(self, *streams), kwargs=tuple(kwargs.items()))


@dataclass(frozen=True, kw_only=True)
class GlobalNode(Node):
    """
    A node that can be used to set global options
    """

    inputs: tuple[OutputStream, ...]

    @override
    def repr(self) -> str:
        return " ".join(self.get_args())

    def stream(self) -> GlobalStream:
        """
        Return the output stream of this node

        Returns:
            the output stream
        """
        return GlobalStream(node=self)

    @override
    def get_args(self, context: DAGContext = None) -> list[str]:
        commands = []
        for key, value in self.kwargs:
            if isinstance(value, bool):
                if value is True:
                    commands += [f"-{key}"]
                elif value is False:
                    commands += [f"-no{key}"]
            else:
                commands += [f"-{key}", str(value)]
        return commands


@dataclass(frozen=True, kw_only=True)
class GlobalStream(Stream, GlobalRunable):
    node: GlobalNode

    @override
    def _global_node(self, *streams: OutputStream, **kwargs: Any) -> GlobalNode:
        """
        Add extra global command-line argument

        Args:
            **kwargs: the extra arguments

        Returns:
            the output stream
        """
        inputs = (*self.node.inputs, *streams)
        kwargs = dict(self.node.kwargs) | kwargs

        new_node = replace(self.node, inputs=inputs, kwargs=tuple(kwargs.items()))
        return new_node
