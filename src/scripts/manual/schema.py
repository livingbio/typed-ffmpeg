from dataclasses import dataclass


@dataclass(kw_only=True)
class FFMpegFilterManuallyDefined:
    name: str

    formula_typings_input: str | None = None
    formula_typings_output: str | None = None

    pre: dict[str, str] = {}
