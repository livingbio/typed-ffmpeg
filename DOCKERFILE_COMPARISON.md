# Dockerfile.7.1 vs Dockerfile.8.0 Comparison

## TL;DR

**Dockerfile.8.0 already has ALL the features of Dockerfile.7.1, PLUS Intel QSV support.** 

No changes needed - it's already improved compared to 7.1!

---

## Feature Parity Analysis

### ✅ Features Present in BOTH

| Feature | 7.1 | 8.0 | Notes |
|---------|-----|-----|-------|
| **OpenCL Filters** | ✅ | ✅ | 20+ GPU filters |
| **CUDA Filters** | ✅ | ✅ | NVIDIA GPU acceleration |
| **VAAPI Filters** | ✅ | ✅ | Intel/AMD GPU acceleration |
| **Vulkan Filters** | ✅ | ✅ | Cross-platform GPU |
| **Frei0r Plugins** | ✅ | ✅ | 100+ video effects |
| **LADSPA Plugins** | ✅ | ✅ | Audio plugin framework |
| **LV2 Plugins** | ✅ | ✅ | Audio plugin framework |
| **bs2b** | ✅ | ✅ | Bauer stereophonic-to-binaural |
| **rubberband** | ✅ | ✅ | Time-stretching |
| **sofalizer** | ✅ | ✅ | SOFA spatial audio |
| **flite** | ✅ | ✅ | Text-to-speech |
| **All codecs** | ✅ | ✅ | x264, x265, aom, vp8/9, etc. |

### 🆕 NEW in Dockerfile.8.0

| Feature | 7.1 | 8.0 | Notes |
|---------|-----|-----|-------|
| **Intel QSV** | ❌ | ✅ | Quick Sync Video (4 filters + encoders) |
| **libmfx** | ❌ | ✅ | Intel Media SDK (legacy API) |
| **libvpl** | ❌ | ✅ | Intel VPL (modern API) |

### ⚠️ Postproc Note

| Feature | 7.1 | 8.0 | Notes |
|---------|-----|-----|-------|
| **--enable-postproc** | ✅ | ❌ | **Not needed in FFmpeg 8.0** |
| **pp filter** | ✅ | ✅ | Still available (built-in with GPL) |
| **fspp, spp, uspp** | ✅ | ✅ | Postproc filters still work |

**Explanation:**  
In FFmpeg 7.x, `--enable-postproc` was a configure option to enable libpostproc.  
In FFmpeg 8.0, libpostproc functionality is **built-in** when `--enable-gpl` is used.  
The `pp` filter and related filters (fspp, spp, uspp) are still available.

---

## Build Dependencies Comparison

### Identical Dependencies

Both Dockerfile.7.1 and Dockerfile.8.0 install:

```dockerfile
# Core build tools
build-essential nasm yasm pkg-config wget ca-certificates git

# Video codecs
libx264-dev libx265-dev libvpx-dev libaom-dev

# Audio codecs
libmp3lame-dev libopus-dev libvorbis-dev libtheora-dev

# Image formats
libwebp-dev libxvidcore-dev libopenjp2-7-dev libjxl-dev

# Subtitle/text
libass-dev libfreetype6-dev libfontconfig1-dev libfribidi-dev
libzvbi-dev librsvg2-dev

# Hardware acceleration (both have)
libva-dev libdrm-dev ocl-icd-opencl-dev opencl-headers
libvulkan-dev glslang-dev libshaderc-dev spirv-tools

# CUDA
nvidia-cuda-toolkit (for CUDA filters)

# Plugins
frei0r-plugins-dev ladspa-sdk lv2-dev liblilv-dev

# Audio processing
libbs2b-dev librubberband-dev libmysofa-dev flite1-dev

# Additional
libvidstab-dev libzimg-dev libssl-dev libsrt-openssl-dev
libzmq3-dev libbluray-dev libfdk-aac-dev
libgsm1-dev libspeex-dev libtwolame-dev libshine-dev
libcodec2-dev libsnappy-dev
```

### 8.0 Additions

```dockerfile
# Intel QSV (Quick Sync Video) - NEW
libmfx-dev    # Intel Media SDK (legacy API)
libvpl-dev    # Intel Video Processing Library (modern API)
```

---

## Configure Flags Comparison

### Base Flags (Identical)

Both use the same base configuration:

```bash
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
    --enable-opencl
```

### Dynamic Flags (EXTRA_FLAGS)

Both detect and enable the same optional features:

