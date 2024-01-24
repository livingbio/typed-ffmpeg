from ..schema import StreamType
from .audio import AudioStream
from .video import VideoStream


class AVStream(AudioStream, VideoStream):
    @property
    def video(self) -> VideoStream:
        """Return the video component of this stream."""
        return VideoStream(node=self.node, index=self.index, selector=StreamType.video)

    @property
    def audio(self) -> AudioStream:
        """Return the audio component of this stream."""
        return AudioStream(node=self.node, index=self.index, selector=StreamType.audio)
