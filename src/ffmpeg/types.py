"""
This module defines the types of FFmpeg options. The types can be one of the following:
The source of these types is defined in the AVOptionType enum in FFmpeg's opt.h header file.
"""

Boolean = bool | str
"""
This represents FFmpeg's boolean type. It can accept either a Python boolean value (`True` or `False`)
or a string that represents a boolean value ("true", "false", "1", or "0").

"""
# TODO: confirm

Duration = str | int | float
"""
This represents FFmpeg's duration type. It can accept either a Python integer or float value
or a string that represents a duration value.

Note:
    [Document](https://ffmpeg.org/ffmpeg-utils.html#Time-duration)
"""

Color = str
"""
It can be the name of a color as defined below (case insensitive match) or a [0x|#]RRGGBB[AA] sequence, possibly followed by @ and a string representing the alpha component.
The alpha component may be a string composed by "0x" followed by an hexadecimal number or a decimal number between 0.0 and 1.0, which represents the opacity value (‘0x00’ or ‘0.0’ means completely transparent, ‘0xff’ or ‘1.0’ completely opaque). If the alpha component is not specified then ‘0xff’ is assumed.
The string ‘random’ will result in a random color.


Note:
    [Document](https://ffmpeg.org/ffmpeg-utils.html#Color)
"""
# TODO: is a Enum

Flags = str
"""
This represents FFmpeg's flags type. It accepts a string in the format "A+B",
where "A" and "B" are individual flags. For example, "fast+bilinear" would
represent two flags, "fast" and "bilinear", to be used in FFmpeg's command line.
"""

Dictionary = str
# format A=B:C=D:E=F
Pix_fmt = str
"""
please see `ffmpeg -pix_fmts` for a list of supported pixel formats.
"""

Int = int | str
"""
This represents FFmpeg's integer type. It can accept either a Python integer value
or a string that represents a integer value.
"""

Int64 = int | str
"""
This represents FFmpeg's integer type. It can accept either a Python integer value
or a string that represents a integer value.
"""

Double = int | float | str
"""
This represents FFmpeg's double type. It can accept either a Python integer or float value
or a string that represents a double value.
"""
# TODO: more info
Float = int | float | str
"""
This represents FFmpeg's float type. It can accept either a Python integer or float value
or a string that represents a float value.
"""
String = str | int | float
"""
This represents FFmpeg's string type. It can accept either a Python string value
or a int/float that will be converted to a string.
"""

Video_rate = str | int | float
"""
Specify the frame rate of a video, expressed as the number of frames generated per second. It has to be a string in the format frame_rate_num/frame_rate_den, an integer number, a float number or a valid video frame rate abbreviation.

Note:
    [Document](https://ffmpeg.org/ffmpeg-utils.html#Video-rate)
"""

# TODO: enum
Image_size = str
"""
Specify the size of the sourced video, it may be a string of the form widthxheight, or the name of a size abbreviation.

Note:
    [Document](https://ffmpeg.org/ffmpeg-utils.html#Video-size)
"""

Rational = str
"""
Specify the frame rate of a video, expressed as the number of frames generated per second. It has to be a string in the format frame_rate_num/frame_rate_den, an integer number, a float number or a valid video frame rate abbreviation.

Note:
    [Document](https://ffmpeg.org/ffmpeg-utils.html#Ratio)
"""


Sample_fmt = str
Binary = str
