FROM ubuntu:24.04

# Install Python and other dependencies
RUN apt-get update && apt-get install -y \
    python3.12 \
    python3-pip \
    wget \
    graphviz \
    git \
    zsh \
    xz-utils \
    build-essential \
    curl \
    software-properties-common \
    ffmpeg \
    && apt-get clean \ 
    && ffmpeg -version

RUN sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
RUN pip3 install --break-system-packages uv