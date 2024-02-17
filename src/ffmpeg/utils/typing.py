from typing import TypeVar

V = TypeVar("V")


def override(func: V) -> V:
    """
    Decorator to indicate overriding a method.
    the true override method is implemented until in python 3.12

    Args:
        func: The function to decorate.

    Returns:
        The decorated function.
    """
    return func
