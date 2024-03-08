from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.single_file import SingleFileSnapshotExtension

from ..pre_compile import precompile


def test_pre_compile_file() -> None:
    precompile()
    