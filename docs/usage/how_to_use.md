# Basic API

## Input

Use `ffmpeg.input` to create a new input stream. Very Simple

```python
import ffmpeg

input_stream = ffmpeg.input('input.mp4')
```

## Output

Use `ffmpeg.output` to create a new output stream. Very Simple

```python

import ffmpeg

ffmpeg.input("input.mp4").output(filename="output.mp4")

```

You can also map more than one input to the output.

```python

import ffmpeg

input1 = ffmpeg.input('input1.mp4')
input2 = ffmpeg.input('input2.mp4')

ffmpeg.output(input1, input2, filename="output.mp4")


```


## Complex Filter

## Get Command Line

## Execute

## Visualize

## Validate & Auto Fix

Easy to reuse graph

# Typing

## Stream Type

## Input

## Output

## Dynamic Input / Dynamic Output

## Filter Options

# Custom Filters

# Serialize
