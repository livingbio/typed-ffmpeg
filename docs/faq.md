# FAQ

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

For more details: please read [Customizing Filters](./usage/complex-filtering.ipynb)

### Additional Notes

Most of FFmpeg’s built-in filters are already available in typed-ffmpeg, so the need to define custom filters should be minimal in most cases.
