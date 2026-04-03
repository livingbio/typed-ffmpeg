# Hardware Acceleration Support in FFmpeg 8.0 Docker

## Overview

The `docker/ffmpeg-builder/Dockerfile.8.0` has been enhanced to include comprehensive hardware acceleration support for multiple GPU vendors and acceleration APIs.

## Added Hardware Acceleration Features

### 1. **Intel QSV (Quick Sync Video)** - NEW ✨
**Build Dependencies:**
- `libmfx-dev` - Intel Media SDK development files
- `libvpl-dev` - Intel Video Processing Library development files

**Runtime Libraries:**
- `libmfx1` - Intel Media SDK runtime
- `libvpl2` - Intel VPL runtime

**Configure Flags:**
- `--enable-libmfx` - Enable Intel Media SDK (older API)
- `--enable-libvpl` - Enable Intel VPL (newer API)

**Available Encoders:**
- `h264_qsv` - H.264/AVC encoding
- `hevc_qsv` - H.265/HEVC encoding
- `av1_qsv` - AV1 encoding
- `vp9_qsv` - VP9 encoding
- `mjpeg_qsv` - MJPEG encoding
- `mpeg2_qsv` - MPEG-2 encoding

**Available Filters:**
- `scale_qsv` - Hardware-accelerated scaling
- `overlay_qsv` - Hardware-accelerated overlay
- `deinterlace_qsv` - Hardware-accelerated deinterlacing
- `vpp_qsv` - Video post-processing

### 2. **VAAPI (Video Acceleration API)** - Already Included
**Purpose:** Intel/AMD GPU acceleration on Linux

**Available Filters:**
- `scale_vaapi` - Scaling
- `overlay_vaapi` - Overlay/composition
- `deinterlace_vaapi` - Deinterlacing
- `denoise_vaapi` - Noise reduction
- `tonemap_vaapi` - HDR tone-mapping
- `sharpness_vaapi` - Sharpening
- `transpose_vaapi` - Rotation/flipping
- `pad_vaapi` - Padding
- `procamp_vaapi` - Color adjustments
- `hstack_vaapi`, `vstack_vaapi`, `xstack_vaapi` - Stacking

**Available Encoders:**
- `h264_vaapi`, `hevc_vaapi`, `av1_vaapi`
- `vp8_vaapi`, `vp9_vaapi`
- `mjpeg_vaapi`, `mpeg2_vaapi`

### 3. **NVIDIA CUDA/NVENC/NVDEC** - Already Included
**Purpose:** NVIDIA GPU acceleration

**Build Requirements:**
- `nvidia-cuda-toolkit` - CUDA compiler (nvcc)
- `nv-codec-headers` - NVIDIA codec headers (built from source)

**Configure Flags:**
- `--enable-cuvid` - CUDA video decoder
- `--enable-nvenc` - NVIDIA hardware encoder
- `--enable-nvdec` - NVIDIA hardware decoder
- `--enable-cuda-nvcc` - CUDA filter support

**Available Encoders:**
- `h264_nvenc` - H.264 encoding
- `hevc_nvenc` - H.265 encoding
- `av1_nvenc` - AV1 encoding

**Available Filters:**
- `scale_cuda` - CUDA-accelerated scaling
- `overlay_cuda` - CUDA-accelerated overlay
- `thumbnail_cuda` - CUDA-accelerated thumbnail generation
- `hwupload_cuda` - Upload frames to CUDA
- `hwdownload` - Download frames from CUDA

### 4. **Vulkan** - Already Included
**Purpose:** Cross-platform GPU compute API

