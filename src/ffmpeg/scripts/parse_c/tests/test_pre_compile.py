from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.single_file import SingleFileSnapshotExtension

from ..pre_compile import precompile, target_folder


def test_pre_compile_file(snapshot: SnapshotAssertion) -> None:
    precompile()
    assert (
        snapshot(extension_class=SingleFileSnapshotExtension) == (target_folder / "fftools/ffmpeg_opt.c").read_bytes()
    )
