import pytest
from syrupy.assertion import SnapshotAssertion

from ...base import input
from ...filters import concat
from ..context import DAGContext
from ..validate import _validate_not_utilize_split, _validate_reuse_stream


def test_validate_reuse_stream(snapshot: SnapshotAssertion) -> None:
    input1 = input("input1.mp4")
    rev = input1.reverse()
    context = DAGContext.build(concat(rev.trim(), rev.trim()).video(0).output(filename="tmp.mp4"))

    with pytest.raises(AssertionError) as e:
        _validate_reuse_stream(context)

    assert snapshot == e


def test_validate_not_utilize_split(snapshot: SnapshotAssertion) -> None:
    input1 = input("input1.mp4")

    context = DAGContext.build(input1.split(outputs=2).video(0).output(filename="tmp.mp4"))
    with pytest.raises(AssertionError) as e:
        _validate_not_utilize_split(context)

    assert snapshot == e


def test_reduntant_split_outputs_1(snapshot: SnapshotAssertion) -> None:
    input1 = input("input1.mp4")

    context = DAGContext.build(input1.split(outputs=1).video(0).output(filename="tmp.mp4"))
    with pytest.raises(AssertionError) as e:
        _validate_not_utilize_split(context)

    assert snapshot == e


def test_reduntant_split_duplicate(snapshot: SnapshotAssertion) -> None:
    input1 = input("input1.mp4")
    s = input1.split(outputs=2)
    s0 = s.video(0)
    s1 = s.video(1)

    s00 = s0.split(outputs=2).video(0)
    s01 = s0.split(outputs=2).video(1)

    context = DAGContext.build(concat(s00, s01, s1, n=3).video(0).output(filename="tmp.mp4"))
    with pytest.raises(AssertionError) as e:
        _validate_not_utilize_split(context)

    assert snapshot == e
