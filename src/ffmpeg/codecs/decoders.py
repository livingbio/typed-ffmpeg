# NOTE: this file is auto-generated, do not modify
from dataclasses import dataclass

from .schema import FFMpegDecoderOption


@dataclass(frozen=True, kw_only=True)
class _012v(FFMpegDecoderOption):
    """Uncompressed 4:2:2 10-bit"""


@dataclass(frozen=True, kw_only=True)
class _4xm(FFMpegDecoderOption):
    """4X Movie"""


@dataclass(frozen=True, kw_only=True)
class _8bps(FFMpegDecoderOption):
    """QuickTime 8BPS video"""


@dataclass(frozen=True, kw_only=True)
class aasc(FFMpegDecoderOption):
    """Autodesk RLE"""


@dataclass(frozen=True, kw_only=True)
class agm(FFMpegDecoderOption):
    """Amuse Graphics Movie"""


@dataclass(frozen=True, kw_only=True)
class aic(FFMpegDecoderOption):
    """Apple Intermediate Codec"""


@dataclass(frozen=True, kw_only=True)
class alias_pix(FFMpegDecoderOption):
    """Alias/Wavefront PIX image"""


@dataclass(frozen=True, kw_only=True)
class amv(FFMpegDecoderOption):
    """AMV Video"""


@dataclass(frozen=True, kw_only=True)
class anm(FFMpegDecoderOption):
    """Deluxe Paint Animation"""


@dataclass(frozen=True, kw_only=True)
class ansi(FFMpegDecoderOption):
    """ASCII/ANSI art"""


@dataclass(frozen=True, kw_only=True)
class apng(FFMpegDecoderOption):
    """APNG (Animated Portable Network Graphics) image"""


@dataclass(frozen=True, kw_only=True)
class arbc(FFMpegDecoderOption):
    """Gryphon's Anim Compressor"""


@dataclass(frozen=True, kw_only=True)
class argo(FFMpegDecoderOption):
    """Argonaut Games Video"""


@dataclass(frozen=True, kw_only=True)
class asv1(FFMpegDecoderOption):
    """ASUS V1"""


@dataclass(frozen=True, kw_only=True)
class asv2(FFMpegDecoderOption):
    """ASUS V2"""


@dataclass(frozen=True, kw_only=True)
class aura(FFMpegDecoderOption):
    """Auravision AURA"""


@dataclass(frozen=True, kw_only=True)
class aura2(FFMpegDecoderOption):
    """Auravision Aura 2"""


@dataclass(frozen=True, kw_only=True)
class libdav1d(FFMpegDecoderOption):
    """dav1d AV1 decoder by VideoLAN (codec av1)"""

    tilethreads: int | None = None
    """Tile threads (from 0 to 256) (default 0)"""

    framethreads: int | None = None
    """Frame threads (from 0 to 256) (default 0)"""

    max_frame_delay: int | None = None
    """Max frame delay (from 0 to 256) (default 0)"""

    filmgrain: bool | None = None
    """Apply Film Grain (default auto)"""

    oppoint: int | None = None
    """Select an operating point of the scalable bitstream (from -1 to 31) (default -1)"""

    alllayers: bool | None = None
    """Output all spatial layers (default false)"""


@dataclass(frozen=True, kw_only=True)
class av1(FFMpegDecoderOption):
    """Alliance for Open Media AV1"""

    operating_point: int | None = None
    """Select an operating point of the scalable bitstream (from 0 to 31) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class av1_cuvid(FFMpegDecoderOption):
    """Nvidia CUVID AV1 decoder (codec av1)"""

    deint: int | None = None
    """Set deinterlacing mode (from 0 to 2) (default weave)"""

    gpu: str | None = None
    """GPU to be used for decoding"""

    surfaces: int | None = None
    """Maximum surfaces to be used for decoding (from -1 to INT_MAX) (default -1)"""

    drop_second_field: bool | None = None
    """Drop second field when deinterlacing (default false)"""

    crop: str | None = None
    """Crop (top)x(bottom)x(left)x(right)"""

    resize: str | None = None
    """Resize (width)x(height)"""


@dataclass(frozen=True, kw_only=True)
class avrn(FFMpegDecoderOption):
    """Avid AVI Codec"""


@dataclass(frozen=True, kw_only=True)
class avrp(FFMpegDecoderOption):
    """Avid 1:1 10-bit RGB Packer"""


@dataclass(frozen=True, kw_only=True)
class avs(FFMpegDecoderOption):
    """AVS (Audio Video Standard) video"""


@dataclass(frozen=True, kw_only=True)
class avui(FFMpegDecoderOption):
    """Avid Meridien Uncompressed"""


@dataclass(frozen=True, kw_only=True)
class ayuv(FFMpegDecoderOption):
    """Uncompressed packed MS 4:4:4:4"""


@dataclass(frozen=True, kw_only=True)
class bethsoftvid(FFMpegDecoderOption):
    """Bethesda VID video"""


@dataclass(frozen=True, kw_only=True)
class bfi(FFMpegDecoderOption):
    """Brute Force & Ignorance"""


@dataclass(frozen=True, kw_only=True)
class binkvideo(FFMpegDecoderOption):
    """Bink video"""


@dataclass(frozen=True, kw_only=True)
class bintext(FFMpegDecoderOption):
    """Binary text"""


@dataclass(frozen=True, kw_only=True)
class bitpacked(FFMpegDecoderOption):
    """Bitpacked"""


@dataclass(frozen=True, kw_only=True)
class bmp(FFMpegDecoderOption):
    """BMP (Windows and OS/2 bitmap)"""


@dataclass(frozen=True, kw_only=True)
class bmv_video(FFMpegDecoderOption):
    """Discworld II BMV video"""


@dataclass(frozen=True, kw_only=True)
class brender_pix(FFMpegDecoderOption):
    """BRender PIX image"""


@dataclass(frozen=True, kw_only=True)
class c93(FFMpegDecoderOption):
    """Interplay C93"""


@dataclass(frozen=True, kw_only=True)
class cavs(FFMpegDecoderOption):
    """Chinese AVS (Audio Video Standard) (AVS1-P2, JiZhun profile)"""


@dataclass(frozen=True, kw_only=True)
class cdgraphics(FFMpegDecoderOption):
    """CD Graphics video"""


@dataclass(frozen=True, kw_only=True)
class cdtoons(FFMpegDecoderOption):
    """CDToons video"""


@dataclass(frozen=True, kw_only=True)
class cdxl(FFMpegDecoderOption):
    """Commodore CDXL video"""


@dataclass(frozen=True, kw_only=True)
class cfhd(FFMpegDecoderOption):
    """GoPro CineForm HD"""


@dataclass(frozen=True, kw_only=True)
class cinepak(FFMpegDecoderOption):
    """Cinepak"""


@dataclass(frozen=True, kw_only=True)
class clearvideo(FFMpegDecoderOption):
    """Iterated Systems ClearVideo"""


@dataclass(frozen=True, kw_only=True)
class cljr(FFMpegDecoderOption):
    """Cirrus Logic AccuPak"""


@dataclass(frozen=True, kw_only=True)
class cllc(FFMpegDecoderOption):
    """Canopus Lossless Codec"""


@dataclass(frozen=True, kw_only=True)
class eacmv(FFMpegDecoderOption):
    """Electronic Arts CMV video (codec cmv)"""


@dataclass(frozen=True, kw_only=True)
class cpia(FFMpegDecoderOption):
    """CPiA video format"""


@dataclass(frozen=True, kw_only=True)
class cri(FFMpegDecoderOption):
    """Cintel RAW"""


@dataclass(frozen=True, kw_only=True)
class camstudio(FFMpegDecoderOption):
    """CamStudio (codec cscd)"""


@dataclass(frozen=True, kw_only=True)
class cyuv(FFMpegDecoderOption):
    """Creative YUV (CYUV)"""


@dataclass(frozen=True, kw_only=True)
class dds(FFMpegDecoderOption):
    """DirectDraw Surface image decoder"""


@dataclass(frozen=True, kw_only=True)
class dfa(FFMpegDecoderOption):
    """Chronomaster DFA"""


@dataclass(frozen=True, kw_only=True)
class dirac(FFMpegDecoderOption):
    """BBC Dirac VC-2"""


@dataclass(frozen=True, kw_only=True)
class dnxhd(FFMpegDecoderOption):
    """VC3/DNxHD"""


@dataclass(frozen=True, kw_only=True)
class dpx(FFMpegDecoderOption):
    """DPX (Digital Picture Exchange) image"""


@dataclass(frozen=True, kw_only=True)
class dsicinvideo(FFMpegDecoderOption):
    """Delphine Software International CIN video"""


@dataclass(frozen=True, kw_only=True)
class dvvideo(FFMpegDecoderOption):
    """DV (Digital Video)"""


@dataclass(frozen=True, kw_only=True)
class dxa(FFMpegDecoderOption):
    """Feeble Files/ScummVM DXA"""


@dataclass(frozen=True, kw_only=True)
class dxtory(FFMpegDecoderOption):
    """Dxtory"""


@dataclass(frozen=True, kw_only=True)
class dxv(FFMpegDecoderOption):
    """Resolume DXV"""


@dataclass(frozen=True, kw_only=True)
class escape124(FFMpegDecoderOption):
    """Escape 124"""


@dataclass(frozen=True, kw_only=True)
class escape130(FFMpegDecoderOption):
    """Escape 130"""


@dataclass(frozen=True, kw_only=True)
class exr(FFMpegDecoderOption):
    """OpenEXR image"""

    layer: str | None = None
    """Set the decoding layer (default "")"""

    part: int | None = None
    """Set the decoding part (from 0 to INT_MAX) (default 0)"""

    gamma: float | None = None
    """Set the float gamma value when decoding (from 0.001 to FLT_MAX) (default 1)"""

    apply_trc: int | None = None
    """color transfer characteristics to apply to EXR linear input (from 1 to 18) (default gamma)"""


@dataclass(frozen=True, kw_only=True)
class ffv1(FFMpegDecoderOption):
    """FFmpeg video codec #1"""


@dataclass(frozen=True, kw_only=True)
class ffvhuff(FFMpegDecoderOption):
    """Huffyuv FFmpeg variant"""


@dataclass(frozen=True, kw_only=True)
class fic(FFMpegDecoderOption):
    """Mirillis FIC"""

    skip_cursor: bool | None = None
    """skip the cursor (default false)"""


