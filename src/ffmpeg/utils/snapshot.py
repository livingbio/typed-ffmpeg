from typing import Optional

from syrupy.extensions.image import PNGImageSnapshotExtension
from syrupy.types import PropertyFilter, PropertyMatcher, SerializableData, SerializedData

from ..dag.schema import Stream


class DAGSnapshotExtenstion(PNGImageSnapshotExtension):
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
        graph_path = stream.view()

        with open(graph_path, "rb") as ifile:
            return super().serialize(ifile.read())
