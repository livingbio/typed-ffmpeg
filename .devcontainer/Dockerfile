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
    && apt-get install -y ffmpeg \
    && apt-get clean \ 
    && ffmpeg -version


RUN sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
RUN pip install uv
