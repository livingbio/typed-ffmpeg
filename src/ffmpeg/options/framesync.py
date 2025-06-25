from typing import Literal

from ..schema import FFMpegOptionGroup
from ..utils.frozendict import merge


class FFMpegFrameSyncOption(FFMpegOptionGroup): ...


def framesync(
    eof_action: Literal["repeat", "pass", "endall"] | None = None,
    shortest: bool | None = None,
    repeatlast: bool | None = None,
    ts_sync_mode: Literal["default", "nearest"] | None = None,
) -> FFMpegFrameSyncOption:
    return FFMpegFrameSyncOption(
        kwargs=merge(
            {
                "eof_action": eof_action,
                "shortest": shortest,
                "repeatlast": repeatlast,
                "ts_sync_mode": ts_sync_mode,
            }
        )
    )
