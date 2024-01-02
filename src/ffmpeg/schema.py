import enum


class StreamType(enum.Enum):
    audio = "audio"
    video = "video"


class Default:
    ...


class DefaultInt(int, Default):
    ...


class DefaultFloat(float, Default):
    ...


class DefaultStr(str, Default):
    ...
