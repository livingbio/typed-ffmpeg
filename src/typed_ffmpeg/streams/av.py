from ..schema import StreamType
from .audio import AudioStream
from .video import VideoStream


class AVStream(AudioStream, VideoStream):
    @property
    def video(self) -> VideoStream:
        return VideoStream(node=self.node, index=self.index, selector=StreamType.video)

    @property
    def audio(self) -> AudioStream:
        return AudioStream(node=self.node, index=self.index, selector=StreamType.audio)
