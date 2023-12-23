import re

from .parse_c_structure import parse_c_structure
from .schema import AVOption


def _parse_av_option(text: str) -> list[AVOption]:
    # the meaning of option_str please see libavutil/opt.h::AVOption
    option_lines = parse_c_structure(text)

    output: list[AVOption] = []

    def _eval_avoption(
        name: str,
        help: str,
        offset: str,
        _type: str,
        default: str = None,
        _min: str = None,
        _max: str = None,
        flags: str = None,
        unit: str = None,
    ) -> AVOption:
        return AVOption(
            name=name.strip('"'),
            help=help.strip('"'),
            offset=offset,
            type=_type,
            default=default,
            min=_min,
            max=_max,
            flags=flags,
            unit=unit and unit.strip('"'),
        )

    def _p(string: str, assert_key: str = None) -> str:
        if not string.startswith("."):
            return string

        assert "=" in string, string

        key, value = string.split("=", 1)
        key = key.strip()[1:]
        if assert_key:
            assert key == key.strip(), string

        return value.strip('" ')

    for option_line in option_lines:
        if isinstance(option_line, str):
            continue

        # NOTE: convert all to string (otherwise default will be list)
        option_line = [str(k) for k in option_line]

        match len(option_line):
            case 9:
                output.append(_eval_avoption(*option_line))
            case 8:
                output.append(_eval_avoption(*option_line))
            case 7:
                # { "size", "set video size", __builtin_offsetof(ScaleContext, size_str), AV_OPT_TYPE_STRING, {.str = ((void*)0)}, 0, 16|(1<<16) },
                name, help, offset, _type, default, a, b = option_line
                if b.startswith(".flags"):
                    flags, _min = b, a
                    output.append(
                        _eval_avoption(name, help, offset, _type, default=default, _min=_min, flags=_p(flags, "flags"))
                    )
                elif a.startswith(".flags"):
                    flags, unit = a, b
                    output.append(
                        _eval_avoption(
                            name, help, offset, _type, default=default, flags=_p(flags, "flags"), unit=_p(unit, "unit")
                        )
                    )
            case 6:
                # { "flags", "Flags to pass to libswscale", __builtin_offsetof(ScaleContext, flags_str), AV_OPT_TYPE_STRING, { .str = "" }, .flags = 16|(1<<16) },
                name, help, offset, _type, default, flags = option_line
                output.append(_eval_avoption(name, help, offset, _type, default=default, flags=_p(flags, "flags")))
            case 5:
                # { "w", "Output video width", __builtin_offsetof(ScaleContext, w_expr), AV_OPT_TYPE_STRING, .flags = 16|(1<<16)|(1<<15) },
                name, help, offset, _type, flags = option_line
                output.append(_eval_avoption(name, help, offset, _type, flags=_p(flags, "flags")))
            case _ if len(option_line) > 4:
                raise NotImplementedError(option_line)
            case _:
                print(option_line)

    return output


def parse_av_option(text: str) -> dict[str, list[AVOption]]:
    output = {}
    for filter, option_str in re.findall(
        r"static const AVOption ([\w\_]+)\[\]\s*=\s*({.*?});", text, re.DOTALL | re.MULTILINE
    ):
        output[filter] = _parse_av_option(option_str)
    return output
