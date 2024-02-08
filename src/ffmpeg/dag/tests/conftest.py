import os
from pathlib import Path
from typing import Callable

import pytest

from ...utils.view import view
from ..schema import Node


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
