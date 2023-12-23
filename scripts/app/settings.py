import pathlib

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    base_path: pathlib.Path = (pathlib.Path(__file__).parent / "../..").resolve()
    document_path: pathlib.Path = base_path / "scripts/source"
    sections_path: pathlib.Path = document_path / "sections"
    schemas_path: pathlib.Path = document_path / "schemas"
    template_path: pathlib.Path = base_path / "scripts/templates"
    source_path: pathlib.Path = base_path / "src/ffmpeg"

    def setup(self) -> None:
        self.document_path.mkdir(exist_ok=True)
        self.sections_path.mkdir(exist_ok=True)
        self.schemas_path.mkdir(exist_ok=True)


settings = Settings()
settings.setup()
