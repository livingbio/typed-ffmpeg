#!/usr/bin/env python3
"""
XSD to Python Dataclasses Generator

This script converts XSD (XML Schema Definition) files to Python dataclasses.
It's specifically designed to work with FFprobe's XSD schema but can be adapted for other XSD files.

Requirements:
    - Python 3.7+
    - lxml
    - types-lxml (for type checking)

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

from lxml import etree


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
        "boolean": "bool",
    }
    return type_mapping.get(xsd_type, "Any")


def generate_dataclass(
    class_name: str, complex_type: etree._Element, ns: dict[str, str]
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

    # Handle sequence elements
    for sequence in complex_type.findall(".//xsd:sequence", ns):
        for element in sequence.findall("./xsd:element", ns):
            name = element.get("name") or ""
            type_name = element.get("type", "").split(":")[-1]
            max_occurs = element.get("maxOccurs", "1")

            if max_occurs == "unbounded":
                field_type = f'Optional[Tuple["{type_name}", ...]]'
            else:
                field_type = f'Optional["{type_name}"]'

            fields.append(f"    {name}: {field_type} = None")

    # Handle choice elements
    for choice in complex_type.findall(".//xsd:choice", ns):
        for element in choice.findall("./xsd:element", ns):
            name = element.get("name") or ""
            type_name = element.get("type", "").split(":")[-1]
            max_occurs = element.get("maxOccurs", "1")

            if max_occurs == "unbounded":
                field_type = f'Optional[Tuple["{type_name}", ...]]'
            else:
                field_type = f'Optional["{type_name}"]'

            fields.append(f"    {name}: {field_type} = None")

    # Handle attributes
    for attr in complex_type.findall("./xsd:attribute", ns):
        name = attr.get("name") or ""
        type_name = attr.get("type", "").split(":")[-1]

        field_type = get_python_type(type_name)
        field_type = f"Optional[{field_type}]"
        fields.append(f"    {name}: {field_type} = None")

    # Generate the dataclass
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
    tree = etree.parse(xsd_file)
    root = tree.getroot()

    # Get namespace
    ns = {"xsd": "http://www.w3.org/2001/XMLSchema"}

    # Find all complex types
    complex_types = root.findall(".//xsd:complexType", ns)
    class_names = []

    # Generate dataclasses
    output = """#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Optional, Tuple

"""

    for complex_type in complex_types:
        name = complex_type.get("name")
        if name:
            class_names.append(name)
            output += generate_dataclass(name, complex_type, ns) + "\n"

    # Add registered_types dictionary
    output += generate_registered_types(class_names)

    # Write to file
    with open("ffprobe_dataclasses.py", "w") as f:
        f.write(output)


if __name__ == "__main__":
    main()
