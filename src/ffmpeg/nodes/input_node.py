from typing import Sequence

from ffmpeg.nodes.base import DAGContext

from ..schema import StreamType
from ..streams.audio import AudioStream
from ..streams.av import AVStream
from ..streams.video import VideoStream
from .base import DAGContext, Node, Stream


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

    def get_args(self, context: DAGContext) -> list[str]:
        commands = []
        commands += self.args
        for key, value in self.kwargs.items():
            commands += [f"-{key}", value]
        commands += ["-i", self.filename]
        return commands
