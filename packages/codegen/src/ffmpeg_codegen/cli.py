"""Command-line interface for FFmpeg code generation."""

import sys
from pathlib import Path


def main() -> int:
    """Main entry point for ffmpeg-codegen CLI."""
    print("ffmpeg-codegen CLI")
    print("Generate language-specific FFmpeg SDKs from metadata")
    print()
    print("Usage:")
    print("  ffmpeg-codegen --metadata <path> --target <lang> --output <path>")
    print()
    print("Targets:")
    print("  python        Generate Python SDK (typed-ffmpeg)")
    print("  typescript    Generate TypeScript SDK (future)")
    print()
    print("Options:")
    print("  --metadata    Path to extracted metadata directory")
    print("  --target      Target language (python, typescript)")
    print("  --output      Output directory for generated code")
    return 0


if __name__ == "__main__":
    sys.exit(main())
