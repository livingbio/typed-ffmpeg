#!/usr/bin/env python3

import json
import types
from dataclasses import is_dataclass
from typing import (
    Any,
    TypeGuard,
    TypeVar,
    Union,
    cast,
    get_args,
    get_origin,
    get_type_hints,
)

from .schema import ffprobeType, registered_types
from .xml2json import xml_string_to_json

T = TypeVar("T")


def _get_actual_type(type_hint: Any) -> type[Any]:
    """
    Get the actual type from a type hint, handling Optional and Union (including | syntax).

    Args:
        type_hint: The type hint to get the actual type from

    Returns:
        The actual type
    """
    # If type_hint is a string, evaluate it in the schema's module context
    if isinstance(type_hint, str):
        type_hint = registered_types[type_hint]

    origin = get_origin(type_hint)
    # Handle typing.Union and types.UnionType (for int | None in Python 3.10+)
    if origin is Union or (hasattr(types, "UnionType") and origin is types.UnionType):
        non_none_types = [t for t in get_args(type_hint) if t is not type(None)]
        if non_none_types:
            return _get_actual_type(non_none_types[0])
    # Handle direct types.UnionType (for int | None in Python 3.10+)
    if hasattr(types, "UnionType") and isinstance(type_hint, types.UnionType):
        non_none_types = [t for t in type_hint.__args__ if t is not type(None)]
        if non_none_types:
            return _get_actual_type(non_none_types[0])
    return type_hint


def is_dataclass_type(obj: type[Any]) -> TypeGuard[type[T]]:
    """
    Check if an object is a dataclass type.

    Args:
        obj: The object to check

    Returns:
        True if the object is a dataclass type, False otherwise
    """
    return is_dataclass(obj)


def _parse_obj_from_dict(data: Any, cls: type[T]) -> T | None:
    """
    Parse a dictionary into a dataclass instance.

    Args:
        data: The dictionary to parse
        cls: The dataclass to parse into

    Returns:
        The parsed dataclass instance
    """

    if data is None:
        return None

    if isinstance(cls, type):
        if cls is str:
            return cast(T, str(data))
        elif cls is int:
            return cast(T, int(data))
        elif cls is float:
            return cast(T, float(data))
        elif cls is bool:
            return cast(T, bool(data))

    if not isinstance(data, dict):
        return cls()

    if isinstance(cls, str):  # NOTE: python 3.10
        cls = registered_types[cls]

    type_hints = get_type_hints(cls)
    kwargs: dict[str, Any] = {}

    for field_name, field_type in type_hints.items():
        actual_type = _get_actual_type(field_type)

        if get_origin(actual_type) is tuple:
            tuple_args = get_args(actual_type)
            if not tuple_args:
                continue
            item_type = tuple_args[0]
            value = data.get(field_name, [])
            if not isinstance(value, list):
                value = [value]
            kwargs[field_name] = tuple(
                _parse_obj_from_dict(item, item_type) for item in value
            )
            continue

        kwargs[field_name] = _parse_obj_from_dict(data.get(field_name), actual_type)

    return cls(**kwargs)


def parse_ffprobe(xml_string: str) -> ffprobeType:
    """
    Parse ffprobe XML output into ffprobeType dataclass using JSON dict.

    Args:
        xml_string: The XML string to parse

    Returns:
        The parsed ffprobeType instance
    """
    json_str = xml_string_to_json(xml_string)
    json_dict = json.loads(json_str)
    # The root key is 'ffprobe'
    root_data = json_dict.get("ffprobe", json_dict)
    return _parse_obj_from_dict(root_data, ffprobeType) or ffprobeType()
