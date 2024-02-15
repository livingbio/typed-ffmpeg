import os
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.image import PNGImageSnapshotExtension
from syrupy.extensions.json import JSONSnapshotExtension

from ..context import DAGContext
from ..schema import Node, Stream




@pytest.fixture(scope="function")
def drawer(snapshot: SnapshotAssertion) -> Callable[[str, Node], None]:

    def draw(name: str, node: Node) -> None:
        stream = Stream(node=node)
        graph_path = stream.view()

        with open(graph_path, "rb") as ifile:
            assert snapshot(name=name, extension_class=PNGImageSnapshotExtension) == ifile.read()

    return draw