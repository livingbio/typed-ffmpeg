import pathlib

from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..parse_ffmpeg_opt_c import parse_ffmpeg_opt_c


def test_parse_ffmpeg_opt_c(snapshot: SnapshotAssertion, datadir: pathlib.Path) -> None:
    assert snapshot(extension_class=JSONSnapshotExtension) == [
        {
            "name": k.name,
            "flags": k.flags,
            "help": k.help,
            "argname": k.argname,
            "is_input_option": k.is_input_option,
            "is_output_option": k.is_output_option,
            "is_global_option": k.is_global_option,
            "is_support_stream_specifier": k.is_support_stream_specifier,
        }
        for k in parse_ffmpeg_opt_c((datadir / "ffmpeg_opt.c").read_text())
    ]
