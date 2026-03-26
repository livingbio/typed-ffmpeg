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
        --prefix=/usr/local \
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

# Runtime stage — copy built libs and install runtime dependencies
FROM ubuntu:${UBUNTU_VERSION}

ENV DEBIAN_FRONTEND=noninteractive

# Install base runtime libs; version-specific packages are optional (|| true)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    libx264-dev libx265-dev libvpx-dev libmp3lame-dev libopus-dev \
    libvorbis-dev libtheora-dev libwebp-dev libxvidcore-dev \
    libopenjp2-7-dev libopencore-amrnb-dev libopencore-amrwb-dev \
    libass-dev libfreetype6-dev libfontconfig1-dev libfribidi-dev \
    libzimg-dev libaom-dev \
    libssl-dev libsrt-openssl-dev libzmq3-dev \
    libva-dev libdrm-dev ocl-icd-opencl-dev \
    && apt-get install -y --no-install-recommends \
        libvidstab-dev libdav1d-dev libsvtav1-dev libharfbuzz-dev 2>/dev/null || true \
    && rm -rf /var/lib/apt/lists/*

COPY --from=build /usr/local/bin/ffmpeg /usr/local/bin/ffmpeg
COPY --from=build /usr/local/bin/ffprobe /usr/local/bin/ffprobe
COPY --from=build /usr/local/lib /usr/local/lib

# Bundle all shared library dependencies into /usr/local/lib so they are
# included when the CI extracts libs via: docker cp container:/usr/local/lib
# Check both the ffmpeg binary AND all libav*.so shared libraries, since
# filters like drawtext depend on libs (e.g. libfreetype) linked through
# libavfilter.so rather than the ffmpeg binary directly.
RUN { ldd /usr/local/bin/ffmpeg; \
      find /usr/local/lib -name 'libav*.so*' -exec ldd {} \; ; \
      find /usr/local/lib -name 'libsw*.so*' -exec ldd {} \; ; \
    } | awk '/=> \// {print $3}' | sort -u \
    | xargs -I{} cp -n {} /usr/local/lib/ 2>/dev/null || true \
    && ldconfig

ENTRYPOINT ["/usr/local/bin/ffmpeg"]
