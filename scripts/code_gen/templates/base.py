from pydantic import BaseModel


class FilterNode(BaseModel):
    name: str