@dataclass(frozen=True, kw_only=True)
class fits(FFMpegDecoderOption):
    """Flexible Image Transport System"""

    blank_value: int | None = None
    """value that is used to replace BLANK pixels in data array (from 0 to 65535) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class flashsv(FFMpegDecoderOption):
    """Flash Screen Video v1"""


@dataclass(frozen=True, kw_only=True)
class flashsv2(FFMpegDecoderOption):
    """Flash Screen Video v2"""


@dataclass(frozen=True, kw_only=True)
class flic(FFMpegDecoderOption):
    """Autodesk Animator Flic video"""


@dataclass(frozen=True, kw_only=True)
class flv(FFMpegDecoderOption):
    """FLV / Sorenson Spark / Sorenson H.263 (Flash Video) (codec flv1)"""


@dataclass(frozen=True, kw_only=True)
class fmvc(FFMpegDecoderOption):
    """FM Screen Capture Codec"""


@dataclass(frozen=True, kw_only=True)
class fraps(FFMpegDecoderOption):
    """Fraps"""


@dataclass(frozen=True, kw_only=True)
class frwu(FFMpegDecoderOption):
    """Forward Uncompressed"""

    change_field_order: bool | None = None
    """Change field order (default false)"""


@dataclass(frozen=True, kw_only=True)
class g2m(FFMpegDecoderOption):
    """Go2Meeting"""


@dataclass(frozen=True, kw_only=True)
class gdv(FFMpegDecoderOption):
    """Gremlin Digital Video"""


@dataclass(frozen=True, kw_only=True)
class gem(FFMpegDecoderOption):
    """GEM Raster image"""


@dataclass(frozen=True, kw_only=True)
class gif(FFMpegDecoderOption):
    """GIF (Graphics Interchange Format)"""

    trans_color: int | None = None
    """color value (ARGB) that is used instead of transparent color (from 0 to UINT32_MAX) (default 16777215)"""


@dataclass(frozen=True, kw_only=True)
class h261(FFMpegDecoderOption):
    """H.261"""


@dataclass(frozen=True, kw_only=True)
class h263(FFMpegDecoderOption):
    """H.263 / H.263-1996, H.263+ / H.263-1998 / H.263 version 2"""


@dataclass(frozen=True, kw_only=True)
class h263_v4l2m2m(FFMpegDecoderOption):
    """V4L2 mem2mem H.263 decoder wrapper (codec h263)"""

    num_output_buffers: int | None = None
    """Number of buffers in the output context (from 2 to INT_MAX) (default 16)"""

    num_capture_buffers: int | None = None
    """Number of buffers in the capture context (from 2 to INT_MAX) (default 20)"""


@dataclass(frozen=True, kw_only=True)
class h263i(FFMpegDecoderOption):
    """Intel H.263"""


@dataclass(frozen=True, kw_only=True)
class h263p(FFMpegDecoderOption):
    """H.263 / H.263-1996, H.263+ / H.263-1998 / H.263 version 2"""


@dataclass(frozen=True, kw_only=True)
class h264(FFMpegDecoderOption):
    """H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10"""

    is_avc: bool | None = None
    """is avc (default false)"""

    nal_length_size: int | None = None
    """nal_length_size (from 0 to 4) (default 0)"""

    enable_er: bool | None = None
    """Enable error resilience on damaged frames (unsafe) (default auto)"""

    x264_build: int | None = None
    """Assume this x264 version if no x264 version found in any SEI (from -1 to INT_MAX) (default -1)"""


@dataclass(frozen=True, kw_only=True)
class h264_v4l2m2m(FFMpegDecoderOption):
    """V4L2 mem2mem H.264 decoder wrapper (codec h264)"""

    num_output_buffers: int | None = None
    """Number of buffers in the output context (from 2 to INT_MAX) (default 16)"""

    num_capture_buffers: int | None = None
    """Number of buffers in the capture context (from 2 to INT_MAX) (default 20)"""


@dataclass(frozen=True, kw_only=True)
class h264_cuvid(FFMpegDecoderOption):
    """Nvidia CUVID H264 decoder (codec h264)"""

    deint: int | None = None
    """Set deinterlacing mode (from 0 to 2) (default weave)"""

    gpu: str | None = None
    """GPU to be used for decoding"""

    surfaces: int | None = None
    """Maximum surfaces to be used for decoding (from -1 to INT_MAX) (default -1)"""

    drop_second_field: bool | None = None
    """Drop second field when deinterlacing (default false)"""

    crop: str | None = None
    """Crop (top)x(bottom)x(left)x(right)"""

    resize: str | None = None
    """Resize (width)x(height)"""


@dataclass(frozen=True, kw_only=True)
class hap(FFMpegDecoderOption):
    """Vidvox Hap"""


@dataclass(frozen=True, kw_only=True)
class hdr(FFMpegDecoderOption):
    """HDR (Radiance RGBE format) image"""


@dataclass(frozen=True, kw_only=True)
class hevc(FFMpegDecoderOption):
    """HEVC (High Efficiency Video Coding)"""

    apply_defdispwin: bool | None = None
    """Apply default display window from VUI (default false)"""

    strict_displaywin: bool | None = None
    """stricly apply default display window size (default false)"""


@dataclass(frozen=True, kw_only=True)
class hevc_v4l2m2m(FFMpegDecoderOption):
    """V4L2 mem2mem HEVC decoder wrapper (codec hevc)"""

    num_output_buffers: int | None = None
    """Number of buffers in the output context (from 2 to INT_MAX) (default 16)"""

    num_capture_buffers: int | None = None
    """Number of buffers in the capture context (from 2 to INT_MAX) (default 20)"""


@dataclass(frozen=True, kw_only=True)
class hevc_cuvid(FFMpegDecoderOption):
    """Nvidia CUVID HEVC decoder (codec hevc)"""

    deint: int | None = None
    """Set deinterlacing mode (from 0 to 2) (default weave)"""

    gpu: str | None = None
    """GPU to be used for decoding"""

    surfaces: int | None = None
    """Maximum surfaces to be used for decoding (from -1 to INT_MAX) (default -1)"""

    drop_second_field: bool | None = None
    """Drop second field when deinterlacing (default false)"""

    crop: str | None = None
    """Crop (top)x(bottom)x(left)x(right)"""

    resize: str | None = None
    """Resize (width)x(height)"""


@dataclass(frozen=True, kw_only=True)
class hnm4video(FFMpegDecoderOption):
    """HNM 4 video"""


@dataclass(frozen=True, kw_only=True)
class hq_hqa(FFMpegDecoderOption):
    """Canopus HQ/HQA"""


@dataclass(frozen=True, kw_only=True)
class hqx(FFMpegDecoderOption):
    """Canopus HQX"""


@dataclass(frozen=True, kw_only=True)
class huffyuv(FFMpegDecoderOption):
    """Huffyuv / HuffYUV"""


@dataclass(frozen=True, kw_only=True)
class hymt(FFMpegDecoderOption):
    """HuffYUV MT"""


@dataclass(frozen=True, kw_only=True)
class idcinvideo(FFMpegDecoderOption):
    """id Quake II CIN video (codec idcin)"""


@dataclass(frozen=True, kw_only=True)
class idf(FFMpegDecoderOption):
    """iCEDraw text"""


@dataclass(frozen=True, kw_only=True)
class iff(FFMpegDecoderOption):
    """IFF ACBM/ANIM/DEEP/ILBM/PBM/RGB8/RGBN (codec iff_ilbm)"""


@dataclass(frozen=True, kw_only=True)
class imm4(FFMpegDecoderOption):
    """Infinity IMM4"""


@dataclass(frozen=True, kw_only=True)
class imm5(FFMpegDecoderOption):
    """Infinity IMM5"""


@dataclass(frozen=True, kw_only=True)
class indeo2(FFMpegDecoderOption):
    """Intel Indeo 2"""


@dataclass(frozen=True, kw_only=True)
class indeo3(FFMpegDecoderOption):
    """Intel Indeo 3"""


@dataclass(frozen=True, kw_only=True)
class indeo4(FFMpegDecoderOption):
    """Intel Indeo Video Interactive 4"""


@dataclass(frozen=True, kw_only=True)
class indeo5(FFMpegDecoderOption):
    """Intel Indeo Video Interactive 5"""


@dataclass(frozen=True, kw_only=True)
class interplayvideo(FFMpegDecoderOption):
    """Interplay MVE video"""


@dataclass(frozen=True, kw_only=True)
class ipu(FFMpegDecoderOption):
    """IPU Video"""


@dataclass(frozen=True, kw_only=True)
class jpeg2000(FFMpegDecoderOption):
    """JPEG 2000"""

    lowres: int | None = None
    """Lower the decoding resolution by a power of two (from 0 to 33) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class jpegls(FFMpegDecoderOption):
    """JPEG-LS"""


@dataclass(frozen=True, kw_only=True)
class libjxl(FFMpegDecoderOption):
    """libjxl JPEG XL (codec jpegxl)"""


@dataclass(frozen=True, kw_only=True)
class jv(FFMpegDecoderOption):
    """Bitmap Brothers JV video"""


@dataclass(frozen=True, kw_only=True)
class kgv1(FFMpegDecoderOption):
    """Kega Game Video"""


@dataclass(frozen=True, kw_only=True)
class kmvc(FFMpegDecoderOption):
    """Karl Morton's video codec"""


@dataclass(frozen=True, kw_only=True)
class lagarith(FFMpegDecoderOption):
    """Lagarith lossless"""


@dataclass(frozen=True, kw_only=True)
class loco(FFMpegDecoderOption):
    """LOCO"""


@dataclass(frozen=True, kw_only=True)
class lscr(FFMpegDecoderOption):
    """LEAD Screen Capture"""


@dataclass(frozen=True, kw_only=True)
class m101(FFMpegDecoderOption):
    """Matrox Uncompressed SD"""


@dataclass(frozen=True, kw_only=True)
class eamad(FFMpegDecoderOption):
    """Electronic Arts Madcow Video (codec mad)"""


@dataclass(frozen=True, kw_only=True)
class magicyuv(FFMpegDecoderOption):
    """MagicYUV video"""


@dataclass(frozen=True, kw_only=True)
class mdec(FFMpegDecoderOption):
    """Sony PlayStation MDEC (Motion DECoder)"""


@dataclass(frozen=True, kw_only=True)
class media100(FFMpegDecoderOption):
    """Media 100"""


@dataclass(frozen=True, kw_only=True)
class mimic(FFMpegDecoderOption):
    """Mimic"""


@dataclass(frozen=True, kw_only=True)
class mjpeg(FFMpegDecoderOption):
    """MJPEG (Motion JPEG)"""

    extern_huff: bool | None = None
    """Use external huffman table. (default false)"""


@dataclass(frozen=True, kw_only=True)
class mjpeg_cuvid(FFMpegDecoderOption):
    """Nvidia CUVID MJPEG decoder (codec mjpeg)"""

    deint: int | None = None
    """Set deinterlacing mode (from 0 to 2) (default weave)"""

    gpu: str | None = None
    """GPU to be used for decoding"""

    surfaces: int | None = None
    """Maximum surfaces to be used for decoding (from -1 to INT_MAX) (default -1)"""

    drop_second_field: bool | None = None
    """Drop second field when deinterlacing (default false)"""

    crop: str | None = None
    """Crop (top)x(bottom)x(left)x(right)"""

    resize: str | None = None
    """Resize (width)x(height)"""


