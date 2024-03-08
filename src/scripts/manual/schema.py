from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class FFMpegFilterManuallyDefined:
    name: str

    forumla_typings_input: str | None = None
    formula_typings_output: str | None = None
