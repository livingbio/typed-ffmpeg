from __future__ import annotations

import logging
import os.path
import shlex
import subprocess
from abc import ABC, abstractproperty
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from ..exceptions import Error
from ..schema import Default, StreamType
from ..utils.escaping import escape
from ..utils.typing import override
from .schema import Node, Stream, _DAGContext, empty_dag_context

if TYPE_CHECKING:
    from ..streams.audio import AudioStream
    from ..streams.av import AVStream
    from ..streams.video import VideoStream


logger = logging.getLogger(__name__)


@dataclass(frozen=True, kw_only=True)
class FilterNode(Node):
    """
    A filter node that can be used to apply filters to streams
    """

    name: str
    inputs: tuple[FilterableStream, ...]
    input_typings: tuple[StreamType, ...] | None = None
    output_typings: tuple[StreamType, ...] | None = None

    @override
    def repr(self) -> str:
        return self.name

    def stream(self, index: int) -> "AVStream":
        """
        Return the stream at the specified index

        Args:
            index: the index of the stream

        Returns:
            the stream at the specified index
        """
        from ..streams.av import AVStream

        if self.output_typings is not None:
            assert (
                len(self.output_typings) > index
            ), f"Specified index {index} is out of range for outputs {len(self.output_typings)}"

        return AVStream(node=self, index=index)

    def video(self, index: int) -> "VideoStream":
        """
        Return the video stream at the specified index

        Args:
            index: the index of the video stream

        Returns:
            the video stream at the specified index
        """
        from ..streams.video import VideoStream

        assert self.output_typings is not None, "Output typings must be specified to use `video`"
        video_outputs = [i for i, k in enumerate(self.output_typings) if k == StreamType.video]
        assert (
            len(video_outputs) > index
        ), f"Specified index {index} is out of range for video outputs {len(video_outputs)}"
        return VideoStream(node=self, index=video_outputs[index])

    def audio(self, index: int) -> "AudioStream":
        """
        Return the audio stream at the specified index

        Args:
            index: the index of the audio stream

        Returns:
            the audio stream at the specified index
        """
        from ..streams.audio import AudioStream

        assert self.output_typings is not None, "Output typings must be specified to use `audio`"
        audio_outputs = [i for i, k in enumerate(self.output_typings) if k == StreamType.audio]
        assert (
            len(audio_outputs) > index
        ), f"Specified index {index} is out of range for audio outputs {len(audio_outputs)}"
        return AudioStream(node=self, index=audio_outputs[index])

    def __post_init__(self) -> None:
        from ..streams.audio import AudioStream
        from ..streams.video import VideoStream

        super().__post_init__()

        if self.input_typings is None:
            return

        if len(self.inputs) != len(self.input_typings):
            raise ValueError(f"Expected {len(self.input_typings)} inputs, got {len(self.inputs)}")

        stream: FilterableStream
        expected_type: StreamType

        for i, (stream, expected_type) in enumerate(zip(self.inputs, self.input_typings)):
            if expected_type == StreamType.video:
                if not isinstance(stream, VideoStream):
                    raise ValueError(f"Expected input {i} to have video component, got {stream.__class__.__name__}")
            if expected_type == StreamType.audio:
                if not isinstance(stream, AudioStream):
                    raise ValueError(f"Expected input {i} to have audio component, got {stream.__class__.__name__}")

    @override
    def get_args(self, context: _DAGContext = empty_dag_context) -> list[str]:
        incoming_labels = "".join(f"[{k.label(context)}]" for k in self.inputs)
        outputs = context.get_outgoing_streams(self)

        outgoing_labels = ""
        for output in sorted(outputs, key=lambda stream: stream.index or 0):
            # NOTE: all outgoing streams must be filterable
            assert isinstance(output, FilterableStream)
            outgoing_labels += f"[{output.label(context)}]"

        commands = []
        for key, value in self.kwargs:
            # Note: the -nooption syntax cannot be used for boolean AVOptions, use -option 0/-option 1.
            if isinstance(value, bool):
                value = str(int(value))

            if not isinstance(value, Default):
                commands += [f"{key}={escape(value)}"]

        if commands:
            return [incoming_labels] + [f"{self.name}="] + [escape(":".join(commands), "\\'[],;")] + [outgoing_labels]
        return [incoming_labels] + [f"{self.name}"] + [outgoing_labels]


