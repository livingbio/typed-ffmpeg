from __future__ import annotations

import logging
import os.path
import shlex
import subprocess
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from ..exceptions import Error
from ..schema import Default, StreamType
from ..utils.escaping import escape
from ..utils.typing import override
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
    inputs: tuple[FilterableStream, ...] = ()
    input_typings: tuple[StreamType, ...] = ()
    output_typings: tuple[StreamType, ...] = ()

    @override
    def repr(self) -> str:
        return self.name

    def video(self, index: int) -> "VideoStream":
        """
        Return the video stream at the specified index

        Args:
            index: the index of the video stream

        Returns:
            the video stream at the specified index
        """
        from ..streams.video import VideoStream

        video_outputs = [i for i, k in enumerate(self.output_typings) if k == StreamType.video]
        if not len(video_outputs) > index:
            raise ValueError(f"Specified index {index} is out of range for video outputs {len(video_outputs)}")
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

        audio_outputs = [i for i, k in enumerate(self.output_typings) if k == StreamType.audio]
        if not len(audio_outputs) > index:
            raise ValueError(f"Specified index {index} is out of range for audio outputs {len(audio_outputs)}")

        return AudioStream(node=self, index=audio_outputs[index])

    def __post_init__(self) -> None:
        from ..streams.audio import AudioStream
        from ..streams.video import VideoStream

        super().__post_init__()

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
            # Note: the -nooption syntax cannot be used for boolean AVOptions, use -option 0/-option 1.
            if isinstance(value, bool):
                value = str(int(value))

            if not isinstance(value, Default):
                commands += [f"{key}={escape(value)}"]

        if commands:
            return [incoming_labels] + [f"{self.name}="] + [escape(":".join(commands), "\\'[],;")] + [outgoing_labels]
        return [incoming_labels] + [f"{self.name}"] + [outgoing_labels]


@dataclass(frozen=True, kw_only=True)
class FilterableStream(Stream):
    """
    A stream that can be used as input to a filter
    """

    node: "FilterNode | InputNode"

    def vfilter(
        self,
        *streams: "FilterableStream",
        name: str,
        input_typings: tuple[StreamType, ...] = (StreamType.video,),
        **kwargs: Any,
    ) -> "VideoStream":
        """
        Apply a custom video filter which has only one output to this stream

        Args:
            *streams (FilterableStream): the streams to apply the filter to
            name: the name of the filter
            **kwargs: the arguments for the filter

        Returns:
            AVStream: the output stream
        """
        return self.filter_multi_output(
            *streams, name=name, input_typings=input_typings, output_typings=(StreamType.video,), **kwargs
        ).video(0)

    def afilter(
        self,
        *streams: "FilterableStream",
        name: str,
        input_typings: tuple[StreamType, ...] = (StreamType.audio,),
        **kwargs: Any,
    ) -> "AudioStream":
        """
        Apply a custom audio filter which has only one output to this stream

        Args:
            *streams (FilterableStream): the streams to apply the filter to
            name: the name of the filter
            **kwargs: the arguments for the filter

        Returns:
            AVStream: the output stream
        """
        return self.filter_multi_output(
            *streams, name=name, input_typings=input_typings, output_typings=(StreamType.audio,), **kwargs
        ).audio(0)

    def filter_multi_output(
        self,
        *streams: "FilterableStream",
        name: str,
        input_typings: tuple[StreamType, ...] = (),
        output_typings: tuple[StreamType, ...] = (),
        **kwargs: Any,
    ) -> "FilterNode":
        """
        Apply a custom filter which has multiple outputs to this stream

        Args:
            *streams (FilterableStream): the streams to apply the filter to
            name: the name of the filter
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
            raise ValueError(f"Unknown stream type: {self.__class__.__name__}")  # pragma: no cover

        if isinstance(self.node, FilterNode):
            if len(self.node.output_typings) > 1:
                return f"{context.get_node_label(self.node)}#{self.index}"
            return f"{context.get_node_label(self.node)}"
        raise ValueError(f"Unknown node type: {self.node.__class__.__name__}")  # pragma: no cover

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
    def get_args(self, context: DAGContext = None) -> list[str]:
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

    @property
    def video(self) -> "VideoStream":
        """
        Return the video stream of this node

        Returns:
            the video stream
        """
        from ..streams.video import VideoStream

        return VideoStream(node=self)

    @property
    def audio(self) -> "AudioStream":
        """
        Return the audio stream of this node

        Returns:
            the audio stream
        """
        from ..streams.audio import AudioStream

        return AudioStream(node=self)

    def stream(self) -> "AVStream":
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
    def get_args(self, context: DAGContext = None) -> list[str]:
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

    def merge_outputs(self, *streams: OutputStream) -> OutputStream:
        return MergeOutputsNode(inputs=streams).stream()

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
            return cmd + compile(self) + ["-y"]

        return cmd + compile(self)

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
            capture_stdout: whether to capture stdout
            capture_stderr: whether to capture stderr
            input: the input
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
    def get_args(self, context: DAGContext = None) -> list[str]:
        # NOTE: the node just used to group outputs, no need to add any commands
        return []
