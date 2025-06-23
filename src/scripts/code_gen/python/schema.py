from ..schema import FFMpegCodecIR, FFMpegOptionIR
from .utils import option_typing, safe_name


class PythonFFMpegCodec(FFMpegCodecIR):
    def safe_name(self) -> str:
        return safe_name(self.name)


class PythonFFMpegOption(FFMpegOptionIR):
    def safe_name(self) -> str:
        return safe_name(self.name)

    def typing(self) -> str:
        return option_typing(self)
