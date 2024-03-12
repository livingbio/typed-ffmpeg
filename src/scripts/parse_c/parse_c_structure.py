import re
from typing import Any


def remove_string_concat(text: str) -> str:
    """
    Remove string concatenation from a string

    Args:
        text: The string to remove string concatenation from

    Returns:
        The string with string concatenation removed
    """

    if text.count('"') > 2:
        return re.sub(r"\"\s*\"", "", text)
    return text


def parse_c_structure(text: str) -> list[Any]:
    """
    Parse a C structure from a string

    Args:
        text: The string to parse

    Returns:
        The parsed C structure
    """

    buffer = ""
    level = 0
    output: list[Any] = []
    in_text = False
    in_bracket = False

    text = text.strip()

    # ignore Line Directives
    lines = text.split("\n")
    text = "\n".join(line for line in lines if not line.strip().startswith("#"))

    for idx, ch in enumerate(text):
        match ch:
            case '"' if text[idx - 1] != "\\":
                in_text = not in_text
                buffer += ch
            case "(" if not in_text:
                in_bracket = True
                buffer += ch
            case ")" if not in_text and in_bracket:
                in_bracket = False
                buffer += ch
            case "," if not in_text and not in_bracket and level == 1:
                if buffer.strip():
                    output.append(remove_string_concat(buffer.strip()))
                buffer = ""
            case "{" if not in_text and not in_bracket:
                level += 1
                if level > 1:
                    buffer += ch
            case "}" if not in_text and not in_bracket:
                level -= 1

                if level == 1:
                    output.append(parse_c_structure(buffer))
                    buffer = ""
                elif level > 1:
                    buffer += ch
            case _:
                buffer += ch

    if buffer.strip():
        output.append(remove_string_concat(buffer.strip()))

    return output
