from typing import Optional, Union

from syrupy.assertion import SnapshotAssertion

from ..parse import _get_actual_type, parse_ffprobe
from ..schema import programVersionType


def test_get_actual_type_simple() -> None:
    assert _get_actual_type(int) is int
    assert _get_actual_type(str) is str


def test_get_actual_type_optional() -> None:
    assert _get_actual_type(Optional[int]) is int  # noqa
    assert _get_actual_type(Union[int, None]) is int  # noqa
    assert _get_actual_type(int | None) is int  # Python 3.10+
    assert _get_actual_type(programVersionType | None) is programVersionType
    assert _get_actual_type(Union[programVersionType, None]) is programVersionType  # noqa
    assert _get_actual_type(Optional[programVersionType]) is programVersionType  # noqa


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


def test_parse_ffprobe_simple(snapshot: SnapshotAssertion) -> None:
    xml = """
    <ffprobe>
        <streams>
        <stream index="0" codec_name="h264" codec_long_name="H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10" profile="High" codec_type="video" codec_tag_string="avc1" codec_tag="0x31637661" width="1280" height="720" coded_width="1280" coded_height="720" closed_captions="0" film_grain="0" has_b_frames="2" sample_aspect_ratio="1:1" display_aspect_ratio="16:9" pix_fmt="yuv420p" level="31" chroma_location="left" field_order="progressive" refs="4" is_avc="true" nal_length_size="4" id="0x1" r_frame_rate="25/1" avg_frame_rate="25/1" time_base="1/12800" start_pts="0" start_time="0.000000" duration_ts="64000" duration="5.000000" bit_rate="1475520" bits_per_raw_sample="8" nb_frames="125" nb_read_frames="125" nb_read_packets="125" extradata_size="47">
            <disposition default="1" dub="0" original="0" comment="0" lyrics="0" karaoke="0" forced="0" hearing_impaired="0" visual_impaired="0" clean_effects="0" attached_pic="0" timed_thumbnails="0" captions="0" descriptions="0" metadata="0" dependent="0" still_image="0"/>
            <tag key="language" value="und"/>
            <tag key="handler_name" value="VideoHandler"/>
            <tag key="vendor_id" value="[0][0][0][0]"/>
        </stream>
        <stream index="1" codec_name="aac" codec_long_name="AAC (Advanced Audio Coding)" profile="LC" codec_type="audio" codec_tag_string="mp4a" codec_tag="0x6134706d" sample_fmt="fltp" sample_rate="48000" channels="6" channel_layout="5.1" bits_per_sample="0" initial_padding="0" id="0x2" r_frame_rate="0/0" avg_frame_rate="0/0" time_base="1/48000" start_pts="0" start_time="0.000000" duration_ts="240000" duration="5.000000" bit_rate="343115" nb_frames="236" nb_read_frames="235" nb_read_packets="236" extradata_size="5">
            <disposition default="1" dub="0" original="0" comment="0" lyrics="0" karaoke="0" forced="0" hearing_impaired="0" visual_impaired="0" clean_effects="0" attached_pic="0" timed_thumbnails="0" captions="0" descriptions="0" metadata="0" dependent="0" still_image="0"/>
            <tag key="language" value="und"/>
            <tag key="handler_name" value="SoundHandler"/>
            <tag key="vendor_id" value="[0][0][0][0]"/>
        </stream>
    </streams>

    <chapters>
    </chapters>
    <format filename="src/ffmpeg/ffprobe/tests/test_probe/test-5sec.mp4" nb_streams="2" nb_programs="0" format_name="mov,mp4,m4a,3gp,3g2,mj2" format_long_name="QuickTime / MOV" start_time="0.000000" duration="5.000000" size="1141852" bit_rate="1826963" probe_score="100">
        <tag key="major_brand" value="isom"/>
        <tag key="minor_version" value="512"/>
        <tag key="compatible_brands" value="isomiso2avc1mp41"/>
        <tag key="encoder" value="Lavf58.76.100"/>
    </format>
</ffprobe>"""

    result = parse_ffprobe(xml)

    assert snapshot() == result
