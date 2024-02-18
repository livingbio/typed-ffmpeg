# Basic FFMpeg
FFmpeg is very complicate, here is some my understanding about ffmpeg
During this project I check ffmpeg cli help, ffmpeg-python, and ffmpeg source code and document to understand the ffmpeg.

## FFMpeg Version
The typed-ffmpeg is build based on ffmpeg version 6.0
Please noted that different version of ffmpeg may have different options and filters.
and ffmpeg has serveral optional module that may be or maynot included in your installed ffmpeg.
Please check your ffmpeg version and installed module before using typed-ffmpeg.

```
(typed-ffmpeg-py3.12) ➜  typed-ffmpeg git:(main) ✗ ffmpeg -version
ffmpeg version 6.1.1 Copyright (c) 2000-2023 the FFmpeg developers
built with Apple clang version 15.0.0 (clang-1500.1.0.2.5)
configuration: --prefix=/opt/homebrew/Cellar/ffmpeg/6.1.1_2 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags='-Wl,-ld_classic' --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopenvino --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox --enable-neon
libavutil      58. 29.100 / 58. 29.100
libavcodec     60. 31.102 / 60. 31.102
libavformat    60. 16.100 / 60. 16.100
libavdevice    60.  3.100 / 60.  3.100
libavfilter     9. 12.100 /  9. 12.100
libswscale      7.  5.100 /  7.  5.100
libswresample   4. 12.100 /  4. 12.100
libpostproc    57.  3.100 / 57.  3.100
```

### FFMpeg Version
`ffmpeg version 6.1.1 Copyright (c) 2000-2023 the FFmpeg developers`

### FFMpeg Configuration

There are lots of configuration options for ffmpeg, here is the configuration of my installed ffmpeg. It decide the feature and module that included in the ffmpeg.

```
configuration: --prefix=/opt/homebrew/Cellar/ffmpeg/6.1.1_2 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags='-Wl,-ld_classic' --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopenvino --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox --enable-neon
```

You can see all configuration options in the ffmpeg cli help.


Note:
  if you face any issue with the typed-ffmpeg in different ffmpeg build or version, please open an issue in the github repository.

## FFMpeg CLI

https://ffmpeg.org/ffmpeg.html#Synopsis

`ffmpeg [global_options] {[input_file_options] -i input_url} ... {[output_file_options] output_url} ...`

For example:

```
ffmpeg -i input.mp4 -vf "hflip" output.mp4
```


brief about ffmpeg cli
 input / output / filter / global options

Complex Filter and DAG


All docuement is generated based on ffmpeg 6.1.1 cli help



video filter


audio filter


filter with dynamic inputs


you can see all support filters in the [filter]()

detail compare with ffmpeg-python
- IDE Friendly
- Complete Split automation

Current Support FFMpeg Filters

## Generated Table
| Filter | Support |
| --- | --- |
| abitscope | ✅ |
