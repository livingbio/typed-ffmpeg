from dataclasses import dataclass

from ..common.serialize import Serializable, serializable
from ..utils.frozendict import FrozenDict


@serializable
@dataclass(frozen=True, kw_only=True)
class FFMpegCodecOption(Serializable):
    kwargs: FrozenDict[str, str | int | float | bool] = FrozenDict({})


@serializable
@dataclass(frozen=True, kw_only=True)
class FFMpegEncoderOption(FFMpegCodecOption): ...


@serializable
@dataclass(frozen=True, kw_only=True)
class FFMpegDecoderOption(FFMpegCodecOption): ...