@dataclass(frozen=True, kw_only=True)
class FilterableStream(Stream, ABC):
    """
    A stream that can be used as input to a filter
    """

    node: "FilterNode | InputNode"

    def filter(self, *streams: "FilterableStream", name: str, **kwargs: Any) -> "AVStream":
        """
        Apply a custom filter which has only one output to this stream

        Args:
            *streams (FilterableStream): the streams to apply the filter to
            name: the name of the filter
            **kwargs: the arguments for the filter

        Returns:
            AVStream: the output stream
        """
        return self.filter_multi_output(*streams, name=name, **kwargs).stream(0)

    def filter_multi_output(self, *streams: "FilterableStream", name: str, **kwargs: Any) -> "FilterNode":
        """
        Apply a custom filter which has multiple outputs to this stream

        Args:
            *streams (FilterableStream): the streams to apply the filter to
            name: the name of the filter
            **kwargs: the arguments for the filter

        Returns:
            the FilterNode
        """
        return FilterNode(name=name, kwargs=tuple(kwargs.items()), inputs=(self, *streams))

    @abstractproperty
    def video(self) -> "VideoStream":
        """
        Return the video component of this stream

        Returns:
            the video component of this stream
        """
        raise NotImplementedError("This stream does not have a video component")

    @abstractproperty
    def audio(self) -> "AudioStream":
        """
        Return the audio component of this stream

        Returns:
            the audio component of this stream
        """
        raise NotImplementedError("This stream does not have an audio component")

    def output(self, *streams: "FilterableStream", filename: str, **kwargs: Any) -> "OutputStream":
        """
        Output the streams to a file URL

        Args:
            *streams: the streams to output
            filename: the filename to output to
            **kwargs: the arguments for the output

        Returns:
            the output stream
        """
        return OutputNode(kwargs=tuple(kwargs.items()), inputs=(self, *streams), filename=filename).stream()

    def label(self, context: _DAGContext) -> str:
        """
        Return the label for this stream

        Args:
            context: the DAG context

        Returns:
            the label for this stream
        """
        if self.selector == StreamType.video:
            selector = "v"
        elif self.selector == StreamType.audio:
            selector = "a"

        if isinstance(self.node, InputNode) or (
            self.node.output_typings is not None and len(self.node.output_typings) == 1
        ):
            # NOTE: if the node has only one output, we don't need to specify the index
            if self.selector:
                return f"{context.get_node_label(self.node)}:{selector}"
            else:
                return f"{context.get_node_label(self.node)}"
        else:
            if self.selector:
                return f"{context.get_node_label(self.node)}#{self.index}:{selector}"
            else:
                return f"{context.get_node_label(self.node)}#{self.index}"

    def view(self) -> str:
        from ..utils.view import view

        return view(self.node)

    def __post_init__(self) -> None:
        if isinstance(self.node, InputNode):
            assert self.index is None, "Input streams cannot have an index"
        else:
            assert self.index is not None, "Filter streams must have an index"


@dataclass(frozen=True, kw_only=True)
class GlobalNode(Node):
    """
    A node that can be used to set global options
    """

    inputs: tuple["OutputStream"]

    @override
    def repr(self) -> str:
        return " ".join(self.get_args())

    def stream(self) -> "OutputStream":
        """
        Return the output stream of this node

        Returns:
            the output stream
        """
        return OutputStream(node=self)

    @override
    def get_args(self, context: _DAGContext = empty_dag_context) -> list[str]:
        commands = [*self.args]
        for key, value in self.kwargs:
            # Options which do not take arguments are boolean options,
            # and set the corresponding value to true. They can be set to
            # false by prefixing the option name with "no". For example
            # using "-nofoo" will set the boolean option with name "foo" to false.
            if isinstance(value, bool):
                if value is True:
                    commands += [f"-{key}"]
                else:
                    commands += [f"-no{key}"]
            else:
                commands += [f"-{key}", str(value)]
        return commands


@dataclass(frozen=True, kw_only=True)
class InputNode(Node):
    """
    A node that can be used to read from files
    """

    filename: str
    inputs: tuple[()] = ()

    @override
    def repr(self) -> str:
        return os.path.basename(self.filename)

    def video(self) -> "VideoStream":
        """
        Return the video stream of this node

        Returns:
            the video stream
        """
        from ..streams.video import VideoStream

        return VideoStream(node=self, selector=StreamType.video)

    def audio(self) -> "AudioStream":
        """
        Return the audio stream of this node

        Returns:
            the audio stream
        """
        from ..streams.audio import AudioStream

        return AudioStream(node=self, selector=StreamType.audio)

    def stream(self) -> "AVStream":
        """
        Return the output stream of this node

        Returns:
            the output stream
        """
        from ..streams.av import AVStream

        return AVStream(node=self)

    @override
    def get_args(self, context: _DAGContext = empty_dag_context) -> list[str]:
        commands = []
        for key, value in self.kwargs:
            commands += [f"-{key}", str(value)]
        commands += ["-i", self.filename]
        return commands


@dataclass(frozen=True, kw_only=True)
class OutputNode(Node):
    filename: str
    inputs: tuple[FilterableStream, ...]

    @override
    def repr(self) -> str:
        return os.path.basename(self.filename)

    def stream(self) -> "OutputStream":
        """
        Return the output stream of this node

        Returns:
            the output stream
        """
        return OutputStream(node=self)

    @override
    def get_args(self, context: _DAGContext = empty_dag_context) -> list[str]:
        # !handle mapping
        commands = []
        for input in self.inputs:
            if isinstance(input.node, InputNode):
                commands += ["-map", input.label(context)]
            else:
                commands += ["-map", f"[{input.label(context)}]"]

        for key, value in self.kwargs:
            if isinstance(value, bool) and value is True:
                commands += [f"-{key}"]
            else:
                commands += [f"-{key}", str(value)]
        commands += [self.filename]
        return commands


