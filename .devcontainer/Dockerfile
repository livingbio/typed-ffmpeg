FROM python:3.10-slim

# Install Node.js and npm
RUN apt-get update && apt-get install -y \
    wget \
    graphviz \
    git \
    zsh \
    xz-utils \
    build-essential \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@9.8.1 \
    && wget https://www.johnvansickle.com/ffmpeg/old-releases/ffmpeg-6.0-arm64-static.tar.xz \
    && tar -xf ffmpeg-6.0-arm64-static.tar.xz \
    && mv ffmpeg-*-arm64-static/ffmpeg /usr/local/bin/ \
    && mv ffmpeg-*-arm64-static/ffprobe /usr/local/bin/ \
    && rm -rf ffmpeg-release-arm64-static.tar.xz ffmpeg-*-arm64-static \
    && apt-get clean

RUN sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
RUN pip install uv
