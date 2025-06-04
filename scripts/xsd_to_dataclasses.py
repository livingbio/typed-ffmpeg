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
    - Includes docstrings for generated classes
    - Handles circular dependencies with forward references
"""

import sys
import xml.etree.ElementTree as ET


def get_python_type(xsd_type: str) -> str:
    """
    Convert XSD type to Python type.

    Args:
        xsd_type: The XSD type to convert

    Returns:
        The corresponding Python type
    """
    type_mapping = {
        "string": "str",
        "int": "int",
        "long": "int",
        "float": "float",
        "double": "float",
        "boolean": "bool",
        "date": "str",
        "dateTime": "str",
        "time": "str",
        "duration": "str",
        "gYear": "str",
        "gMonth": "str",
        "gDay": "str",
        "gYearMonth": "str",
        "gMonthDay": "str",
        "hexBinary": "bytes",
        "base64Binary": "bytes",
        "anyURI": "str",
        "QName": "str",
        "NOTATION": "str",
        "normalizedString": "str",
        "token": "str",
        "language": "str",
        "NMTOKEN": "str",
        "NMTOKENS": "List[str]",
        "Name": "str",
        "NCName": "str",
        "ID": "str",
        "IDREF": "str",
        "IDREFS": "List[str]",
        "ENTITY": "str",
        "ENTITIES": "List[str]",
        "integer": "int",
        "nonPositiveInteger": "int",
        "negativeInteger": "int",
        "nonNegativeInteger": "int",
        "positiveInteger": "int",
        "unsignedLong": "int",
        "unsignedInt": "int",
        "unsignedShort": "int",
        "unsignedByte": "int",
        "decimal": "float",
    }
    return type_mapping.get(xsd_type, "Any")


def get_field_docstring(element: ET.Element, ns: dict[str, str]) -> str:
    """
    Generate docstring for a field based on XSD annotations.

    Args:
        element: The XSD element
        ns: The XML namespace mapping

    Returns:
        A docstring for the field
    """
    doc = []
    for annotation in element.findall(".//xsd:annotation/xsd:documentation", ns):
        if annotation.text:
            doc.append(annotation.text.strip())
    return " ".join(doc)


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
    fields = []
    field_docs = []

    # Get class docstring
    class_doc = []
    for annotation in complex_type.findall(".//xsd:annotation/xsd:documentation", ns):
        if annotation.text:
            class_doc.append(annotation.text.strip())
    class_doc_str = " ".join(class_doc)

    # Handle sequence elements
    for sequence in complex_type.findall(".//xsd:sequence", ns):
        for element in sequence.findall("./xsd:element", ns):
            name = element.get("name") or ""
            type_name = element.get("type", "").split(":")[-1]
            max_occurs = element.get("maxOccurs", "1")

            if max_occurs == "unbounded":
                field_type = f'Optional[List["{type_name}"]]'
            else:
                field_type = f'Optional["{type_name}"]'

            fields.append(f"    {name}: {field_type} = None")

            # Add field documentation
            doc = get_field_docstring(element, ns)
            if doc:
                field_docs.append(f"    {name}: {doc}")

    # Handle choice elements
    for choice in complex_type.findall(".//xsd:choice", ns):
        for element in choice.findall("./xsd:element", ns):
            name = element.get("name") or ""
            type_name = element.get("type", "").split(":")[-1]
            max_occurs = element.get("maxOccurs", "1")

            if max_occurs == "unbounded":
                field_type = f'Optional[List["{type_name}"]]'
            else:
                field_type = f'Optional["{type_name}"]'

            fields.append(f"    {name}: {field_type} = None")

            # Add field documentation
            doc = get_field_docstring(element, ns)
            if doc:
                field_docs.append(f"    {name}: {doc}")

    # Handle attributes
    for attr in complex_type.findall("./xsd:attribute", ns):
        name = attr.get("name") or ""
        type_name = attr.get("type", "").split(":")[-1]

        field_type = get_python_type(type_name)
        field_type = f"Optional[{field_type}]"
        fields.append(f"    {name}: {field_type} = None")

        # Add field documentation
        doc = get_field_docstring(attr, ns)
        if doc:
            field_docs.append(f"    {name}: {doc}")

    # Generate the dataclass
    fields_str = "\n".join(fields)
    field_docs_str = "\n".join(field_docs)

    # Generate docstring
    docstring = f'    """{class_name} dataclass.\n\n'
    if class_doc_str:
        docstring += f"    {class_doc_str}\n\n"
    if field_docs:
        docstring += "    Attributes:\n" + field_docs_str + "\n"
    docstring += '    """'

    return f"""@dataclass(kw_only=True, frozen=True)
class {class_name}:
{docstring}
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
        "List": "List",
        "Optional": "Optional",
        "Any": "Any",
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
    try:
        tree = ET.parse(xsd_file)
    except ET.ParseError as e:
        print(f"Error parsing XSD file: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"XSD file not found: {xsd_file}")
        sys.exit(1)

    root = tree.getroot()

    # Get namespace
    ns = {"xsd": "http://www.w3.org/2001/XMLSchema"}

    # Find all complex types
    try:
        complex_types = root.findall(".//xsd:complexType", ns)
    except Exception as e:
        print(f"Error finding complex types: {e}")
        sys.exit(1)

    class_names = []

    # Generate dataclasses
    output = """#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Any, List, Optional

"""

    for complex_type in complex_types:
        name = complex_type.get("name")
        if name:
            class_names.append(name)
            output += generate_dataclass(name, complex_type, ns) + "\n"

    # Add registered_types dictionary
    output += generate_registered_types(class_names)

    # Write to file
    try:
        with open("ffprobe_dataclasses.py", "w") as f:
            f.write(output)
    except OSError as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
