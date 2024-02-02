from __future__ import annotations

from tempfile import mktemp

from ..dag.base import Node
from ..dag.nodes import FilterNode, InputNode, OutputNode
from .compile import DAGContext


def _get_node_color(node: Node) -> str | None:
    if isinstance(node, InputNode):
        color = "#99cc00"
    elif isinstance(node, OutputNode):
        color = "#99ccff"
    elif isinstance(node, FilterNode):
        color = "#ffcc00"
    else:
        color = None
    return color


def view(node: Node) -> str:
    try:
        import graphviz  # type: ignore
    except ImportError:
        raise ImportError(
            "failed to import graphviz; please make sure graphviz is installed (e.g. " "`pip install graphviz`)"
        )

    filename = mktemp()

    graph = graphviz.Digraph(format="png")
    graph.attr(rankdir="LR")

    context = DAGContext.build(node)

    for node in context.all_nodes:
        color = _get_node_color(node)
        graph.node(name=node.hex, label=repr(node), shape="box", style="filled", fillcolor=color)

    for node in context.all_nodes:
        for stream in node.incoming_streams:
            graph.edge(stream.node.hex, node.hex)

    graph.render(filename)
    return filename
