from dataclasses import asdict, is_dataclass
from typing import Any


def dump(items: list[Any] | dict[str, Any] | Any) -> list[Any] | dict[str, Any] | Any:
    if isinstance(items, list):
        return [dump(item) for item in items]
    elif isinstance(items, dict):
        return {key: dump(value) for key, value in items.items()}
    elif is_dataclass(items):
        return asdict(items)
    return items
