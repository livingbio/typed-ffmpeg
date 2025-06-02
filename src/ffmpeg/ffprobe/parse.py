#!/usr/bin/env python3

import json
import types
from typing import Any, TypeVar, Union, get_args, get_origin, get_type_hints

from .schema import ffprobeType, registered_types, tagsType, tagType
from .xml2json import xml_string_to_json

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


def _parse_optional_type(value: Any, type_hint: type[Any]) -> Any:
    """Parse a string value into the appropriate type based on type hint."""
    if value is None:
        return None

    actual_type = _get_actual_type(type_hint)
    print(f"Parsing value: {value!r} as {actual_type!r}")

    if actual_type is str:
        return str(value)
    elif actual_type is int:
        return int(value)
    elif actual_type is float:
        return float(value)
    elif actual_type is bool:
        return str(value).lower() == "true"
    else:
        return value


def _parse_tags_from_dict(tags: Any) -> tagsType | None:
    """Parse tags from a dictionary."""
    if not tags or "tag" not in tags:
        return None
    tag_list = tags["tag"]
    if isinstance(tag_list, dict):
        tag_list = [tag_list]
    result = []
    for tag in tag_list:
        key = tag.get("key")
        value = tag.get("value")
        if key is not None and value is not None:
            result.append(tagType(key=key, value=value))
    return tagsType(tag=tuple(result)) if result else None


def _parse_dataclass_from_dict(data: dict[str, Any], cls: type[T]) -> T:
    """Parse a dictionary into a dataclass instance."""
    type_hints = get_type_hints(cls)
    kwargs: dict[str, Any] = {}
    for field_name, field_type in type_hints.items():
        if field_name == "tags":
            tags_data = data.get("tags") or data.get("tag")
            kwargs[field_name] = _parse_tags_from_dict(
                {"tag": tags_data} if tags_data else None
            )
            continue
        actual_type = _get_actual_type(field_type)
        if hasattr(actual_type, "__dataclass_fields__"):
            nested_data = data.get(field_name)
            if nested_data is not None:
                kwargs[field_name] = _parse_dataclass_from_dict(
                    nested_data, actual_type
                )
            continue
        if get_origin(field_type) is tuple:
            item_type = get_args(field_type)[0]
            if hasattr(item_type, "__dataclass_fields__"):
                items_data = data.get(field_name)
                if items_data is not None:
                    # Handle both single dict and list of dicts
                    if isinstance(items_data, dict):
                        items_data = [items_data]
                    elif not isinstance(items_data, list):
                        items_data = []
                    items = [
                        _parse_dataclass_from_dict(item, item_type)
                        if isinstance(item, dict)
                        else item
                        for item in items_data
                    ]
                    kwargs[field_name] = tuple(items) if items else None
                else:
                    kwargs[field_name] = None
                continue
        value = data.get(field_name)
        if value is not None:
            kwargs[field_name] = _parse_optional_type(value, field_type)
    return cls(**kwargs)


def parse_ffprobe(xml_string: str) -> ffprobeType:
    """Parse ffprobe XML output into ffprobeType dataclass using JSON dict."""
    json_str = xml_string_to_json(xml_string)
    json_dict = json.loads(json_str)
    # The root key is 'ffprobe'
    root_data = json_dict.get("ffprobe", json_dict)
    return _parse_dataclass_from_dict(root_data, ffprobeType)
