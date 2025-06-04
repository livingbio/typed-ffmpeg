#!/usr/bin/env python3
"""
XSD to Python Dataclasses Generator

This script converts XSD (XML Schema Definition) files to Python dataclasses.
It's specifically designed to work with FFprobe's XSD schema but can be adapted for other XSD files.

Requirements:
    - Python 3.7+

Usage:
    python xsd_to_dataclasses.py ffprobe.xsd

This will generate a new file called 'ffprobe_dataclasses.py' containing all the dataclass definitions.

Features:
    - Converts XSD complex types to Python dataclasses
    - Handles optional fields and unbounded sequences
    - Preserves type information from XSD
    - Generates frozen dataclasses with keyword-only arguments
    - Generates a registered_types dictionary for type resolution
"""

import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass


@dataclass(frozen=True)
class XSDElement:
    """Represents an XSD element with its properties."""

    name: str
    type_name: str
    max_occurs: str = "1"


@dataclass(frozen=True)
class XSDAttribute:
    """Represents an XSD attribute with its properties."""

    name: str
    type_name: str


def get_python_type(xsd_type: str) -> str:
    """
    Convert XSD type to Python type.

    Args:
        xsd_type: The XSD type to convert

    Returns:
        The corresponding Python type

    Examples:
        >>> get_python_type("string")
        'str'
        >>> get_python_type("int")
        'int'
        >>> get_python_type("unknown")
        'Any'
    """
    type_mapping = {
        "string": "str",
        "int": "int",
        "long": "int",
        "float": "float",
        "boolean": "bool",
    }
    return type_mapping.get(xsd_type, "Any")


def parse_xsd_element(element: ET.Element) -> XSDElement:
    """
    Parse an XSD element into a structured object.

    Args:
        element: The XSD element to parse

    Returns:
        An XSDElement object containing the parsed information
    """
    name = element.get("name", "")
    type_name = element.get("type", "").split(":")[-1]
    max_occurs = element.get("maxOccurs", "1")
    return XSDElement(name=name, type_name=type_name, max_occurs=max_occurs)


def parse_xsd_attribute(attr: ET.Element) -> XSDAttribute:
    """
    Parse an XSD attribute into a structured object.

    Args:
        attr: The XSD attribute to parse

    Returns:
        An XSDAttribute object containing the parsed information
    """
    name = attr.get("name", "")
    type_name = attr.get("type", "").split(":")[-1]
    return XSDAttribute(name=name, type_name=type_name)


def get_field_type(element: XSDElement) -> str:
    """
    Generate the Python type annotation for an XSD element.

    Args:
        element: The XSD element to generate type for

    Returns:
        A string representing the Python type annotation

    Examples:
        >>> get_field_type(XSDElement("test", "string", "1"))
        'Optional["string"]'
        >>> get_field_type(XSDElement("test", "string", "unbounded"))
        'Optional[tuple["string", ...]]'
    """
    if element.max_occurs == "unbounded":
        return f'Optional[tuple["{element.type_name}", ...]]'
    return f'Optional["{element.type_name}"]'


def find_elements_with_namespace(
    element: ET.Element, xpath: str, ns: dict[str, str]
) -> list[ET.Element]:
    """
    Find elements using XPath-like syntax with namespace support.

    Args:
        element: The root element to search from
        xpath: The XPath-like expression to search for
        ns: The namespace mapping

    Returns:
        A list of matching elements
    """
    # Only support simple .//prefix:tag or //prefix:tag
    if xpath.startswith(".//"):
        part = xpath[3:]
    elif xpath.startswith("//"):
        part = xpath[2:]
    else:
        part = xpath
    if ":" in part:
        prefix, tag = part.split(":")
        if prefix in ns:
            tag = f"{{{ns[prefix]}}}{tag}"
    else:
        tag = part
    # Use iter to find all descendants with the tag
    return list(element.iter(tag))


def get_choice_types(choice: ET.Element, ns: dict[str, str]) -> list[str]:
    """
    Get the types from a choice element.

    Args:
        choice: The choice element
        ns: The namespace mapping

    Returns:
        A list of type names
    """
    types = []
    for element in choice.findall("./{*}element"):
        type_name = element.get("type", "").split(":")[-1]
        if type_name:
            types.append(type_name)
    return types


