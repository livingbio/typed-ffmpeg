from typing import Literal

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..parse_formats import (
    _extract_format,
    _extract_list,
    _parse_format,
    _parse_list,
    extract,
)


@pytest.mark.dev_only
@pytest.mark.parametrize("type", ["muxers", "demuxers"])
def test_extract_list(
    snapshot: SnapshotAssertion, type: Literal["muxers", "demuxers"]
) -> None:
    codecs = _extract_list(type)
    assert snapshot(extension_class=JSONSnapshotExtension) == codecs


@pytest.mark.parametrize(
    "text",
    [
        pytest.param(
            """File formats:
 D. = Demuxing supported
 .E = Muxing supported
 --
 D  3dostr          3DO STR
  E 3g2             3GP2 (3GPP2 file format)
  E 3gp             3GP (3GPP file format)
 D  4xm             4X Technologies
  E a64             a64 - video for Commodore 64
 D  aa              Audible AA format files
 D  aac             raw ADTS AAC (Advanced Audio Coding)
 D  aax             CRI AAX
 DE ac3             raw AC-3
 DE ac4             raw AC-4
 D  ace             tri-Ace Audio Container""",
            id="formats",
        ),
        pytest.param(
            """File formats:
 D. = Demuxing supported
 .E = Muxing supported
 --
  E 3g2             3GP2 (3GPP2 file format)
  E 3gp             3GP (3GPP file format)
  E a64             a64 - video for Commodore 64
  E ac3             raw AC-3
  E ac4             raw AC-4
  E adts            ADTS AAC (Advanced Audio Coding)
  E adx             CRI ADX
  E aiff            Audio IFF
  E alaw            PCM A-law
  E alp             LEGO Racers ALP
  E alsa            ALSA audio output""",
            id="muxers",
        ),
        pytest.param(
            """File formats:
 D. = Demuxing supported
 .E = Muxing supported
 --
 D  3dostr          3DO STR
 D  4xm             4X Technologies
 D  aa              Audible AA format files
 D  aac             raw ADTS AAC (Advanced Audio Coding)
 D  aax             CRI AAX
 D  ac3             raw AC-3
 D  ac4             raw AC-4
 D  ace             tri-Ace Audio Container
 D  acm             Interplay ACM
 D  act             ACT Voice file format
 D  adf             Artworx Data Format""",
            id="demuxers",
        ),
    ],
)
def test_parse_list(snapshot: SnapshotAssertion, text: str) -> None:
    codecs = _parse_list(text)
    assert snapshot(extension_class=JSONSnapshotExtension) == codecs


@pytest.mark.parametrize(
    "text",
    [
        pytest.param(
            """Muxer mp4 [MP4 (MPEG-4 Part 14)]:
    Common extensions: mp4.
    Mime type: video/mp4.
    Default video codec: h264.
    Default audio codec: aac.
mov/mp4/tgp/psp/tg2/ipod/ismv/f4v muxer AVOptions:
  -movflags          <flags>      E.......... MOV muxer flags (default 0)
     rtphint                      E.......... Add RTP hint tracks
     empty_moov                   E.......... Make the initial moov atom empty
     frag_keyframe                E.......... Fragment at video keyframes
     frag_every_frame              E.......... Fragment at every frame
     separate_moof                E.......... Write separate moof/mdat atoms for each track
     frag_custom                  E.......... Flush fragments on caller requests
     isml                         E.......... Create a live smooth streaming feed (for pushing to a publishing point)
     faststart                    E.......... Run a second pass to put the index (moov atom) at the beginning of the file""",
            id="muxer-mp4",
        ),
        pytest.param(
            """Muxer mov [QuickTime / MOV]:
    Common extensions: mov.
    Default video codec: h264.
    Default audio codec: aac.
mov/mp4/tgp/psp/tg2/ipod/ismv/f4v muxer AVOptions:
  -movflags          <flags>      E.......... MOV muxer flags (default 0)
     rtphint                      E.......... Add RTP hint tracks
     empty_moov                   E.......... Make the initial moov atom empty
     frag_keyframe                E.......... Fragment at video keyframes
     frag_every_frame              E.......... Fragment at every frame
     separate_moof                E.......... Write separate moof/mdat atoms for each track
     frag_custom                  E.......... Flush fragments on caller requests
     isml                         E.......... Create a live smooth streaming feed (for pushing to a publishing point)
     faststart                    E.......... Run a second pass to put the index (moov atom) at the beginning of the file
     omit_tfhd_offset              E.......... Omit the base data offset in tfhd atoms""",
            id="muxer-mov",
        ),
    ],
)
def test_parse_format(snapshot: SnapshotAssertion, text: str) -> None:
    options = _parse_format(text)
    assert snapshot(extension_class=JSONSnapshotExtension) == options


@pytest.mark.parametrize(
    "format, type",
    [
        ("wav", "demuxer"),
        ("mp3", "demuxer"),
        ("mp4", "muxer"),
        ("mov", "muxer"),
    ],
)
def test_extract_format_options(
    snapshot: SnapshotAssertion, format: str, type: Literal["muxer", "demuxer"]
) -> None:
    options = _extract_format(format, type)
    assert snapshot(extension_class=JSONSnapshotExtension) == options


@pytest.mark.dev_only
def test_extract_all_formats(snapshot: SnapshotAssertion) -> None:
    codecs = extract()
    assert snapshot(extension_class=JSONSnapshotExtension) == codecs
