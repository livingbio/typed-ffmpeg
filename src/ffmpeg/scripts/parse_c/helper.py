from typing import Any

import pydantic


def dump(items: list[Any] | dict[str, Any] | Any) -> list[Any] | dict[str, Any] | Any:
    if isinstance(items, list):
        return [dump(item) for item in items]
    elif isinstance(items, dict):
        return {key: dump(value) for key, value in items.items()}
    elif isinstance(items, pydantic.BaseModel):
        return items.model_dump()
    return items
