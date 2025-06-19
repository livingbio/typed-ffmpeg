from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..parse_help import _parse, extract


def test_parse(snapshot: SnapshotAssertion) -> None:
    text = """

Subtitle options:
-s size             set frame size (WxH or abbreviation)
-sn                 disable subtitle
-scodec codec       force subtitle codec ('copy' to copy stream)
-stag fourcc/tag    force subtitle tag/fourcc
-fix_sub_duration   fix subtitles duration
-canvas_size size   set canvas size (WxH or abbreviation)
-spre preset        set the subtitle options to the indicated preset


AVCodecContext AVOptions:
  -b                 <int64>      E..VA...... set bitrate (in bits/s) (from 0 to I64_MAX) (default 200000)
  -ab                <int64>      E...A...... set bitrate (in bits/s) (from 0 to INT_MAX) (default 128000)
  -bt                <int>        E..VA...... Set video bitrate tolerance (in bits/s). In 1-pass mode, bitrate tolerance specifies how far ratecontrol is willing to deviate from the target average bitrate value. This is not related to minimum/maximum bitrate. Lowering tolerance too much has an adverse effect on quality. (from 0 to INT_MAX) (default 4000000)
  -flags             <flags>      ED.VAS..... (default 0)
     unaligned                    .D.V....... allow decoders to produce unaligned output
     mv4                          E..V....... use four motion vectors per macroblock (MPEG-4)
    """
    assert snapshot(extension_class=JSONSnapshotExtension) == _parse(text)


def test_extract_options_from_help(snapshot: SnapshotAssertion) -> None:
    snapshot(extension_class=JSONSnapshotExtension) == extract()
