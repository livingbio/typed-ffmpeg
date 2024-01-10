from typing import Sequence

import pytest
from pydantic import ValidationError

from ..base import Node, Stream, _DAGContext, empty_dag_context


class SimpleNode(Node):
    name: str
    streams: list[Stream] = []

    @property
    def incoming_streams(self) -> Sequence[Stream]:
        return self.streams

    def get_args(self, context: _DAGContext = empty_dag_context) -> list[str]:
        return []


def test_dag() -> None:
    # Linear Chain
    a = SimpleNode(name="A")
    b = SimpleNode(name="B", streams=[Stream(node=a)])
    c = SimpleNode(name="C", streams=[Stream(node=b)])
    d = SimpleNode(name="D", streams=[Stream(node=c)])

    # Self-loop
    a = SimpleNode(name="A")
    b = SimpleNode(name="B")
    c = SimpleNode(name="C")
    c.streams = [Stream(node=a)]

    with pytest.raises(ValidationError):
        b.streams = [Stream(node=b), Stream(node=a)]
