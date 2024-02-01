from __future__ import annotations

from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
from functools import cached_property
from typing import Iterable, Sequence

from ..schema import StreamType
from ..utils.dag import is_dag
from ..utils.typing import override


class _DAGContext(ABC):
    """
    An abstract class context for DAG.
    """

    @abstractmethod
    def get_node_label(self, node: Node) -> str:
        """
        Get the label of the node.

        Args:
            node: The node to get the label of.

        Returns:
            The label of the node.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_outgoing_streams(self, node: Node) -> Iterable[Stream]:
        """
        Extract all node's outgoing streams from the given set of streams, Because a node only know its incoming streams.

        Args:
            node: The node to get the outgoing streams of.

        Returns:
            The outgoing streams of the node.
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
    """
    A 'Stream' represents a sequence of data flow in the Directed Acyclic Graph (DAG).

    Note:
        Each stream in the DAG is a sequence of operations that transforms the data from its input form to its output form. The stream is an essential component of the DAG, as it defines the order and the nature of the operations that are performed on the data.
    """

    node: Node
    """
    Represents the node that the stream is connected to in the upstream direction.

    Note:
        In the context of a data stream, the 'upstream' refers to the source of the data, or where the data is coming from. Therefore, the 'upstream node' is the node that is providing the data to the current stream.
    """
    selector: StreamType | None = None
    """
    Represents the type of the stream.

    Notes:
        See Also: [Stream specifiers](https://ffmpeg.org/ffmpeg.html#Stream-specifiers-1) `stream_type`
    """

    index: int | None = None  # the nth child of the node
    """
    Represents the index of the stream in the node's output streams.

    Note:
        See Also: [Stream specifiers](https://ffmpeg.org/ffmpeg.html#Stream-specifiers-1) `stream_index`
    """


@dataclass(frozen=True, kw_only=True)
class Node(HashableBaseModel, ABC):
    """
    A 'Node' represents a single operation in the Directed Acyclic Graph (DAG).

    Note:
        Each node in the DAG represents a single operation that transforms the data from its input form to its output form. The node is an essential component of the DAG, as it defines the nature of the operations that are performed on the data.
    """

    args: tuple[str, ...] = ()
    kwargs: tuple[tuple[str, str | int | float | bool], ...] = ()

    @abstractproperty
    def incoming_streams(self) -> Sequence["Stream"]:
        """
        Return the incoming streams of this node.

        Returns:
            The incoming streams of this node.
        """
        raise NotImplementedError()

    def __post_init__(self) -> None:
        # Validate the DAG
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
        Get the arguments of the node.

        Args:
            context: The DAG context. Defaults to empty_dag_context.

        Returns:
            The arguments of the node.
        """
        raise NotImplementedError()
