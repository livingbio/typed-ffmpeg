from dataclasses import dataclass

from ..schema import (
    FFMpegAVOptionIR,
    FFMpegCodecIR,
    FFMpegFilterIR,
    FFMpegFormatIR,
    FFMpegOptionChoiceIR,
)
from .utils import option_typing, safe_name


@dataclass(frozen=True, kw_only=True)
class PythonFFMpegOptionChoice(FFMpegOptionChoiceIR): ...


@dataclass(frozen=True, kw_only=True)
class PythonFFMpegCodec(FFMpegCodecIR):
    @property
    def safe_name(self) -> str:
        return safe_name(self.name)


@dataclass(frozen=True, kw_only=True)
class PythonFFMpegOption(FFMpegAVOptionIR):
    @property
    def safe_name(self) -> str:
        return safe_name(self.name)

    @property
    def typing(self) -> str:
        return option_typing(self)


@dataclass(frozen=True, kw_only=True)
class PythonFFMpegFormat(FFMpegFormatIR):
    @property
    def safe_name(self) -> str:
        return safe_name(self.name)


@dataclass(frozen=True, kw_only=True)
class PythonFFMpegFilter(FFMpegFilterIR):
    @property
    def safe_name(self) -> str:
        return safe_name(self.name)

    @property
    def return_typing(self) -> str:
        raise NotImplementedError()
