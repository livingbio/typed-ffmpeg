from typing import Any
import jinja2
from .schema import FFMpegCodec, FFMpegFilter, FFMpegOption, FFMpegFormat
from pathlib import Path

def render(
    template_folder: Path,
    outpath: Path,
    **kwargs: Any
) -> list[Path]:
    """
    Render the filter and option documents

    Args:
        filters: The filters
        options: The options
        codecs: The codecs
        outpath: The output path

    Returns:
        The rendered files
    """
    loader = jinja2.FileSystemLoader(template_folder)
    env = jinja2.Environment(
        loader=loader,
    )

    outpath.mkdir(exist_ok=True)
    output = []

    for template_file in template_folder.glob("**/*.jinja"):
        template_path = template_file.relative_to(template_folder)

        template = env.get_template(str(template_path))
        code = template.render(**kwargs)

        opath = outpath / str(template_path).replace(".jinja", "")
        opath.parent.mkdir(parents=True, exist_ok=True)

        with opath.open("w") as ofile:
            ofile.write(code)

        output.append(opath)

    return output
