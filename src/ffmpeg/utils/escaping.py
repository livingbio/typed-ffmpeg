from collections.abc import Iterable
from typing import Any


def escape(text: str | int | float, chars: str = "\\'=:") -> str:
    """
    Helper function to escape uncomfortable characters.

    Args:
        text: The text to escape.
        chars: The characters to escape.

    Returns:
        The escaped text.
    """
    text = str(text)
    _chars = list(set(chars))
    if "\\" in _chars:
        _chars.remove("\\")
        _chars.insert(0, "\\")

    for ch in _chars:
        text = text.replace(ch, "\\" + ch)

    return text


def convert_kwargs_to_cmd_line_args(kwargs: dict[str, Any]) -> list[str]:
    """
    Helper function to build command line arguments out of dict.

    Args:
        kwargs: The dict to convert.

    Returns:
        The command line arguments.
    """
    args = []
    for k in sorted(kwargs.keys()):
        v = kwargs[k]
        if isinstance(v, Iterable) and not isinstance(v, str):
            for value in v:
                args.append(f"-{k}")
                if value is not None:
                    args.append(f"{value}")
            continue
        args.append(f"-{k}")
        if v is not None:
            args.append(f"{v}")
    return args
