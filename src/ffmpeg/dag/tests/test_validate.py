from typing import Callable

import pytest
from syrupy.assertion import SnapshotAssertion

from ...base import input
from ...filters import concat
from ..context import DAGContext
from ..nodes import OutputStream
from ..validate import _validate_not_utilize_split, _validate_reuse_stream


def do_validate(output: OutputStream, func: Callable[[DAGContext], DAGContext]) -> DAGContext:
    context = DAGContext.build(output.node)
    return func(context)


def test_validate_reuse_stream(snapshot: SnapshotAssertion) -> None:
    input1 = input("input1.mp4")

    with pytest.raises(AssertionError) as e:
        rev = input1.reverse()
        do_validate(concat(rev.trim(), rev.trim()).video(0).output(filename="tmp.mp4"), _validate_reuse_stream)

    assert snapshot == e


def test_validate_not_utilize_split(snapshot: SnapshotAssertion) -> None:
    input1 = input("input1.mp4")

    with pytest.raises(AssertionError) as e:
        do_validate(input1.split(outputs=2).video(0).output(filename="tmp.mp4"), _validate_not_utilize_split)

    assert snapshot == e


def test_reduntant_split_outputs_1(snapshot: SnapshotAssertion) -> None:
    input1 = input("input1.mp4")

    with pytest.raises(AssertionError) as e:
        do_validate(input1.split(outputs=1).video(0).output(filename="tmp.mp4"), _validate_not_utilize_split)

    assert snapshot == e


def test_reduntant_split_duplicate(snapshot: SnapshotAssertion) -> None:
    input1 = input("input1.mp4")
    s = input1.split(outputs=2)
    s0 = s.video(0)
    s1 = s.video(1)

    s00 = s0.split(outputs=2).video(0)
    s01 = s0.split(outputs=2).video(1)

    with pytest.raises(AssertionError) as e:
        do_validate(concat(s00, s01, s1, n=3).video(0).output(filename="tmp.mp4"), _validate_not_utilize_split)

    assert snapshot == e
