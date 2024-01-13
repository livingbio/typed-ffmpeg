from __future__ import annotations

from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
from functools import cached_property
from typing import Any, Iterable, Sequence

from ..schema import StreamType
from ..utils.dag import is_dag


@dataclass(frozen=True, kw_only=True)
class _DAGContext(ABC):
    @abstractmethod
    def get_node_label(self, node: Node) -> str:
        """Get the label of the node"""
        raise NotImplementedError()

    @abstractmethod
    def get_outgoing_streams(self, node: Node) -> Iterable[Stream]:
        """Extract all node's outgoing streams from the given set of streams, Because a node only know its incoming streams"""
        raise NotImplementedError()


@dataclass(frozen=True, kw_only=True)
class DummyDAGContext(_DAGContext):
    """A dummy DAG context that does not do anything"""

    def get_node_label(self, node: Node) -> str:
        return str(node)

    def get_outgoing_streams(self, node: Node) -> Iterable[Stream]:
        return []


empty_dag_context = DummyDAGContext()


@dataclass(frozen=True, kw_only=True)
class HashableBaseModel:
    @cached_property
    def hex(self) -> str:
        return hex(abs(hash(self)))[2:]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.hex})"


@dataclass(frozen=True, kw_only=True)
class Stream(HashableBaseModel):
    node: Node
    selector: StreamType | None = None
    index: int | None = None  # the nth child of the node


@dataclass(frozen=True, kw_only=True)
class Node(HashableBaseModel, ABC):
    kwargs: tuple[tuple[str, Any], ...] = ()

    @abstractproperty
    def incoming_streams(self) -> Sequence["Stream"]:
        raise NotImplementedError()

    def __post_init__(self) -> None:
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

        if not is_dag(output):
            raise ValueError(f"Graph is not a DAG: {output}")

    @abstractmethod
    def get_args(self, context: _DAGContext = empty_dag_context) -> list[str]:
        raise NotImplementedError()
