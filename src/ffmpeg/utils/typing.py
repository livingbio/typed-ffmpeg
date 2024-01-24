from typing import TypeVar

V = TypeVar("V")


def override(func: V) -> V:
    return func
