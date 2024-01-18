from pydantic import BaseModel


class AVChoice(BaseModel):
    name: str
    help: str
    value: int | str
    flags: str = None


class AVOption(BaseModel):
    name: str
    alias: list[str] = []
    description: str | None = None

    typing: str
    min: float = None
    max: float = None
    default: str | int | float | None = None
    choices: list[AVChoice] = []
    flags: str = None


class AVFilter(BaseModel):
    name: str
    description: str

    is_dynamic_inputs: bool = False
    is_dynamic_outputs: bool = False
    input_types: list[str] = None
    output_types: list[str] = None

    options: list[AVOption] = []
