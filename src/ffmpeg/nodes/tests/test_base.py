from dataclasses import dataclass
from typing import Sequence

from ..base import Node, Stream, _DAGContext, empty_dag_context


@dataclass(frozen=True, kw_only=True)
class SimpleNode(Node):
    name: str
    streams: tuple[Stream, ...] = ()

    @property
    def incoming_streams(self) -> Sequence[Stream]:
        return self.streams

    def get_args(self, context: _DAGContext = empty_dag_context) -> list[str]:
        return []


def test_dag() -> None:
    # Linear Chain
    a = SimpleNode(name="A")
    b = SimpleNode(name="B", streams=(Stream(node=a),))
    c = SimpleNode(name="C", streams=(Stream(node=b),))
    d = SimpleNode(name="D", streams=(Stream(node=c),))

    # # Self-loop
    # a = SimpleNode(name="A")
    # b = SimpleNode(name="B")
    # c = SimpleNode(name="C")
    # c.streams = [Stream(node=a)]

    # with pytest.raises(ValueError):
    #     b.streams = [Stream(node=b), Stream(node=a)]
