from syrupy.assertion import SnapshotAssertion

from ...base import input
from ...common.schema import FFMpegFilterDef
from ...schema import Auto
from ..factory import filter_node_factory


def test_filter_node_factory(snapshot: SnapshotAssertion) -> None:
    in_file = input("foo.mp4")

    f = filter_node_factory(
        FFMpegFilterDef(name="foo", typings_input="[StreamType.video]*n"),
        **{"n": Auto("len(streams)")},
    )
    assert snapshot == f
    assert f.kwargs == tuple({"n": 0}.items())

    f = filter_node_factory(
        FFMpegFilterDef(name="foo", typings_input="[StreamType.video]*n"),
        in_file.video,
        **{"n": Auto("len(streams)")},
    )
    assert snapshot == f
    assert f.kwargs == tuple({"n": 1}.items())

    f = filter_node_factory(
        FFMpegFilterDef(name="foo", typings_input="[StreamType.video]*n"),
        in_file.video,
        in_file.video,
        **{"n": Auto("len(streams)")},
    )
    assert snapshot == f
    assert f.kwargs == tuple({"n": 2}.items())
