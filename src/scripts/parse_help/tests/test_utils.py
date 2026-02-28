import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..utils import (
    parse_av_option,
    parse_general_option,
    parse_section_tree,
    run_ffmpeg_command,
)


def test_run_ffmpeg_command() -> None:
    """Test that run_ffmpeg_command executes and returns output."""
    output = run_ffmpeg_command(["-version"])
    assert "ffmpeg version" in output
    assert len(output) > 0


@pytest.mark.parametrize(
    "text",
    [
        pytest.param(
            """Print help / information / capabilities:
-L                  show license
-h topic            show help
-? topic            show help
-help topic         show help""",
            id="help",
        ),
        pytest.param(
            """AVCodecContext AVOptions:
  -b                 <int64>      E..VA...... set bitrate (in bits/s) (from 0 to I64_MAX) (default 200000)
  -ab                <int64>      E...A...... set bitrate (in bits/s) (from 0 to INT_MAX) (default 128000)
  -bt                <int>        E..VA...... Set video bitrate tolerance (in bits/s). In 1-pass mode, bitrate tolerance specifies how far ratecontrol is willing to deviate from the target average bitrate value. This is not related to minimum/maximum bitrate. Lowering tolerance too much has an adverse effect on quality. (from 0 to INT_MAX) (default 4000000)
  -flags             <flags>      ED.VAS..... (default 0)
     unaligned                    .D.V....... allow decoders to produce unaligned output
     mv4                          E..V....... use four motion vectors per macroblock (MPEG-4)
    """,
            id="AVOptions",
        ),
        pytest.param(
            """Hyper fast Audio and Video encoder
usage: ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}...

Getting help:
    -h      -- print basic options
    -h long -- print more options
    -h full -- print all options (including all format and codec specific options, very long)
    -h type=name -- print all options for the named decoder/encoder/demuxer/muxer/filter/bsf/protocol
    See man ffmpeg for detailed description of the options.
""",
            id="help_full_with_noise",
        ),
        pytest.param(
            """ffv1 encoder AVOptions:
  -slicecrc          <boolean>    E..V....... Protect slices with CRCs (default auto)
  -coder             <int>        E..V....... Coder type (from -2 to 2) (default rice)
     rice            0            E..V....... Golomb rice
     range_def       -2           E..V....... Range with default table
     range_tab       2            E..V....... Range with custom table
     ac              1            E..V....... Range with custom table (the ac option exists for compatibility and is deprecated)
  -context           <int>        E..V....... Context model (from 0 to 1) (default 0)

ffvhuff AVOptions:
  -non_deterministic <boolean>    E..V....... Allow multithreading for e.g. context=1 at the expense of determinism (default false)
  -pred              <int>        E..V....... Prediction method (from 0 to 2) (default left)
     left            0            E..V.......
     plane           1            E..V.......
     median          2            E..V.......
  -context           <int>        E..V....... Set per-frame huffman tables (from 0 to 1) (default 0)
""",
            id="multiple_sections",
        ),
        pytest.param(
            """Filter overlay
  Overlay a video source on top of the input.
    slice threading supported
    Inputs:
       #0: main (video)
       #1: overlay (video)
    Outputs:
       #0: default (video)""",
            id="filter_help_with_io",
        ),
    ],
)
def test_parse_section_tree(text: str, snapshot: SnapshotAssertion) -> None:
    tree = parse_section_tree(text)
    assert snapshot(extension_class=JSONSnapshotExtension) == tree


@pytest.mark.parametrize(
    "text, section",
    [
        pytest.param(
            """ffvhuff AVOptions:
  -non_deterministic <boolean>    E..V....... Allow multithreading for e.g. context=1 at the expense of determinism (default false)
  -pred              <int>        E..V....... Prediction method (from 0 to 2) (default left)
     left            0            E..V.......
     plane           1            E..V.......
     median          2            E..V.......
  -context           <int>        E..V....... Set per-frame huffman tables (from 0 to 1) (default 0)""",
            "ffvhuff AVOptions:",
            id="option-without-min-max",
        ),
        pytest.param(
            """dfpwm demuxer AVOptions:
  -sample_rate       <int>        .D.........  (from 0 to INT_MAX) (default 48000)
  -channels          <int>        .D........P  (from 0 to INT_MAX) (default 1)
  -ch_layout         <channel_layout> .D......... """,
            "dfpwm demuxer AVOptions:",
            id="option-without-default",
        ),
    ],
)
def test_parse_av_option(text: str, section: str, snapshot: SnapshotAssertion) -> None:
    tree = parse_section_tree(text)
    assert snapshot(extension_class=JSONSnapshotExtension) == parse_av_option(
        section, tree
    )


def test_parse_general_option(snapshot: SnapshotAssertion) -> None:
    text = """General options:
-cpuflags flags     force specific cpu flags
-cpucount count     force specific cpu count
-copy_unknown       Copy unknown stream types
"""
    tree = parse_section_tree(text)
    assert snapshot(extension_class=JSONSnapshotExtension) == parse_general_option(
        "General options:", tree
    )
