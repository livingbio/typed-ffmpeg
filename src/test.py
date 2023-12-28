from pydantic import BaseModel, Field


class A(BaseModel):
    f: str = Field(..., description="f description")
