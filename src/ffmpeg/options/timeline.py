from ..expressions import Expression
from ..schema import FFMpegOptionGroup


class FFMpegTimelineOption(FFMpegOptionGroup):
    """Timeline options."""


def timeline(enable: str | Expression) -> FFMpegTimelineOption:
    """Timeline options."""
    return FFMpegTimelineOption(enable=enable)
