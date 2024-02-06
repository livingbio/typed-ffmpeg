from __future__ import annotations

from ..dag.context import DAGContext
from ..dag.nodes import FilterNode, InputNode, OutputNode
from ..dag.schema import Node


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

    graph = graphviz.Digraph(format="png")
    graph.attr(rankdir="LR")

    context = DAGContext.build(node)

    for node in context.all_nodes:
        color = _get_node_color(node)
        graph.node(name=node.hex, label=node.repr(), shape="box", style="filled", fillcolor=color)

    for node in context.all_nodes:
        for stream in node.inputs:
            graph.edge(stream.node.hex, node.hex)

    return graph.render(format="png")