@dataclass(frozen=True, kw_only=True)
class mjpegb(FFMpegDecoderOption):
    """Apple MJPEG-B"""


@dataclass(frozen=True, kw_only=True)
class mmvideo(FFMpegDecoderOption):
    """American Laser Games MM Video"""


@dataclass(frozen=True, kw_only=True)
class mobiclip(FFMpegDecoderOption):
    """MobiClip Video"""


@dataclass(frozen=True, kw_only=True)
class motionpixels(FFMpegDecoderOption):
    """Motion Pixels video"""


@dataclass(frozen=True, kw_only=True)
class mpeg1video(FFMpegDecoderOption):
    """MPEG-1 video"""


@dataclass(frozen=True, kw_only=True)
class mpeg1_v4l2m2m(FFMpegDecoderOption):
    """V4L2 mem2mem MPEG1 decoder wrapper (codec mpeg1video)"""

    num_output_buffers: int | None = None
    """Number of buffers in the output context (from 2 to INT_MAX) (default 16)"""

    num_capture_buffers: int | None = None
    """Number of buffers in the capture context (from 2 to INT_MAX) (default 20)"""


@dataclass(frozen=True, kw_only=True)
class mpeg1_cuvid(FFMpegDecoderOption):
    """Nvidia CUVID MPEG1VIDEO decoder (codec mpeg1video)"""

    deint: int | None = None
    """Set deinterlacing mode (from 0 to 2) (default weave)"""

    gpu: str | None = None
    """GPU to be used for decoding"""

    surfaces: int | None = None
    """Maximum surfaces to be used for decoding (from -1 to INT_MAX) (default -1)"""

    drop_second_field: bool | None = None
    """Drop second field when deinterlacing (default false)"""

    crop: str | None = None
    """Crop (top)x(bottom)x(left)x(right)"""

    resize: str | None = None
    """Resize (width)x(height)"""


@dataclass(frozen=True, kw_only=True)
class mpeg2video(FFMpegDecoderOption):
    """MPEG-2 video"""


@dataclass(frozen=True, kw_only=True)
class mpegvideo(FFMpegDecoderOption):
    """MPEG-1 video (codec mpeg2video)"""


@dataclass(frozen=True, kw_only=True)
class mpeg2_v4l2m2m(FFMpegDecoderOption):
    """V4L2 mem2mem MPEG2 decoder wrapper (codec mpeg2video)"""

    num_output_buffers: int | None = None
    """Number of buffers in the output context (from 2 to INT_MAX) (default 16)"""

    num_capture_buffers: int | None = None
    """Number of buffers in the capture context (from 2 to INT_MAX) (default 20)"""


@dataclass(frozen=True, kw_only=True)
class mpeg2_cuvid(FFMpegDecoderOption):
    """Nvidia CUVID MPEG2VIDEO decoder (codec mpeg2video)"""

    deint: int | None = None
    """Set deinterlacing mode (from 0 to 2) (default weave)"""

    gpu: str | None = None
    """GPU to be used for decoding"""

    surfaces: int | None = None
    """Maximum surfaces to be used for decoding (from -1 to INT_MAX) (default -1)"""

    drop_second_field: bool | None = None
    """Drop second field when deinterlacing (default false)"""

    crop: str | None = None
    """Crop (top)x(bottom)x(left)x(right)"""

    resize: str | None = None
    """Resize (width)x(height)"""


@dataclass(frozen=True, kw_only=True)
class mpeg4(FFMpegDecoderOption):
    """MPEG-4 part 2"""


@dataclass(frozen=True, kw_only=True)
class mpeg4_v4l2m2m(FFMpegDecoderOption):
    """V4L2 mem2mem MPEG4 decoder wrapper (codec mpeg4)"""

    num_output_buffers: int | None = None
    """Number of buffers in the output context (from 2 to INT_MAX) (default 16)"""

    num_capture_buffers: int | None = None
    """Number of buffers in the capture context (from 2 to INT_MAX) (default 20)"""


@dataclass(frozen=True, kw_only=True)
class mpeg4_cuvid(FFMpegDecoderOption):
    """Nvidia CUVID MPEG4 decoder (codec mpeg4)"""

    deint: int | None = None
    """Set deinterlacing mode (from 0 to 2) (default weave)"""

    gpu: str | None = None
    """GPU to be used for decoding"""

    surfaces: int | None = None
    """Maximum surfaces to be used for decoding (from -1 to INT_MAX) (default -1)"""

    drop_second_field: bool | None = None
    """Drop second field when deinterlacing (default false)"""

    crop: str | None = None
    """Crop (top)x(bottom)x(left)x(right)"""

    resize: str | None = None
    """Resize (width)x(height)"""


@dataclass(frozen=True, kw_only=True)
class msa1(FFMpegDecoderOption):
    """MS ATC Screen"""


@dataclass(frozen=True, kw_only=True)
class mscc(FFMpegDecoderOption):
    """Mandsoft Screen Capture Codec"""


@dataclass(frozen=True, kw_only=True)
class msmpeg4v1(FFMpegDecoderOption):
    """MPEG-4 part 2 Microsoft variant version 1"""


@dataclass(frozen=True, kw_only=True)
class msmpeg4v2(FFMpegDecoderOption):
    """MPEG-4 part 2 Microsoft variant version 2"""


@dataclass(frozen=True, kw_only=True)
class msmpeg4(FFMpegDecoderOption):
    """MPEG-4 part 2 Microsoft variant version 3 (codec msmpeg4v3)"""


@dataclass(frozen=True, kw_only=True)
class msp2(FFMpegDecoderOption):
    """Microsoft Paint (MSP) version 2"""


@dataclass(frozen=True, kw_only=True)
class msrle(FFMpegDecoderOption):
    """Microsoft RLE"""


@dataclass(frozen=True, kw_only=True)
class mss1(FFMpegDecoderOption):
    """MS Screen 1"""


@dataclass(frozen=True, kw_only=True)
class mss2(FFMpegDecoderOption):
    """MS Windows Media Video V9 Screen"""


@dataclass(frozen=True, kw_only=True)
class msvideo1(FFMpegDecoderOption):
    """Microsoft Video 1"""


@dataclass(frozen=True, kw_only=True)
class mszh(FFMpegDecoderOption):
    """LCL (LossLess Codec Library) MSZH"""


@dataclass(frozen=True, kw_only=True)
class mts2(FFMpegDecoderOption):
    """MS Expression Encoder Screen"""


@dataclass(frozen=True, kw_only=True)
class mv30(FFMpegDecoderOption):
    """MidiVid 3.0"""


@dataclass(frozen=True, kw_only=True)
class mvc1(FFMpegDecoderOption):
    """Silicon Graphics Motion Video Compressor 1"""


@dataclass(frozen=True, kw_only=True)
class mvc2(FFMpegDecoderOption):
    """Silicon Graphics Motion Video Compressor 2"""


@dataclass(frozen=True, kw_only=True)
class mvdv(FFMpegDecoderOption):
    """MidiVid VQ"""


@dataclass(frozen=True, kw_only=True)
class mvha(FFMpegDecoderOption):
    """MidiVid Archive Codec"""


@dataclass(frozen=True, kw_only=True)
class mwsc(FFMpegDecoderOption):
    """MatchWare Screen Capture Codec"""


@dataclass(frozen=True, kw_only=True)
class mxpeg(FFMpegDecoderOption):
    """Mobotix MxPEG video"""


@dataclass(frozen=True, kw_only=True)
class notchlc(FFMpegDecoderOption):
    """NotchLC"""


@dataclass(frozen=True, kw_only=True)
class nuv(FFMpegDecoderOption):
    """NuppelVideo/RTJPEG"""


@dataclass(frozen=True, kw_only=True)
class paf_video(FFMpegDecoderOption):
    """Amazing Studio Packed Animation File Video"""


@dataclass(frozen=True, kw_only=True)
class pam(FFMpegDecoderOption):
    """PAM (Portable AnyMap) image"""


@dataclass(frozen=True, kw_only=True)
class pbm(FFMpegDecoderOption):
    """PBM (Portable BitMap) image"""


@dataclass(frozen=True, kw_only=True)
class pcx(FFMpegDecoderOption):
    """PC Paintbrush PCX image"""


@dataclass(frozen=True, kw_only=True)
class pdv(FFMpegDecoderOption):
    """PDV (PlayDate Video)"""


@dataclass(frozen=True, kw_only=True)
class pfm(FFMpegDecoderOption):
    """PFM (Portable FloatMap) image"""


@dataclass(frozen=True, kw_only=True)
class pgm(FFMpegDecoderOption):
    """PGM (Portable GrayMap) image"""


@dataclass(frozen=True, kw_only=True)
class pgmyuv(FFMpegDecoderOption):
    """PGMYUV (Portable GrayMap YUV) image"""


@dataclass(frozen=True, kw_only=True)
class pgx(FFMpegDecoderOption):
    """PGX (JPEG2000 Test Format)"""


@dataclass(frozen=True, kw_only=True)
class phm(FFMpegDecoderOption):
    """PHM (Portable HalfFloatMap) image"""


