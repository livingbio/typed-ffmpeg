from dataclasses import asdict
from typing import Optional, Callable
import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ffmpeg.dag.nodes import OutputStream

from ...base import input
from ...filters import concat
from ..context import DAGContext
from ..validate import _validate_not_utilize_split, _validate_reused_stream, _validate_nouse_split
from ..compile import compile

def reuse_stream() -> OutputStream:
    input1 = input("input1.mp4")
    rev = input1.reverse()
    return concat(rev.trim(), rev.trim()).video(0).output(filename="tmp.mp4")


def not_utilize_split() -> OutputStream:
    input1 = input("input1.mp4")
    return input1.split(outputs=2).video(0).output(filename="tmp.mp4")

def no_use_split() -> OutputStream:
    input1 = input("input1.mp4")
    return input1.split(outputs=1).video(0).output(filename="tmp.mp4")


@pytest.mark.parametrize("stream, validater", [
    pytest.param(reuse_stream(), _validate_reused_stream, id="reuse-stream"),
    # pytest.param(not_utilize_split(), _validate_not_utilize_split, id="not-utilize-split"),
    # pytest.param(no_use_split(), _validate_nouse_split, id="no-use-split"),
    ])
def test_validate(stream: OutputStream, validater: Callable[[DAGContext ,Optional[bool]], DAGContext], snapshot: SnapshotAssertion) -> None:
    context = DAGContext.build(stream.node)

    assert snapshot(name="before", extension_class=JSONSnapshotExtension) == compile(stream.node, do_validate=False)

    with pytest.raises(AssertionError) as e:
        validater(context)

    assert snapshot == e

    new_context = validater(context, True)

    assert snapshot(extension_class=JSONSnapshotExtension) == asdict(new_context.node)
    assert snapshot(name="after", extension_class=JSONSnapshotExtension) == compile(new_context.node, do_validate=False)



# def test_validate_nouse_split(snapshot: SnapshotAssertion) -> None:
#     input1 = input("input1.mp4")

#     context = DAGContext.build(input1.split(outputs=1).video(0).output(filename="tmp.mp4"))
#     with pytest.raises(AssertionError) as e:
#         _validate_nouse_split(context)

#     assert snapshot == e

#     new_context = _validate_nouse_split(context, auto_fix=True)

#     assert snapshot(extension_class=JSONSnapshotExtension) == asdict(new_context.node)


# def test_reduntant_split_duplicate(snapshot: SnapshotAssertion) -> None:
#     input1 = input("input1.mp4")
#     s = input1.split(outputs=2)
#     s0 = s.video(0)
#     s1 = s.video(1)

#     s00 = s0.split(outputs=2).video(0)
#     s01 = s0.split(outputs=2).video(1)

#     context = DAGContext.build(concat(s00, s01, s1, n=3).video(0).output(filename="tmp.mp4"))
#     with pytest.raises(AssertionError) as e:
#         _validate_not_utilize_split(context)

#     assert snapshot == e
