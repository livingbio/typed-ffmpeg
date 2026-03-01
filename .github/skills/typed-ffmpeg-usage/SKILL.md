---
name: typed-ffmpeg-usage
description: Guide for using typed-ffmpeg, a modern Python FFmpeg wrapper with extensive typing support and comprehensive filter support. Use this when working with FFmpeg operations, video/audio processing, or filter graphs in Python.
license: MIT
metadata:
  author: livingbio
  version: "1.0"
  compatibility: Python 3.10+
---

# typed-ffmpeg Usage Skill

This skill provides comprehensive guidance for using the **typed-ffmpeg** package, a modern Python FFmpeg wrapper that emphasizes type safety, IDE integration, and comprehensive filter support.

## Package Overview

**typed-ffmpeg** is a zero-dependency Python library (pure standard library) that provides:
- Extensive support for FFmpeg filters with detailed typing and documentation
- Full IDE auto-completion and type checking
- Filter graph visualization and serialization
- Media file analysis (ffprobe integration)
- Input/output options support
- Partial evaluation for modular filter construction

## Installation

```bash
# Basic installation
pip install typed-ffmpeg

# With graph visualization support
pip install 'typed-ffmpeg[graph]'

# For compatibility with ffmpeg-python
pip install typed-ffmpeg-compatible
```

**Note**: FFmpeg must be installed on your system.

## Core API Patterns

### 1. Basic Input and Output

```python
import ffmpeg

# Simple transcoding
stream = ffmpeg.input("input.mp4")
stream = stream.output("output.mp4")
stream.run()

# Chain operations
ffmpeg.input("input.mp4").output("output.mp4").run()
```

### 2. Input Options

```python
# Input with options
stream = ffmpeg.input(
    "input.mp4",
    ss="00:00:10",      # Start at 10 seconds
    t="00:00:30",       # Duration of 30 seconds
    r=30,               # Frame rate
    s="1920x1080"       # Resolution
)

# Format-specific options
stream = ffmpeg.input(
    "input.mp4",
    f="mp4",            # Force format
    codec="h264",       # Codec selection
    hwaccel="cuda"      # Hardware acceleration
)
```

### 3. Output Options

```python
# Output with encoding options
stream = (
    ffmpeg
    .input("input.mp4")
    .output(
        "output.mp4",
        vcodec="libx264",      # Video codec
        acodec="aac",          # Audio codec
        video_bitrate="2M",    # Video bitrate
        audio_bitrate="192k",  # Audio bitrate
        preset="fast",         # Encoding preset
        crf=23                 # Quality (lower = better)
    )
)
```

### 4. Stream Selection

```python
# Select specific streams
video = ffmpeg.input("input.mp4").video  # Video stream
audio = ffmpeg.input("input.mp4").audio  # Audio stream

# Select by index
stream = ffmpeg.input("input.mp4")[0]  # First stream
video = ffmpeg.input("input.mp4").video(0)  # First video stream
audio = ffmpeg.input("input.mp4").audio(0)  # First audio stream
```

## Filter Application

### Basic Filters

```python
import ffmpeg

# Apply video filters
stream = (
    ffmpeg
    .input("input.mp4")
    .hflip()                    # Horizontal flip
    .vflip()                    # Vertical flip
    .scale(width=1280, height=720)  # Scale video
    .output("output.mp4")
)

# Audio filters
stream = (
    ffmpeg
    .input("input.mp3")
    .audio
    .volume(volume=2.0)         # Increase volume
    .output("output.mp3")
)
```

### Complex Filter Graphs

```python
import ffmpeg
import ffmpeg.filters

# Multiple inputs
in1 = ffmpeg.input("video1.mp4")
in2 = ffmpeg.input("video2.mp4")

# Concatenate videos
output = (
    ffmpeg.filters
    .concat(in1, in2, n=2, v=1, a=0)
    .video(0)
    .output("output.mp4")
)

# Overlay example
main = ffmpeg.input("main.mp4")
overlay = ffmpeg.input("overlay.png")

output = (
    main
    .video
    .overlay(
        overlay.hflip(),
        x=10,
        y=10
    )
    .output("output.mp4")
)
```

### Filter with Expressions

```python
import ffmpeg

# Use expressions for dynamic values
stream = (
    ffmpeg
    .input("input.mp4")
    .drawtext(
        text="Time: %{pts\\:hms}",
        x="(w-text_w)/2",       # Center horizontally
        y="h-th-10",            # Bottom with padding
        fontsize=24,
        fontcolor="white"
    )
    .output("output.mp4")
)
```

## Media File Analysis (ffprobe)

### Basic Probing

