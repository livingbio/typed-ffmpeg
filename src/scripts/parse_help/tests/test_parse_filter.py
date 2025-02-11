import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension
from syrupy.extensions.single_file import SingleFileSnapshotExtension

from ffmpeg.common.serialize import to_dict_with_class_info

from ..parse_filter import (
    extract_avfilter_info_from_help,
    extract_filter_help_text,
    parse_section_tree,
)


@pytest.mark.parametrize(
    "filter_name",
    [
        "amovie",  # typing: dictionary
        "adrawgraph",  # typing: color
        "mergeplanes",  # typing: pix_fmt
        "a3dscope",  # typing: video_rate, image_size
        "acrossfade",  # cover _remove_repeat_options
        "bitplanenoise",
        "anlmf",
        "negate",
        "abuffersink",
        "abuffer",
        "afade",
        "trim",
        "scale",
        "blend",
        "adeclip",
        "concat",
        "scale2ref",
        "overlay",  # has duplicate option
        "alphamerge",  # support timeline
    ],
)
def test_parse_filter(snapshot: SnapshotAssertion, filter_name: str) -> None:
    assert snapshot(
        name="help-text", extension_class=SingleFileSnapshotExtension
    ) == extract_filter_help_text(filter_name=filter_name).encode("utf-8")
    assert snapshot(
        name="extract-help-text", extension_class=JSONSnapshotExtension
    ) == to_dict_with_class_info(
        extract_avfilter_info_from_help(filter_name=filter_name)
    )
    assert snapshot(
        name="parse-section-tree", extension_class=JSONSnapshotExtension
    ) == parse_section_tree(text=extract_filter_help_text(filter_name=filter_name))


def test_extract_not_exist_filter() -> None:
    with pytest.raises(ValueError):
        extract_avfilter_info_from_help("not-exist")
