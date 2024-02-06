from dataclasses import asdict, dataclass

from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..schema import Node, Stream, _DAGContext, empty_dag_context


@dataclass(frozen=True, kw_only=True, repr=False)
class SimpleNode(Node):
    name: str

    def get_args(self, context: _DAGContext = empty_dag_context) -> list[str]:
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

    # # Self-loop
    # a = SimpleNode(name="A")
    # b = SimpleNode(name="B")
    # c = SimpleNode(name="C")
    # c.streams = [Stream(node=a)]

    # with pytest.raises(ValueError):
    #     b.streams = [Stream(node=b), Stream(node=a)]


def test_replace_linear(snapshot: SnapshotAssertion) -> None:
    a = SimpleNode(name="A")
    b = SimpleNode(name="B", inputs=(Stream(node=a),))
    c = SimpleNode(name="C", inputs=(Stream(node=b),))
    d = SimpleNode(name="D", inputs=(Stream(node=c),))

    e = SimpleNode(name="E", inputs=(Stream(node=a),))

    assert snapshot(name="replace a", extension_class=JSONSnapshotExtension) == asdict(d.replace(a, e))
    assert snapshot(name="replace b", extension_class=JSONSnapshotExtension) == asdict(d.replace(b, e))
    assert snapshot(name="replace c", extension_class=JSONSnapshotExtension) == asdict(d.replace(c, e))
    assert snapshot(name="replace d", extension_class=JSONSnapshotExtension) == asdict(d.replace(d, e))


def test_replace_loop(snapshot: SnapshotAssertion) -> None:
    a = SimpleNode(name="A")
    b = SimpleNode(name="B", inputs=(Stream(node=a),))
    c = SimpleNode(name="C", inputs=(Stream(node=a),))
    d = SimpleNode(name="D", inputs=(Stream(node=c), Stream(node=b)))

    e = SimpleNode(name="E", inputs=(Stream(node=a),))

    assert snapshot(name="replace a", extension_class=JSONSnapshotExtension) == asdict(d.replace(a, e))

    assert snapshot(name="replace b", extension_class=JSONSnapshotExtension) == asdict(d.replace(b, e))

    assert snapshot(name="replace c", extension_class=JSONSnapshotExtension) == asdict(d.replace(c, e))

    assert snapshot(name="replace d", extension_class=JSONSnapshotExtension) == asdict(d.replace(d, e))
