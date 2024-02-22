"""
Defines the basic schema for the ffmpeg command line options.
"""

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


COMMON_TYPE = str | int | float | bool

def _to_tuple(
    kwargs: dict[str, COMMON_TYPE | dict[str, COMMON_TYPE] | Default]
) -> tuple[tuple[str, COMMON_TYPE], ...]:
    """
    Convert the values of the dictionary to strings.
    """
    return tuple((k, v) for k, v in kwargs.items() if not isinstance(v, Default))
