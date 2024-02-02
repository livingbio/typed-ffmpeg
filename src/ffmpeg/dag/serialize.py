from __future__ import absolute_import, annotations

import datetime
import json  # noqa
from dataclasses import fields, is_dataclass
from enum import Enum
from typing import Any, TypeVar, cast

T = TypeVar("T")


def load_class(path: str) -> Any:
    module_path, class_name = path.rsplit(".", 1)
    module = __import__(module_path, fromlist=[class_name])
    return getattr(module, class_name)


class Encoder(json.JSONEncoder):
    # Extend JSON encoder to support more type, especial for Schematic Model
    # NOTE: it won't validate schematic model during encode / decode

    def default(self, obj: Any) -> Any:
        if isinstance(obj, Enum):
            return {
                "__class__": f"{obj.__class__.__module__}.{obj.__class__.__name__}",
                "value": obj.value,
            }
        elif isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S.%f%z")
        elif is_dataclass(obj):
            output = {}
            for field in fields(obj):
                v = getattr(obj, field.name)
                output[field.name] = self.default(v)

            return {
                "__class__": f"{obj.__class__.__module__}.{obj.__class__.__name__}",
                **output,
            }
        return obj


class Decoder(json.JSONDecoder):
    # Extend JSON decoder to support more type

    def __init__(self, *args: Any, **kwargs: Any):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def frozen(self, v: Any) -> Any:
        if isinstance(v, list):
            return tuple(self.frozen(i) for i in v)

        if isinstance(v, dict):
            return tuple((key, self.frozen(value)) for key, value in v.items())

        return v

    def object_hook(self, obj: Any) -> Any:  # pylint: disable=method-hidden
        if isinstance(obj, dict):
            if obj.get("__class__"):
                cls = load_class(obj.pop("__class__"))

                if is_dataclass(cls):
                    # NOTE: in our application, the dataclass is always frozen
                    return cls(**{k: self.frozen(v) for k, v in obj.items()})

                return cls(**{k: v for k, v in obj.items()})

        return obj


def loads(cls: type[T], raw: str) -> T:
    data = json.loads(raw, cls=Decoder)
    return cast(T, data)


# Serialization
def dumps(instance: Any) -> str:
    return json.dumps(instance, cls=Encoder)
