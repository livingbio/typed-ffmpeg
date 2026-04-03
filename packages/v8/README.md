# typed-ffmpeg-v8

Typed FFmpeg bindings for FFmpeg 8.x.

## Installation

```bash
pip install typed-ffmpeg-v8
```

Or install the latest version (which uses v8):

```bash
pip install typed-ffmpeg
```

## Usage

```python
import ffmpeg

# Input and output
input_file = ffmpeg.input("input.mp4")
output_file = input_file.hflip().output("output.mp4")
output_file.run()

# Complex filter graph
in_file = ffmpeg.input("input.mp4")
overlay_file = ffmpeg.input("overlay.png")

output = (
    ffmpeg.filters
    .concat(
        in_file.trim(start_frame=10, end_frame=20),
        in_file.trim(start_frame=30, end_frame=40),
    )
    .video(0)
    .overlay(overlay_file.hflip())
    .output("out.mp4")
)

output.run()
```

## Requirements

- Python 3.10+
- FFmpeg 8.x installed on your system

## Features

- Full type hints for all FFmpeg 8.x filters, codecs, and formats
- IDE autocomplete support
- Runtime validation
- Filter graph visualization
- JSON serialization

## Documentation

- [Full Documentation](https://livingbio.github.io/typed-ffmpeg/)
- [API Reference](https://livingbio.github.io/typed-ffmpeg/api/v8/)

## License

MIT License - see LICENSE file for details