**Version Requirement:** >= 1.3.277 (upgraded from Ubuntu's 1.3.275)

**Configure Flags:**
- `--enable-vulkan`
- `--enable-libshaderc` - Shader compiler support

### 5. **OpenCL** - Already Included
**Purpose:** General-purpose GPU computing

**Build Dependencies:**
- `ocl-icd-opencl-dev`
- `opencl-headers`

**Runtime:**
- `ocl-icd-libopencl1`

**Configure Flag:**
- `--enable-opencl`

## Usage Examples

### Intel QSV Encoding
```bash
# H.264 encoding with QSV
ffmpeg -i input.mp4 -c:v h264_qsv -preset medium output.mp4

# HEVC encoding with QSV
ffmpeg -i input.mp4 -c:v hevc_qsv -preset slow -b:v 5M output.mp4

# QSV scaling
ffmpeg -hwaccel qsv -i input.mp4 -vf scale_qsv=1920:1080 output.mp4
```

### VAAPI Encoding
```bash
# H.264 encoding with VAAPI
ffmpeg -vaapi_device /dev/dri/renderD128 -i input.mp4 \
  -vf 'format=nv12,hwupload' -c:v h264_vaapi output.mp4

# VAAPI scaling and overlay
ffmpeg -vaapi_device /dev/dri/renderD128 \
  -i video.mp4 -i logo.png \
  -filter_hw_device hw \
  -vf 'format=nv12,hwupload,scale_vaapi=1920:1080,overlay_vaapi' \
  -c:v h264_vaapi output.mp4
```

### NVIDIA NVENC Encoding
```bash
# H.264 encoding with NVENC
ffmpeg -i input.mp4 -c:v h264_nvenc -preset p7 -b:v 5M output.mp4

# HEVC encoding with NVENC
ffmpeg -i input.mp4 -c:v hevc_nvenc -preset p7 -rc vbr output.mp4

# CUDA scaling
ffmpeg -hwaccel cuda -i input.mp4 \
  -vf scale_cuda=1920:1080 -c:v h264_nvenc output.mp4
```

## Building the Docker Image

```bash
cd docker/ffmpeg-builder

# Build FFmpeg 8.0 with all hardware acceleration
docker build -f Dockerfile.8.0 \
  --build-arg FFMPEG_SOURCE_VERSION=8.0 \
  -t ffmpeg:8.0-hw .
```

## Verification

After building, verify hardware acceleration support:

```bash
# Check available hardware acceleration methods
docker run --rm ffmpeg:8.0-hw -hwaccels

# Check QSV encoders
docker run --rm ffmpeg:8.0-hw -encoders 2>&1 | grep qsv

# Check VAAPI encoders
docker run --rm ffmpeg:8.0-hw -encoders 2>&1 | grep vaapi

# Check CUDA/NVENC encoders (requires NVIDIA GPU)
docker run --rm --gpus all ffmpeg:8.0-hw -encoders 2>&1 | grep nvenc

# Check hardware filters
docker run --rm ffmpeg:8.0-hw -filters 2>&1 | grep -E "qsv|vaapi|cuda"
```

## Hardware Requirements

### Intel QSV
- **Required:** Intel CPU with integrated graphics (HD Graphics, Iris, etc.)
- **Recommended:** 6th generation Intel Core (Skylake) or newer
- **Device:** `/dev/dri/renderD128` must be accessible

### VAAPI
- **Required:** Intel or AMD GPU with VA-API support
- **Device:** `/dev/dri/renderD128` must be accessible
- **Driver:** Mesa drivers or Intel Media Driver

### NVIDIA CUDA/NVENC
- **Required:** NVIDIA GPU (GTX 600 series or newer)
- **Driver:** NVIDIA proprietary drivers (470.x or newer)
- **Runtime:** `--gpus all` flag when running Docker

## Notes

1. **Multiple APIs:** The same GPU may support multiple APIs (e.g., Intel supports both QSV and VAAPI)
2. **Performance:** QSV generally provides better quality/speed trade-off than VAAPI for Intel GPUs
3. **Compatibility:** VAAPI is more widely supported across different Intel/AMD hardware
4. **NVIDIA:** Requires NVIDIA Container Toolkit for Docker GPU access

## Changelog

### 2026-04-04
- ✨ Added Intel QSV support (libmfx/libvpl)
- 📝 Enhanced documentation with hardware acceleration details
- 🔧 Added QSV runtime libraries to Docker image
- 📄 Updated header comments with supported features

### Previous
- ✅ VAAPI support
- ✅ NVIDIA CUDA/NVENC/NVDEC support
- ✅ Vulkan support (upgraded to 1.3.283)
- ✅ OpenCL support
