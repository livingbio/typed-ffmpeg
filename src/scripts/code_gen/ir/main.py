from pathlib import Path
from typing import Any
from ...parse_help import parse_codecs
import jinja2

class CodeGen:
    def __init__(self, template_folder: Path, outpath: Path):
        self.template_folder = template_folder
        self.outpath = outpath
        self.loader = jinja2.FileSystemLoader(self.template_folder)
        self.env = jinja2.Environment(
            loader=self.loader,
        )

    def render(self, **kwargs: Any) -> list[Path]:
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
        self.outpath.mkdir(exist_ok=True)
        output = []

        for template_file in self.template_folder.glob("**/*.jinja"):
            template_path = template_file.relative_to(self.template_folder)

            template = self.env.get_template(str(template_path))
            code = template.render(**kwargs)

            opath = self.outpath / str(template_path).replace(".jinja", "")
            opath.parent.mkdir(parents=True, exist_ok=True)

            with opath.open("w") as ofile:
                ofile.write(code)

            output.append(opath)

        return output

    def context(self) -> dict[str, Any]:
        return {
            "codecs": parse_codecs.extract(),
        }