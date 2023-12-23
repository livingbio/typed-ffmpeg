import re

from .parse_c_structure import parse_c_structure
from .schema import AVFilterPad


def parse_av_filter_pad(text: str) -> dict[str, AVFilterPad]:
    output = {}
    for filter, filter_desc in re.findall(
        r"static const AVFilterPad ([\w\_]+)\[\]\s*=\s*({.*?});", text, re.DOTALL | re.MULTILINE
    ):
        descs: list[str] = parse_c_structure(filter_desc)[0]
        config = {}
        for desc in descs:
            if "=" not in desc:
                continue

            var, value = desc.split("=", 1)
            config[var.strip()] = value.strip('" ')

        output[filter] = AVFilterPad(
            name=config[".name"],
            type=config[".type"],
        )
    return output
