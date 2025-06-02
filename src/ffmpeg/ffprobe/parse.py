#!/usr/bin/env python3

import types
import xml.etree.ElementTree as ET
from typing import Any, TypeVar, Union, get_args, get_origin, get_type_hints

from .schema import ffprobeType, registered_types, tagsType, tagType

T = TypeVar("T")


def _get_actual_type(type_hint: Any) -> type[Any]:
    """Get the actual type from a type hint, handling Optional and Union (including | syntax)."""
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


def _parse_optional_type(value: str, type_hint: type[Any]) -> Any:
    """Parse a string value into the appropriate type based on type hint."""
    if value is None:
        return None

    actual_type = _get_actual_type(type_hint)
    print(f"Parsing value: {value!r} as {actual_type!r}")

    if actual_type is str:
        return value
    elif actual_type is int:
        return int(value)
    elif actual_type is float:
        return float(value)
    elif actual_type is bool:
        return value.lower() == "true"
    else:
        return value


def _parse_tags(element: ET.Element) -> tagsType | None:
    """Parse tags from an XML element."""
    tags = []
    for tag in element.findall(".//tag"):
        key = tag.get("key")
        value = tag.get("value")
        if key and value:
            tags.append(tagType(key=key, value=value))
    return tagsType(tag=tuple(tags)) if tags else None


def _parse_dataclass(element: ET.Element, cls: type[T]) -> T:
    """Parse an XML element into a dataclass instance."""
    type_hints = get_type_hints(cls)
    kwargs: dict[str, Any] = {}

    # Handle nested elements
    for field_name, field_type in type_hints.items():
        if field_name == "tags":
            kwargs[field_name] = _parse_tags(element)
            continue

        # Handle nested dataclass fields
        actual_type = _get_actual_type(field_type)
        if hasattr(actual_type, "__dataclass_fields__"):
            nested_elem = element.find(field_name)
            if nested_elem is not None:
                kwargs[field_name] = _parse_dataclass(nested_elem, actual_type)
            continue

        # Handle tuple fields (for lists of items)
        if get_origin(field_type) is tuple:
            item_type = get_args(field_type)[0]
            if hasattr(item_type, "__dataclass_fields__"):
                items = []
                for item_elem in element.findall(field_name):
                    items.append(_parse_dataclass(item_elem, item_type))
                kwargs[field_name] = tuple(items) if items else None
                continue

        # Handle simple attributes
        value = element.get(field_name)
        if value is not None:
            print(
                f"_parse_dataclass: field={field_name}, value={value!r}, type_hint={field_type!r}"
            )
            kwargs[field_name] = _parse_optional_type(value, field_type)

    return cls(**kwargs)


def parse_ffprobe(xml_string: str) -> ffprobeType:
    """Parse ffprobe XML output into ffprobeType dataclass."""
    root = ET.fromstring(xml_string)
    return _parse_dataclass(root, ffprobeType)
