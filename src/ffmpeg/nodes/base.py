from __future__ import annotations

from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
from functools import cached_property
from typing import Iterable, Sequence

from ..schema import StreamType
from ..utils.dag import is_dag
from ..utils.typing import override


class _DAGContext(ABC):
    @abstractmethod
    def get_node_label(self, node: Node) -> str:
        """
        Get the label of the node

        Parameters:
        -----------
        :param node: the node to get the label of the node

        Returns:
        --------
        :return: the label of the node
        """
        raise NotImplementedError()

    @abstractmethod
    def get_outgoing_streams(self, node: Node) -> Iterable[Stream]:
        """
        Extract all node's outgoing streams from the given set of streams, Because a node only know its incoming streams

        Parameters:
        -----------
        :param node: the node to get the outgoing streams of the node

        Returns:
        --------
        :return: the outgoing streams of the node
        """
        raise NotImplementedError()


class DummyDAGContext(_DAGContext):
    """A dummy DAG context that does not do anything"""

    @override
    def get_node_label(self, node: Node) -> str:
        return str(node)

    @override
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
    args: tuple[str, ...] = ()
    kwargs: tuple[tuple[str, str | int | float | bool], ...] = ()

    @abstractproperty
    def incoming_streams(self) -> Sequence["Stream"]:
        """
        Return the incoming streams of this node

        Returns:
        --------
        :return: the incoming streams of this node
        """
        raise NotImplementedError()

    def __post_init__(self) -> None:
        """Validate the DAG"""
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
        """
        Get the arguments of the node

        Parameters:
        -----------
        :param context: the DAG context

        Returns:
        --------
        :return: the arguments of the node
        """
        raise NotImplementedError()
