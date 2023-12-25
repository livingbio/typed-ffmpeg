import re

from .parse_c_structure import parse_c_structure
from .schema import AVOption


def _p(string: str, assert_key: str = None) -> str:
    if not "=" in string or not string.startswith("."):
        return string

    key, value = string.split("=", 1)
    key = key.strip()[1:]
    if assert_key:
        assert assert_key == key.strip(), string

    return string


def _aligns(values: list[str]) -> dict[str, str]:
    vars = ["name", "help", "offset", "type", "default", "min", "max", "flags", "unit"]
    output = {}

    assert len(values) <= len(vars), values
    j = 0

    for i, var in enumerate(vars):
        if j < len(values):
            try:
                v = _p(values[j], var)
                output[var] = v
                j += 1
            except AssertionError:
                output[var] = None
        else:
            output[var] = None

    assert j == len(values), values
    return output


def _parse_av_option(text: str) -> list[AVOption]:
    # the meaning of option_str please see libavutil/opt.h::AVOption
    option_lines = parse_c_structure(text)

    output: list[AVOption] = []

    def _eval_avoption(
        _name: str,
        _help: str,
        _offset: str,
        _type: str,
        _default: str = None,
        _min: str = None,
        _max: str = None,
        _flags: str = None,
        _unit: str = None,
    ) -> AVOption:
        return AVOption(
            name=_name.strip('"'),
            help=_help.strip('"'),
            offset=_offset,
            type=_type,
            default=_default,
            min=_min,
            max=_max,
            flags=_flags,
            unit=_unit and _unit.strip('"'),
        )

    for option_line in option_lines:
        if isinstance(option_line, str):
            continue

        # NOTE: convert all to string (otherwise default will be list)
        option_line = [str(k) for k in option_line]

        if len(option_line) < 4:
            continue

        kwargs = _aligns(option_line)
        output.append(_eval_avoption(**{"_" + k: v for k, v in kwargs.items()}))

    return output


def parse_av_option(text: str) -> dict[str, list[AVOption]]:
    output = {}
    for filter, option_str in re.findall(
        r"static const AVOption ([\w\_]+)\[\]\s*=\s*({.*?});", text, re.DOTALL | re.MULTILINE
    ):
        output[filter] = _parse_av_option(option_str)
    return output
