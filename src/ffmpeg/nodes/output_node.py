from __future__ import annotations

from typing import Sequence

from .base import Node, Stream, _DAGContext, empty_dag_context
from .filter_node import FilterableStream
from .global_node import GlobalNode


class OutputNode(Node):
    inputs: list[FilterableStream]

    def stream(self) -> "OutputStream":
        return OutputStream(node=self)

    @property
    def incoming_streams(self) -> Sequence[Stream]:
        return self.inputs

    def get_args(self, context: _DAGContext = empty_dag_context) -> list[str]:
        # TODO: implementation
        raise NotImplementedError("Not implemented yet")


# TODO: handle mapping


class OutputStream(Stream):
    node: OutputNode | GlobalNode | MergeOutputsNode

    def global_args(self, **kwargs: str | bool | int | float | None) -> "OutputStream":
        return GlobalNode(input=self, kwargs=kwargs).stream()

    def overwrite_output(self) -> "OutputStream":
        return GlobalNode(input=self, kwargs={"y": True}).stream()


class MergeOutputsNode(Node):
    inputs: list[OutputStream]

    def stream(self) -> "OutputStream":
        return OutputStream(node=self)

    @property
    def incoming_streams(self) -> Sequence[Stream]:
        return self.inputs
