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


Boolean = bool | str
"""
This represents FFmpeg's boolean type. It can accept either a Python boolean value (`True` or `False`)
or a string that represents a boolean value ("true", "false", "1", or "0").

"""
# TODO: confirm

Duration = str | int | float
"""
This represents FFmpeg's duration type. It can accept either a Python integer or float value
or a string that represents a duration value.

Note:
    [Document](https://ffmpeg.org/ffmpeg-utils.html#Time-duration)
"""

Color = str
"""
This represents FFmpeg's color type. It can accept either a Python string value
or a string that represents a color value.

Note:
    [Document](https://ffmpeg.org/ffmpeg-utils.html#Color)
"""
# TODO: is a Enum

Flags = str
"""
This represents FFmpeg's flags type. It can accept either a Python string value
or a string that represents a flags value.

Format: A+B
"""

Dictionary = str
# format A=B:C=D:E=F
Pix_fmt = str

Int = int | str
Int64 = int | str
Double = int | float | str
Float = int | float | str
String = str | int | float

Video_rate = str | int | float
# Specify the frame rate of a video, expressed as the number of frames generated per second. It has to be a string in the format frame_rate_num/frame_rate_den, an integer number, a float number or a valid video frame rate abbreviation.
# https://ffmpeg.org/ffmpeg-utils.html#Video-rate

# https://ffmpeg.org/ffmpeg-utils.html#Video-size
Image_size = str
Rational = str
# https://ffmpeg.org/ffmpeg-utils.html#Ratio
Sample_fmt = str
Binary = str
