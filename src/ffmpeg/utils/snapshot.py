from typing import Optional

from syrupy.extensions.image import PNGImageSnapshotExtension

from ..schema import Stream


class DAGSnapshotExtenstion(PNGImageSnapshotExtension):
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
