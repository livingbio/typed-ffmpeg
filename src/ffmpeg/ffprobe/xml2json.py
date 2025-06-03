import json
import xml.etree.ElementTree as ET
from typing import Any, cast


def xml_to_dict(element: ET.Element) -> dict[str, Any]:
    """Convert an XML Element to a dictionary representation.

    This function recursively converts an XML Element and its children into a nested
    dictionary structure. Attributes are preserved as dictionary keys, and text content
    is stored under the 'text' key when present.

    Args:
        element: The XML Element to convert.

    Returns:
        A dictionary representation of the XML Element.
            - Attributes are stored as key-value pairs
            - Child elements are stored as nested dictionaries
            - Multiple elements with the same tag are stored as lists
            - Text content is stored under the 'text' key
    """
    node: dict[str, Any] = {}
    if element.attrib:
        node.update(element.attrib)
    children: list[ET.Element] = list(element)
    if children:
        child_dict: dict[str, dict[str, Any] | list[dict[str, Any]]] = {}
        for child in children:
            child_result = xml_to_dict(child)
            if child.tag in child_dict:
                current = child_dict[child.tag]
                if not isinstance(current, list):
                    child_dict[child.tag] = [current]
                cast(list[dict[str, Any]], child_dict[child.tag]).append(child_result)
            else:
                child_dict[child.tag] = child_result
        node.update(child_dict)
    text = (element.text or "").strip()
    if text and (not children or node == {}):
        node["text"] = text
    return node


def xml_string_to_json(xml_string: str) -> str:
    """Convert an XML string to a JSON string.

    This function takes an XML string, parses it into an ElementTree structure,
    converts it to a dictionary using xml_to_dict, and then serializes it to a JSON string.

    Args:
        xml_string: A string containing valid XML data.

    Returns:
        A JSON string representation of the XML data, with the root element's
             tag as the top-level key and the converted dictionary as its value.

    Example:
        >>> xml = "<root><item>value</item></root>"
        >>> xml_string_to_json(xml)
        '{
          "root": {
            "item": {
              "text": "value"
            }
          }
        }'
    """
    root = ET.fromstring(xml_string)
    return json.dumps({root.tag: xml_to_dict(root)}, indent=2)
