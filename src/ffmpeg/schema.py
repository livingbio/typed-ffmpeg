from pydantic import BaseModel


class Default(BaseModel):
    value: str | int | float | bool | None
