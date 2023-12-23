import re

from .parse_c_structure import parse_c_structure
from .schema import AVFilter


def parse_av_filter(text: str) -> list[AVFilter]:
    output = []
    for filter, filter_desc in re.findall(r"const AVFilter ([\w\_]+) = ({.*?});", text, re.DOTALL | re.MULTILINE):
        descs: list[str] = parse_c_structure(filter_desc)
        config = {}
        for desc in descs:
            if "=" not in desc:
                continue

            var, value = desc.split("=", 1)
            config[var.strip()] = value.strip()

        output.append(
            AVFilter(
                name=config[".name"].strip('"'),
                description=config[".description"].strip('"'),
            )
        )
    return output
