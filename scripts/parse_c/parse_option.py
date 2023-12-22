import re
from typing import Any

from .schema import AVFilter, AVOption


def parse_option_str(text: str) -> list[Any]:

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


def parse_av_filter(text: str) -> list[AVFilter]:
    output = []
    for filter, filter_desc in re.findall(r"const AVFilter ([\w\_]+) = ({.*});", text, re.DOTALL | re.MULTILINE):
        descs: list[str] = parse_option_str(filter_desc)
        config = {}
        for desc in descs:
            if "=" not in desc:
                continue

            var, value = desc.split("=", 1)
            config[var.strip()] = value.strip()

        output.append(AVFilter(name=config[".name"].strip('"'), description=config[".description"].strip('"')))
    return output


def parse_av_options(text: str) -> dict[str, list[AVOption]]:
    output = {}
    for filter, option_str in re.findall(
        r"static const AVOption ([\w\_]+)_options\[\] = ({.*?});", text, re.DOTALL | re.MULTILINE
    ):
        output[filter] = parse_av_option(option_str)
    return output


def extract_av_options(text: str) -> list[AVFilter]:
    output = []

    av_options = parse_av_options(text)
    av_filters = parse_av_filter(text)

    for av_filter in av_filters:
        av_filter.options = av_options.get(av_filter.name, [])
        output.append(av_filter)

    return output
