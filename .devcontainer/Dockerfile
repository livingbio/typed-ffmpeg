FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    ffmpeg \
    graphviz \
    git \
    zsh \
    && rm -rf /var/lib/apt/lists/*
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
RUN pip install poetry
