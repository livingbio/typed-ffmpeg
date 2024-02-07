from ..dag.nodes import InputNode
from ..utils.typing import override
from .audio import AudioStream
from .video import VideoStream


class AVStream(AudioStream, VideoStream):
    node: InputNode

    @property
    @override
    def video(self) -> VideoStream:
        return VideoStream(node=self.node, index=self.index)

    @property
    @override
    def audio(self) -> AudioStream:
        return AudioStream(node=self.node, index=self.index)
