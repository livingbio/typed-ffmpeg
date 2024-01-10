# from functools import cached_property

# from pydantic import BaseModel

# from ..nodes.base import Node, Stream
# from ..nodes.filter_node import FilterNode
# from ..nodes.global_node import GlobalNode
# from ..nodes.input_node import InputNode


# def _collect(node: Node) -> tuple[set[Node], set[Stream]]:
#     """Collect all nodes and streams that are upstreamed to the given node"""
#     nodes, streams = set(), set()

#     for stream in node.incoming_streams:
#         _nodes, _streams = _collect(stream.node)
#         nodes |= _nodes
#         streams |= _streams

#     return nodes, streams


# class FFMpegBuilder(BaseModel):
#     node: Node

#     @cached_property
#     def all_nodes(self) -> set[Node]:
#         return _collect(self.node)[0]

#     @cached_property
#     def all_streams(self) -> set[Stream]:
#         return _collect(self.node)[1]

#     @property
#     def all_global_nodes(self) -> list[GlobalNode]:
#         return [node for node in self.all_nodes if isinstance(node, GlobalNode)]

#     @property
#     def all_input_nodes(self) -> list[InputNode]:
#         return [node for node in self.all_nodes if isinstance(node, InputNode)]

#     @property
#     def all_filter_nodes(self) -> list[FilterNode]:
#         return [node for node in self.all_nodes if isinstance(node, FilterNode)]

#     @cached_property
#     def assign_nodes_index(self) -> dict[Node, int]:
#         """Assign the index of each input/filter node"""
#         nodes_index: dict[Node, int] = {}

#         for idx, node in enumerate(self.all_input_nodes + self.all_filter_nodes):
#             nodes_index[node] = idx

#         return nodes_index

#     def outgoing_streams(self, node: Node) -> set[Stream]:
#         """Extract all node's outgoing streams from the given set of streams, Because a node only know its incoming streams"""
#         outgoing_streams: set[Stream] = set()

#         for stream in self.all_streams:
#             if stream.node == node:
#                 outgoing_streams.add(stream)

#         return outgoing_streams

#     def compile_global_args(self) -> list[str]:
#         commands = []
#         for global_node in self.all_global_nodes:
#             commands += global_node.args

#             for key, value in global_node.kwargs.items():
#                 commands += [f"-{key}", value]
#         return commands

#     def compile_input_args(self) -> list[str]:
#         commands = []
#         for input_node in self.all_input_nodes:
#             commands += input_node.args

#             for key, value in input_node.kwargs.items():
#                 commands += [f"-{key}", value]
#         commands += ["-i", input_node.filename]
#         return commands

#     def compile_filter_args(self) -> list[str]:
#         commands = []
#         for filter_node in self.all_filter_nodes:
#             filter_node.incoming_streams
#             self.outgoing_streams(filter_node)

#             commands += filter_node.args

#             for key, value in filter_node.kwargs.items():
#                 commands += [f"-{key}", value]
#         return commands

#     def compile(self) -> list[str]:
#         commands = ["ffmpeg"]

#         commands += self.compile_global_args()
#         commands += self.compile_input_args()
