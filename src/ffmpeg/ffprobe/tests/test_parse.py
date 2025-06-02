from dataclasses import asdict
from typing import Optional, Union

from syrupy.assertion import SnapshotAssertion

from ..parse import _get_actual_type, parse_ffprobe


def test_get_actual_type_simple() -> None:
    assert _get_actual_type(int) is int
    assert _get_actual_type(str) is str


def test_get_actual_type_optional() -> None:
    assert _get_actual_type(Optional[int]) is int  # noqa
    assert _get_actual_type(Union[int, None]) is int  # noqa
    assert _get_actual_type(int | None) is int  # Python 3.10+


def test_get_actual_type_nested_union() -> None:
    assert (
        _get_actual_type(Union[int, str, None]) is int  # noqa
    )  # Should return the first non-None type
    assert (
        _get_actual_type(Union[None, str, int]) is str  # noqa
    )  # Should return the first non-None type


def test_get_actual_type_string_annotation() -> None:
    # Simulate string annotation as might be found in dataclasses
    assert _get_actual_type("int") is int
    assert _get_actual_type("str") is str


def test_parse_ffprobe(snapshot: SnapshotAssertion) -> None:
    xml = """
    <ffprobe>
    <format filename="src/ffmpeg/ffprobe/tests/test_probe/test-5sec.mp4" nb_streams="2" nb_programs="0" format_name="mov,mp4,m4a,3gp,3g2,mj2" format_long_name="QuickTime / MOV" start_time="0.000000" duration="5.000000" size="1141852" bit_rate="1826963" probe_score="100">
        <tag key="major_brand" value="isom"/>
        <tag key="minor_version" value="512"/>
        <tag key="compatible_brands" value="isomiso2avc1mp41"/>
        <tag key="encoder" value="Lavf58.76.100"/>
    </format>
</ffprobe>"""

    result = parse_ffprobe(xml)
    result_dict = asdict(result)

    assert snapshot == result_dict
