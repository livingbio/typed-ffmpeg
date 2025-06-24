from ..schema import FFMpegCodecIR, FFMpegAVOptionIR, FFMpegOptionChoiceIR, FFMpegFormatIR
from .utils import option_typing, safe_name
from dataclasses import dataclass

@dataclass(frozen=True, kw_only=True)
class PythonFFMpegOptionChoice(FFMpegOptionChoiceIR):
    ...

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

