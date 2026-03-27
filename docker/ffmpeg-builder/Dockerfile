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
    build-essential nasm yasm pkg-config wget ca-certificates git \
    libx264-dev libx265-dev libnuma-dev libvpx-dev libmp3lame-dev \
    libopus-dev libvorbis-dev libtheora-dev libwebp-dev libxvidcore-dev \
    libopenjp2-7-dev libopencore-amrnb-dev libopencore-amrwb-dev \
    libass-dev libfreetype6-dev libfontconfig1-dev libfribidi-dev \
    libzimg-dev libvidstab-dev libaom-dev \
    libssl-dev libsrt-openssl-dev libzmq3-dev \
    libva-dev libdrm-dev ocl-icd-opencl-dev opencl-headers \
    # CUDA (header-only, no GPU required at build time)
    # Vulkan
    libvulkan-dev glslang-dev libshaderc-dev spirv-tools \
    # Frei0r plugin framework
    frei0r-plugins-dev \
    # Audio: LADSPA, LV2, BS2B, Rubberband, SOFA (sofalizer)
    ladspa-sdk \
    lv2-dev liblilv-dev \
    libbs2b-dev \
    librubberband-dev \
    libmysofa-dev \
    # Flite (text-to-speech)
    flite1-dev \
    && rm -rf /var/lib/apt/lists/*

# These may not exist on all Ubuntu versions — ignore failures
RUN apt-get update \
    && apt-get install -y libdav1d-dev libsvtav1-dev libharfbuzz-dev libplacebo-dev 2>/dev/null || true \
    && rm -rf /var/lib/apt/lists/*

# Install nv-codec-headers (CUDA/NVENC support without a physical GPU)
RUN git clone --depth 1 https://github.com/FFmpeg/nv-codec-headers.git /tmp/nv-codec-headers \
    && cd /tmp/nv-codec-headers \
    && make install PREFIX=/usr/local \
    && rm -rf /tmp/nv-codec-headers

# Upgrade Vulkan headers if the system version is below 1.3.277
# (FFmpeg 8.0 requires >= 1.3.277; Ubuntu 24.04 ships 1.3.275)
RUN if ! pkg-config --atleast-version=1.3.277 vulkan 2>/dev/null; then \
      git clone --depth 1 --branch v1.3.283 https://github.com/KhronosGroup/Vulkan-Headers.git /tmp/vulkan-headers; \
      cp -r /tmp/vulkan-headers/include/vulkan /usr/include/; \
      find /usr /lib -name 'vulkan.pc' 2>/dev/null -exec sed -i 's/^Version:.*/Version: 1.3.283/' {} +; \
      rm -rf /tmp/vulkan-headers; \
    fi

# Verify key dependencies
RUN pkg-config --exists harfbuzz && echo "harfbuzz: OK" || echo "WARNING: harfbuzz not found"
RUN pkg-config --exists vulkan && echo "vulkan: OK" || echo "WARNING: vulkan not found"
RUN pkg-config --modversion vulkan 2>/dev/null && echo "vulkan version OK" || echo "WARNING: vulkan version check failed"
RUN pkg-config --exists ffnvcodec && echo "ffnvcodec: OK" || echo "WARNING: nv-codec-headers not found"

RUN wget -q "https://ffmpeg.org/releases/ffmpeg-${FFMPEG_SOURCE_VERSION}.tar.bz2" \
    && tar xf "ffmpeg-${FFMPEG_SOURCE_VERSION}.tar.bz2" \
    && mv "ffmpeg-${FFMPEG_SOURCE_VERSION}" /ffmpeg-src

WORKDIR /ffmpeg-src

