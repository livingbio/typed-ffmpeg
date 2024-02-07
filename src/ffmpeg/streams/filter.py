from ..dag.nodes import FilterableStream, FilterNode
from ..dag.schema import _DAGContext
from ..utils.typing import override
from .audio import AudioFilter
from .video import VideoFilter


class _FilterStream(FilterableStream):
    node: FilterNode
    index: int

    @override
    def label(self, context: _DAGContext) -> str:
        if self.node.output_typings and len(self.node.output_typings) > 1:
            return f"{context.get_node_label(self.node)}#{self.index}"
        return f"{context.get_node_label(self.node)}"


class AudioStream(AudioFilter, _FilterStream):
    pass


class VideoStream(VideoFilter, _FilterStream):
    pass
