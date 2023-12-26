import keyword
import pathlib
from pathlib import Path

import jinja2

from .schema import FFmpegFilter

template_path = Path(__file__).parent / "templates"

loader = jinja2.FileSystemLoader(template_path)
env = jinja2.Environment(
    loader=loader,
)


def stream_name_safe(string: str) -> str:
    opt_name = option_name_safe(string)
    if not opt_name.startswith("_"):
        return "_" + opt_name
    return opt_name


def option_name_safe(string: str) -> str:
    if string in keyword.kwlist:
        return "_" + string
    if string[0].isdigit():
        return "_" + string
    if "-" in string:
        return string.replace("-", "_")

    return string


env.filters["stream_name_safe"] = stream_name_safe
env.filters["option_name_safe"] = option_name_safe


def render(filters: list[FFmpegFilter], outpath: pathlib.Path) -> list[pathlib.Path]:
    outpath.mkdir(exist_ok=True)
    output = []
    for template_file in template_path.glob("*.py.jinja"):
        template = env.get_template(template_file.name)
        code = template.render(filters=filters)

        opath = outpath / template_file.name.replace(".jinja", "")
        with opath.open("w") as ofile:
            ofile.write(code)

        output.append(opath)

    return output
