# FFmpeg Builder Docker Images

Production-ready FFmpeg builds with comprehensive codec and hardware acceleration support.

## Quick Start

### Build FFmpeg 8.0

```bash
cd docker/ffmpeg-builder

# Build the image
docker build -f Dockerfile.8.0 \
  --build-arg FFMPEG_SOURCE_VERSION=8.0 \
  -t ffmpeg:8.0 .

# Verify hardware acceleration support
./verify-hardware-accel.sh ffmpeg:8.0
```

### Usage

```bash
# Basic usage
docker run --rm -v $(pwd):/workspace ffmpeg:8.0 \
  -i /workspace/input.mp4 \
  -c:v libx264 -crf 23 \
  /workspace/output.mp4

# With Intel QSV (requires /dev/dri access)
docker run --rm \
  --device=/dev/dri:/dev/dri \
  -v $(pwd):/workspace \
  ffmpeg:8.0 \
  -hwaccel qsv -i /workspace/input.mp4 \
  -c:v h264_qsv -preset medium \
  /workspace/output.mp4

# With NVIDIA GPU (requires nvidia-container-toolkit)
docker run --rm --gpus all \
  -v $(pwd):/workspace \
  ffmpeg:8.0 \
  -hwaccel cuda -i /workspace/input.mp4 \
  -c:v h264_nvenc -preset p7 \
  /workspace/output.mp4
```

## Hardware Acceleration Support

### Intel Quick Sync Video (QSV)

**Encoders:**
- `h264_qsv`, `hevc_qsv`, `av1_qsv`
- `vp9_qsv`, `mjpeg_qsv`, `mpeg2_qsv`

**Filters:**
- `scale_qsv` - Hardware scaling
- `overlay_qsv` - Hardware overlay
- `deinterlace_qsv` - Deinterlacing
- `vpp_qsv` - Video post-processing

**Requirements:**
- Intel CPU with integrated graphics (6th gen+)
- `/dev/dri/renderD128` device access

**Example:**
```bash
docker run --rm --device=/dev/dri:/dev/dri \
  -v $(pwd):/workspace ffmpeg:8.0 \
  -hwaccel qsv -c:v h264_qsv -i /workspace/input.mp4 \
  -vf scale_qsv=1920:1080 \
  -c:v hevc_qsv -preset slow -b:v 5M \
  /workspace/output.mp4
```

### VAAPI (Video Acceleration API)

**Encoders:**
- `h264_vaapi`, `hevc_vaapi`, `av1_vaapi`
- `vp8_vaapi`, `vp9_vaapi`

**Filters:**
- `scale_vaapi`, `overlay_vaapi`, `deinterlace_vaapi`
- `denoise_vaapi`, `tonemap_vaapi`, `sharpness_vaapi`
- `transpose_vaapi`, `pad_vaapi`, `procamp_vaapi`

**Requirements:**
- Intel or AMD GPU
- `/dev/dri/renderD128` device access

**Example:**
```bash
docker run --rm --device=/dev/dri:/dev/dri \
  -v $(pwd):/workspace ffmpeg:8.0 \
  -vaapi_device /dev/dri/renderD128 -i /workspace/input.mp4 \
  -vf 'format=nv12,hwupload,scale_vaapi=1920:1080' \
  -c:v h264_vaapi -b:v 5M \
  /workspace/output.mp4
```

### NVIDIA CUDA/NVENC

**Encoders:**
- `h264_nvenc`, `hevc_nvenc`, `av1_nvenc`

**Filters:**
- `scale_cuda`, `overlay_cuda`, `thumbnail_cuda`
- `hwupload_cuda`, `hwdownload`

**Requirements:**
- NVIDIA GPU (GTX 600 series or newer)
- NVIDIA drivers and nvidia-container-toolkit

**Example:**
```bash
docker run --rm --gpus all \
  -v $(pwd):/workspace ffmpeg:8.0 \
  -hwaccel cuda -hwaccel_output_format cuda -i /workspace/input.mp4 \
  -vf scale_cuda=1920:1080 \
  -c:v hevc_nvenc -preset p7 -rc vbr \
  /workspace/output.mp4
```

## Verification

Verify all hardware acceleration features:

```bash
./verify-hardware-accel.sh ffmpeg:8.0
```

Expected output:
```
✅ Intel QSV Support
✅ VAAPI Support
✅ Vulkan Support
✅ OpenCL Support

Score: 4/4 features available
🎉 All expected hardware acceleration features are available!
```

## Available Dockerfiles

| Dockerfile | FFmpeg Version | Base OS | Status |
|------------|---------------|---------|---------|
| Dockerfile.8.0 | 8.0.x | Ubuntu 24.04 | ✅ Current |
| Dockerfile.7.1 | 7.1.x | Ubuntu 22.04 | ✅ Maintained |

## Build Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| `FFMPEG_SOURCE_VERSION` | `8.0` | FFmpeg version to build |
| `UBUNTU_VERSION` | `24.04` | Ubuntu base image version |

Example:
```bash
docker build -f Dockerfile.8.0 \
  --build-arg FFMPEG_SOURCE_VERSION=8.0.1 \
  --build-arg UBUNTU_VERSION=24.04 \
  -t ffmpeg:8.0.1 .
```

## Features

### Codecs
- **Video:** H.264 (x264), H.265 (x265), AV1 (aom/svtav1), VP8/VP9, MPEG-2, Xvid, Theora
- **Audio:** MP3 (LAME), Opus, Vorbis, AAC (FDK-AAC), AMR-NB/WB, Speex
- **Image:** JPEG, PNG, WebP, JPEG-XL, OpenJPEG, TIFF

### Hardware Acceleration
- Intel QSV (Quick Sync Video)
- VAAPI (Intel/AMD)
- NVIDIA CUDA/NVENC/NVDEC
- Vulkan
- OpenCL

### Filters & Plugins
- Video stabilization (vidstab)
- Subtitle rendering (libass, libzvbi)
- Audio effects (BS2B, Rubberband, SOFA)
- Frei0r plugins
- LADSPA, LV2 plugin frameworks

### Network & Streaming
- RTMP, SRT, RTSP support
- SSL/TLS (OpenSSL)
- SSH protocol support

## Troubleshooting

### QSV: "No QSV devices found"
- Ensure `/dev/dri` is mounted: `--device=/dev/dri:/dev/dri`
- Check if Intel GPU is available: `ls -la /dev/dri/`
- Verify Intel drivers are installed on host

### VAAPI: "Cannot load libva"
- Mount `/dev/dri`: `--device=/dev/dri:/dev/dri`
- Check VAAPI drivers: `vainfo` on host
- Ensure user has access to render nodes

### NVENC: "Cannot load libnvidia-encode"
- Install nvidia-container-toolkit on host
- Use `--gpus all` flag
- Check NVIDIA drivers: `nvidia-smi` on host

## Contributing

See the main repository's [CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines.

## License

FFmpeg is licensed under LGPL 2.1+ or GPL 2+. This Dockerfile builds FFmpeg with GPL components (`--enable-gpl --enable-nonfree`).

## References

- [FFmpeg Official Documentation](https://ffmpeg.org/documentation.html)
- [Hardware Acceleration Guide](../../HARDWARE_ACCELERATION.md)
- [Intel QSV Documentation](https://www.intel.com/content/www/us/en/developer/articles/technical/quick-sync-video-installation.html)
- [NVIDIA NVENC Documentation](https://docs.nvidia.com/video-technologies/video-codec-sdk/)
