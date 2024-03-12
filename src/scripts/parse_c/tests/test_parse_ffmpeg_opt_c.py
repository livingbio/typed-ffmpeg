from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..parse_ffmpeg_opt_c import parse_ffmpeg_opt_c
from ..pre_compile import precompile, target_folder


def test_parse_ffmpeg_opt_c(snapshot: SnapshotAssertion) -> None:
    precompile()
    p = target_folder / "fftools/ffmpeg_opt.c"

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
