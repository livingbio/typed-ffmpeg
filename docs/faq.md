# FAQ

## How to use source filter

typed-ffmpeg support ffmpeg source filters:

- How to use predefined video/audio source filter can be found [Complex Filters](./usage/complex-filtering.ipynb)
- How to customize video/audio source filter can be found [Customizing Filters](./usage/customizing-filters.ipynb)


## Why are numeric options like `drawbox(x=..., width=...)` typed as `String`?

Many FFmpeg filter options that look numeric are declared by FFmpeg itself as string options, because they accept **expressions** evaluated per frame, e.g. `x="(iw-w)/2"`, `width="iw/2"` or `thickness="fill"`. typed-ffmpeg mirrors FFmpeg's declared option type, so these parameters are annotated as `String`.

`String` is a type alias, not `str`. It also accepts `int` and `float`, so you never need to convert numbers yourself:

```python
(
    ffmpeg.input("in.mp4")
    .video.drawbox(x=10, y=20, width=320, height=180, thickness=5, color="red")
)
# drawbox=x=10:y=20:width=320:height=180:color=red:thickness=5
```

Values of any other type (e.g. a `list`) are rejected by type checkers such as mypy, pyright or ty. See `ffmpeg.types` for the full definition of each option type.

## Differences Between ffmpeg-python and typed-ffmpeg

typed-ffmpeg is designed with inspiration from ffmpeg-python and aims to follow good design principles. However, due to differences in approach and static typing requirements, there are some key distinctions. Below are the major differences between ffmpeg-python and typed-ffmpeg. If you notice any discrepancies or have suggestions for improvements, feel free to open an issue or submit a pull request.

### Defining Custom Filters for single output

There are two major differences when defining custom filters in typed-ffmpeg:

1.	Explicit Type Declaration: You must specify whether the filter’s output is video or audio, as typed-ffmpeg requires this information for static type checking.
2.	Keyword-Only Arguments: All filter options must be specified using keyword arguments (kwargs); positional arguments (args) are not allowed.

For example, in ffmpeg-python:

```
(
    ffmpeg.input("in.mp4")
    .filter('crop', 'in_w-2*10', 'in_h-2*20')
)
```
The equivalent in typed-ffmpeg would be:
```
(
    ffmpeg.input("in.mp4")
    .vfilter("crop", out_w="in_w-2*10", out_h="in_h-2*20")
)
```

For more details: please read [Complex Filters](./usage/complex-filtering.ipynb)

### Additional Notes

Most of FFmpeg’s built-in filters are already available in typed-ffmpeg, so the need to define custom filters should be minimal in most cases.
