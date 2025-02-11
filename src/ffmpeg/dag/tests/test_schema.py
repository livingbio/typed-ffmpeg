from dataclasses import asdict, dataclass
from typing import Any

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ...utils.snapshot import DAGSnapshotExtenstion
from ..context import DAGContext
from ..schema import Node, Stream


@dataclass(frozen=True, kw_only=True, repr=False)
class SimpleNode(Node):
    name: str

    def get_args(self, context: DAGContext = None) -> list[str]:
        return []

    def __repr__(self) -> str:
        return self.name


def test_dag(snapshot: SnapshotAssertion) -> None:
    # Linear Chain
    a = SimpleNode(name="A")
    b = SimpleNode(name="B", inputs=(Stream(node=a),))
    c = SimpleNode(name="C", inputs=(Stream(node=b),))
    d = SimpleNode(name="D", inputs=(Stream(node=c),))

    assert snapshot(extension_class=JSONSnapshotExtension) == asdict(d)
    assert snapshot(extension_class=DAGSnapshotExtenstion, name="org") == d

    # # Self-loop
    # a = SimpleNode(name="A")
    # b = SimpleNode(name="B")
    # c = SimpleNode(name="C")
    # c.streams = [Stream(node=a)]

    # with pytest.raises(ValueError):
    #     b.streams = [Stream(node=b), Stream(node=a)]


def linear() -> Any:
    a = SimpleNode(name="A")
    b = SimpleNode(name="B", inputs=(Stream(node=a),))
    c = SimpleNode(name="C", inputs=(Stream(node=b),))
    d = SimpleNode(name="D", inputs=(Stream(node=c),))

    e = SimpleNode(name="E", inputs=(Stream(node=a),))

    return pytest.param(d, [(a, e), (b, e), (c, e), (d, e)], id="linear")


def simple_loop() -> Any:
    a = SimpleNode(name="A")
    b = SimpleNode(name="B", inputs=(Stream(node=a),))
    c = SimpleNode(name="C", inputs=(Stream(node=a),))
    d = SimpleNode(name="D", inputs=(Stream(node=c), Stream(node=b)))

    e = SimpleNode(name="E", inputs=(Stream(node=a),))

    return pytest.param(d, [(a, e), (b, e), (c, e), (d, e)], id="simple_loop")


def multi_loop() -> Any:
    a = SimpleNode(name="A")
    b = SimpleNode(name="B", inputs=(Stream(node=a),))
    c = SimpleNode(name="C", inputs=(Stream(node=a), Stream(node=b)))
    d = SimpleNode(name="D", inputs=(Stream(node=c), Stream(node=b)))

    e = SimpleNode(name="E", inputs=(Stream(node=a),))

    return pytest.param(d, [(a, e), (b, e), (c, e), (d, e)], id="multi_loop")


def update_node() -> Any:
    a = SimpleNode(name="A")
    b = SimpleNode(name="B", inputs=(Stream(node=a),))
    c = SimpleNode(name="C", inputs=(Stream(node=b), Stream(node=a)))
    d = SimpleNode(name="D", inputs=(Stream(node=c), Stream(node=b)))

    b_new = SimpleNode(name="B#", inputs=(Stream(node=a),))
    c_new = SimpleNode(name="C#", inputs=(Stream(node=b), Stream(node=a)))
    c_new_new = SimpleNode(name="C##", inputs=(Stream(node=b_new), Stream(node=a)))

    return pytest.param(d, [(b, b_new), (c, c_new), (c, c_new_new)], id="update_node")


@pytest.mark.parametrize(
    "graph, replace_pattern", [linear(), simple_loop(), multi_loop(), update_node()]
)
def test_replace(
    graph: Node,
    replace_pattern: list[tuple[Node, Node]],
    snapshot: SnapshotAssertion,
) -> None:
    assert snapshot(name="org", extension_class=DAGSnapshotExtenstion) == graph

    for node, replaced_node in replace_pattern:
        new_g = graph.replace(node, replaced_node)
        assert (
            snapshot(
                name=f"replace {node} -> {replaced_node}",
                extension_class=DAGSnapshotExtenstion,
            )
            == new_g
        )


@pytest.mark.skip("Not stable")
def test_stream_view(snapshot: SnapshotAssertion) -> None:
    a = SimpleNode(name="A")
    b = SimpleNode(name="B", inputs=(Stream(node=a),))
    c = SimpleNode(name="C", inputs=(Stream(node=b), Stream(node=a)))
    d = SimpleNode(name="D", inputs=(Stream(node=c), Stream(node=b)))
    stream = Stream(node=d)
    stream.view()

    # test node.view()
    stream.node.view()

    # png results it not stable
    # with open(png, "rb") as ifile:
    #     assert snapshot(extension_class=PNGImageSnapshotExtension) == ifile.read()

    # SVG and Dot Result is not stable
    # svg = stream.view(format="svg")
    # with open(svg, "r") as ifile:
    #     assert snapshot(extension_class=SVGImageSnapshotExtension) == ifile.read()

    # dot = stream.view(format="dot")

    # with open(dot, "r") as ifile:
    #     assert snapshot() == ifile.read()
