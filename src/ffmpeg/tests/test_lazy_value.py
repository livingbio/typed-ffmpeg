from syrupy.assertion import SnapshotAssertion

from ffmpeg.base import input
from ffmpeg.utils.lazy_eval.schema import Symbol


def test_symbol(snapshot: SnapshotAssertion) -> None:
    w = Symbol("w")

    assert snapshot() == input("input.mp4").scale(w=w).output(filename="output.mp4")
