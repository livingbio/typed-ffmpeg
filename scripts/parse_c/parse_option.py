from typing import Any


def parse_option_str(text: str) -> list[Any]:

    buffer = ""
    level = 0
    output = []
    in_text = False

    text = text.strip()

    for idx, ch in enumerate(text):
        print(f"{ch=} {buffer=} {level=} {in_text=}")

        match ch:
            case '"' if text[idx - 1] != "\\":
                in_text = not in_text
                buffer += ch
            case "," if not in_text and level == 1:
                output.append(buffer.strip())
                buffer = ""
            case "{" if not in_text:
                level += 1
                if level > 1:
                    buffer += ch
            case "}" if not in_text:
                level -= 1

                if level == 1:
                    output.append(parse_option_str(buffer))
                    buffer = ""
                elif level > 1:
                    buffer += ch
            case _:
                buffer += ch

    if buffer.strip():
        output.append(buffer.strip())

    return output
