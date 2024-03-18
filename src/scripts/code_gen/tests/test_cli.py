from pathlib import Path
from tempfile import TemporaryDirectory

from ..cli import generate


def test_generate() -> None:
    outpath = Path(TemporaryDirectory().name)
    generate(outpath)
