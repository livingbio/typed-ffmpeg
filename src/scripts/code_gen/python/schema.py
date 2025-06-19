from ..ir.schema import FFMpegCodec, FFMpegOption, FFMpegOptionChoice
from .utils import safe_name, option_typing

class PythonFFMpegCodec(FFMpegCodec):
    def safe_name(self) -> str:
        return safe_name(self.name)

class PythonFFMpegOption(FFMpegOption):
    def safe_name(self) -> str:
        return safe_name(self.name)

    def typing(self) -> str:
        return option_typing(self)