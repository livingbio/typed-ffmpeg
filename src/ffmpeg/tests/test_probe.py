from pathlib import Path

from ffmpeg.probe import probe


def test_probe(datadir: Path) -> None:
    info = probe(datadir / "test-5sec.mp4")

    Path(info["format"]["filename"]).name == "test-5sec.mp4"
