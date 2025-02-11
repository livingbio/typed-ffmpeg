from __future__ import annotations

import importlib
import json
from dataclasses import fields, is_dataclass
from enum import Enum
from functools import partial
from pathlib import Path
from typing import Any


def load_class(path: str, strict: bool = True) -> Any:
    """
    Load a class from a string path

    Args:
        path: The path to the class.
        strict: If True, raise an error if the class is not in ffmpeg package.

    Returns:
        The class.
    """
    if strict:
        assert path.startswith("ffmpeg."), (
            f"Only support loading class from ffmpeg package: {path}"
        )

    module_path, class_name = path.rsplit(".", 1)
    module = importlib.import_module(module_path)
    return getattr(module, class_name)


def frozen(v: Any) -> Any:
    """
    Convert the instance to a frozen instance

    Args:
        v: The instance to convert.

    Returns:
        The frozen instance.
    """
    if isinstance(v, list):
        return tuple(frozen(i) for i in v)

    if isinstance(v, dict):
        return tuple((key, frozen(value)) for key, value in v.items())

    return v


def object_hook(obj: Any, strict: bool = True) -> Any:
    """
    Convert the dictionary to an instance

    Args:
        obj: The dictionary to convert.

    Returns:
        The instance.
    """
    if isinstance(obj, dict):
        if obj.get("__class__"):
            cls = load_class(obj.pop("__class__"), strict=strict)

            if is_dataclass(cls):
                # NOTE: in our application, the dataclass is always frozen
                return cls(**{k: frozen(v) for k, v in obj.items()})

            return cls(**dict(obj.items()))

    return obj


def loads(raw: str, strict: bool = True) -> Any:
    """
    Deserialize the JSON string to an instance

    Args:
        raw: The JSON string to deserialize.

    Returns:
        The deserialized instance.
    """
    object_hook_strict = partial(object_hook, strict=strict)

    return json.loads(raw, object_hook=object_hook_strict)


def to_dict_with_class_info(instance: Any) -> Any:
    """
    Convert the instance to a dictionary with class information

    Args:
        instance: The instance to convert.

    Returns:
        The dictionary with class information
    """

    if isinstance(instance, dict):
        return {k: to_dict_with_class_info(v) for k, v in instance.items()}
    elif isinstance(instance, list):
        return [to_dict_with_class_info(v) for v in instance]
    elif isinstance(instance, tuple):
        return tuple(to_dict_with_class_info(v) for v in instance)
    elif isinstance(instance, Path):
        return str(instance)
    elif is_dataclass(instance):
        return {
            "__class__": f"{instance.__class__.__module__}.{instance.__class__.__name__}",
            **{
                k.name: to_dict_with_class_info(getattr(instance, k.name))
                for k in fields(instance)
            },
        }
    elif isinstance(instance, Enum):
        return {
            "__class__": f"{instance.__class__.__module__}.{instance.__class__.__name__}",
            "value": instance.value,
        }
    return instance


# Serialization
def dumps(instance: Any) -> str:
    """
    Serialize the instance to a JSON string

    Args:
        instance: The instance to serialize.

    Returns:
        The serialized instance.
    """
    obj = to_dict_with_class_info(instance)
    return json.dumps(obj, indent=2)
