import re

from .parse_c_structure import parse_c_structure
from .schema import OptionDef


def parse_ffmpeg_opt_c(text: str) -> list[OptionDef]:
    match = re.findall(r"const OptionDef options\[\] = (\{.*?\n\})", text, re.MULTILINE | re.DOTALL)
    data = parse_c_structure(match[0])

    output = []

    for line in data:
        if len(line) == 4:
            name, flags, _, help = line
            arg_name = None
        elif len(line) == 5:
            name, flags, _, help, arg_name = line
        elif len(line) == 1:
            continue
        else:
            raise ValueError(line)

        name = name.strip('"')
        help = help.strip('"')
        arg_name = arg_name.strip('"') if arg_name else None
        flags = flags.replace("\n", "")
        flags = eval(flags)
        output.append(OptionDef(name=name, flags=flags, help=help, argname=arg_name))

    return output
