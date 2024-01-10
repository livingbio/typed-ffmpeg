from typing import Sequence

from ..schema import StreamType
from ..streams.audio import AudioStream
from ..streams.av import AVStream
from ..streams.video import VideoStream
from .base import Node, Stream


class InputNode(Node):
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
