import re

from .parse_c_structure import parse_c_structure
from .schema import AVOption


def _parse_av_option(text: str) -> list[AVOption]:
    # the meaning of option_str please see libavutil/opt.h::AVOption
    option_lines = parse_c_structure(text)

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
        type, value = [k.strip() for k in text.split("=", 1)]

        match type:
            case ".i64":
                try:
                    return int(value)
                except ValueError:
                    return value
            case ".dbl":
                try:
                    return float(value)
                except ValueError:
                    return value
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

    return output


def parse_av_option(text: str) -> dict[str, list[AVOption]]:
    output = {}
    for filter, option_str in re.findall(
        r"static const AVOption ([\w\_]+)\[\] = ({.*?});", text, re.DOTALL | re.MULTILINE
    ):
        output[filter] = _parse_av_option(option_str)
    return output
