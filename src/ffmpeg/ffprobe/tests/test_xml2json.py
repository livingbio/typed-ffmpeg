import json
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..xml2json import xml_string_to_json, xml_to_dict

test_folder = Path(__file__).parent / "test_xml2json"


def test_xml_to_dict_simple() -> None:
    xml = '<root><item id="1">foo</item><item id="2">bar</item></root>'
    root = ET.fromstring(xml)
    result = xml_to_dict(root)
    expected = {"item": [{"id": "1", "text": "foo"}, {"id": "2", "text": "bar"}]}
    assert result == expected


def test_xml_to_dict_with_attributes_and_text() -> None:
    xml = '<root a="b">hello</root>'
    root = ET.fromstring(xml)
    result = xml_to_dict(root)
    expected = {"a": "b", "text": "hello"}
    assert result == expected


def test_xml_string_to_json() -> None:
    xml = "<root><meta><author>John</author></meta></root>"
    result_json = xml_string_to_json(xml)
    expected_dict = {"root": {"meta": {"author": {"text": "John"}}}}
    assert json.loads(result_json) == expected_dict


@pytest.mark.parametrize(
    "xml",
    [pytest.param(test_folder / p, id=p.name) for p in test_folder.glob("*.xml")],
)
def test_ffprobe_xml(snapshot: SnapshotAssertion, xml: Path) -> None:
    with open(xml) as f:
        xml_string = f.read()
    result_json = xml_string_to_json(xml_string)
    result_dict = json.loads(result_json)
    assert "ffprobe" in result_dict
    assert snapshot(extension_class=JSONSnapshotExtension) == result_dict
