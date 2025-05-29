from pathlib import Path

from ..probe import probe


def test_probe(datadir: Path) -> None:
    info = probe(datadir / "test-5sec.mp4")

    assert info.format is not None
    assert info.format.filename is not None

    Path(info.format.filename).name == "test-5sec.mp4"
