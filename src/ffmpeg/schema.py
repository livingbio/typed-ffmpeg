import enum


class StreamType(enum.Enum):
    """
    The type of a stream. (audio or video)
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


def to_tuple(kwargs: dict[str, str | int | float | bool | Default]) -> tuple[tuple[str, str | int | float | bool], ...]:
    """
    Convert the values of the dictionary to strings.
    """
    return tuple((k, v) for k, v in kwargs.items() if not isinstance(v, Default))
