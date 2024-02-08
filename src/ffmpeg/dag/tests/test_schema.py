import os
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ffmpeg.dag.context import DAGContext

from ...utils.view import view
from ..schema import Node, Stream, _DAGContext, empty_dag_context


@dataclass(frozen=True, kw_only=True, repr=False)
class SimpleNode(Node):
    name: str

    def get_args(self, context: _DAGContext = empty_dag_context) -> list[str]:
        return []

    def __repr__(self) -> str:
        return self.name


@pytest.fixture(scope="function")
def drawer(request: pytest.FixtureRequest) -> Callable[[str, Node], Path]:
    # Get the test file path and function name
    file_path = request.module.__file__
    function_name = request.node.name

    # Get the parameter id (if it exists)
    param_id = getattr(request, "param", None)
    if hasattr(param_id, "id"):
        param_id = param_id.id  # type: ignore

    # Construct the folder name based on test file location, function name, and parameter value or id
    if param_id:
        function_name = f"{function_name}[{param_id}]"

    folder = Path(file_path).parent / f"graph/{function_name}/"
    folder.mkdir(parents=True, exist_ok=True)

    def draw(name: str, node: Node) -> Path:
        graph_path = view(node)
        os.rename(graph_path, folder / f"{name}.png")
        return folder / f"{name}.png"

    return draw


def test_dag(snapshot: SnapshotAssertion, drawer: Callable[[str, Node], Path]) -> None:
    # Linear Chain
    a = SimpleNode(name="A")
    b = SimpleNode(name="B", inputs=(Stream(node=a),))
    c = SimpleNode(name="C", inputs=(Stream(node=b),))
    d = SimpleNode(name="D", inputs=(Stream(node=c),))

    assert snapshot(extension_class=JSONSnapshotExtension) == asdict(d)
    drawer("org", d)

    # # Self-loop
    # a = SimpleNode(name="A")
    # b = SimpleNode(name="B")
    # c = SimpleNode(name="C")
    # c.streams = [Stream(node=a)]

    # with pytest.raises(ValueError):
    #     b.streams = [Stream(node=b), Stream(node=a)]


def linear() -> Any:
    a = SimpleNode(name="A")
    b = SimpleNode(name="B", inputs=(Stream(node=a),))
    c = SimpleNode(name="C", inputs=(Stream(node=b),))
    d = SimpleNode(name="D", inputs=(Stream(node=c),))

    e = SimpleNode(name="E", inputs=(Stream(node=a),))

    return pytest.param(d, e, id="linear")


def simple_loop() -> Any:
    a = SimpleNode(name="A")
    b = SimpleNode(name="B", inputs=(Stream(node=a),))
    c = SimpleNode(name="C", inputs=(Stream(node=a),))
    d = SimpleNode(name="D", inputs=(Stream(node=c), Stream(node=b)))

    e = SimpleNode(name="E", inputs=(Stream(node=a),))

    return pytest.param(d, e, id="simple_loop")


def multi_loop() -> Any:
    a = SimpleNode(name="A")
    b = SimpleNode(name="B", inputs=(Stream(node=a),))
    c = SimpleNode(name="C", inputs=(Stream(node=a), Stream(node=b)))
    d = SimpleNode(name="D", inputs=(Stream(node=c), Stream(node=b)))

    e = SimpleNode(name="E", inputs=(Stream(node=a),))

    return pytest.param(d, e, id="multi_loop")


@pytest.mark.parametrize("graph, replaced_node", [linear(), simple_loop(), multi_loop()])
def test_replace(
    graph: Node, replaced_node: Node, snapshot: SnapshotAssertion, drawer: Callable[[str, Node], Path]
) -> None:
    drawer("org", graph)

    context = DAGContext.build(graph)

    for node in context.all_nodes:
        new_g = graph.replace(node, replaced_node)
        drawer(f"replace_{node}", new_g)
        assert snapshot(name=f"replace {node}", extension_class=JSONSnapshotExtension) == asdict(new_g)
