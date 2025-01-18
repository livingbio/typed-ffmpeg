from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.code_gen.cli import generate


def test_generate() -> None:
    outpath = Path(TemporaryDirectory().name)
    generate(outpath)
