from ..dag.nodes import InputNode
from .audio import AudioStream
from .subtitle import SubtitleStream
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

    @property
    def subtitle(self) -> SubtitleStream:
        """
        Get the subtitle stream from the input node.

        Returns:
            SubtitleStream: The subtitle stream from the input node.
        """
        return SubtitleStream(node=self.node, index=self.index)

    def video_stream(self, index: int | None = None) -> VideoStream:
        """
        Get the video stream from the input node with a specified index.

        Args:
            index: The index of the video stream.

        Returns:
            VideoStream: The video stream from the input node.
        """
        return VideoStream(node=self.node, index=index)

    def audio_stream(self, index: int | None = None) -> AudioStream:
        """
        Get the audio stream from the input node with a specified index.

        Args:
            index: The index of the audio stream.

        Returns:
            AudioStream: The audio stream from the input node.
        """
        return AudioStream(node=self.node, index=index)

    def subtitle_stream(self, index: int | None = None) -> SubtitleStream:
        """
        Get the subtitle stream from the input node with a specified index.

        Args:
            index: The index of the subtitle stream.

        Returns:
            SubtitleStream: The subtitle stream from the input node.
        """
        return SubtitleStream(node=self.node, index=index)
