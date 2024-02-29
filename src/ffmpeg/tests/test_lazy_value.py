from ..base import input, merge_outputs, output, vfilter
from ..utils.lazy_eval.schema import Symbol
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

def test_symbol(snapshot: SnapshotAssertion) -> None:
    w = Symbol("w")

    assert snapshot(extension_class=JSONSnapshotExtension) == input("input.mp4").scale(w=w).output(filename="output.mp4").compile()