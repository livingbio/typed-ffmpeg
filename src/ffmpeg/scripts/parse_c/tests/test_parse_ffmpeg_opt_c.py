import tempfile
from pathlib import Path

from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..parse_ffmpeg_opt_c import parse_ffmpeg_opt_c
from ..pre_compile import pre_compile_file, source_folder


def test_parse_ffmpeg_opt_c(snapshot: SnapshotAssertion) -> None:
    filename = tempfile.NamedTemporaryFile()
    p = Path(filename.name)
    pre_compile_file(source_folder / "fftools/ffmpeg_opt.c", p)

    assert snapshot(extension_class=JSONSnapshotExtension) == [
        {
            "is_input_option": k.is_input_option,
            "is_output_option": k.is_output_option,
            "is_global_option": k.is_global_option,
            "is_support_stream_specifier": k.is_support_stream_specifier,
        }
        | k.__dict__
        for k in parse_ffmpeg_opt_c(p.read_text())
    ]