def generate_dataclass_fields(
    complex_type: ET.Element, ns: dict[str, str]
) -> list[str]:
    """
    Generate field definitions for a dataclass from an XSD complex type.

    Args:
        complex_type: The XSD complex type element
        ns: The XML namespace mapping

    Returns:
        A list of field definition strings
    """
    fields = []

    # Handle sequence elements
    for sequence in find_elements_with_namespace(complex_type, ".//xsd:sequence", ns):
        for element in sequence.findall("./{*}element"):
            xsd_element = parse_xsd_element(element)
            if xsd_element.max_occurs == "unbounded":
                # Inline the unbounded sequence directly
                field_type = f'Optional[tuple["{xsd_element.type_name}", ...]]'
                fields.append(f"    {xsd_element.name}: {field_type} = None")
            else:
                field_type = f'Optional["{xsd_element.type_name}"]'
                fields.append(f"    {xsd_element.name}: {field_type} = None")

    # Handle choice elements
    for choice in find_elements_with_namespace(complex_type, ".//xsd:choice", ns):
        choice_types = get_choice_types(choice, ns)
        if choice_types:
            # Get the name from the parent element's name attribute
            name = complex_type.get("name", "choice")

            # Create a Union type for the choice
            union_type = " | ".join(f'"{t}"' for t in choice_types)
            if choice.get("maxOccurs") == "unbounded":
                field_type = f"Optional[tuple[Union[{union_type}], ...]]"
            else:
                field_type = f"Optional[Union[{union_type}]]"
            fields.append(f"    {name}: {field_type} = None")

    # Handle attributes
    for attr in complex_type.findall("./{*}attribute"):
        xsd_attr = parse_xsd_attribute(attr)
        field_type = f"Optional[{get_python_type(xsd_attr.type_name)}]"
        fields.append(f"    {xsd_attr.name}: {field_type} = None")

    return fields


def generate_dataclass(
    class_name: str, complex_type: ET.Element, ns: dict[str, str]
) -> str:
    """
    Generate a dataclass definition from an XSD complex type.

    Args:
        class_name: The name of the class to generate
        complex_type: The XSD complex type element
        ns: The XML namespace mapping

    Returns:
        A string containing the dataclass definition
    """
    fields = generate_dataclass_fields(complex_type, ns)
    fields_str = "\n".join(fields)

    return f"""@dataclass(kw_only=True, frozen=True)
class {class_name}:
{fields_str}
"""


def generate_registered_types(class_names: list[str]) -> str:
    """
    Generate the registered_types dictionary.

    Args:
        class_names: List of all generated class names

    Returns:
        A string containing the registered_types dictionary definition
    """
    # Add common Python types
    common_types = {
        "int": "int",
        "str": "str",
        "float": "float",
        "bool": "bool",
        "None": "None",
    }

    # Create entries for all classes
    class_entries = {name: name for name in class_names}

    # Combine all entries
    all_entries = {**class_entries, **common_types}

    # Generate the dictionary string
    entries = [f'    "{key}": {value},' for key, value in sorted(all_entries.items())]
    entries_str = "\n".join(entries)

    return f"""\nregistered_types = {{
{entries_str}
}}"""


def parse_xsd_file(xsd_file: str) -> tuple[ET.Element, dict[str, str]]:
    """
    Parse an XSD file and return its root element and namespace mapping.

    Args:
        xsd_file: Path to the XSD file

    Returns:
        A tuple containing the root element and namespace mapping
    """
    tree = ET.parse(xsd_file)
    root = tree.getroot()

    # Extract namespace from root element
    ns = {}
    for key, value in root.attrib.items():
        if key.startswith("xmlns:"):
            ns[key[6:]] = value
        elif key == "xmlns":
            ns["xsd"] = value

    # Ensure xsd namespace is present
    if "xsd" not in ns:
        ns["xsd"] = "http://www.w3.org/2001/XMLSchema"

    return root, ns


def generate_dataclasses(root: ET.Element, ns: dict[str, str]) -> tuple[str, list[str]]:
    """
    Generate dataclass definitions from an XSD root element.

    Args:
        root: The XSD root element
        ns: The XML namespace mapping

    Returns:
        A tuple containing the generated code and list of class names
    """
    complex_types = find_elements_with_namespace(root, ".//xsd:complexType", ns)
    class_names = []
    output = """#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Optional, Union, tuple

"""

    for complex_type in complex_types:
        name = complex_type.get("name")
        if name:
            class_names.append(name)
            output += generate_dataclass(name, complex_type, ns) + "\n"

    output += generate_registered_types(class_names)
    return output, class_names


def main() -> None:
    """
    Main function to convert XSD to Python dataclasses.

    Usage:
        python xsd_to_dataclasses.py <xsd_file>
    """
    if len(sys.argv) != 2:
        print("Usage: python xsd_to_dataclasses.py <xsd_file>")
        sys.exit(1)

    xsd_file = sys.argv[1]
    root, ns = parse_xsd_file(xsd_file)
    output, _ = generate_dataclasses(root, ns)

    with open("ffprobe_dataclasses.py", "w") as f:
        f.write(output)


if __name__ == "__main__":
    main()
