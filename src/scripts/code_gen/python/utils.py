import keyword

from ..schema import FFMpegAVOptionIR


def safe_name(string: str) -> str:
    """
    Convert option name to safe name

    Args:
        string: The option name

    Returns:
        The option name safe
    """
    if string in keyword.kwlist:
        return "_" + string
    if string[0].isdigit():
        return "_" + string
    if "-" in string:
        return string.replace("-", "_")

    return string


def option_typing(option: FFMpegAVOptionIR) -> str:
    base_type = option.type.capitalize()

    if not option.choices:
        return base_type

    values = ",".join(f'"{i.name}"' for i in option.choices)
    return base_type + f"| Literal[{values}]"
