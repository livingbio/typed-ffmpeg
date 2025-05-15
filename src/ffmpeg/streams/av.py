from ..dag.nodes import InputNode
from .audio import AudioStream
from .video import VideoStream


class AVStream(AudioStream, VideoStream):
    """
    A stream that contains both audio and video. This is for input nodes only.
    """

    node: InputNode

    @property
    def video(self) -> VideoStream:
        return VideoStream(node=self.node, index=self.index)

    @property
    def audio(self) -> AudioStream:
        return AudioStream(node=self.node, index=self.index)

    def video_stream(self, index: int) -> VideoStream:
        return VideoStream(node=self.node, index=index)

    def audio_stream(self, index: int) -> AudioStream:
        return AudioStream(node=self.node, index=index)
