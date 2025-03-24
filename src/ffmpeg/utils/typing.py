"""
Typing utilities for enhanced type annotations.

This module provides utilities for improving type annotations and enforcing
typing conventions within the codebase, offering better support for type checking
and documentation.
"""

from typing import TypeVar

V = TypeVar("V")


def override(func: V) -> V:
    """
    Decorator to indicate a method that overrides a method in a superclass.

    This decorator serves as a placeholder until Python 3.12, which introduces
    a built-in @override decorator. Using this decorator helps with code clarity
    and can catch errors where a method intended to override a parent class method
    doesn't actually override anything (e.g., due to a typo in the method name).

    Args:
        func: The function to mark as an override of a superclass method

    Returns:
        The original function, unchanged (the decorator is used only for documentation)

    Example:
        ```python
        class Parent:
            def method(self):
                pass


        class Child(Parent):
            @override
            def method(self):  # Correctly overrides Parent.method
                pass
        ```
    """
    return func
