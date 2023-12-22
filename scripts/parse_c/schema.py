import pydantic


class AVOption(pydantic.BaseModel):
    name: str
    help: str
    # the offset of the field in the struct, it required Macro to get the value
    # offset: int
    type: str
    default: int | float | str
    min: float | str
    max: float | str
    flags: str
    unit: str | None = None


class AVFilter(pydantic.BaseModel):
    name: str
    description: str
    options: list[AVOption] = []