@dataclass(frozen=True, kw_only=True)
class photocd(FFMpegDecoderOption):
    """Kodak Photo CD"""

    lowres: int | None = None
    """Lower the decoding resolution by a power of two (from 0 to 4) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class pictor(FFMpegDecoderOption):
    """Pictor/PC Paint"""


@dataclass(frozen=True, kw_only=True)
class pixlet(FFMpegDecoderOption):
    """Apple Pixlet"""


@dataclass(frozen=True, kw_only=True)
class png(FFMpegDecoderOption):
    """PNG (Portable Network Graphics) image"""


@dataclass(frozen=True, kw_only=True)
class ppm(FFMpegDecoderOption):
    """PPM (Portable PixelMap) image"""


@dataclass(frozen=True, kw_only=True)
class prores(FFMpegDecoderOption):
    """Apple ProRes (iCodec Pro)"""


@dataclass(frozen=True, kw_only=True)
class prosumer(FFMpegDecoderOption):
    """Brooktree ProSumer Video"""


@dataclass(frozen=True, kw_only=True)
class psd(FFMpegDecoderOption):
    """Photoshop PSD file"""


@dataclass(frozen=True, kw_only=True)
class ptx(FFMpegDecoderOption):
    """V.Flash PTX image"""


@dataclass(frozen=True, kw_only=True)
class qdraw(FFMpegDecoderOption):
    """Apple QuickDraw"""


@dataclass(frozen=True, kw_only=True)
class qoi(FFMpegDecoderOption):
    """QOI (Quite OK Image format) image"""


@dataclass(frozen=True, kw_only=True)
class qpeg(FFMpegDecoderOption):
    """Q-team QPEG"""


@dataclass(frozen=True, kw_only=True)
class qtrle(FFMpegDecoderOption):
    """QuickTime Animation (RLE) video"""


@dataclass(frozen=True, kw_only=True)
class r10k(FFMpegDecoderOption):
    """AJA Kona 10-bit RGB Codec"""


@dataclass(frozen=True, kw_only=True)
class r210(FFMpegDecoderOption):
    """Uncompressed RGB 10-bit"""


@dataclass(frozen=True, kw_only=True)
class rasc(FFMpegDecoderOption):
    """RemotelyAnywhere Screen Capture"""

    skip_cursor: bool | None = None
    """skip the cursor (default false)"""


@dataclass(frozen=True, kw_only=True)
class rawvideo(FFMpegDecoderOption):
    """raw video"""

    top: bool | None = None
    """top field first (default auto)"""


@dataclass(frozen=True, kw_only=True)
class rl2(FFMpegDecoderOption):
    """RL2 video"""


@dataclass(frozen=True, kw_only=True)
class roqvideo(FFMpegDecoderOption):
    """id RoQ video (codec roq)"""


@dataclass(frozen=True, kw_only=True)
class rpza(FFMpegDecoderOption):
    """QuickTime video (RPZA)"""


@dataclass(frozen=True, kw_only=True)
class rscc(FFMpegDecoderOption):
    """innoHeim/Rsupport Screen Capture Codec"""


@dataclass(frozen=True, kw_only=True)
class rtv1(FFMpegDecoderOption):
    """RTV1 (RivaTuner Video)"""


@dataclass(frozen=True, kw_only=True)
class rv10(FFMpegDecoderOption):
    """RealVideo 1.0"""


@dataclass(frozen=True, kw_only=True)
class rv20(FFMpegDecoderOption):
    """RealVideo 2.0"""


@dataclass(frozen=True, kw_only=True)
class rv30(FFMpegDecoderOption):
    """RealVideo 3.0"""


@dataclass(frozen=True, kw_only=True)
class rv40(FFMpegDecoderOption):
    """RealVideo 4.0"""


@dataclass(frozen=True, kw_only=True)
class sanm(FFMpegDecoderOption):
    """LucasArts SANM/Smush video"""


@dataclass(frozen=True, kw_only=True)
class scpr(FFMpegDecoderOption):
    """ScreenPressor"""


@dataclass(frozen=True, kw_only=True)
class screenpresso(FFMpegDecoderOption):
    """Screenpresso"""


@dataclass(frozen=True, kw_only=True)
class sga(FFMpegDecoderOption):
    """Digital Pictures SGA Video"""


@dataclass(frozen=True, kw_only=True)
class sgi(FFMpegDecoderOption):
    """SGI image"""


@dataclass(frozen=True, kw_only=True)
class sgirle(FFMpegDecoderOption):
    """Silicon Graphics RLE 8-bit video"""


@dataclass(frozen=True, kw_only=True)
class sheervideo(FFMpegDecoderOption):
    """BitJazz SheerVideo"""


@dataclass(frozen=True, kw_only=True)
class simbiosis_imx(FFMpegDecoderOption):
    """Simbiosis Interactive IMX Video"""


@dataclass(frozen=True, kw_only=True)
class smackvid(FFMpegDecoderOption):
    """Smacker video (codec smackvideo)"""


@dataclass(frozen=True, kw_only=True)
class smc(FFMpegDecoderOption):
    """QuickTime Graphics (SMC)"""


@dataclass(frozen=True, kw_only=True)
class smvjpeg(FFMpegDecoderOption):
    """SMV JPEG"""


@dataclass(frozen=True, kw_only=True)
class snow(FFMpegDecoderOption):
    """Snow"""


@dataclass(frozen=True, kw_only=True)
class sp5x(FFMpegDecoderOption):
    """Sunplus JPEG (SP5X)"""


@dataclass(frozen=True, kw_only=True)
class speedhq(FFMpegDecoderOption):
    """NewTek SpeedHQ"""


@dataclass(frozen=True, kw_only=True)
class srgc(FFMpegDecoderOption):
    """Screen Recorder Gold Codec"""


@dataclass(frozen=True, kw_only=True)
class sunrast(FFMpegDecoderOption):
    """Sun Rasterfile image"""


@dataclass(frozen=True, kw_only=True)
class librsvg(FFMpegDecoderOption):
    """Librsvg rasterizer (codec svg)"""

    width: int | None = None
    """Width to render to (0 for default) (from 0 to INT_MAX) (default 0)"""

    height: int | None = None
    """Height to render to (0 for default) (from 0 to INT_MAX) (default 0)"""

    keep_ar: bool | None = None
    """Keep aspect ratio with custom width/height (default true)"""


@dataclass(frozen=True, kw_only=True)
class svq1(FFMpegDecoderOption):
    """Sorenson Vector Quantizer 1 / Sorenson Video 1 / SVQ1"""


@dataclass(frozen=True, kw_only=True)
class svq3(FFMpegDecoderOption):
    """Sorenson Vector Quantizer 3 / Sorenson Video 3 / SVQ3"""


@dataclass(frozen=True, kw_only=True)
class targa(FFMpegDecoderOption):
    """Truevision Targa image"""


@dataclass(frozen=True, kw_only=True)
class targa_y216(FFMpegDecoderOption):
    """Pinnacle TARGA CineWave YUV16"""


@dataclass(frozen=True, kw_only=True)
class tdsc(FFMpegDecoderOption):
    """TDSC"""


@dataclass(frozen=True, kw_only=True)
class eatgq(FFMpegDecoderOption):
    """Electronic Arts TGQ video (codec tgq)"""


@dataclass(frozen=True, kw_only=True)
class eatgv(FFMpegDecoderOption):
    """Electronic Arts TGV video (codec tgv)"""


@dataclass(frozen=True, kw_only=True)
class theora(FFMpegDecoderOption):
    """Theora"""


@dataclass(frozen=True, kw_only=True)
class thp(FFMpegDecoderOption):
    """Nintendo Gamecube THP video"""


@dataclass(frozen=True, kw_only=True)
class tiertexseqvideo(FFMpegDecoderOption):
    """Tiertex Limited SEQ video"""


@dataclass(frozen=True, kw_only=True)
class tiff(FFMpegDecoderOption):
    """TIFF image"""

    subimage: bool | None = None
    """decode subimage instead if available (default false)"""

    thumbnail: bool | None = None
    """decode embedded thumbnail subimage instead if available (default false)"""

    page: int | None = None
    """page number of multi-page image to decode (starting from 1) (from 0 to 65535) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class tmv(FFMpegDecoderOption):
    """8088flex TMV"""


@dataclass(frozen=True, kw_only=True)
class eatqi(FFMpegDecoderOption):
    """Electronic Arts TQI Video (codec tqi)"""


@dataclass(frozen=True, kw_only=True)
class truemotion1(FFMpegDecoderOption):
    """Duck TrueMotion 1.0"""


@dataclass(frozen=True, kw_only=True)
class truemotion2(FFMpegDecoderOption):
    """Duck TrueMotion 2.0"""


@dataclass(frozen=True, kw_only=True)
class truemotion2rt(FFMpegDecoderOption):
    """Duck TrueMotion 2.0 Real Time"""


@dataclass(frozen=True, kw_only=True)
class camtasia(FFMpegDecoderOption):
    """TechSmith Screen Capture Codec (codec tscc)"""


@dataclass(frozen=True, kw_only=True)
class tscc2(FFMpegDecoderOption):
    """TechSmith Screen Codec 2"""


@dataclass(frozen=True, kw_only=True)
class txd(FFMpegDecoderOption):
    """Renderware TXD (TeXture Dictionary) image"""


@dataclass(frozen=True, kw_only=True)
class ultimotion(FFMpegDecoderOption):
    """IBM UltiMotion (codec ulti)"""


@dataclass(frozen=True, kw_only=True)
class utvideo(FFMpegDecoderOption):
    """Ut Video"""


