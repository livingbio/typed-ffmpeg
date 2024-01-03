import pytest
from pydantic import ValidationError
from syrupy.assertion import SnapshotAssertion

from ..base import input
from ..streams.video import VideoStream


def test_filter_node(snapshot: SnapshotAssertion) -> None:
    input1 = input("input1")
    input2 = input("input2")
    input3 = input("input3")

    with pytest.raises(ValidationError) as e:
        input1.concat(*(input2, input2))
    assert snapshot == e

    input1.concat(*(input2, input3), n=3)
    assert isinstance(input1.concat(*(input2, input3), n=3).stream(0), VideoStream)

    input1.concat(*(input2.video, input3.video), n=3)

    with pytest.raises(ValidationError) as e:
        input1.concat(*(input2.audio, input3.audio), n=3)
    assert snapshot == e
