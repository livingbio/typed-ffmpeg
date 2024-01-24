import enum


class StreamType(enum.Enum):
    audio = "audio"
    video = "video"


class Default(str):
    """
    Default value for an option
    """

    ...


Boolean = bool | str
Duration = str | int | float
# https://ffmpeg.org/ffmpeg-utils.html#Time-duration

Color = str
# https://ffmpeg.org/ffmpeg-utils.html#color-syntax
# is a Enum

Flags = str
# format A+B
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