@dataclass(frozen=True, kw_only=True)
class v210(FFMpegDecoderOption):
    """Uncompressed 4:2:2 10-bit"""

    custom_stride: int | None = None
    """Custom V210 stride (from -1 to INT_MAX) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class v210x(FFMpegDecoderOption):
    """Uncompressed 4:2:2 10-bit"""


@dataclass(frozen=True, kw_only=True)
class v308(FFMpegDecoderOption):
    """Uncompressed packed 4:4:4"""


@dataclass(frozen=True, kw_only=True)
class v408(FFMpegDecoderOption):
    """Uncompressed packed QT 4:4:4:4"""


@dataclass(frozen=True, kw_only=True)
class v410(FFMpegDecoderOption):
    """Uncompressed 4:4:4 10-bit"""


@dataclass(frozen=True, kw_only=True)
class vb(FFMpegDecoderOption):
    """Beam Software VB"""


@dataclass(frozen=True, kw_only=True)
class vble(FFMpegDecoderOption):
    """VBLE Lossless Codec"""


@dataclass(frozen=True, kw_only=True)
class vbn(FFMpegDecoderOption):
    """Vizrt Binary Image"""


@dataclass(frozen=True, kw_only=True)
class vc1(FFMpegDecoderOption):
    """SMPTE VC-1"""


@dataclass(frozen=True, kw_only=True)
class vc1_v4l2m2m(FFMpegDecoderOption):
    """V4L2 mem2mem VC1 decoder wrapper (codec vc1)"""

    num_output_buffers: int | None = None
    """Number of buffers in the output context (from 2 to INT_MAX) (default 16)"""

    num_capture_buffers: int | None = None
    """Number of buffers in the capture context (from 2 to INT_MAX) (default 20)"""


@dataclass(frozen=True, kw_only=True)
class vc1_cuvid(FFMpegDecoderOption):
    """Nvidia CUVID VC1 decoder (codec vc1)"""

    deint: int | None = None
    """Set deinterlacing mode (from 0 to 2) (default weave)"""

    gpu: str | None = None
    """GPU to be used for decoding"""

    surfaces: int | None = None
    """Maximum surfaces to be used for decoding (from -1 to INT_MAX) (default -1)"""

    drop_second_field: bool | None = None
    """Drop second field when deinterlacing (default false)"""

    crop: str | None = None
    """Crop (top)x(bottom)x(left)x(right)"""

    resize: str | None = None
    """Resize (width)x(height)"""


@dataclass(frozen=True, kw_only=True)
class vc1image(FFMpegDecoderOption):
    """Windows Media Video 9 Image v2"""


@dataclass(frozen=True, kw_only=True)
class vcr1(FFMpegDecoderOption):
    """ATI VCR1"""


@dataclass(frozen=True, kw_only=True)
class xl(FFMpegDecoderOption):
    """Miro VideoXL (codec vixl)"""


@dataclass(frozen=True, kw_only=True)
class vmdvideo(FFMpegDecoderOption):
    """Sierra VMD video"""


@dataclass(frozen=True, kw_only=True)
class vmix(FFMpegDecoderOption):
    """vMix Video"""


@dataclass(frozen=True, kw_only=True)
class vmnc(FFMpegDecoderOption):
    """VMware Screen Codec / VMware Video"""


@dataclass(frozen=True, kw_only=True)
class vnull(FFMpegDecoderOption):
    """null video"""


@dataclass(frozen=True, kw_only=True)
class vp3(FFMpegDecoderOption):
    """On2 VP3"""


@dataclass(frozen=True, kw_only=True)
class vp4(FFMpegDecoderOption):
    """On2 VP4"""


@dataclass(frozen=True, kw_only=True)
class vp5(FFMpegDecoderOption):
    """On2 VP5"""


@dataclass(frozen=True, kw_only=True)
class vp6(FFMpegDecoderOption):
    """On2 VP6"""


@dataclass(frozen=True, kw_only=True)
class vp6a(FFMpegDecoderOption):
    """On2 VP6 (Flash version, with alpha channel)"""


@dataclass(frozen=True, kw_only=True)
class vp6f(FFMpegDecoderOption):
    """On2 VP6 (Flash version)"""


@dataclass(frozen=True, kw_only=True)
class vp7(FFMpegDecoderOption):
    """On2 VP7"""


@dataclass(frozen=True, kw_only=True)
class vp8(FFMpegDecoderOption):
    """On2 VP8"""


@dataclass(frozen=True, kw_only=True)
class vp8_v4l2m2m(FFMpegDecoderOption):
    """V4L2 mem2mem VP8 decoder wrapper (codec vp8)"""

    num_output_buffers: int | None = None
    """Number of buffers in the output context (from 2 to INT_MAX) (default 16)"""

    num_capture_buffers: int | None = None
    """Number of buffers in the capture context (from 2 to INT_MAX) (default 20)"""


@dataclass(frozen=True, kw_only=True)
class libvpx(FFMpegDecoderOption):
    """libvpx VP8 (codec vp8)"""


@dataclass(frozen=True, kw_only=True)
class vp8_cuvid(FFMpegDecoderOption):
    """Nvidia CUVID VP8 decoder (codec vp8)"""

    deint: int | None = None
    """Set deinterlacing mode (from 0 to 2) (default weave)"""

    gpu: str | None = None
    """GPU to be used for decoding"""

    surfaces: int | None = None
    """Maximum surfaces to be used for decoding (from -1 to INT_MAX) (default -1)"""

    drop_second_field: bool | None = None
    """Drop second field when deinterlacing (default false)"""

    crop: str | None = None
    """Crop (top)x(bottom)x(left)x(right)"""

    resize: str | None = None
    """Resize (width)x(height)"""


@dataclass(frozen=True, kw_only=True)
class vp9(FFMpegDecoderOption):
    """Google VP9"""


@dataclass(frozen=True, kw_only=True)
class vp9_v4l2m2m(FFMpegDecoderOption):
    """V4L2 mem2mem VP9 decoder wrapper (codec vp9)"""

    num_output_buffers: int | None = None
    """Number of buffers in the output context (from 2 to INT_MAX) (default 16)"""

    num_capture_buffers: int | None = None
    """Number of buffers in the capture context (from 2 to INT_MAX) (default 20)"""


@dataclass(frozen=True, kw_only=True)
class vp9_cuvid(FFMpegDecoderOption):
    """Nvidia CUVID VP9 decoder (codec vp9)"""

    deint: int | None = None
    """Set deinterlacing mode (from 0 to 2) (default weave)"""

    gpu: str | None = None
    """GPU to be used for decoding"""

    surfaces: int | None = None
    """Maximum surfaces to be used for decoding (from -1 to INT_MAX) (default -1)"""

    drop_second_field: bool | None = None
    """Drop second field when deinterlacing (default false)"""

    crop: str | None = None
    """Crop (top)x(bottom)x(left)x(right)"""

    resize: str | None = None
    """Resize (width)x(height)"""


@dataclass(frozen=True, kw_only=True)
class vqc(FFMpegDecoderOption):
    """ViewQuest VQC"""


@dataclass(frozen=True, kw_only=True)
class wbmp(FFMpegDecoderOption):
    """WBMP (Wireless Application Protocol Bitmap) image"""


@dataclass(frozen=True, kw_only=True)
class wcmv(FFMpegDecoderOption):
    """WinCAM Motion Video"""


@dataclass(frozen=True, kw_only=True)
class webp(FFMpegDecoderOption):
    """WebP image"""


@dataclass(frozen=True, kw_only=True)
class wmv1(FFMpegDecoderOption):
    """Windows Media Video 7"""


@dataclass(frozen=True, kw_only=True)
class wmv2(FFMpegDecoderOption):
    """Windows Media Video 8"""


@dataclass(frozen=True, kw_only=True)
class wmv3(FFMpegDecoderOption):
    """Windows Media Video 9"""


@dataclass(frozen=True, kw_only=True)
class wmv3image(FFMpegDecoderOption):
    """Windows Media Video 9 Image"""


@dataclass(frozen=True, kw_only=True)
class wnv1(FFMpegDecoderOption):
    """Winnov WNV1"""


@dataclass(frozen=True, kw_only=True)
class wrapped_avframe(FFMpegDecoderOption):
    """AVPacket to AVFrame passthrough"""


@dataclass(frozen=True, kw_only=True)
class vqavideo(FFMpegDecoderOption):
    """Westwood Studios VQA (Vector Quantized Animation) video (codec ws_vqa)"""


@dataclass(frozen=True, kw_only=True)
class xan_wc3(FFMpegDecoderOption):
    """Wing Commander III / Xan"""


@dataclass(frozen=True, kw_only=True)
class xan_wc4(FFMpegDecoderOption):
    """Wing Commander IV / Xxan"""


@dataclass(frozen=True, kw_only=True)
class xbin(FFMpegDecoderOption):
    """eXtended BINary text"""


@dataclass(frozen=True, kw_only=True)
class xbm(FFMpegDecoderOption):
    """XBM (X BitMap) image"""


@dataclass(frozen=True, kw_only=True)
class xface(FFMpegDecoderOption):
    """X-face image"""


@dataclass(frozen=True, kw_only=True)
class xpm(FFMpegDecoderOption):
    """XPM (X PixMap) image"""


@dataclass(frozen=True, kw_only=True)
class xwd(FFMpegDecoderOption):
    """XWD (X Window Dump) image"""


@dataclass(frozen=True, kw_only=True)
class y41p(FFMpegDecoderOption):
    """Uncompressed YUV 4:1:1 12-bit"""


@dataclass(frozen=True, kw_only=True)
class ylc(FFMpegDecoderOption):
    """YUY2 Lossless Codec"""


@dataclass(frozen=True, kw_only=True)
class yop(FFMpegDecoderOption):
    """Psygnosis YOP Video"""


@dataclass(frozen=True, kw_only=True)
class yuv4(FFMpegDecoderOption):
    """Uncompressed packed 4:2:0"""


@dataclass(frozen=True, kw_only=True)
class zerocodec(FFMpegDecoderOption):
    """ZeroCodec Lossless Video"""


@dataclass(frozen=True, kw_only=True)
class zlib(FFMpegDecoderOption):
    """LCL (LossLess Codec Library) ZLIB"""


@dataclass(frozen=True, kw_only=True)
class zmbv(FFMpegDecoderOption):
    """Zip Motion Blocks Video"""


@dataclass(frozen=True, kw_only=True)
class _8svx_exp(FFMpegDecoderOption):
    """8SVX exponential"""


@dataclass(frozen=True, kw_only=True)
class _8svx_fib(FFMpegDecoderOption):
    """8SVX fibonacci"""


@dataclass(frozen=True, kw_only=True)
class aac(FFMpegDecoderOption):
    """AAC (Advanced Audio Coding)"""

    dual_mono_mode: int | None = None
    """Select the channel to decode for dual mono (from -1 to 2) (default auto)"""

    channel_order: int | None = None
    """Order in which the channels are to be exported (from 0 to 1) (default default)"""


@dataclass(frozen=True, kw_only=True)
class aac_fixed(FFMpegDecoderOption):
    """AAC (Advanced Audio Coding) (codec aac)"""

    dual_mono_mode: int | None = None
    """Select the channel to decode for dual mono (from -1 to 2) (default auto)"""

    channel_order: int | None = None
    """Order in which the channels are to be exported (from 0 to 1) (default default)"""


@dataclass(frozen=True, kw_only=True)
class aac_latm(FFMpegDecoderOption):
    """AAC LATM (Advanced Audio Coding LATM syntax)"""


@dataclass(frozen=True, kw_only=True)
class ac3(FFMpegDecoderOption):
    """ATSC A/52A (AC-3)"""


@dataclass(frozen=True, kw_only=True)
class ac3_fixed(FFMpegDecoderOption):
    """ATSC A/52A (AC-3) (codec ac3)"""


@dataclass(frozen=True, kw_only=True)
class adpcm_4xm(FFMpegDecoderOption):
    """ADPCM 4X Movie"""


@dataclass(frozen=True, kw_only=True)
class adpcm_adx(FFMpegDecoderOption):
    """SEGA CRI ADX ADPCM"""


@dataclass(frozen=True, kw_only=True)
class adpcm_afc(FFMpegDecoderOption):
    """ADPCM Nintendo Gamecube AFC"""


@dataclass(frozen=True, kw_only=True)
class adpcm_agm(FFMpegDecoderOption):
    """ADPCM AmuseGraphics Movie"""


@dataclass(frozen=True, kw_only=True)
class adpcm_aica(FFMpegDecoderOption):
    """ADPCM Yamaha AICA"""


@dataclass(frozen=True, kw_only=True)
class adpcm_argo(FFMpegDecoderOption):
    """ADPCM Argonaut Games"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ct(FFMpegDecoderOption):
    """ADPCM Creative Technology"""


@dataclass(frozen=True, kw_only=True)
class adpcm_dtk(FFMpegDecoderOption):
    """ADPCM Nintendo Gamecube DTK"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ea(FFMpegDecoderOption):
    """ADPCM Electronic Arts"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ea_maxis_xa(FFMpegDecoderOption):
    """ADPCM Electronic Arts Maxis CDROM XA"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ea_r1(FFMpegDecoderOption):
    """ADPCM Electronic Arts R1"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ea_r2(FFMpegDecoderOption):
    """ADPCM Electronic Arts R2"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ea_r3(FFMpegDecoderOption):
    """ADPCM Electronic Arts R3"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ea_xas(FFMpegDecoderOption):
    """ADPCM Electronic Arts XAS"""


@dataclass(frozen=True, kw_only=True)
class g722(FFMpegDecoderOption):
    """G.722 ADPCM (codec adpcm_g722)"""

    bits_per_codeword: int | None = None
    """Bits per G722 codeword (from 6 to 8) (default 8)"""


