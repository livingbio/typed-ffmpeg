from dataclasses import asdict
from typing import Optional

from syrupy.extensions.json import JSONSnapshotExtension
from syrupy.types import (
    PropertyFilter,
    PropertyMatcher,
    SerializableData,
    SerializedData,
)

from ..dag.schema import Stream


class DAGSnapshotExtenstion(JSONSnapshotExtension):
    """
    A snapshot extension for the DAG. This extension is used to serialize and match the DAG.
    """

    def serialize(
        self,
        data: "SerializableData",
        *,
        exclude: Optional["PropertyFilter"] = None,
        include: Optional["PropertyFilter"] = None,
        matcher: Optional["PropertyMatcher"] = None,
    ) -> "SerializedData":
        stream = Stream(node=data)

        return super().serialize(asdict(stream))
