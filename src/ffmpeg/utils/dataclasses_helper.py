import json
from dataclasses import asdict, is_dataclass
from typing import Any, ClassVar, Dict, Protocol, TypeVar, cast


class IsDataclass(Protocol):
    # as already noted in comments, checking for this attribute is currently
    # the most reliable way to ascertain that something is a dataclass
    __dataclass_fields__: ClassVar[Dict[str, Any]]


T = TypeVar("T", bound=IsDataclass)


def load(cls: type[T], raw: str) -> T:
    data = json.loads(raw)
    return _load(cls, data)


def _load(cls: type[T], data: dict[str, Any]) -> T:
    """
    Deserialize a dictionary into a dataclass of type cls.

    :param cls: The type of the dataclass to deserialize into.
    :param data: A dictionary representing the serialized dataclass.
    :return: An instance of the specified dataclass.
    """

    if is_dataclass(cls):
        field_types = cls.__annotations__
        field_data = {}
        for field_name, field_type in field_types.items():
            field_value = data.get(field_name)
            if is_dataclass(field_type) and isinstance(field_value, dict):
                # Recursive call for nested dataclasses
                field_data[field_name] = _load(field_type, field_value)
            else:
                field_data[field_name] = field_value
        return cast(T, cls(**field_data))

    raise TypeError(f"The provided class {cls.__name__} is not a dataclass")


# Serialization
def dump(instance: IsDataclass) -> str:
    return json.dumps(asdict(instance))
