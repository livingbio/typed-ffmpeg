import enum


class StreamType(enum.Enum):
    """
    Stream type (audio or video)
    """

    audio = "audio"
    """it is an audio stream"""
    video = "video"
    """it is a video stream"""


class Default(str):
    """
    This is the default value for an option. It is used for annotation purposes only
    and will not be passed to the ffmpeg command line.
    """

    ...