@dataclass(frozen=True, kw_only=True)
class g726(FFMpegDecoderOption):
    """G.726 ADPCM (codec adpcm_g726)"""


@dataclass(frozen=True, kw_only=True)
class g726le(FFMpegDecoderOption):
    """G.726 ADPCM little-endian (codec adpcm_g726le)"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_acorn(FFMpegDecoderOption):
    """ADPCM IMA Acorn Replay"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_alp(FFMpegDecoderOption):
    """ADPCM IMA High Voltage Software ALP"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_amv(FFMpegDecoderOption):
    """ADPCM IMA AMV"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_apc(FFMpegDecoderOption):
    """ADPCM IMA CRYO APC"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_apm(FFMpegDecoderOption):
    """ADPCM IMA Ubisoft APM"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_cunning(FFMpegDecoderOption):
    """ADPCM IMA Cunning Developments"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_dat4(FFMpegDecoderOption):
    """ADPCM IMA Eurocom DAT4"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_dk3(FFMpegDecoderOption):
    """ADPCM IMA Duck DK3"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_dk4(FFMpegDecoderOption):
    """ADPCM IMA Duck DK4"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_ea_eacs(FFMpegDecoderOption):
    """ADPCM IMA Electronic Arts EACS"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_ea_sead(FFMpegDecoderOption):
    """ADPCM IMA Electronic Arts SEAD"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_iss(FFMpegDecoderOption):
    """ADPCM IMA Funcom ISS"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_moflex(FFMpegDecoderOption):
    """ADPCM IMA MobiClip MOFLEX"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_mtf(FFMpegDecoderOption):
    """ADPCM IMA Capcom's MT Framework"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_oki(FFMpegDecoderOption):
    """ADPCM IMA Dialogic OKI"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_qt(FFMpegDecoderOption):
    """ADPCM IMA QuickTime"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_rad(FFMpegDecoderOption):
    """ADPCM IMA Radical"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_smjpeg(FFMpegDecoderOption):
    """ADPCM IMA Loki SDL MJPEG"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_ssi(FFMpegDecoderOption):
    """ADPCM IMA Simon & Schuster Interactive"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_wav(FFMpegDecoderOption):
    """ADPCM IMA WAV"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ima_ws(FFMpegDecoderOption):
    """ADPCM IMA Westwood"""


@dataclass(frozen=True, kw_only=True)
class adpcm_ms(FFMpegDecoderOption):
    """ADPCM Microsoft"""


@dataclass(frozen=True, kw_only=True)
class adpcm_mtaf(FFMpegDecoderOption):
    """ADPCM MTAF"""


@dataclass(frozen=True, kw_only=True)
class adpcm_psx(FFMpegDecoderOption):
    """ADPCM Playstation"""


@dataclass(frozen=True, kw_only=True)
class adpcm_sbpro_2(FFMpegDecoderOption):
    """ADPCM Sound Blaster Pro 2-bit"""


@dataclass(frozen=True, kw_only=True)
class adpcm_sbpro_3(FFMpegDecoderOption):
    """ADPCM Sound Blaster Pro 2.6-bit"""


@dataclass(frozen=True, kw_only=True)
class adpcm_sbpro_4(FFMpegDecoderOption):
    """ADPCM Sound Blaster Pro 4-bit"""


@dataclass(frozen=True, kw_only=True)
class adpcm_swf(FFMpegDecoderOption):
    """ADPCM Shockwave Flash"""


@dataclass(frozen=True, kw_only=True)
class adpcm_thp(FFMpegDecoderOption):
    """ADPCM Nintendo THP"""


@dataclass(frozen=True, kw_only=True)
class adpcm_thp_le(FFMpegDecoderOption):
    """ADPCM Nintendo THP (little-endian)"""


@dataclass(frozen=True, kw_only=True)
class adpcm_vima(FFMpegDecoderOption):
    """LucasArts VIMA audio"""


@dataclass(frozen=True, kw_only=True)
class adpcm_xa(FFMpegDecoderOption):
    """ADPCM CDROM XA"""


@dataclass(frozen=True, kw_only=True)
class adpcm_xmd(FFMpegDecoderOption):
    """ADPCM Konami XMD"""


@dataclass(frozen=True, kw_only=True)
class adpcm_yamaha(FFMpegDecoderOption):
    """ADPCM Yamaha"""


@dataclass(frozen=True, kw_only=True)
class adpcm_zork(FFMpegDecoderOption):
    """ADPCM Zork"""


@dataclass(frozen=True, kw_only=True)
class alac(FFMpegDecoderOption):
    """ALAC (Apple Lossless Audio Codec)"""

    extra_bits_bug: bool | None = None
    """Force non-standard decoding process (default false)"""


@dataclass(frozen=True, kw_only=True)
class amrnb(FFMpegDecoderOption):
    """AMR-NB (Adaptive Multi-Rate NarrowBand) (codec amr_nb)"""


@dataclass(frozen=True, kw_only=True)
class amrwb(FFMpegDecoderOption):
    """AMR-WB (Adaptive Multi-Rate WideBand) (codec amr_wb)"""


@dataclass(frozen=True, kw_only=True)
class anull(FFMpegDecoderOption):
    """null audio"""


@dataclass(frozen=True, kw_only=True)
class apac(FFMpegDecoderOption):
    """Marian's A-pac audio"""


@dataclass(frozen=True, kw_only=True)
class ape(FFMpegDecoderOption):
    """Monkey's Audio"""

    max_samples: int | None = None
    """maximum number of samples decoded per call (from 1 to INT_MAX) (default 4608)"""


@dataclass(frozen=True, kw_only=True)
class aptx(FFMpegDecoderOption):
    """aptX (Audio Processing Technology for Bluetooth)"""


@dataclass(frozen=True, kw_only=True)
class aptx_hd(FFMpegDecoderOption):
    """aptX HD (Audio Processing Technology for Bluetooth)"""


@dataclass(frozen=True, kw_only=True)
class atrac1(FFMpegDecoderOption):
    """ATRAC1 (Adaptive TRansform Acoustic Coding)"""


@dataclass(frozen=True, kw_only=True)
class atrac3(FFMpegDecoderOption):
    """ATRAC3 (Adaptive TRansform Acoustic Coding 3)"""


@dataclass(frozen=True, kw_only=True)
class atrac3al(FFMpegDecoderOption):
    """ATRAC3 AL (Adaptive TRansform Acoustic Coding 3 Advanced Lossless)"""


@dataclass(frozen=True, kw_only=True)
class atrac3plus(FFMpegDecoderOption):
    """ATRAC3+ (Adaptive TRansform Acoustic Coding 3+) (codec atrac3p)"""


@dataclass(frozen=True, kw_only=True)
class atrac3plusal(FFMpegDecoderOption):
    """ATRAC3+ AL (Adaptive TRansform Acoustic Coding 3+ Advanced Lossless) (codec atrac3pal)"""


@dataclass(frozen=True, kw_only=True)
class atrac9(FFMpegDecoderOption):
    """ATRAC9 (Adaptive TRansform Acoustic Coding 9)"""


@dataclass(frozen=True, kw_only=True)
class on2avc(FFMpegDecoderOption):
    """On2 Audio for Video Codec (codec avc)"""


@dataclass(frozen=True, kw_only=True)
class binkaudio_dct(FFMpegDecoderOption):
    """Bink Audio (DCT)"""


@dataclass(frozen=True, kw_only=True)
class binkaudio_rdft(FFMpegDecoderOption):
    """Bink Audio (RDFT)"""


@dataclass(frozen=True, kw_only=True)
class bmv_audio(FFMpegDecoderOption):
    """Discworld II BMV audio"""


@dataclass(frozen=True, kw_only=True)
class bonk(FFMpegDecoderOption):
    """Bonk audio"""


@dataclass(frozen=True, kw_only=True)
class cbd2_dpcm(FFMpegDecoderOption):
    """DPCM Cuberoot-Delta-Exact"""


@dataclass(frozen=True, kw_only=True)
class libcodec2(FFMpegDecoderOption):
    """codec2 decoder using libcodec2 (codec codec2)"""


@dataclass(frozen=True, kw_only=True)
class comfortnoise(FFMpegDecoderOption):
    """RFC 3389 comfort noise generator"""


@dataclass(frozen=True, kw_only=True)
class cook(FFMpegDecoderOption):
    """Cook / Cooker / Gecko (RealAudio G2)"""


@dataclass(frozen=True, kw_only=True)
class derf_dpcm(FFMpegDecoderOption):
    """DPCM Xilam DERF"""


@dataclass(frozen=True, kw_only=True)
class dfpwm(FFMpegDecoderOption):
    """DFPWM1a audio"""


@dataclass(frozen=True, kw_only=True)
class dolby_e(FFMpegDecoderOption):
    """Dolby E"""

    channel_order: int | None = None
    """Order in which the channels are to be exported (from 0 to 1) (default default)"""


@dataclass(frozen=True, kw_only=True)
class dsd_lsbf(FFMpegDecoderOption):
    """DSD (Direct Stream Digital), least significant bit first"""


@dataclass(frozen=True, kw_only=True)
class dsd_lsbf_planar(FFMpegDecoderOption):
    """DSD (Direct Stream Digital), least significant bit first, planar"""


@dataclass(frozen=True, kw_only=True)
class dsd_msbf(FFMpegDecoderOption):
    """DSD (Direct Stream Digital), most significant bit first"""


@dataclass(frozen=True, kw_only=True)
class dsd_msbf_planar(FFMpegDecoderOption):
    """DSD (Direct Stream Digital), most significant bit first, planar"""


@dataclass(frozen=True, kw_only=True)
class dsicinaudio(FFMpegDecoderOption):
    """Delphine Software International CIN audio"""


@dataclass(frozen=True, kw_only=True)
class dss_sp(FFMpegDecoderOption):
    """Digital Speech Standard - Standard Play mode (DSS SP)"""


@dataclass(frozen=True, kw_only=True)
class dst(FFMpegDecoderOption):
    """DST (Digital Stream Transfer)"""


@dataclass(frozen=True, kw_only=True)
class dca(FFMpegDecoderOption):
    """DCA (DTS Coherent Acoustics) (codec dts)"""

    core_only: bool | None = None
    """Decode core only without extensions (default false)"""

    channel_order: int | None = None
    """Order in which the channels are to be exported (from 0 to 1) (default default)"""

    downmix: str | None = None
    """Request a specific channel layout from the decoder"""


@dataclass(frozen=True, kw_only=True)
class dvaudio(FFMpegDecoderOption):
    """Ulead DV Audio"""


@dataclass(frozen=True, kw_only=True)
class eac3(FFMpegDecoderOption):
    """ATSC A/52B (AC-3, E-AC-3)"""


@dataclass(frozen=True, kw_only=True)
class evrc(FFMpegDecoderOption):
    """EVRC (Enhanced Variable Rate Codec)"""

    postfilter: bool | None = None
    """enable postfilter (default true)"""


