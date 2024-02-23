import ffmpeg


def run(stream):
    print(stream.compile())
    stream.run()


run(
    ffmpeg.input("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")
    .output(
        filename="output_t.mp4",
        t=3,
    )
    .overwrite_output()
)

in_file = ffmpeg.input("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")
run(
    ffmpeg.output(
        in_file.trim(duration=3),
        in_file.filter("atrim", duration=3),
        filename="trim_filter_atrim_duration.mp4",
    ).overwrite_output()
)
f = open("files.txt", "w")
f.write(
    """
file 'output_t.mp4'
file 'trim_filter_atrim_duration.mp4'
"""
)
f.close()
run(ffmpeg.input("files.txt", f="concat", safe=0).output(filename="concat_demuxer.mp4", c="copy").overwrite_output())
