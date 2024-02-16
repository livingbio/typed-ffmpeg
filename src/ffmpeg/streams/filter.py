from ..dag.nodes import FilterableStream, FilterNode
from ..dag.context import DAGContext
from ..utils.typing import override
from .audio import AudioFilter
from .video import VideoFilter


class FilterStream(FilterableStream):
    node: FilterNode
    index: int

    @override
    def label(self, context: DAGContext) -> str:
        if self.node.output_typings and len(self.node.output_typings) > 1:
            return f"{context.get_node_label(self.node)}#{self.index}"
        return f"{context.get_node_label(self.node)}"


class AudioStream(AudioFilter, FilterStream):
    pass


class VideoStream(VideoFilter, FilterStream):
    pass
