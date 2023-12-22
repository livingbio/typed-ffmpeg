import re
from typing import Any

from .schema import AVFilter, AVOption


def parse_option_str(text: str) -> list[Any]:

    buffer = ""
    level = 0
    output = []
    in_text = False

    text = text.strip()

    for idx, ch in enumerate(text):
        match ch:
            case '"' if text[idx - 1] != "\\":
                in_text = not in_text
                buffer += ch
            case "," if not in_text and level == 1:
                if buffer.strip():
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


def parse_av_option(text: str) -> list[AVOption]:
    # the meaning of option_str please see libavutil/opt.h::AVOption
    option_lines = parse_option_str(text)
    print(option_lines)

    output: list[AVOption] = []

    def _v(s: str) -> float | str:
        if "0x" in s:
            return int(s, 16)
        try:
            return float(s)
        except ValueError:
            return s

    def _d(s: tuple[str]) -> int | float | str:
        text = s[0]
        type, value = [k.strip() for k in text.split("=")]

        match type:
            case ".i64":
                try:
                    return int(value)
                except ValueError:
                    return value
            case ".dbl":
                return float(value)
            case ".str":
                return value.strip('"')
            case _:
                raise NotImplementedError(type)

    for option_line in option_lines:
        if isinstance(option_line, str):
            continue

        if len(option_line) in {8, 9}:
            name, help, offset, _type, default, _min, _max, flags = option_line[:8]
            unit = option_line[8].strip('"') if len(option_line) == 9 else None

            output.append(
                AVOption(
                    name=name.strip('"'),
                    help=help.strip('"'),
                    #    offset=int(offset),
                    type=_type,
                    default=_d(default),
                    min=_v(_min),
                    max=_v(_max),
                    flags=flags,
                    unit=unit,
                )
            )
        else:
            print(option_line)

    return output


def extract_av_options(text: str) -> list[AVFilter]:
    output = []
    for filter, option_str in re.findall(
        r"static const AVOption ([\w\_]+)_options\[\] = ({.*?});", text, re.DOTALL | re.MULTILINE
    ):
        print(f"{filter} {option_str}")
        output.append(AVFilter(name=filter, description="", options=parse_av_option(option_str)))

    return output
