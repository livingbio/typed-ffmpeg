from syrupy.assertion import SnapshotAssertion

from ..base import input
from ..utils.lazy_eval.schema import Symbol


def test_symbol(snapshot: SnapshotAssertion) -> None:
    w = Symbol("w")

    assert snapshot() == input("input.mp4").scale(w=w).output(filename="output.mp4")
