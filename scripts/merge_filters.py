import json
from pathlib import Path
from typing import Any


def convert_nan_to_string(obj: Any) -> Any:
    if isinstance(obj, float) and obj != obj:  # Check for NaN
        return "NaN"
    elif isinstance(obj, dict):
        return {k: convert_nan_to_string(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_nan_to_string(item) for item in obj]
    return obj


def merge_filter_files() -> None:
    # Source directory containing individual filter JSON files
    source_dir = Path("src/scripts/cache/FFMpegFilter")

    # Destination file path
    dest_file = Path("ffmpeg-flow-editor/src/config/filters.json")

    # Create destination directory if it doesn't exist
    dest_file.parent.mkdir(parents=True, exist_ok=True)

    # List to store all filter data
    filters: list[dict[str, Any]] = []

    # Get all JSON files
    json_files = list(source_dir.glob("*.json"))

    if not json_files:
        print(f"No JSON files found in {source_dir}")
        return

    # Read all JSON files in the source directory
    for json_file in json_files:
        try:
            with open(json_file) as f:
                filter_data = json.load(f)
                # Convert NaN values to strings
                filter_data = convert_nan_to_string(filter_data)
                filters.append(filter_data)
        except json.JSONDecodeError as e:
            print(f"Error reading {json_file}: {e}")
        except Exception as e:
            print(f"Unexpected error processing {json_file}: {e}")

    if not filters:
        print("No valid filter data found")
        return

    # Create the final structure
    output_data = {"filters": filters}

    # Write to destination file
    try:
        with open(dest_file, "w") as f:
            json.dump(output_data, f, indent=2)
        print(f"Successfully merged {len(filters)} filters into {dest_file}")
    except Exception as e:
        print(f"Error writing to {dest_file}: {e}")


if __name__ == "__main__":
    merge_filter_files()
