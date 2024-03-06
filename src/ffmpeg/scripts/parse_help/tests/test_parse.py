import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension
from syrupy.extensions.single_file import SingleFileSnapshotExtension

from ....common.serialize import to_dict_with_class_info
from ..parse import extract_avfilter_info_from_help, help_text, parse_section_tree


@pytest.mark.parametrize(
    "filter_name",
    [
        "amovie",  # typing: dictionary
        "adrawgraph",  # typing: color
        "mergeplanes",  # typing: pix_fmt
        "a3dscope",  # typing: video_rate, image_size
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
    ],
)
def test_help_text(snapshot: SnapshotAssertion, filter_name: str) -> None:
    assert snapshot(name="help-text", extension_class=SingleFileSnapshotExtension) == help_text(
        filter_name=filter_name
    ).encode("utf-8")
    assert snapshot(name="extract-help-text", extension_class=JSONSnapshotExtension) == to_dict_with_class_info(
        extract_avfilter_info_from_help(filter_name=filter_name)
    )
    assert snapshot(name="parse-section-tree", extension_class=JSONSnapshotExtension) == parse_section_tree(
        text=help_text(filter_name=filter_name)
    )
