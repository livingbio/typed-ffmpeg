from __future__ import annotations

from abc import ABC, abstractproperty
from typing import Any, Iterable, Mapping

from pydantic import BaseModel, model_validator

from ..schema import StreamType
from ..utils.dag import is_dag


class HashableBaseModel(BaseModel):
    def __hash__(self) -> int:
        return hash(self.model_dump_json())


class Node(HashableBaseModel, ABC, validate_assignment=True):
    name: str
    args: list[str] = []
    kwargs: Mapping[str, Any] = {}

    @abstractproperty
    def incoming_streams(self) -> Iterable[Stream]:
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


class Stream(HashableBaseModel):
    node: Node
    index: int = 0  # the nth child of the node
    selector: StreamType | None = None