@dataclass(frozen=True, kw_only=True)
class OutputStream(Stream):
    node: OutputNode | GlobalNode | MergeOutputsNode

    def global_args(self, *args: str, **kwargs: Any) -> "OutputStream":
        """
        Add extra global command-line argument

        Args:
            *args: the extra arguments
            **kwargs: the extra arguments

        Returns:
            the output stream
        """
        return GlobalNode(inputs=(self,), args=args, kwargs=tuple(kwargs.items())).stream()

    def overwrite_output(self) -> "OutputStream":
        """
        Overwrite output files without asking (ffmpeg `-y` option)

        Returns:
            the output stream
        """
        return GlobalNode(inputs=(self,), kwargs=(("y", True),)).stream()

    def compile(self, cmd: str | list[str] = "ffmpeg", overwrite_output: bool = False) -> list[str]:
        """
        Build command-line for invoking ffmpeg.

        Args:
            cmd: the command to invoke ffmpeg
            overwrite_output: whether to overwrite output files without asking

        Returns:
            the command-line
        """
        from .compile import compile

        if isinstance(cmd, str):
            cmd = [cmd]

        if overwrite_output:
            return cmd + compile(self.node) + ["-y"]

        return cmd + compile(self.node)

    def compile_line(self, cmd: str | list[str] = "ffmpeg", overwrite_output: bool = False) -> str:
        """
        Build command-line for invoking ffmpeg.

        Args:
            cmd: the command to invoke ffmpeg
            overwrite_output: whether to overwrite output files without asking

        Returns:
            the command-line
        """
        return " ".join(shlex.quote(arg) for arg in self.compile(cmd, overwrite_output=overwrite_output))

    def run_async(
        self,
        cmd: str | list[str] = "ffmpeg",
        pipe_stdin: bool = False,
        pipe_stdout: bool = False,
        pipe_stderr: bool = False,
        quiet: bool = False,
        overwrite_output: bool = False,
    ) -> subprocess.Popen[bytes]:
        """
        Run ffmpeg asynchronously.

        Args:
            cmd: the command to invoke ffmpeg
            pipe_stdin: whether to pipe stdin
            pipe_stdout: whether to pipe stdout
            pipe_stderr: whether to pipe stderr
            quiet: whether to pipe stderr to stdout
            overwrite_output: whether to overwrite output files without asking

        Returns:
            the process
        """

        args = self.compile(cmd, overwrite_output=overwrite_output)
        stdin_stream = subprocess.PIPE if pipe_stdin else None
        stdout_stream = subprocess.PIPE if pipe_stdout or quiet else None
        stderr_stream = subprocess.PIPE if pipe_stderr or quiet else None

        logger.info(f"Running command: {self.compile_line(cmd, overwrite_output=overwrite_output)}")

        return subprocess.Popen(
            args,
            stdin=stdin_stream,
            stdout=stdout_stream,
            stderr=stderr_stream,
        )

    def run(
        self,
        cmd: str | list[str] = "ffmpeg",
        capture_stdout: bool = False,
        capture_stderr: bool = False,
        input: bytes | None = None,
        quiet: bool = False,
        overwrite_output: bool = False,
    ) -> tuple[bytes, bytes]:
        """
        Run ffmpeg synchronously.

        Args:
            cmd: the command to invoke ffmpeg
            pipe_stdin: whether to pipe stdin
            pipe_stdout: whether to pipe stdout
            pipe_stderr: whether to pipe stderr
            quiet: whether to pipe stderr to stdout
            overwrite_output: whether to overwrite output files without asking

        Returns:
            the stdout
            the stderr
        """

        process = self.run_async(
            cmd,
            pipe_stdin=input is not None,
            pipe_stdout=capture_stdout,
            pipe_stderr=capture_stderr,
            quiet=quiet,
            overwrite_output=overwrite_output,
        )
        stdout, stderr = process.communicate(input)
        retcode = process.poll()

        if retcode:
            raise Error(
                retcode=retcode,
                cmd=self.compile_line(cmd, overwrite_output=overwrite_output),
                stdout=stdout,
                stderr=stderr,
            )

        return stdout, stderr


@dataclass(frozen=True, kw_only=True)
class MergeOutputsNode(Node):
    """
    A node that can be used to merge multiple outputs
    """

    inputs: tuple[OutputStream, ...]

    @override
    def repr(self) -> str:
        return "Merge"

    def stream(self) -> "OutputStream":
        """
        Return the output stream of this node

        Returns:
            the output stream
        """
        return OutputStream(node=self)

    @override
    def get_args(self, context: _DAGContext = empty_dag_context) -> list[str]:
        # NOTE: the node just used to group outputs, no need to add any commands
        return []
