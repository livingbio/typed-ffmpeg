"""
typed-ffmpeg: Modern Python FFmpeg wrappers (latest version).

This package re-exports the latest version of typed-ffmpeg (v8).
For version-specific bindings, install typed-ffmpeg-v6, typed-ffmpeg-v7, etc.
"""

# Re-export everything from typed-ffmpeg-v8
try:
    # Try importing from installed package
    from typed_ffmpeg_v8.ffmpeg import *  # noqa: F401, F403
    
    # Import specific items for type checking
    from typed_ffmpeg_v8.ffmpeg import (  # noqa: F401
        input,
        output,
        merge_outputs,
        probe,
        filters,
        streams,
        codecs,
        formats,
    )
except ImportError:
    # Fallback for development: import from workspace
    import sys
    from pathlib import Path
    
    # Add v8 package to path
    v8_path = Path(__file__).parent.parent.parent.parent / "v8" / "src"
    if v8_path.exists():
        sys.path.insert(0, str(v8_path))
        from ffmpeg import *  # noqa: F401, F403

__version__ = "8.0.0"
