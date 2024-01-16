import enum


class StreamType(enum.Enum):
    audio = "audio"
    video = "video"


class Default(str):
    ...
