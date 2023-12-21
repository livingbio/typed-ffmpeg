import pathlib

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    document_path: pathlib.Path = pathlib.Path("./source")
    sections_path: pathlib.Path = document_path / "sections"
    schemas_path: pathlib.Path = document_path / "schemas"
    template_path: pathlib.Path = pathlib.Path("./utils/templates")
    source_path: pathlib.Path = pathlib.Path("../src")

    def setup(self) -> None:
        self.document_path.mkdir(exist_ok=True)
        self.sections_path.mkdir(exist_ok=True)
        self.schemas_path.mkdir(exist_ok=True)


settings = Settings()
settings.setup()
