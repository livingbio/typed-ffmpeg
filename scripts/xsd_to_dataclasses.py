#!/usr/bin/env python3

import sys

from lxml import etree


def get_python_type(xsd_type: str) -> str:
    """Convert XSD type to Python type."""
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
    """Generate a dataclass definition from an XSD complex type."""
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


def main() -> None:
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

    # Generate dataclasses
    output = """#!/usr/bin/env python3

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Union, Tuple

"""

    for complex_type in complex_types:
        name = complex_type.get("name")
        if name:
            output += generate_dataclass(name, complex_type, ns) + "\n"

    # Write to file
    with open("ffprobe_dataclasses.py", "w") as f:
        f.write(output)


if __name__ == "__main__":
    main()
