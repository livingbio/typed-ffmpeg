from dataclasses import asdict

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..parse_filters import (
    _extract_filter,
    _extract_list,
    _parse_filter,
    _parse_list,
    extract,
)


@pytest.mark.dev_only
def test_extract_list(snapshot: SnapshotAssertion) -> None:
    codecs = _extract_list()
    assert snapshot(extension_class=JSONSnapshotExtension) == codecs


def test_parse_list(snapshot: SnapshotAssertion) -> None:
    text = """Filters:
  T.. = Timeline support
  .S. = Slice threading
  ..C = Command support
  A = Audio input/output
  V = Video input/output
  N = Dynamic number and/or type of input/output
  | = Source or sink filter
 ... abench            A->A       Benchmark part of a filtergraph.
 ..C acompressor       A->A       Audio compressor.
 ... acontrast         A->A       Simple audio dynamic range compression/expansion filter.
 ... acopy             A->A       Copy the input audio unchanged to the output.
 ... acue              A->A       Delay filtering to match a cue.
 ... acrossfade        AA->A      Cross fade two input audio streams.
 .S. acrossover        A->N       Split audio into per-bands streams.
    """
    filters = _parse_list(text)
    assert snapshot(extension_class=JSONSnapshotExtension) == filters


@pytest.mark.parametrize(
    "text",
    [
        pytest.param(
            """Filter overlay
  Overlay a video source on top of the input.
    slice threading supported
    Inputs:
       #0: main (video)
       #1: overlay (video)
    Outputs:
       #0: default (video)
overlay AVOptions:
   x                 <string>     ..FV....... set the x expression (default "0")
   y                 <string>     ..FV....... set the y expression (default "0")
   eof_action        <int>        ..FV....... Action to take when encountering EOF from secondary input  (from 0 to 2) (default repeat)
     repeat          0            ..FV....... Repeat the previous frame.
     endall          1            ..FV....... End both streams.
     pass            2            ..FV....... Pass through the main input.
        """,
            id="overlay",
        ),
        pytest.param(
            """Filter scale
  Scale the input video size and/or convert the image format.
    Inputs:
       #0: default (video)
    Outputs:
       #0: default (video)
scale(2ref) AVOptions:
   w                 <string>     ..FV.....T. Output video width
   width             <string>     ..FV.....T. Output video width
   h                 <string>     ..FV.....T. Output video height
   height            <string>     ..FV.....T. Output video height
   flags             <string>     ..FV....... Flags to pass to libswscale (default "")
   interl            <boolean>    ..FV....... set interlacing (default false)
   in_color_matrix   <string>     ..FV....... set input YCbCr type (default "auto")
     auto                         ..FV.......
                     """,
            id="scale",
        ),
    ],
)
def test_parse_filter_options(snapshot: SnapshotAssertion, text: str) -> None:
    options = _parse_filter(text)
    assert snapshot(extension_class=JSONSnapshotExtension) == asdict(options)


@pytest.mark.parametrize(
    "filter",
    [
        "overlay",  # framesync, slice threading
        "scale",
        "concat",  # dynamic input/output
        "alphamerge",  # timeline
    ],
)
def test_extract_filter(snapshot: SnapshotAssertion, filter: str) -> None:
    options = _extract_filter(filter)
    assert snapshot(extension_class=JSONSnapshotExtension) == asdict(options)


@pytest.mark.dev_only
def test_extract_all_filters(snapshot: SnapshotAssertion) -> None:
    filters = extract()
    assert snapshot(extension_class=JSONSnapshotExtension) == filters
