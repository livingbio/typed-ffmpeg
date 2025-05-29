import xml.etree.ElementTree as ET


def convert_xsd_type_to_python(xsd_type: str) -> str:
    """Convert XSD type to Python type."""
    type_mapping = {
        "xsd:string": "str",
        "xsd:int": "int",
        "xsd:long": "int",
        "xsd:float": "float",
        "xsd:boolean": "bool",
    }
    return type_mapping.get(xsd_type, "Any")


def get_python_type(attribute) -> str:
    """Get Python type for an attribute."""
    xsd_type = attribute.get("type", "xsd:string")
    python_type = convert_xsd_type_to_python(xsd_type)

    # Make all fields optional for version compatibility
    return f"Optional[{python_type}]"


def generate_dataclass(
    class_name: str, complex_type: ET.Element, namespace: str
) -> str:
    """Generate a Python dataclass from an XSD complex type."""
    fields = []

    # Handle attributes
    for attribute in complex_type.findall(
        ".//xsd:attribute", namespaces={"xsd": namespace}
    ):
        name = attribute.get("name")
        python_type = get_python_type(attribute)
        fields.append(f"    {name}: {python_type} = None")

    # Handle nested elements
    for element in complex_type.findall(
        ".//xsd:element", namespaces={"xsd": namespace}
    ):
        name = element.get("name")
        type_name = element.get("type", "").split(":")[-1]
        max_occurs = element.get("maxOccurs", "1")

        if max_occurs == "unbounded":
            python_type = f'Optional[Tuple["{type_name}", ...]]'
            default = "field(default_factory=tuple)"
        else:
            python_type = f'Optional["{type_name}"]'
            default = "None"

        fields.append(f"    {name}: {python_type} = {default}")

    # Generate the dataclass with frozen=True and kw_only=True
    class_def = f"""@dataclass(frozen=True, kw_only=True)
class {class_name}:
{chr(10).join(fields)}
"""
    return class_def


def process_xsd_file(xsd_file: str) -> str:
    """Process XSD file and generate Python dataclasses."""
    tree = ET.parse(xsd_file)
    root = tree.getroot()

    # Get namespace
    namespace = root.tag.split("}")[0].strip("{")

    # Generate imports
    imports = """from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Union, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from typing import ForwardRef

"""

    # Process all complex types
    complex_types = root.findall(".//xsd:complexType", namespaces={"xsd": namespace})
    class_definitions = []

    for complex_type in complex_types:
        class_name = complex_type.get("name")
        if class_name:
            class_def = generate_dataclass(class_name, complex_type, namespace)
            class_definitions.append(class_def)

    return imports + "\n\n".join(class_definitions)


def main():
    input_file = "ffmpeg/doc/ffprobe.xsd"
    output_file = "ffprobe_dataclasses.py"

    try:
        python_code = process_xsd_file(input_file)
        with open(output_file, "w") as f:
            f.write(python_code)
        print(f"Successfully generated {output_file}")
    except Exception as e:
        print(f"Error processing XSD file: {e}")


if __name__ == "__main__":
    main()
