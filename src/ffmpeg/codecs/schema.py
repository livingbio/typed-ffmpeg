from dataclasses import dataclass

from ..schema import FFMpegOptionGroup


@dataclass(frozen=True, kw_only=True)
class FFMpegEncoderOption(FFMpegOptionGroup): ...


@dataclass(frozen=True, kw_only=True)
class FFMpegDecoderOption(FFMpegOptionGroup): ...
