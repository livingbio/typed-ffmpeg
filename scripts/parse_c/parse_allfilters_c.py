import pathlib
import re


def parse_all_filter_names(path: pathlib.Path) -> list[tuple[str, str, str]]:
    with path.open() as f:
        code = f.read()

    output = []
    for line in re.findall(r"extern const AVFilter ([\w\_]+);", code):
        _, flag, name = line.split("_", 2)
        output.append((flag, name, line))

    return output
