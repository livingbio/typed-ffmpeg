from typing import Any


def parse_c_structure(text: str) -> list[Any]:

    buffer = ""
    level = 0
    output = []
    in_text = False
    in_bracket = False

    text = text.strip()

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
                    output.append(buffer.strip())
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
        output.append(buffer.strip())

    return output
