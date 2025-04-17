from dataclasses import dataclass

from ffmpeg.common.serialize import Serializable


@dataclass(kw_only=True)
class FFMpegFilterManuallyDefined(Serializable):
    """
    Manual definitions for FFmpeg filters

    This class represents manually defined configuration for FFmpeg filters, particularly
    for complex filters that cannot be fully automatically typed through parsing alone.
    It allows for defining custom input/output type formulas and pre-processing steps
    that are applied before code generation.
    """

    name: str

    formula_typings_input: str | None = None
    formula_typings_output: str | None = None

    pre: tuple[tuple[str, str], ...] = ()
