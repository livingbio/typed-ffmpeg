import pathlib
from pathlib import Path

import jinja2

from .schema import FFmpegFilter

template_path = Path(__file__).parent / "templates"

loader = jinja2.FileSystemLoader(template_path)
env = jinja2.Environment(
    loader=loader,
)


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
