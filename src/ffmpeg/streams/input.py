from dataclasses import dataclass

from ..dag.nodes import FilterableStream, InputNode
from ..dag.schema import _DAGContext
from ..utils.typing import override
from .audio import AudioFilter
from .video import VideoFilter


@dataclass(frozen=True, kw_only=True)
class InputStream(FilterableStream):
    node: InputNode
    index: int | None = None


@dataclass(frozen=True, kw_only=True)
class VideoIStream(VideoFilter, InputStream):
    @override
    def label(self, context: _DAGContext) -> str:
        return f"{context.get_node_label(self.node)}:v"


@dataclass(frozen=True, kw_only=True)
class AudioIStream(AudioFilter, InputStream):
    @override
    def label(self, context: _DAGContext) -> str:
        return f"{context.get_node_label(self.node)}:a"


@dataclass(frozen=True, kw_only=True)
class AVStream(VideoFilter, AudioFilter, InputStream):
    @property
    def video(self) -> VideoIStream:
        return VideoIStream(node=self.node, index=self.index)

    @property
    def audio(self) -> AudioIStream:
        return AudioIStream(node=self.node, index=self.index)

    @override
    def label(self, context: _DAGContext) -> str:
        return context.get_node_label(self.node)
