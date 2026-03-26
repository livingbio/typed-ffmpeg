# Build FFmpeg with full descriptions (no --enable-small) and hardware acceleration
# Usage: docker build --build-arg FFMPEG_VERSION=7.1 --build-arg FFMPEG_SOURCE_VERSION=7.1.1 -t ffmpeg:7.1 .
ARG FFMPEG_VERSION=7.1
ARG FFMPEG_SOURCE_VERSION=${FFMPEG_VERSION}
ARG UBUNTU_VERSION=24.04

FROM ubuntu:${UBUNTU_VERSION} AS build

ARG FFMPEG_VERSION
ARG FFMPEG_SOURCE_VERSION

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    build-essential nasm yasm pkg-config wget ca-certificates \
    libx264-dev libx265-dev libnuma-dev libvpx-dev libmp3lame-dev \
    libopus-dev libvorbis-dev libtheora-dev libwebp-dev libxvidcore-dev \
    libopenjp2-7-dev libopencore-amrnb-dev libopencore-amrwb-dev \
    libass-dev libfreetype6-dev libfontconfig1-dev libfribidi-dev \
    libzimg-dev libvidstab-dev libaom-dev \
    libssl-dev libsrt-openssl-dev libzmq3-dev \
    libva-dev libdrm-dev ocl-icd-opencl-dev opencl-headers \
    && rm -rf /var/lib/apt/lists/*

# These may not exist on all Ubuntu versions — ignore failures
RUN apt-get update \
    && apt-get install -y libdav1d-dev libsvtav1-dev libharfbuzz-dev 2>/dev/null || true \
    && rm -rf /var/lib/apt/lists/*

RUN wget -q "https://ffmpeg.org/releases/ffmpeg-${FFMPEG_SOURCE_VERSION}.tar.bz2" \
    && tar xf "ffmpeg-${FFMPEG_SOURCE_VERSION}.tar.bz2" \
    && mv "ffmpeg-${FFMPEG_SOURCE_VERSION}" /ffmpeg-src

WORKDIR /ffmpeg-src

# Build without --enable-small so descriptions are preserved in the binary
RUN ./configure \
        --prefix=/opt/ffmpeg \
        --disable-debug \
        --disable-doc \
        --disable-ffplay \
        --enable-gpl \
        --enable-nonfree \
        --enable-version3 \
        --enable-shared \
        --enable-libx264 \
        --enable-libx265 \
        --enable-libvpx \
        --enable-libmp3lame \
        --enable-libopus \
        --enable-libvorbis \
        --enable-libtheora \
        --enable-libwebp \
        --enable-libxvid \
        --enable-libopenjpeg \
        --enable-libopencore-amrnb \
        --enable-libopencore-amrwb \
        --enable-libass \
        --enable-libfreetype \
        --enable-fontconfig \
        --enable-libfribidi \
        --enable-libzimg \
        --enable-libvidstab \
        --enable-libaom \
        --enable-openssl \
        --enable-libsrt \
        --enable-libzmq \
        --enable-vaapi \
        --enable-opencl \
    && make -j$(nproc) \
    && make install

# Runtime stage
FROM ubuntu:${UBUNTU_VERSION}

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    ca-certificates \
    libx264-164 libx265-199 libvpx9 libmp3lame0 libopus0 \
    libvorbis0a libvorbisenc2 libtheora0 libwebp7 libxvidcore4 \
    libopenjp2-7 libopencore-amrnb0 libopencore-amrwb0 \
    libass9 libfreetype6 libfontconfig1 libfribidi0 \
    libzimg2 libvidstab1.2 libaom3 \
    libssl3 libsrt1.5-openssl libzmq5 \
    libva2 libdrm2 ocl-icd-libopencl1 \
    && apt-get install -y libdav1d7 libsvtav1enc1d1 libharfbuzz0b 2>/dev/null || true \
    && rm -rf /var/lib/apt/lists/*

COPY --from=build /opt/ffmpeg /opt/ffmpeg

ENV PATH=/opt/ffmpeg/bin:$PATH
ENV LD_LIBRARY_PATH=/opt/ffmpeg/lib

ENTRYPOINT ["/opt/ffmpeg/bin/ffmpeg"]
