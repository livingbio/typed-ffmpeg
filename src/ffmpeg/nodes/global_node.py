from typing import Sequence

from .base import Node
from .output_node import OutputStream


class GlobalNode(Node):
    input: OutputStream

    def stream(self) -> "OutputStream":
        return OutputStream(node=self)

    @property
    def incoming_streams(self) -> Sequence[OutputStream]:
        return [self.input]
