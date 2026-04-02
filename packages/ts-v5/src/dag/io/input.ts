// NOTE: this file is auto-generated, do not modify
/**
 * Typed input() function with all FFmpeg input options.
 */

import { InputNode, AVStream } from "@typed-ffmpeg/core/dag/nodes";
import { merge } from "@typed-ffmpeg/core/utils/frozenRecord";
import type { FFMpegDecoderOption } from "../../codecs/decoders.js";
import type { FFMpegDemuxerOption } from "../../formats/demuxers.js";
import type { FFMpegAVFormatContextDecoderOption } from "../../options/format.js";
import type { FFMpegAVCodecContextDecoderOption } from "../../options/codec.js";
import type {
  FFBoolean, FFInt, FFInt64, FFFloat, FFDouble, FFString,
  FFDuration, FFFunc, FFTime,
} from "@typed-ffmpeg/core/types";

/**
 * Input file URL (ffmpeg `-i` option)
 *
 * @param filename - Input file URL
 * @param options - Input options
 * @returns Input stream
 */
export function input(
  filename: string,
  options?: {
    f?: FFFunc;
    c?: FFFunc;
    codec?: FFFunc;
    t?: FFFunc;
    to?: FFFunc;
    ss?: FFFunc;
    sseof?: FFFunc;
    seek_timestamp?: FFFunc;
    accurate_seek?: FFFunc;
    isync?: FFFunc;
    itsoffset?: FFFunc;
    itsscale?: FFFunc;
    re?: FFFunc;
    readrate?: FFFunc;
    bitexact?: FFFunc;
    tag?: FFFunc;
    reinit_filter?: FFFunc;
    dump_attachment?: FFFunc;
    stream_loop?: FFFunc;
    discard?: FFFunc;
    thread_queue_size?: FFFunc;
    find_stream_info?: FFFunc;
    r?: FFFunc;
    s?: FFFunc;
    pix_fmt?: FFFunc;
    vn?: FFFunc;
    vcodec?: FFFunc;
    top?: FFFunc;
    vtag?: FFFunc;
    hwaccel?: FFFunc;
    hwaccel_device?: FFFunc;
    hwaccel_output_format?: FFFunc;
    autorotate?: FFFunc;
    ar?: FFFunc;
    ac?: FFFunc;
    an?: FFFunc;
    acodec?: FFFunc;
    sample_fmt?: FFFunc;
    channel_layout?: FFFunc;
    ch_layout?: FFFunc;
    guess_layout_max?: FFFunc;
    sn?: FFFunc;
    scodec?: FFFunc;
    fix_sub_duration?: FFFunc;
    canvas_size?: FFFunc;
    bsf?: FFFunc;
    dcodec?: FFFunc;
    dn?: FFFunc;
    decoderOptions?: FFMpegDecoderOption;
    demuxerOptions?: FFMpegDemuxerOption;
    formatOptions?: FFMpegAVFormatContextDecoderOption;
    codecOptions?: FFMpegAVCodecContextDecoderOption;
    extraOptions?: Record<string, unknown>;
  },
): AVStream {
  return new InputNode(
    filename,
    merge(
      {
        "f": options?.f,
        "c": options?.c,
        "codec": options?.codec,
        "t": options?.t,
        "to": options?.to,
        "ss": options?.ss,
        "sseof": options?.sseof,
        "seek_timestamp": options?.seek_timestamp,
        "accurate_seek": options?.accurate_seek,
        "isync": options?.isync,
        "itsoffset": options?.itsoffset,
        "itsscale": options?.itsscale,
        "re": options?.re,
        "readrate": options?.readrate,
        "bitexact": options?.bitexact,
        "tag": options?.tag,
        "reinit_filter": options?.reinit_filter,
        "dump_attachment": options?.dump_attachment,
        "stream_loop": options?.stream_loop,
        "discard": options?.discard,
        "thread_queue_size": options?.thread_queue_size,
        "find_stream_info": options?.find_stream_info,
        "r": options?.r,
        "s": options?.s,
        "pix_fmt": options?.pix_fmt,
        "vn": options?.vn,
        "vcodec": options?.vcodec,
        "top": options?.top,
        "vtag": options?.vtag,
        "hwaccel": options?.hwaccel,
        "hwaccel_device": options?.hwaccel_device,
        "hwaccel_output_format": options?.hwaccel_output_format,
        "autorotate": options?.autorotate,
        "ar": options?.ar,
        "ac": options?.ac,
        "an": options?.an,
        "acodec": options?.acodec,
        "sample_fmt": options?.sample_fmt,
        "channel_layout": options?.channel_layout,
        "ch_layout": options?.ch_layout,
        "guess_layout_max": options?.guess_layout_max,
        "sn": options?.sn,
        "scodec": options?.scodec,
        "fix_sub_duration": options?.fix_sub_duration,
        "canvas_size": options?.canvas_size,
        "bsf": options?.bsf,
        "dcodec": options?.dcodec,
        "dn": options?.dn,
      },
      options?.decoderOptions as Record<string, unknown> | undefined,
      options?.demuxerOptions as Record<string, unknown> | undefined,
      options?.formatOptions as Record<string, unknown> | undefined,
      options?.codecOptions as Record<string, unknown> | undefined,
      options?.extraOptions,
    ),
  ).stream();
}
