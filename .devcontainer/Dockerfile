FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    wget \
    graphviz \
    git \
    zsh \
    xz-utils \
    && wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz \
    && tar -xf ffmpeg-release-amd64-static.tar.xz \
    && mv ffmpeg-*-amd64-static/ffmpeg /usr/local/bin/ \
    && mv ffmpeg-*-amd64-static/ffprobe /usr/local/bin/ \
    && rm -rf ffmpeg-release-amd64-static.tar.xz ffmpeg-*-amd64-static \
    && apt-get clean

RUN sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
RUN pip install poetry
