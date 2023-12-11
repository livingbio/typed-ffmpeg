import pathlib

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    document_path: pathlib.Path = pathlib.Path("./source")


settings = Settings()
