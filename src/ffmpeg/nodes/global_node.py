from typing import Sequence

from .base import Node, _DAGContext
from .output_node import OutputStream


class GlobalNode(Node):
    input: OutputStream

    def stream(self) -> "OutputStream":
        return OutputStream(node=self)

    @property
    def incoming_streams(self) -> Sequence[OutputStream]:
        return [self.input]

    def get_args(self, context: _DAGContext) -> list[str]:
        commands = []
        commands += self.args
        for key, value in self.kwargs.items():
            commands += [f"-{key}", value]
        return commands
