import pathlib

from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..helper import dump
from ..parse_ffmpeg_opt_c import parse_ffmpeg_opt_c


def test_parse_ffmpeg_opt_c(snapshot: SnapshotAssertion, datadir: pathlib.Path) -> None:
    assert snapshot(extension_class=JSONSnapshotExtension) == dump(
        parse_ffmpeg_opt_c((datadir / "ffmpeg_opt.c").read_text())
    )
