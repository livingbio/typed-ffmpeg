"""Example demonstrating large filtergraph recursion and performance issues."""

import sys

import ffmpeg

f = ffmpeg.input("in.mp4")
sys.setrecursionlimit(50000)

# Increase loop count to exceed system argument limit (e.g., 5000+ on Linux)
for _ in range(5000):
    f = f.drawtext(
        text="123",
        x="100",
        y="100",
        fontsize=100,
        fontcolor="red",
    )
f = f.output(filename="out.mp4")
f.run()