```python
import ffmpeg

# Get media information
info = ffmpeg.probe("video.mp4")

# Access format information
duration = float(info['format']['duration'])
bitrate = int(info['format']['bit_rate'])
format_name = info['format']['format_name']

# Access stream information
for stream in info['streams']:
    codec_type = stream['codec_type']  # 'video', 'audio', etc.
    codec_name = stream['codec_name']
    
    if codec_type == 'video':
        width = stream['width']
        height = stream['height']
        fps = eval(stream['r_frame_rate'])  # e.g., "30/1"
```

### Structured Probing

```python
import ffmpeg

# Get structured probe object
probe_result = ffmpeg.probe_obj("video.mp4")

# Access with typed attributes
format_info = probe_result.format
print(f"Duration: {format_info.duration}s")
print(f"Size: {format_info.size} bytes")

# Iterate streams
for stream in probe_result.streams:
    if stream.codec_type == 'video':
        print(f"Video: {stream.width}x{stream.height} @ {stream.r_frame_rate}")
    elif stream.codec_type == 'audio':
        print(f"Audio: {stream.sample_rate}Hz, {stream.channels} channels")
```

## Advanced Features

### Filter Graph Compilation

```python
import ffmpeg

# Build filter graph
stream = (
    ffmpeg
    .input("input.mp4")
    .hflip()
    .scale(width=1280, height=720)
    .output("output.mp4")
)

# Compile to FFmpeg command (without executing)
cmd = ffmpeg.compile(stream)
print(" ".join(cmd))
# Output: ['ffmpeg', '-i', 'input.mp4', '-filter_complex', '...', 'output.mp4']

# Execute the command
stream.run()

# Execute with custom options
stream.run(overwrite_output=True, capture_stdout=True)
```

### Graph Visualization

```python
import ffmpeg

# Create filter graph
stream = (
    ffmpeg
    .input("input.mp4")
    .hflip()
    .scale(width=1280, height=720)
    .output("output.mp4")
)

# Visualize in Jupyter/IPython (returns IPython display object)
stream  # Just return the stream object

# Get Graphviz source
graph = stream.view()  # Returns Graphviz object

# Save visualization
graph.render("filter_graph", format="png")
```

### Multiple Inputs and Outputs

```python
import ffmpeg

# Multiple inputs
video = ffmpeg.input("video.mp4")
audio = ffmpeg.input("audio.mp3")

# Combine video and audio
output = (
    ffmpeg
    .output(
        video.video,
        audio.audio,
        filename="output.mp4",
        vcodec="copy",
        acodec="copy"
    )
)

# Multiple outputs from one input
input_stream = ffmpeg.input("input.mp4")

output1 = input_stream.output("output1.mp4", vcodec="libx264")
output2 = input_stream.output("output2.webm", vcodec="libvpx")

# Merge outputs
merged = ffmpeg.merge_outputs(output1, output2)
merged.run()
```

### Partial Evaluation

```python
import ffmpeg

# Create reusable filter chains
def watermark_filter(stream, watermark_path):
    """Reusable watermark filter."""
    watermark = ffmpeg.input(watermark_path)
    return stream.overlay(watermark, x=10, y=10)

# Apply to different videos
video1 = ffmpeg.input("video1.mp4")
video2 = ffmpeg.input("video2.mp4")

output1 = watermark_filter(video1, "logo.png").output("out1.mp4")
output2 = watermark_filter(video2, "logo.png").output("out2.mp4")
```

## Type Safety and IDE Integration

### Type Annotations

```python
import ffmpeg
from ffmpeg import VideoStream, AudioStream, AVStream

# Functions with type hints work seamlessly
def process_video(input_path: str) -> VideoStream:
    """Process video with type safety."""
    stream: AVStream = ffmpeg.input(input_path)
    video: VideoStream = stream.video
    return video.hflip().scale(width=1280, height=720)

# IDE will provide auto-completion for filter methods
result = process_video("input.mp4")
```

### Filter Parameters

```python
# Most filter parameters have type hints and documentation
stream = (
    ffmpeg
    .input("input.mp4")
    .scale(
        width=1920,           # int | str | Expression
        height=1080,          # int | str | Expression
        flags="bilinear",     # str (scaling algorithm)
        force_original_aspect_ratio="disable"  # Literal type
    )
)

# IDE will show:
# - Parameter names and types
# - Documentation from FFmpeg
# - Valid values for enums/literals
```

## Error Handling

### Exception Types

```python
import ffmpeg
from ffmpeg import FFMpegExecuteError, FFMpegTypeError, FFMpegValueError

try:
    stream = ffmpeg.input("input.mp4").output("output.mp4")
    stream.run()
except FFMpegExecuteError as e:
    # FFmpeg command failed during execution
    print(f"FFmpeg error: {e.stderr}")
    print(f"Command: {e.cmd}")
except FFMpegTypeError as e:
    # Type-related error (e.g., wrong stream type)
    print(f"Type error: {e}")
except FFMpegValueError as e:
    # Value-related error (e.g., invalid parameter)
    print(f"Value error: {e}")
```

