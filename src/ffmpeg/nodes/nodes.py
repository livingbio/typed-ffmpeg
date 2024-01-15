from __future__ import annotations

import subprocess
from abc import ABC, abstractproperty
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Sequence

from ..schema import Default, StreamType
from ..utils.escaping import escape
from .base import Node, Stream, _DAGContext, empty_dag_context

if TYPE_CHECKING:
    from ..streams.audio import AudioStream
    from ..streams.av import AVStream
    from ..streams.video import VideoStream


@dataclass(frozen=True, kw_only=True)
class FilterNode(Node):
    name: str
    inputs: tuple[FilterableStream, ...]
    input_typings: tuple[StreamType, ...] | None = None
    output_typings: tuple[StreamType, ...] | None = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}:{self.name}({self.hex})"

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

    def get_args(self, context: _DAGContext = empty_dag_context) -> list[str]:
        incoming_labels = "".join(k.label(context) for k in self.inputs)
        outputs = context.get_outgoing_streams(self)

        outgoing_labels = ""
        for output in sorted(outputs, key=lambda stream: stream.index or 0):
            # NOTE: all outgoing streams must be filterable
            assert isinstance(output, FilterableStream)
            outgoing_labels += output.label(context)

        commands = []
        for key, value in self.kwargs:
            if isinstance(value, bool):
                value = str(int(value))

            if not isinstance(value, Default):
                commands += [f"{key}={escape(value)}"]

        if commands:
            return [incoming_labels] + [f"{self.name}="] + [escape(":".join(commands), "\\'[],;")] + [outgoing_labels]
        return [incoming_labels] + [f"{self.name}"] + [outgoing_labels]


@dataclass(frozen=True, kw_only=True)
class FilterableStream(Stream, ABC):
    node: "FilterNode | InputNode"

    def filter(self, *streams: "FilterableStream", name: str, **kwargs: str) -> "AVStream":
        return self.filter_multi_output(*streams, name=name, **kwargs).stream(0)

    def filter_multi_output(self, *streams: "FilterableStream", name: str, **kwargs: Any) -> "FilterNode":
        return FilterNode(name=name, kwargs=tuple(kwargs.items()), inputs=(self, *streams))

    @abstractproperty
    def video(self) -> "VideoStream":
        raise NotImplementedError("This stream does not have a video component")

    @abstractproperty
    def audio(self) -> "AudioStream":
        raise NotImplementedError("This stream does not have an audio component")

    def output(self, *streams: "FilterableStream", filename: str, **kwargs: Any) -> "OutputStream":
        return OutputNode(kwargs=tuple(kwargs.items()), inputs=(self, *streams), filename=filename).stream()

    def label(self, context: _DAGContext) -> str:
        if self.selector == StreamType.video:
            selector = "v"
        elif self.selector == StreamType.audio:
            selector = "a"

        if isinstance(self.node, InputNode) or (
            self.node.output_typings is not None and len(self.node.output_typings) == 1
        ):
            # NOTE: if the node has only one output, we don't need to specify the index
            if self.selector:
                return f"[{context.get_node_label(self.node)}:{selector}]"
            else:
                return f"[{context.get_node_label(self.node)}]"
        else:
            if self.selector:
                return f"[{context.get_node_label(self.node)}#{self.index}:{selector}]"
            else:
                return f"[{context.get_node_label(self.node)}#{self.index}]"

    def __post_init__(self) -> None:
        if isinstance(self.node, InputNode):
            assert self.index is None, "Input streams cannot have an index"
        else:
            assert self.index is not None, "Filter streams must have an index"


@dataclass(frozen=True, kw_only=True)
class GlobalNode(Node):
    input: "OutputStream"

    def stream(self) -> "OutputStream":
        return OutputStream(node=self)

    @property
    def incoming_streams(self) -> Sequence[OutputStream]:
        return [self.input]

    def get_args(self, context: _DAGContext = empty_dag_context) -> list[str]:
        commands = []
        for key, value in self.kwargs:
            if isinstance(value, bool) and value is True:
                commands += [f"-{key}"]
            else:
                commands += [f"-{key}", str(value)]
        return commands


