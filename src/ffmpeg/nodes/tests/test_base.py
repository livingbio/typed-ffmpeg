from typing import Iterable

import pytest
from pydantic import ValidationError

from ..base import Node, Stream


class SimpleNode(Node):
    streams: list[Stream] = []

    @property
    def incoming_streams(self) -> Iterable[Stream]:
        return self.streams


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
