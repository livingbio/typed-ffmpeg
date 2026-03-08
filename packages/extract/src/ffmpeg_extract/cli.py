"""Command-line interface for FFmpeg metadata extraction."""

import sys


def main() -> int:
    """Main entry point for ffmpeg-extract CLI."""
    print("ffmpeg-extract CLI")
    print("Extract structured metadata from FFmpeg sources")
    print()
    print("Commands:")
    print("  parse-c       Parse C header files")
    print("  parse-help    Parse FFmpeg --help output")
    print("  parse-docs    Parse FFmpeg documentation")
    print()
    print("Run 'ffmpeg-extract <command> --help' for more information")
    return 0


if __name__ == "__main__":
    sys.exit(main())
