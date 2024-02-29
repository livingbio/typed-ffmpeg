import re

from .parse_c_structure import parse_c_structure
from .schema import OptionDef


def parse_ffmpeg_opt_c(text: str) -> list[OptionDef]:
    match = re.findall(r"const OptionDef options\[\] = (\{.*?\n\})", text, re.MULTILINE | re.DOTALL)
    data = parse_c_structure(match[0])

    output: dict[str, OptionDef] = {}

    for line in data:
        name = None
        type = None
        flags = None
        help = None
        arg_name = None
        canon = None

        if len(line) == 5:
            name, type, flags, _, help = line
        elif len(line) == 6:
            name, type, flags, _, help, arg_name = line
        elif len(line) == 7:
            name, type, flags, _, help, arg_name, canon = line
        elif len(line) == 1:
            continue
        else:
            raise ValueError(line)

        name = name.strip('"')
        help = help.strip('"')
        arg_name = arg_name.strip('"') if arg_name else None
        flags = flags.replace("\n", "")
        flags = eval(flags)
        output[name] = OptionDef(name=name, type=type, flags=flags, help=help, argname=arg_name, canon=canon)

    # process canon
    for opt in output.values():
        if opt.canon and "name_canon" in opt.canon:
            ref = opt.canon.split("=")[1].strip().strip('"')
            opt.type = output[ref].type

    return output.values()
