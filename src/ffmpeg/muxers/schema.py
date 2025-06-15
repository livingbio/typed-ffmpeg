from dataclasses import dataclass

from ..common.serialize import Serializable
from ..utils.frozendict import FrozenDict


@dataclass(frozen=True, kw_only=True)
class FFMpegMuxerOptionBase(Serializable):
    kwargs: FrozenDict[str, str | int | float | bool] = FrozenDict({})


@dataclass(frozen=True, kw_only=True)
class FFMpegMuxerOption(FFMpegMuxerOptionBase): ...


@dataclass(frozen=True, kw_only=True)
class FFMpegDemuxerOption(FFMpegMuxerOptionBase): ...
