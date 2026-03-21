"""Cache utilities for FFmpeg operations."""

import sys
from pathlib import Path
from typing import TypeVar

from .serialize import dumps, loads

T = TypeVar("T")


def get_cache_path() -> Path:
    """
    Get the cache directory path.

    Returns the cache directory path, creating it if it doesn't exist.
    When running as a frozen application (e.g., PyInstaller), uses the
    temporary extraction directory. Otherwise, uses the cache subdirectory
    relative to this module.

    Returns:
        Path: The cache directory path

    """
    if getattr(sys, "frozen", False):
        base_path = Path(getattr(sys, "_MEIPASS", ""))
    else:
        base_path = Path(__file__).parent

    cache_path = base_path / "cache"
    cache_path.mkdir(exist_ok=True)
    return cache_path


cache_path = get_cache_path()


def load(cls: type[T], id: str) -> T:
    """
    Load an object from the cache.

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
    Save an object to the cache.

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
    List all objects of a class in the cache.

    Args:
        cls: The class of the objects

    Returns:
        A list of all objects of the class in the cache

    """
    path = cache_path / f"{cls.__name__}"

    return [loads(i.read_text()) for i in path.glob("*.json")]


def clean(cls: type[T]) -> None:
    """Clean the cache for a class."""
    path = cache_path / f"{cls.__name__}"
    for i in path.glob("*.json"):
        i.unlink()
