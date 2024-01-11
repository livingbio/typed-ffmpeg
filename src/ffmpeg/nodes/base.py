from __future__ import annotations

from abc import ABC, abstractmethod, abstractproperty
from functools import cached_property
from typing import Any, Iterable, Mapping, Sequence

from pydantic import BaseModel, model_validator

from ..schema import StreamType
from ..utils.dag import is_dag


class _DAGContext(BaseModel, ABC):
    @abstractmethod
    def get_node_label(self, node: Node) -> str:
        """Get the label of the node"""
        raise NotImplementedError()

    @abstractmethod
    def get_outgoing_streams(self, node: Node) -> Iterable[Stream]:
        """Extract all node's outgoing streams from the given set of streams, Because a node only know its incoming streams"""
        raise NotImplementedError()


class DummyDAGContext(_DAGContext):
    """A dummy DAG context that does not do anything"""

    def get_node_label(self, node: Node) -> str:
        return str(node)

    def get_outgoing_streams(self, node: Node) -> Iterable[Stream]:
        return []


empty_dag_context = DummyDAGContext()


class HashableBaseModel(BaseModel):
    def __hash__(self) -> int:
        return hash(self.model_dump_json())

    @cached_property
    def hex(self) -> str:
        return hex(abs(hash(self)))[2:]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.hex})"


class Stream(HashableBaseModel):
    node: Node
    selector: StreamType | None = None
    index: int | None = None  # the nth child of the node


class Node(HashableBaseModel, ABC, validate_assignment=True):
    kwargs: Mapping[str, Any] = {}

    @abstractproperty
    def incoming_streams(self) -> Sequence["Stream"]:
        raise NotImplementedError()

    @model_validator(mode="after")
    def validate_dag(self) -> Node:
        passed = set()
        nodes = [self]
        output = {}

        while nodes:
            node = nodes.pop()

            if node in passed:
                continue
            passed.add(node)

            nodes.extend(k.node for k in node.incoming_streams)

            output[str(node)] = set(str(k.node) for k in node.incoming_streams)

        assert is_dag(output), f"Graph is not a DAG: {output}"
        return self

    @abstractmethod
    def get_args(self, context: _DAGContext = empty_dag_context) -> list[str]:
        raise NotImplementedError()
