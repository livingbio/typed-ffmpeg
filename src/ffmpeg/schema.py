"""
Defines the basic schema for the ffmpeg command line options.
"""

from .common.schema import StreamType


class Default(str):
    """
    This is the default value for an option. It is used for annotation purposes only
    and will not be passed to the ffmpeg command line.
    """

    ...


class Auto(Default):
    """
    This is the auto value for an option. It is used for annotation purposes only
    and will not be passed to the ffmpeg command line.
    """


__all__ = [
    "Auto",
    "Default",
    "StreamType",
]
