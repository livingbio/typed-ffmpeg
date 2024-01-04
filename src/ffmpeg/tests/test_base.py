import pytest
from pydantic import ValidationError
from syrupy.assertion import SnapshotAssertion

from ..base import input
from ..filters import concat
from ..streams.video import VideoStream


def test_filter_node(snapshot: SnapshotAssertion) -> None:
    input1 = input("input1")
    input2 = input("input2")
    input3 = input("input3")

    with pytest.raises(ValidationError) as e:
        concat(*(input1, input2, input2))
    assert snapshot == e

    concat(*(input1, input2, input3), n=3)
    assert isinstance(concat(*(input1, input2, input3), n=3).stream(0), VideoStream)

    concat(*(input1, input2.video, input3.video), n=3)

    with pytest.raises(ValidationError) as e:
        concat(*(input1, input2.audio, input3.audio), n=3)
    assert snapshot == e