@dataclass(frozen=True, kw_only=True)
class fastaudio(FFMpegDecoderOption):
    """MobiClip FastAudio"""


@dataclass(frozen=True, kw_only=True)
class flac(FFMpegDecoderOption):
    """FLAC (Free Lossless Audio Codec)"""

    use_buggy_lpc: bool | None = None
    """emulate old buggy lavc behavior (default false)"""


@dataclass(frozen=True, kw_only=True)
class ftr(FFMpegDecoderOption):
    """FTR Voice"""


@dataclass(frozen=True, kw_only=True)
class g723_1(FFMpegDecoderOption):
    """G.723.1"""

    postfilter: bool | None = None
    """enable postfilter (default true)"""


@dataclass(frozen=True, kw_only=True)
class g729(FFMpegDecoderOption):
    """G.729"""


@dataclass(frozen=True, kw_only=True)
class gremlin_dpcm(FFMpegDecoderOption):
    """DPCM Gremlin"""


@dataclass(frozen=True, kw_only=True)
class gsm(FFMpegDecoderOption):
    """GSM"""


@dataclass(frozen=True, kw_only=True)
class libgsm(FFMpegDecoderOption):
    """libgsm GSM (codec gsm)"""


@dataclass(frozen=True, kw_only=True)
class gsm_ms(FFMpegDecoderOption):
    """GSM Microsoft variant"""


@dataclass(frozen=True, kw_only=True)
class libgsm_ms(FFMpegDecoderOption):
    """libgsm GSM Microsoft variant (codec gsm_ms)"""


@dataclass(frozen=True, kw_only=True)
class hca(FFMpegDecoderOption):
    """CRI HCA"""


@dataclass(frozen=True, kw_only=True)
class hcom(FFMpegDecoderOption):
    """HCOM Audio"""


@dataclass(frozen=True, kw_only=True)
class iac(FFMpegDecoderOption):
    """IAC (Indeo Audio Coder)"""


@dataclass(frozen=True, kw_only=True)
class ilbc(FFMpegDecoderOption):
    """iLBC (Internet Low Bitrate Codec)"""


@dataclass(frozen=True, kw_only=True)
class imc(FFMpegDecoderOption):
    """IMC (Intel Music Coder)"""


@dataclass(frozen=True, kw_only=True)
class interplay_dpcm(FFMpegDecoderOption):
    """DPCM Interplay"""


@dataclass(frozen=True, kw_only=True)
class interplayacm(FFMpegDecoderOption):
    """Interplay ACM"""


@dataclass(frozen=True, kw_only=True)
class mace3(FFMpegDecoderOption):
    """MACE (Macintosh Audio Compression/Expansion) 3:1"""


@dataclass(frozen=True, kw_only=True)
class mace6(FFMpegDecoderOption):
    """MACE (Macintosh Audio Compression/Expansion) 6:1"""


@dataclass(frozen=True, kw_only=True)
class metasound(FFMpegDecoderOption):
    """Voxware MetaSound"""


@dataclass(frozen=True, kw_only=True)
class misc4(FFMpegDecoderOption):
    """Micronas SC-4 Audio"""


@dataclass(frozen=True, kw_only=True)
class mlp(FFMpegDecoderOption):
    """MLP (Meridian Lossless Packing)"""

    downmix: str | None = None
    """Request a specific channel layout from the decoder"""


@dataclass(frozen=True, kw_only=True)
class mp1(FFMpegDecoderOption):
    """MP1 (MPEG audio layer 1)"""


@dataclass(frozen=True, kw_only=True)
class mp1float(FFMpegDecoderOption):
    """MP1 (MPEG audio layer 1) (codec mp1)"""


@dataclass(frozen=True, kw_only=True)
class mp2(FFMpegDecoderOption):
    """MP2 (MPEG audio layer 2)"""


@dataclass(frozen=True, kw_only=True)
class mp2float(FFMpegDecoderOption):
    """MP2 (MPEG audio layer 2) (codec mp2)"""


@dataclass(frozen=True, kw_only=True)
class mp3float(FFMpegDecoderOption):
    """MP3 (MPEG audio layer 3) (codec mp3)"""


@dataclass(frozen=True, kw_only=True)
class mp3(FFMpegDecoderOption):
    """MP3 (MPEG audio layer 3)"""


@dataclass(frozen=True, kw_only=True)
class mp3adufloat(FFMpegDecoderOption):
    """ADU (Application Data Unit) MP3 (MPEG audio layer 3) (codec mp3adu)"""


@dataclass(frozen=True, kw_only=True)
class mp3adu(FFMpegDecoderOption):
    """ADU (Application Data Unit) MP3 (MPEG audio layer 3)"""


@dataclass(frozen=True, kw_only=True)
class mp3on4float(FFMpegDecoderOption):
    """MP3onMP4 (codec mp3on4)"""


@dataclass(frozen=True, kw_only=True)
class mp3on4(FFMpegDecoderOption):
    """MP3onMP4"""


@dataclass(frozen=True, kw_only=True)
class als(FFMpegDecoderOption):
    """MPEG-4 Audio Lossless Coding (ALS) (codec mp4als)"""


@dataclass(frozen=True, kw_only=True)
class msnsiren(FFMpegDecoderOption):
    """MSN Siren"""


@dataclass(frozen=True, kw_only=True)
class mpc7(FFMpegDecoderOption):
    """Musepack SV7 (codec musepack7)"""


@dataclass(frozen=True, kw_only=True)
class mpc8(FFMpegDecoderOption):
    """Musepack SV8 (codec musepack8)"""


@dataclass(frozen=True, kw_only=True)
class nellymoser(FFMpegDecoderOption):
    """Nellymoser Asao"""


@dataclass(frozen=True, kw_only=True)
class opus(FFMpegDecoderOption):
    """Opus"""

    apply_phase_inv: bool | None = None
    """Apply intensity stereo phase inversion (default true)"""


@dataclass(frozen=True, kw_only=True)
class libopus(FFMpegDecoderOption):
    """libopus Opus (codec opus)"""

    apply_phase_inv: bool | None = None
    """Apply intensity stereo phase inversion (default true)"""


@dataclass(frozen=True, kw_only=True)
class osq(FFMpegDecoderOption):
    """OSQ (Original Sound Quality)"""


@dataclass(frozen=True, kw_only=True)
class paf_audio(FFMpegDecoderOption):
    """Amazing Studio Packed Animation File Audio"""


@dataclass(frozen=True, kw_only=True)
class pcm_alaw(FFMpegDecoderOption):
    """PCM A-law / G.711 A-law"""


@dataclass(frozen=True, kw_only=True)
class pcm_bluray(FFMpegDecoderOption):
    """PCM signed 16|20|24-bit big-endian for Blu-ray media"""


@dataclass(frozen=True, kw_only=True)
class pcm_dvd(FFMpegDecoderOption):
    """PCM signed 16|20|24-bit big-endian for DVD media"""


@dataclass(frozen=True, kw_only=True)
class pcm_f16le(FFMpegDecoderOption):
    """PCM 16.8 floating point little-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_f24le(FFMpegDecoderOption):
    """PCM 24.0 floating point little-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_f32be(FFMpegDecoderOption):
    """PCM 32-bit floating point big-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_f32le(FFMpegDecoderOption):
    """PCM 32-bit floating point little-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_f64be(FFMpegDecoderOption):
    """PCM 64-bit floating point big-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_f64le(FFMpegDecoderOption):
    """PCM 64-bit floating point little-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_lxf(FFMpegDecoderOption):
    """PCM signed 20-bit little-endian planar"""


@dataclass(frozen=True, kw_only=True)
class pcm_mulaw(FFMpegDecoderOption):
    """PCM mu-law / G.711 mu-law"""


@dataclass(frozen=True, kw_only=True)
class pcm_s16be(FFMpegDecoderOption):
    """PCM signed 16-bit big-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_s16be_planar(FFMpegDecoderOption):
    """PCM signed 16-bit big-endian planar"""


@dataclass(frozen=True, kw_only=True)
class pcm_s16le(FFMpegDecoderOption):
    """PCM signed 16-bit little-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_s16le_planar(FFMpegDecoderOption):
    """PCM signed 16-bit little-endian planar"""


@dataclass(frozen=True, kw_only=True)
class pcm_s24be(FFMpegDecoderOption):
    """PCM signed 24-bit big-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_s24daud(FFMpegDecoderOption):
    """PCM D-Cinema audio signed 24-bit"""


@dataclass(frozen=True, kw_only=True)
class pcm_s24le(FFMpegDecoderOption):
    """PCM signed 24-bit little-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_s24le_planar(FFMpegDecoderOption):
    """PCM signed 24-bit little-endian planar"""


@dataclass(frozen=True, kw_only=True)
class pcm_s32be(FFMpegDecoderOption):
    """PCM signed 32-bit big-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_s32le(FFMpegDecoderOption):
    """PCM signed 32-bit little-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_s32le_planar(FFMpegDecoderOption):
    """PCM signed 32-bit little-endian planar"""


@dataclass(frozen=True, kw_only=True)
class pcm_s64be(FFMpegDecoderOption):
    """PCM signed 64-bit big-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_s64le(FFMpegDecoderOption):
    """PCM signed 64-bit little-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_s8(FFMpegDecoderOption):
    """PCM signed 8-bit"""


@dataclass(frozen=True, kw_only=True)
class pcm_s8_planar(FFMpegDecoderOption):
    """PCM signed 8-bit planar"""


@dataclass(frozen=True, kw_only=True)
class pcm_sga(FFMpegDecoderOption):
    """PCM SGA"""


