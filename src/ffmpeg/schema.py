import enum


class StreamType(enum.Enum):
    audio = "audio"
    video = "video"


class Default(str):
    ...


BOOLEAN = bool
DURATION = str | int | float
# https://ffmpeg.org/ffmpeg-utils.html#Time-duration

COLOR = str
# https://ffmpeg.org/ffmpeg-utils.html#color-syntax

FLAGS = str
DICTIONARY = str
PIX_FMT = str

INT = int
INT64 = int
DOUBLE = float
FLOAT = float
STRING = str | int | float

VIDEO_RATE = str | int | float
# Specify the frame rate of a video, expressed as the number of frames generated per second. It has to be a string in the format frame_rate_num/frame_rate_den, an integer number, a float number or a valid video frame rate abbreviation.
# https://ffmpeg.org/ffmpeg-utils.html#Video-rate

# https://ffmpeg.org/ffmpeg-utils.html#Video-size
IMAGE_SIZE = str
RATIONAL = str
# https://ffmpeg.org/ffmpeg-utils.html#Ratio
SAMPLE_FMT = str
BINARY = str
