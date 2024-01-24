from ..schema import StreamType
from ..utils.typing import override
from .audio import AudioStream
from .video import VideoStream


class AVStream(AudioStream, VideoStream):
    @property
    @override
    def video(self) -> VideoStream:
        return VideoStream(node=self.node, index=self.index, selector=StreamType.video)

    @property
    @override
    def audio(self) -> AudioStream:
        return AudioStream(node=self.node, index=self.index, selector=StreamType.audio)