### Validation

```python
import ffmpeg

# Enable validation during filter graph construction
stream = (
    ffmpeg
    .input("input.mp4")
    .hflip()
    .output("output.mp4")
)

# Compile checks for basic errors
try:
    cmd = ffmpeg.compile(stream)
except Exception as e:
    print(f"Filter graph error: {e}")
```

## Common Patterns and Examples

### Video Transcoding

```python
import ffmpeg

# Transcode to H.264 with specific settings
(
    ffmpeg
    .input("input.mkv")
    .output(
        "output.mp4",
        vcodec="libx264",
        preset="medium",
        crf=23,
        acodec="aac",
        audio_bitrate="192k"
    )
    .run()
)
```

### Extract Audio from Video

```python
import ffmpeg

# Extract audio only
(
    ffmpeg
    .input("video.mp4")
    .output("audio.mp3", acodec="libmp3lame", audio_bitrate="320k")
    .run()
)

# Or using stream selection
(
    ffmpeg
    .input("video.mp4")
    .audio
    .output("audio.wav", acodec="pcm_s16le")
    .run()
)
```

### Thumbnail Generation

```python
import ffmpeg

# Generate thumbnail at specific time
(
    ffmpeg
    .input("video.mp4", ss="00:01:30")
    .output("thumbnail.jpg", vframes=1)
    .run()
)

# Generate multiple thumbnails
(
    ffmpeg
    .input("video.mp4")
    .filter("fps", fps=1/10)  # One frame every 10 seconds
    .output("thumbnails/thumb_%04d.jpg")
    .run()
)
```

### Video Concat Without Re-encoding

```python
import ffmpeg

# Create concat demuxer input
inputs = [
    ffmpeg.input(f"part{i}.mp4") for i in range(1, 4)
]

# Concatenate without re-encoding
(
    ffmpeg
    .concat(*inputs, v=1, a=1)
    .output("full_video.mp4", codec="copy")
    .run()
)
```

### Picture-in-Picture

```python
import ffmpeg

# Main video
main = ffmpeg.input("main.mp4")

# PiP video (scaled down)
pip_video = (
    ffmpeg
    .input("pip.mp4")
    .scale(width=320, height=240)
)

# Overlay in top-right corner
output = (
    main
    .overlay(
        pip_video,
        x="main_w-overlay_w-10",  # 10px from right
        y="10"                     # 10px from top
    )
    .output("output.mp4")
)

output.run()
```

### Apply Filters Conditionally

```python
import ffmpeg

def process_video(input_path, should_flip=False, target_width=None):
    """Process video with optional transformations."""
    stream = ffmpeg.input(input_path)
    
    if should_flip:
        stream = stream.hflip()
    
    if target_width:
        stream = stream.scale(width=target_width, height=-1)  # -1 = auto
    
    return stream.output("output.mp4")

# Use with different configurations
process_video("input.mp4", should_flip=True, target_width=1920).run()
```

## Best Practices

### 1. Always Specify Codecs

```python
# Good - explicit codecs
ffmpeg.input("input.mp4").output(
    "output.mp4",
    vcodec="libx264",
    acodec="aac"
)

# Avoid - implicit codec selection
ffmpeg.input("input.mp4").output("output.mp4")  # May use defaults
```

### 2. Use Hardware Acceleration When Available

```python
# With NVENC (NVIDIA)
stream = ffmpeg.input("input.mp4").output(
    "output.mp4",
    vcodec="h264_nvenc",
    preset="fast"
)

# With hardware decoding
stream = ffmpeg.input(
    "input.mp4",
    hwaccel="cuda"
).output(
    "output.mp4",
    vcodec="h264_nvenc"
)
```

### 3. Check Media Info Before Processing

```python
import ffmpeg

# Probe before processing
info = ffmpeg.probe("input.mp4")
video_stream = next(s for s in info['streams'] if s['codec_type'] == 'video')

width = video_stream['width']
height = video_stream['height']

# Decide processing based on properties
if width > 1920:
    # Downscale large videos
    stream = ffmpeg.input("input.mp4").scale(width=1920, height=-1)
else:
    # Keep original size
    stream = ffmpeg.input("input.mp4")
```

### 4. Handle Errors Gracefully

```python
import ffmpeg
from ffmpeg import FFMpegExecuteError

def safe_transcode(input_path, output_path):
    """Transcode with error handling."""
    try:
        (
            ffmpeg
            .input(input_path)
            .output(output_path, vcodec="libx264", acodec="aac")
            .run(capture_stdout=True, capture_stderr=True)
        )
        return True
    except FFMpegExecuteError as e:
        print(f"Error transcoding {input_path}:")
        print(e.stderr.decode())
        return False
```

