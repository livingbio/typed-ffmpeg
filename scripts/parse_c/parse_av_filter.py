import re

from .parse_c_structure import parse_c_structure
from .schema import AVFilter


def parse_av_filter(text: str) -> dict[str, AVFilter]:
    output = {}
    for filter, filter_desc in re.findall(r"const AVFilter ([\w\_]+)\s*=\s*({.*?});", text, re.DOTALL | re.MULTILINE):
        descs: list[str] = parse_c_structure(filter_desc)
        config = {}
        for desc in descs:
            if "=" not in desc:
                continue

            var, value = desc.split("=", 1)
            config[var.strip()] = value.strip('" ')

        output[filter] = AVFilter(
            id=filter,
            name=config[".name"],
            description=config[".description"],
            priv_class=config.get(".priv_class"),
            flags=config.get(".flags"),
            inputs=config.get(".inputs"),
            outputs=config.get(".outputs"),
            init=config.get(".init"),
        )
    return output
