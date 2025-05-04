from pathlib import Path
from typing import TypeVar

from .serialize import dumps, loads

T = TypeVar("T")

cache_path = Path(__file__).parent / "cache"
cache_path.mkdir(exist_ok=True)


def load(cls: type[T], id: str) -> T:
    """
    Load an object from the cache

    Args:
        cls: The class of the object
        id: The id of the object

    Returns:
        The loaded object
    """
    path = cache_path / f"{cls.__name__}/{id}.json"

    with path.open() as ifile:
        obj = loads(ifile.read())
        return obj


def save(obj: T, id: str) -> None:
    """
    Save an object to the cache

    Args:
        obj: The object to save
        id: The id of the object
    """
    schema_path = cache_path / f"{obj.__class__.__name__}"
    schema_path.mkdir(exist_ok=True)

    with (schema_path / f"{id}.json").open("w") as ofile:
        ofile.write(dumps(obj))


def list_all(cls: type[T]) -> list[T]:
    """
    List all objects of a class in the cache

    Args:
        cls: The class of the objects

    Returns:
        A list of all objects of the class in the cache
    """
    path = cache_path / f"{cls.__name__}"

    return [loads(i.read_text()) for i in path.glob("*.json")]


def clean(cls: type[T]) -> None:
    """
    Clean the cache for a class
    """
    path = cache_path / f"{cls.__name__}"
    for i in path.glob("*.json"):
        i.unlink()
