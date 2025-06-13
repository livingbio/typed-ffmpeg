from dataclasses import dataclass

from ..common.serialize import Serializable
from ..utils.frozendict import FrozenDict


@dataclass(frozen=True, kw_only=True)
class FFMpegCodecOption(Serializable):
    kwargs: FrozenDict[str, str | int | float | bool] = FrozenDict({})


@dataclass(frozen=True, kw_only=True)
class FFMpegEncoderOption(FFMpegCodecOption): ...


@dataclass(frozen=True, kw_only=True)
class FFMpegDecoderOption(FFMpegCodecOption): ...
