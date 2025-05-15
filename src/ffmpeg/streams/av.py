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
        """
        Get the video stream from the input node.

        Returns:
            VideoStream: The video stream from the input node.
        """
        return VideoStream(node=self.node, index=self.index)

    @property
    def audio(self) -> AudioStream:
        """
        Get the audio stream from the input node.

        Returns:
            AudioStream: The audio stream from the input node.
        """
        return AudioStream(node=self.node, index=self.index)

    def video_stream(self, index: int) -> VideoStream:
        """
        Get the video stream from the input node with a specified index.

        Args:
            index: The index of the video stream.

        Returns:
            VideoStream: The video stream from the input node.
        """
        return VideoStream(node=self.node, index=index)

    def audio_stream(self, index: int) -> AudioStream:
        """
        Get the audio stream from the input node with a specified index.

        Args:
            index: The index of the audio stream.

        Returns:
            AudioStream: The audio stream from the input node.
        """
        return AudioStream(node=self.node, index=index)
