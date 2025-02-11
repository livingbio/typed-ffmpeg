from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, replace
from functools import cached_property
from typing import TYPE_CHECKING, Literal

from ..utils.lazy_eval.schema import LazyValue
from .utils import is_dag

if TYPE_CHECKING:
    from .context import DAGContext


@dataclass(frozen=True, kw_only=True)
class HashableBaseModel:
    """
    A base class for hashable dataclasses.
    """

    @cached_property
    def hex(self) -> str:
        """
        Get the hexadecimal hash of the object.
        """
        return hex(abs(hash(self)))[2:]


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

    index: int | None = None  # the nth child of the node
    """
    Represents the index of the stream in the node's output streams.

    Note:
        See Also: [Stream specifiers](https://ffmpeg.org/ffmpeg.html#Stream-specifiers-1) `stream_index`
    """

    def view(self, format: Literal["png", "svg", "dot"] = "png") -> str:
        """
        Visualize the stream.

        Args:
            format: The format of the view.

        Returns:
            The file path of the visualization.
        """
        from ..utils.view import view

        return view(self.node, format=format)

    def _repr_png_(self) -> bytes:  # pragma: no cover
        with open(self.view(format="png"), "rb") as f:
            return f.read()

    def _repr_svg_(self) -> str:  # pragma: no cover
        with open(self.view(format="svg")) as f:
            return f.read()


@dataclass(frozen=True, kw_only=True)
class Node(HashableBaseModel, ABC):
    """
    A 'Node' represents a single operation in the Directed Acyclic Graph (DAG).

    Note:
        Each node in the DAG represents a single operation that transforms the data from its input form to its output form. The node is an essential component of the DAG, as it defines the nature of the operations that are performed on the data.
    """

    # Filter_Node_Option_Type
    kwargs: tuple[tuple[str, str | int | float | bool | LazyValue], ...] = ()
    """
    Represents the keyword arguments of the node.
    """

    inputs: tuple[Stream, ...] = ()
    """
    Represents the input streams of the node.
    """

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

            nodes.extend(k.node for k in node.inputs)

            output[node.hex] = {k.node.hex for k in node.inputs}

        if not is_dag(output):
            raise ValueError(f"Graph is not a DAG: {output}")  # pragma: no cover

    @abstractmethod
    def get_args(self, context: DAGContext = None) -> list[str]:
        """
        Get the arguments of the node.

        Args:
            context: The DAG context.

        Returns:
            The arguments of the node.
        """

    def repr(self) -> str:
        """
        Get the representation of the node.

        Returns:
            The representation of the node.
        """
        return repr(self)

    def replace(self, old_node: Node, new_node: Node) -> Node:
        """
        Replace the old node in the graph with the new node.

        Args:
            old_node: The old node to replace.
            new_node: The new node to replace with.

        Returns:
            The new graph with the replaced node.
        """
        if self == old_node:
            return new_node

        inputs = []

        for stream in self.inputs:
            new_stream_node = stream.node.replace(old_node, new_node)

            if new_stream_node != stream.node:
                # need to create a new stream
                new_stream = replace(stream, node=new_stream_node)
                inputs.append(new_stream)
            else:
                inputs.append(stream)

        return replace(self, inputs=tuple(inputs))

    @property
    def max_depth(self) -> int:
        """
        Get the maximum depth of the node.

        Returns:
            The maximum depth of the node.
        """
        return max((i.node.max_depth for i in self.inputs), default=0) + 1

    @property
    def upstream_nodes(self) -> set[Node]:
        """
        Get all upstream nodes of the node.

        Returns:
            The upstream nodes of the node.
        """
        output = {self}
        for input in self.inputs:
            output |= input.node.upstream_nodes

        return output

    def view(self, format: Literal["png", "svg", "dot"] = "png") -> str:
        """
        Visualize the Node.

        Args:
            format: The format of the view.

        Returns:
            The file path of the visualization.
        """
        from ..utils.view import view

        return view(self, format=format)

    def _repr_png_(self) -> bytes:  # pragma: no cover
        with open(self.view(format="png"), "rb") as f:
            return f.read()

    def _repr_svg_(self) -> str:  # pragma: no cover
        with open(self.view(format="svg")) as f:
            return f.read()