# Helper: add a configure flag only when the FFmpeg version supports it AND
# the library is available (detected via pkg-config or file existence).
# Build without --enable-small so descriptions are preserved in the binary.
RUN HELP=$(./configure --help 2>&1); \
    chk() { echo "$HELP" | grep -q -- "--enable-$1"; }; \
    EXTRA_FLAGS=""; \
    # Version-gated libraries (not available on all Ubuntu releases)
    chk libharfbuzz  && pkg-config --exists harfbuzz   && EXTRA_FLAGS="$EXTRA_FLAGS --enable-libharfbuzz" || true; \
    chk libdav1d     && pkg-config --exists dav1d      && EXTRA_FLAGS="$EXTRA_FLAGS --enable-libdav1d" || true; \
    chk libsvtav1    && pkg-config --exists SvtAv1Enc  && EXTRA_FLAGS="$EXTRA_FLAGS --enable-libsvtav1" || true; \
    # libplacebo: compile-test the exact API field FFmpeg older versions need;
    # Ubuntu 24.04 ships libplacebo 6.x which removed force_icc_lut — only
    # enable when the installed headers are API-compatible with this FFmpeg.
    if chk libplacebo && pkg-config --exists libplacebo 2>/dev/null; then \
        if printf '#include <libplacebo/render.h>\nint f(void){struct pl_render_params p;(void)p.force_icc_lut;return 0;}\n' | \
           cc -x c - -c -o /dev/null $(pkg-config --cflags libplacebo) 2>/dev/null; then \
            EXTRA_FLAGS="$EXTRA_FLAGS --enable-libplacebo"; \
        else \
            echo "INFO: libplacebo API incompatible with this FFmpeg version (force_icc_lut missing), skipping"; \
        fi; \
    fi; \
    # Vulkan: mirror FFmpeg 8.0's exact requirement (>= 1.3.277 / VK_HEADER_VERSION >= 277)
    if chk vulkan; then \
        VULKAN_CFLAGS=$(pkg-config --cflags vulkan 2>/dev/null || echo ""); \
        if printf '#include <vulkan/vulkan.h>\n#if !(defined(VK_VERSION_1_4)||(defined(VK_VERSION_1_3)&&VK_HEADER_VERSION>=277))\n#error "Vulkan headers too old"\n#endif\nint main(void){return 0;}\n' | \
           cc -x c - -o /dev/null $VULKAN_CFLAGS -lvulkan 2>/dev/null; then \
            EXTRA_FLAGS="$EXTRA_FLAGS --enable-vulkan"; \
        else \
            echo "WARNING: Vulkan headers < 1.3.277 or link failed, skipping --enable-vulkan"; \
        fi; \
    fi; \
    chk libshaderc   && pkg-config --exists shaderc    && EXTRA_FLAGS="$EXTRA_FLAGS --enable-libshaderc" || true; \
    # CUDA / NVENC (header-only — no GPU needed)
    chk cuvid        && pkg-config --exists ffnvcodec  && EXTRA_FLAGS="$EXTRA_FLAGS --enable-cuvid --enable-nvenc --enable-nvdec" || true; \
    # Frei0r
    chk frei0r       && EXTRA_FLAGS="$EXTRA_FLAGS --enable-frei0r" || true; \
    # Audio plugins
    chk ladspa       && EXTRA_FLAGS="$EXTRA_FLAGS --enable-ladspa" || true; \
    chk lv2          && pkg-config --exists lilv-0     && EXTRA_FLAGS="$EXTRA_FLAGS --enable-lv2" || true; \
    chk libbs2b      && pkg-config --exists libbs2b    && EXTRA_FLAGS="$EXTRA_FLAGS --enable-libbs2b" || true; \
    chk librubberband && pkg-config --exists rubberband && EXTRA_FLAGS="$EXTRA_FLAGS --enable-librubberband" || true; \
    chk libmysofa    && pkg-config --exists libmysofa  && EXTRA_FLAGS="$EXTRA_FLAGS --enable-libmysofa" || true; \
    chk libflite     && [ -f /usr/include/flite/flite.h ] && EXTRA_FLAGS="$EXTRA_FLAGS --enable-libflite" || true; \
    echo "Extra configure flags: $EXTRA_FLAGS"; \
    ./configure \
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
        $EXTRA_FLAGS \
    || { echo "=== configure failed — ffbuild/config.log ==="; \
         cat ffbuild/config.log 2>/dev/null || cat config.log 2>/dev/null; \
         exit 1; } \
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
    # Vulkan runtime
    libvulkan1 \
    # Audio plugin runtimes
    libbs2b0 librubberband2 libmysofa1 liblilv-0-0 \
    # Frei0r plugins
    frei0r-plugins \
    && apt-get install -y --no-install-recommends \
        libvidstab-dev libdav1d-dev libsvtav1-dev libharfbuzz-dev \
        libplacebo-dev libshaderc-dev flite1-dev 2>/dev/null || true \
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