@dataclass(frozen=True, kw_only=True)
class InputNode(Node):
    filename: str

    @property
    def incoming_streams(self) -> Sequence[Stream]:
        return []

    def video(self) -> "VideoStream":
        from ..streams.video import VideoStream

        return VideoStream(node=self, selector=StreamType.video)

    def audio(self) -> "AudioStream":
        from ..streams.audio import AudioStream

        return AudioStream(node=self, selector=StreamType.audio)

    def stream(self) -> "AVStream":
        from ..streams.av import AVStream

        return AVStream(node=self)

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

    def stream(self) -> "OutputStream":
        return OutputStream(node=self)

    @property
    def incoming_streams(self) -> Sequence[Stream]:
        return self.inputs

    def get_args(self, context: _DAGContext = empty_dag_context) -> list[str]:
        # !handle mapping
        commands = []
        for input in self.inputs:
            commands += ["-map", input.label(context)]

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

    def global_args(self, **kwargs: str | bool | int | float | None) -> "OutputStream":
        return GlobalNode(input=self, kwargs=tuple(kwargs.items())).stream()

    def overwrite_output(self) -> "OutputStream":
        return GlobalNode(input=self, kwargs=(("y", True),)).stream()

    def compile(self, cmd: str | list[str] = "ffmpeg", overwrite_output: bool = False) -> list[str]:
        from ..utils.compile import compile

        if isinstance(cmd, str):
            cmd = [cmd]

        if overwrite_output:
            return cmd + compile(self.node) + ["-y"]

        return cmd + compile(self.node)

    def run_async(
        self,
        cmd: str | list[str] = "ffmpeg",
        pipe_stdin: bool = False,
        pipe_stdout: bool = False,
        pipe_stderr: bool = False,
        quiet: bool = False,
        overwrite_output: bool = False,
        cwd: str | None = None,
    ) -> subprocess.Popen[bytes]:
        args = self.compile(cmd, overwrite_output=overwrite_output)
        stdin_stream = subprocess.PIPE if pipe_stdin else None
        stdout_stream = subprocess.PIPE if pipe_stdout else None
        stderr_stream = subprocess.PIPE if pipe_stderr else None
        if quiet:
            stderr_stream = subprocess.STDOUT
            stdout_stream = subprocess.DEVNULL
        return subprocess.Popen(
            args,
            stdin=stdin_stream,
            stdout=stdout_stream,
            stderr=stderr_stream,
            cwd=cwd,
        )

    def run(
        self,
        cmd: str | list[str] = "ffmpeg",
        pipe_stdin: bool = False,
        pipe_stdout: bool = False,
        pipe_stderr: bool = False,
        quiet: bool = False,
        overwrite_output: bool = False,
        cwd: str | None = None,
    ) -> tuple[bytes, bytes]:
        process = self.run_async(
            cmd,
            pipe_stdin=pipe_stdin,
            pipe_stdout=pipe_stdout,
            pipe_stderr=pipe_stderr,
            quiet=quiet,
            overwrite_output=overwrite_output,
            cwd=cwd,
        )
        stdout, stderr = process.communicate()
        retcode = process.poll()

        if retcode:
            raise subprocess.CalledProcessError(retcode, process.args, output=stdout, stderr=stderr)
        return stdout, stderr


@dataclass(frozen=True, kw_only=True)
class MergeOutputsNode(Node):
    inputs: tuple[OutputStream, ...]

    def stream(self) -> "OutputStream":
        return OutputStream(node=self)

    @property
    def incoming_streams(self) -> Sequence[Stream]:
        return self.inputs

    def get_args(self, context: _DAGContext = empty_dag_context) -> list[str]:
        # NOTE: the node just used to group outputs, no need to add any commands
        return []
