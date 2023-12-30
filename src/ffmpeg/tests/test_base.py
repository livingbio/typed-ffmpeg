from syrupy.assertion import SnapshotAssertion

from ..base import input


def test_input(snapshot: SnapshotAssertion) -> None:
    assert snapshot == input("filename", arg1="value1", arg2="value2").node.compile()