### 5. Use Overwrite Protection

```python
import ffmpeg
import os

output_path = "output.mp4"

# Check if file exists
if os.path.exists(output_path):
    response = input(f"{output_path} exists. Overwrite? (y/n): ")
    if response.lower() != 'y':
        exit()

# Or use overwrite_output parameter
stream = ffmpeg.input("input.mp4").output(output_path)
stream.run(overwrite_output=True)  # Will overwrite without asking
```

## Common Gotchas

### 1. Stream Types Matter

```python
# Error: can't apply video filter to audio stream
audio = ffmpeg.input("input.mp3").audio
audio.hflip()  # ERROR: hflip is for video only

# Correct: use appropriate stream type
video = ffmpeg.input("input.mp4").video
video.hflip()  # OK
```

### 2. Filter Order Matters

```python
# Order affects output
stream = (
    ffmpeg
    .input("input.mp4")
    .scale(width=1920, height=1080)
    .crop(x=0, y=0, width=1280, height=720)  # Crops from scaled video
)

# vs
stream = (
    ffmpeg
    .input("input.mp4")
    .crop(x=0, y=0, width=1280, height=720)  # Crops from original
    .scale(width=1920, height=1080)
)
```

### 3. Stream Selection is Explicit

```python
# Won't work as expected - outputs all streams
input_stream = ffmpeg.input("input.mp4")
output = input_stream.output("output.mp4")  # All streams

# Correct - select specific stream
input_stream = ffmpeg.input("input.mp4")
output = input_stream.video.output("output.mp4")  # Only video
```

### 4. Some Filters Need String Parameters

```python
# Some filters accept expressions as strings
stream = (
    ffmpeg
    .input("input.mp4")
    .scale(width="iw*2", height="ih*2")  # String expression
)

# vs direct values
stream = (
    ffmpeg
    .input("input.mp4")
    .scale(width=1920, height=1080)  # Integer values
)
```

## Getting Help

### In-IDE Documentation

```python
import ffmpeg

# IDE will show docstrings with Ctrl+Space or similar
ffmpeg.input(  # Shows all parameters and their types

# Filter documentation includes FFmpeg docs
stream.scale(  # Shows scale filter documentation
```

### Debugging Filter Graphs

```python
import ffmpeg

# See the generated FFmpeg command
stream = ffmpeg.input("input.mp4").hflip().output("output.mp4")
cmd = ffmpeg.compile(stream)
print(" ".join(cmd))

# Visualize the filter graph (requires graphviz)
stream.view()
```

### Testing Without Execution

```python
import ffmpeg

# Compile but don't run
stream = ffmpeg.input("input.mp4").output("output.mp4")
cmd = ffmpeg.compile(stream)

# Manually run to see FFmpeg output
import subprocess
subprocess.run(cmd)
```

## Package Information

- **Repository**: https://github.com/livingbio/typed-ffmpeg
- **Documentation**: https://livingbio.github.io/typed-ffmpeg/
- **Interactive Playground**: https://livingbio.github.io/typed-ffmpeg-playground/
- **PyPI**: https://pypi.org/project/typed-ffmpeg/
- **Python Version**: 3.10+ required
- **Dependencies**: None (pure Python standard library)
- **Optional Dependencies**: graphviz (for visualization)

## Additional Resources

- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)
- [typed-ffmpeg Examples](https://livingbio.github.io/typed-ffmpeg/usage/typed/)
- [Filter Reference](https://ffmpeg.org/ffmpeg-filters.html)

## Notes for AI Agents

When helping users with typed-ffmpeg:

1. **Always import ffmpeg first**: `import ffmpeg`
2. **Use type hints**: The library is fully typed, leverage this for correctness
3. **Chain operations**: The fluent API allows method chaining
4. **Check stream types**: Video, audio, and subtitle streams have different available filters
5. **Probe before processing**: Use `ffmpeg.probe()` to check media properties
6. **Compile to debug**: Use `ffmpeg.compile()` to see the generated command
7. **Handle errors**: Wrap execution in try/except for `FFMpegExecuteError`
8. **Reference FFmpeg docs**: Filter parameters match FFmpeg's filter documentation
9. **Use visualization**: Graph visualization helps understand complex filter chains
10. **Zero dependencies**: Remember this is pure Python - no external deps besides FFmpeg binary

---

This skill file provides comprehensive guidance for working with typed-ffmpeg. Use it to help users build FFmpeg filter graphs, transcode media, and leverage Python's type system for safer video/audio processing workflows.
