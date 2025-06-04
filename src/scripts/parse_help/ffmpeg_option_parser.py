import re
from dataclasses import dataclass, field


@dataclass
class FFmpegOption:
    name: str
    type: str | None = None
    description: str = ""
    is_global: bool = False
    is_advanced: bool = False
    is_per_file: bool = False
    flags: list[str] = field(default_factory=list)
    default_value: str | None = None


def parse_ffmpeg_options(help_text: str) -> list[FFmpegOption]:
    options = []
    current_section = None

    # Split the text into lines and process
    lines = help_text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Skip empty lines
        if not line:
            i += 1
            continue

        # Check for section headers
        if line.endswith(":"):
            current_section = line.lower()
            i += 1
            continue

        # Parse option lines
        if line.startswith("-"):
            # Extract option name and type
            parts = line.split(maxsplit=1)
            option_name = parts[0]

            # Initialize option
            option = FFmpegOption(
                name=option_name,
                description=parts[1] if len(parts) > 1 else "",
                is_global="global" in current_section if current_section else False,
                is_advanced="advanced" in current_section if current_section else False,
                is_per_file="per-file" in current_section if current_section else False,
            )

            # Extract type if present in description (both formats: <type> and type)
            type_match = re.search(r"<(\w+)>|(\w+)\s+", option.description)
            if type_match:
                option.type = type_match.group(1) or type_match.group(2)

            # Extract flags (format: X..Y..Z..)
            flags_match = re.search(r"([A-Z.]+)\s+", option.description)
            if flags_match:
                flags_str = flags_match.group(1)
                # Split flags into individual characters, excluding dots
                option.flags = [f for f in flags_str if f != "."]

            # Extract default value
            default_match = re.search(r"\(default\s+([^)]+)\)", option.description)
            if default_match:
                option.default_value = default_match.group(1)

            options.append(option)

        i += 1

    return options


def print_options(options: list[FFmpegOption]) -> None:
    for option in options:
        print(f"\nOption: {option.name}")
        if option.type:
            print(f"Type: {option.type}")
        print(f"Description: {option.description}")
        print(
            f"Category: {'Global' if option.is_global else 'Per-file' if option.is_per_file else 'Advanced' if option.is_advanced else 'Unknown'}"
        )
        if option.flags:
            print(f"Flags: {', '.join(option.flags)}")
        if option.default_value:
            print(f"Default: {option.default_value}")


def main() -> None:
    # Read the help text from file
    with open("ffmpeg-h-full.txt") as f:
        help_text = f.read()

    # Parse options
    options = parse_ffmpeg_options(help_text)

    # Print results
    print(f"Found {len(options)} options")
    print_options(options)


if __name__ == "__main__":
    main()
