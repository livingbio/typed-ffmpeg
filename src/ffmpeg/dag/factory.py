import re
from typing import Any

from ..common.schema import FFMpegFilterDef, StreamType
from ..utils.run import _to_tuple
from .nodes import FilterableStream, FilterNode


def filter_node_factory(filter: FFMpegFilterDef, *inputs: FilterableStream, **kwargs: Any) -> FilterNode:

    if isinstance(filter.typings_input, str):
        input_typings = eval(
            filter.typings_input,
            {
                "StreamType": StreamType,
                "re": re,
            }
            | kwargs,
        )
    else:
        input_typings = filter.typings_input

    if isinstance(filter.typings_output, str):
        output_typings = eval(filter.typings_output)
    else:
        output_typings = filter.typings_output

    return FilterNode(
        name=filter.name,
        input_typings=input_typings,
        output_typings=output_typings,
        inputs=inputs,
        kwargs=_to_tuple(kwargs),
    )