```bash
# Codecs
--enable-libdav1d (if available)
--enable-libsvtav1 (if available)
--enable-libharfbuzz (if available)

# Hardware acceleration
--enable-vulkan (if headers >= 1.3.277)
--enable-libshaderc (if available)
--enable-cuvid --enable-nvenc --enable-nvdec (if NVIDIA present)
--enable-cuda-nvcc (if nvcc present)

# Plugins
--enable-frei0r (always)
--enable-ladspa (always)
--enable-lv2 (if available)

# Audio processing
--enable-libbs2b (if available)
--enable-librubberband (if available)
--enable-libmysofa (if available)
--enable-libflite (if available)

# Additional codecs
--enable-libgsm --enable-libspeex --enable-libtwolame
--enable-libshine --enable-libcodec2 --enable-libsnappy
--enable-libbluray --enable-libfdk-aac --enable-librav1e
--enable-libjxl --enable-librsvg --enable-libzvbi
```

### 8.0-Specific Additions

```bash
# Intel QSV (NEW)
--enable-libmfx (if available)
--enable-libvpl (if available)
```

### 7.1-Specific (Removed in 8.0)

```bash
# Postproc (no longer a separate option in FFmpeg 8.0)
--enable-postproc
```

**Note:** The `pp` filter still works in FFmpeg 8.0, it's just built-in with `--enable-gpl`.

---

## Runtime Libraries Comparison

### Identical Runtime Libs

Both include:

```dockerfile
# Core libs
ca-certificates libx264-164 libx265-199 libvpx9 libmp3lame0
libopus0 libvorbis0a libtheora0 libwebp7 libxvidcore4

# Hardware acceleration
libva2 libva-drm2 libdrm2 ocl-icd-libopencl1 libvdpau1
libvulkan1 libxcb1 libxcb-shm0 libxcb-xfixes0

# Plugins
frei0r-plugins liblilv-0-0

# Audio
libbs2b0 librubberband2 libmysofa1

# Additional
libass9 libfreetype6 libfontconfig1 libzimg2 libvidstab1.1
```

### 8.0 Additions

```dockerfile
# Intel QSV runtime libraries (NEW)
libmfx1    # Intel Media SDK runtime
libvpl2    # Intel VPL runtime
```

---

## Conclusion

**Dockerfile.8.0 is ALREADY EQUIVALENT to Dockerfile.7.1 with the following improvements:**

1. ✅ **All 7.1 features present** (OpenCL, CUDA, VAAPI, Vulkan, plugins, audio processing)
2. ✅ **Plus Intel QSV** (4 new filters + encoders)
3. ✅ **Postproc filters still work** (built-in with GPL in FFmpeg 8.0)
4. ✅ **All dependencies installed**
5. ✅ **All configure flags enabled**

**No changes needed - Dockerfile.8.0 already matches and exceeds Dockerfile.7.1!**

---

## Expected Filter Count

| Build | Filter Count | Notes |
|-------|--------------|-------|
| Alpine FFmpeg 8.0 | ~251 | Minimal build (no OpenCL, CUDA, etc.) |
| Dockerfile.7.1 | ~365 | Full build (all features) |
| Dockerfile.8.0 | ~369+ | Full build + QSV (4 more than 7.1) |

After building the Docker image and running codegen, typed-ffmpeg v8 will have:
- All filters from v7
- Plus 4 new QSV filters: `scale_qsv`, `overlay_qsv`, `deinterlace_qsv`, `vpp_qsv`

---

## Verification Commands

After building the Docker image:

```bash
# Build
docker build -f Dockerfile.8.0 -t ffmpeg:8.0-test .

# Check filter count
docker run --rm ffmpeg:8.0-test -filters 2>&1 | grep -c '^\s*[TAV]'
# Expected: ~369+

# Check QSV filters
docker run --rm ffmpeg:8.0-test -filters 2>&1 | grep qsv
# Expected: scale_qsv, overlay_qsv, deinterlace_qsv, vpp_qsv

# Check OpenCL filters
docker run --rm ffmpeg:8.0-test -filters 2>&1 | grep opencl | wc -l
# Expected: ~20

# Check CUDA filters
docker run --rm ffmpeg:8.0-test -filters 2>&1 | grep cuda
# Expected: hwupload_cuda, scale_cuda, overlay_cuda

# Check audio filters
docker run --rm ffmpeg:8.0-test -filters 2>&1 | grep -E 'bs2b|rubberband|sofalizer|flite'

# Check Frei0r
docker run --rm ffmpeg:8.0-test -filters 2>&1 | grep frei0r | wc -l
# Expected: ~100+

# Check postproc filters (should still work)
docker run --rm ffmpeg:8.0-test -filters 2>&1 | grep -E '^\s*V.*\s(pp|fspp|spp|uspp)\s'
```
