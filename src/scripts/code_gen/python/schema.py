from ..schema import FFMpegCodecIR, FFMpegOptionIR, FFMpegOptionChoiceIR
from .utils import safe_name, option_typing

class PythonFFMpegCodec(FFMpegCodecIR):
    def safe_name(self) -> str:
        return safe_name(self.name)

class PythonFFMpegOption(FFMpegOptionIR):
    def safe_name(self) -> str:
        return safe_name(self.name)

    def typing(self) -> str:
        return option_typing(self)