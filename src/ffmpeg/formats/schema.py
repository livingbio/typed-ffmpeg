from dataclasses import dataclass

from ..schema import FFMpegOptionGroup


@dataclass(frozen=True, kw_only=True)
class FFMpegMuxerOption(FFMpegOptionGroup): ...


@dataclass(frozen=True, kw_only=True)
class FFMpegDemuxerOption(FFMpegOptionGroup): ...
