import pytest
from syrupy.assertion import SnapshotAssertion

from ..ffmpeg_option_parser import parse_ffmpeg_options


@pytest.mark.parametrize(
    "help_text",
    [
        pytest.param(
            """
    -i, --input <input>
    """,
            id="simple_option",
        ),
        pytest.param(
            """
        -s size             set frame size (WxH or abbreviation)
        """,
            id="option_with_description",
        ),
        pytest.param(
            """  -b                 <int64>      E..VA...... set bitrate (in bits/s) (from 0 to I64_MAX) (default 200000)
        """,
            id="option_with_type",
        ),
        pytest.param(
            """
AVFormatContext AVOptions:
  -avioflags         <flags>      ED......... (default 0)
     direct                       ED......... reduce buffering
  -probesize         <int64>      .D......... set probing size (from 32 to I64_MAX) (default 5000000)
  -formatprobesize   <int>        .D......... number of bytes to probe file format (from 0 to 2.14748e+09) (default 1048576)
  -packetsize        <int>        E.......... set packet size (from 0 to INT_MAX) (default 0)
  -fflags            <flags>      ED......... (default autobsf)
     flush_packets                E.......... reduce the latency by flushing out packets immediately
     ignidx                       .D......... ignore index
     genpts                       .D......... generate pts
     nofillin                     .D......... do not fill in missing values that can be exactly calculated
     noparse                      .D......... disable AVParsers, this needs nofillin too
     igndts                       .D......... ignore dts
     discardcorrupt               .D......... discard corrupted frames
     sortdts                      .D......... try to interleave outputted packets by dts
     fastseek                     .D......... fast but inaccurate seeks
     nobuffer                     .D......... reduce the latency introduced by optional buffering
     bitexact                     E.......... do not write random/volatile data
     shortest                     E.........P stop muxing with the shortest stream
     autobsf                      E.......... add needed bsfs automatically""",
            id="option_with_default_value",
        ),
        pytest.param(
            """
Global options (affect whole program instead of just one file):
-loglevel loglevel  set logging level
-v loglevel         set logging level
-report             generate a report
-max_alloc bytes    set maximum size of a single allocated block
-y                  overwrite output files
-n                  never overwrite output files
-ignore_unknown     Ignore unknown stream types
-filter_threads     number of non-complex filter threads
-filter_complex_threads  number of threads for -filter_complex
-stats              print progress report during encoding
-max_error_rate maximum error rate  ratio of decoding errors (0.0: no errors, 1.0: 100% errors) above which ffmpeg returns an error instead of success.
""",
            id="global_options",
        ),
    ],
)
def test_parse_ffmpeg_options(snapshot: SnapshotAssertion, help_text: str) -> None:
    options = parse_ffmpeg_options(help_text)
    assert snapshot == options
