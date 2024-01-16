from typing import Any, Iterable


def escape(text: str | int | float, chars: str = "\\'=:") -> str:
    """Helper function to escape uncomfortable characters."""
    text = str(text)
    _chars = list(set(chars))
    if "\\" in _chars:
        _chars.remove("\\")
        _chars.insert(0, "\\")

    for ch in _chars:
        text = text.replace(ch, "\\" + ch)

    return text


def convert_kwargs_to_cmd_line_args(kwargs: dict[str, Any]) -> list[str]:
    """Helper function to build command line arguments out of dict."""
    args = []
    for k in sorted(kwargs.keys()):
        v = kwargs[k]
        if isinstance(v, Iterable) and not isinstance(v, str):
            for value in v:
                args.append("-{}".format(k))
                if value is not None:
                    args.append("{}".format(value))
            continue
        args.append("-{}".format(k))
        if v is not None:
            args.append("{}".format(v))
    return args
