from typing import Optional

from syrupy.extensions.image import PNGImageSnapshotExtension
from syrupy.types import PropertyFilter, PropertyMatcher, SerializableData, SerializedData

from ..dag.schema import Stream


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

    # def matches(
    #     self,
    #     *,
    #     serialized_data: "SerializableData",
    #     snapshot_data: "SerializableData",
    # ) -> bool:
    #     """
    #     Compares serialized data and snapshot data and returns
    #     whether they match.
    #     """
    #     snapshot_image = Image.open(BytesIO(snapshot_data))
    #     serialized_image = Image.open(BytesIO(serialized_data))

    #     snapshot_hash = imagehash.average_hash(snapshot_image)
    #     serialized_hash = imagehash.average_hash(serialized_image)

    #     print(f"snapshot_hash: {snapshot_hash} serialized_hash: {serialized_hash}")
    #     return snapshot_hash == serialized_hash
