# https://ffmpeg.org/ffmpeg-filters.html
import urllib.request

import typer


def download_ffmpeg_filter_documents() -> None:
    url = "https://ffmpeg.org/ffmpeg-filters.html"
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode("utf-8")
    with open("ffmpeg-filters.html", "w") as f:
        f.write(text)


if __name__ == "__main__":
    typer.run(download_ffmpeg_filter_documents)
