import pathlib
import re


def all_filter_names(path: pathlib.Path) -> list[str]:
    with path.open() as f:
        code = f.read()
    return re.findall(r"extern const AVFilter ([\w\_]+);", code)
