from dataclasses import dataclass

from ..common.serialize import Serializable
from ..utils.frozendict import FrozenDict


@dataclass(frozen=True, kw_only=True)
class FFMpegFormatOption(Serializable):
    kwargs: FrozenDict[str, str | int | float | bool] = FrozenDict({})


@dataclass(frozen=True, kw_only=True)
class FFMpegMuxerOption(FFMpegFormatOption): ...


@dataclass(frozen=True, kw_only=True)
class FFMpegDemuxerOption(FFMpegFormatOption): ...