@dataclass(frozen=True, kw_only=True)
class pcm_u16be(FFMpegDecoderOption):
    """PCM unsigned 16-bit big-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_u16le(FFMpegDecoderOption):
    """PCM unsigned 16-bit little-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_u24be(FFMpegDecoderOption):
    """PCM unsigned 24-bit big-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_u24le(FFMpegDecoderOption):
    """PCM unsigned 24-bit little-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_u32be(FFMpegDecoderOption):
    """PCM unsigned 32-bit big-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_u32le(FFMpegDecoderOption):
    """PCM unsigned 32-bit little-endian"""


@dataclass(frozen=True, kw_only=True)
class pcm_u8(FFMpegDecoderOption):
    """PCM unsigned 8-bit"""


@dataclass(frozen=True, kw_only=True)
class pcm_vidc(FFMpegDecoderOption):
    """PCM Archimedes VIDC"""


@dataclass(frozen=True, kw_only=True)
class qcelp(FFMpegDecoderOption):
    """QCELP / PureVoice"""


@dataclass(frozen=True, kw_only=True)
class qdm2(FFMpegDecoderOption):
    """QDesign Music Codec 2"""


@dataclass(frozen=True, kw_only=True)
class qdmc(FFMpegDecoderOption):
    """QDesign Music Codec 1"""


@dataclass(frozen=True, kw_only=True)
class real_144(FFMpegDecoderOption):
    """RealAudio 1.0 (14.4K) (codec ra_144)"""


@dataclass(frozen=True, kw_only=True)
class real_288(FFMpegDecoderOption):
    """RealAudio 2.0 (28.8K) (codec ra_288)"""


@dataclass(frozen=True, kw_only=True)
class ralf(FFMpegDecoderOption):
    """RealAudio Lossless"""


@dataclass(frozen=True, kw_only=True)
class rka(FFMpegDecoderOption):
    """RKA (RK Audio)"""


@dataclass(frozen=True, kw_only=True)
class roq_dpcm(FFMpegDecoderOption):
    """DPCM id RoQ"""


@dataclass(frozen=True, kw_only=True)
class s302m(FFMpegDecoderOption):
    """SMPTE 302M"""

    non_pcm_mode: int | None = None
    """Chooses what to do with NON-PCM (from 0 to 3) (default decode_drop)"""


@dataclass(frozen=True, kw_only=True)
class sbc(FFMpegDecoderOption):
    """SBC (low-complexity subband codec)"""


@dataclass(frozen=True, kw_only=True)
class sdx2_dpcm(FFMpegDecoderOption):
    """DPCM Squareroot-Delta-Exact"""


@dataclass(frozen=True, kw_only=True)
class shorten(FFMpegDecoderOption):
    """Shorten"""


@dataclass(frozen=True, kw_only=True)
class sipr(FFMpegDecoderOption):
    """RealAudio SIPR / ACELP.NET"""


@dataclass(frozen=True, kw_only=True)
class siren(FFMpegDecoderOption):
    """Siren"""


@dataclass(frozen=True, kw_only=True)
class smackaud(FFMpegDecoderOption):
    """Smacker audio (codec smackaudio)"""


@dataclass(frozen=True, kw_only=True)
class sol_dpcm(FFMpegDecoderOption):
    """DPCM Sol"""


@dataclass(frozen=True, kw_only=True)
class sonic(FFMpegDecoderOption):
    """Sonic"""


@dataclass(frozen=True, kw_only=True)
class speex(FFMpegDecoderOption):
    """Speex"""


@dataclass(frozen=True, kw_only=True)
class libspeex(FFMpegDecoderOption):
    """libspeex Speex (codec speex)"""


@dataclass(frozen=True, kw_only=True)
class tak(FFMpegDecoderOption):
    """TAK (Tom's lossless Audio Kompressor)"""


@dataclass(frozen=True, kw_only=True)
class truehd(FFMpegDecoderOption):
    """TrueHD"""

    downmix: str | None = None
    """Request a specific channel layout from the decoder"""


@dataclass(frozen=True, kw_only=True)
class truespeech(FFMpegDecoderOption):
    """DSP Group TrueSpeech"""


@dataclass(frozen=True, kw_only=True)
class tta(FFMpegDecoderOption):
    """TTA (True Audio)"""

    password: str | None = None
    """Set decoding password"""


@dataclass(frozen=True, kw_only=True)
class twinvq(FFMpegDecoderOption):
    """VQF TwinVQ"""


@dataclass(frozen=True, kw_only=True)
class vmdaudio(FFMpegDecoderOption):
    """Sierra VMD audio"""


@dataclass(frozen=True, kw_only=True)
class vorbis(FFMpegDecoderOption):
    """Vorbis"""


@dataclass(frozen=True, kw_only=True)
class libvorbis(FFMpegDecoderOption):
    """libvorbis (codec vorbis)"""


@dataclass(frozen=True, kw_only=True)
class wady_dpcm(FFMpegDecoderOption):
    """DPCM Marble WADY"""


@dataclass(frozen=True, kw_only=True)
class wavarc(FFMpegDecoderOption):
    """Waveform Archiver"""


@dataclass(frozen=True, kw_only=True)
class wavesynth(FFMpegDecoderOption):
    """Wave synthesis pseudo-codec"""


@dataclass(frozen=True, kw_only=True)
class wavpack(FFMpegDecoderOption):
    """WavPack"""


@dataclass(frozen=True, kw_only=True)
class ws_snd1(FFMpegDecoderOption):
    """Westwood Audio (SND1) (codec westwood_snd1)"""


@dataclass(frozen=True, kw_only=True)
class wmalossless(FFMpegDecoderOption):
    """Windows Media Audio Lossless"""


@dataclass(frozen=True, kw_only=True)
class wmapro(FFMpegDecoderOption):
    """Windows Media Audio 9 Professional"""


@dataclass(frozen=True, kw_only=True)
class wmav1(FFMpegDecoderOption):
    """Windows Media Audio 1"""


@dataclass(frozen=True, kw_only=True)
class wmav2(FFMpegDecoderOption):
    """Windows Media Audio 2"""


@dataclass(frozen=True, kw_only=True)
class wmavoice(FFMpegDecoderOption):
    """Windows Media Audio Voice"""


@dataclass(frozen=True, kw_only=True)
class xan_dpcm(FFMpegDecoderOption):
    """DPCM Xan"""


@dataclass(frozen=True, kw_only=True)
class xma1(FFMpegDecoderOption):
    """Xbox Media Audio 1"""


@dataclass(frozen=True, kw_only=True)
class xma2(FFMpegDecoderOption):
    """Xbox Media Audio 2"""


@dataclass(frozen=True, kw_only=True)
class ssa(FFMpegDecoderOption):
    """ASS (Advanced SubStation Alpha) subtitle (codec ass)"""


@dataclass(frozen=True, kw_only=True)
class ass(FFMpegDecoderOption):
    """ASS (Advanced SubStation Alpha) subtitle"""


@dataclass(frozen=True, kw_only=True)
class dvbsub(FFMpegDecoderOption):
    """DVB subtitles (codec dvb_subtitle)"""

    compute_edt: bool | None = None
    """compute end of time using pts or timeout (default false)"""

    compute_clut: bool | None = None
    """compute clut when not available(-1) or only once (-2) or always(1) or never(0) (default auto)"""

    dvb_substream: int | None = None
    """(from -1 to 63) (default -1)"""


@dataclass(frozen=True, kw_only=True)
class libzvbi_teletextdec(FFMpegDecoderOption):
    """Libzvbi DVB teletext decoder (codec dvb_teletext)"""

    txt_page: str | None = None
    """page numbers to decode, subtitle for subtitles, * for all (default "*")"""

    txt_default_region: int | None = None
    """default G0 character set used for decoding (from -1 to 87) (default -1)"""

    txt_chop_top: int | None = None
    """discards the top teletext line (from 0 to 1) (default 1)"""

    txt_format: int | None = None
    """format of the subtitles (bitmap or text or ass) (from 0 to 2) (default bitmap)"""

    txt_left: int | None = None
    """x offset of generated bitmaps (from 0 to 65535) (default 0)"""

    txt_top: int | None = None
    """y offset of generated bitmaps (from 0 to 65535) (default 0)"""

    txt_chop_spaces: int | None = None
    """chops leading and trailing spaces from text (from 0 to 1) (default 1)"""

    txt_duration: int | None = None
    """display duration of teletext pages in msecs (from -1 to 8.64e+07) (default -1)"""

    txt_transparent: int | None = None
    """force transparent background of the teletext (from 0 to 1) (default 0)"""

    txt_opacity: int | None = None
    """set opacity of the transparent background (from -1 to 255) (default -1)"""


@dataclass(frozen=True, kw_only=True)
class dvdsub(FFMpegDecoderOption):
    """DVD subtitles (codec dvd_subtitle)"""

    palette: str | None = None
    """set the global palette"""

    ifo_palette: str | None = None
    """obtain the global palette from .IFO file"""

    forced_subs_only: bool | None = None
    """Only show forced subtitles (default false)"""


@dataclass(frozen=True, kw_only=True)
class cc_dec(FFMpegDecoderOption):
    """Closed Caption (EIA-608 / CEA-708) (codec eia_608)"""

    real_time: bool | None = None
    """emit subtitle events as they are decoded for real-time display (default false)"""

    real_time_latency_msec: int | None = None
    """minimum elapsed time between emitting real-time subtitle events (from 0 to 500) (default 200)"""

    data_field: int | None = None
    """select data field (from -1 to 1) (default auto)"""


@dataclass(frozen=True, kw_only=True)
class pgssub(FFMpegDecoderOption):
    """HDMV Presentation Graphic Stream subtitles (codec hdmv_pgs_subtitle)"""

    forced_subs_only: bool | None = None
    """Only show forced subtitles (default false)"""


@dataclass(frozen=True, kw_only=True)
class jacosub(FFMpegDecoderOption):
    """JACOsub subtitle"""


@dataclass(frozen=True, kw_only=True)
class microdvd(FFMpegDecoderOption):
    """MicroDVD subtitle"""


@dataclass(frozen=True, kw_only=True)
class mov_text(FFMpegDecoderOption):
    """3GPP Timed Text subtitle"""

    width: int | None = None
    """Frame width, usually video width (from 0 to INT_MAX) (default 0)"""

    height: int | None = None
    """Frame height, usually video height (from 0 to INT_MAX) (default 0)"""


@dataclass(frozen=True, kw_only=True)
class mpl2(FFMpegDecoderOption):
    """MPL2 subtitle"""


@dataclass(frozen=True, kw_only=True)
class pjs(FFMpegDecoderOption):
    """PJS subtitle"""


@dataclass(frozen=True, kw_only=True)
class realtext(FFMpegDecoderOption):
    """RealText subtitle"""


@dataclass(frozen=True, kw_only=True)
class sami(FFMpegDecoderOption):
    """SAMI subtitle"""


@dataclass(frozen=True, kw_only=True)
class stl(FFMpegDecoderOption):
    """Spruce subtitle format"""


@dataclass(frozen=True, kw_only=True)
class srt(FFMpegDecoderOption):
    """SubRip subtitle (codec subrip)"""


@dataclass(frozen=True, kw_only=True)
class subrip(FFMpegDecoderOption):
    """SubRip subtitle"""


@dataclass(frozen=True, kw_only=True)
class subviewer(FFMpegDecoderOption):
    """SubViewer subtitle"""


@dataclass(frozen=True, kw_only=True)
class subviewer1(FFMpegDecoderOption):
    """SubViewer1 subtitle"""


@dataclass(frozen=True, kw_only=True)
class text(FFMpegDecoderOption):
    """Raw text subtitle"""


@dataclass(frozen=True, kw_only=True)
class vplayer(FFMpegDecoderOption):
    """VPlayer subtitle"""


@dataclass(frozen=True, kw_only=True)
class webvtt(FFMpegDecoderOption):
    """WebVTT subtitle"""


@dataclass(frozen=True, kw_only=True)
class xsub(FFMpegDecoderOption):
    """XSUB"""
