from pathlib import Path
from typing import TypeVar

from ..common.serialize import dumps, loads

T = TypeVar("T")

cache_path = Path(__file__).parent / "cache"
cache_path.mkdir(exist_ok=True)


def load(cls: type[T], id: str) -> T:
    path = cache_path / f"{cls.__name__}/{id}.json"

    with path.open() as ifile:
        obj = loads(ifile.read())
        return obj


def save(obj: T, id: str) -> None:
    schema_path = cache_path / f"{obj.__class__.__name__}"
    schema_path.mkdir(exist_ok=True)

    with (schema_path / f"{id}.json").open("w") as ofile:
        ofile.write(dumps(obj))
