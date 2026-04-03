// NOTE: this file is auto-generated, do not modify
/**
 * Typed output() function with all FFmpeg output options.
 */

import { OutputNode, OutputStream } from "@typed-ffmpeg/core/dag/nodes";
import { FilterableStream } from "@typed-ffmpeg/core/dag/baseStreams";
import { merge } from "@typed-ffmpeg/core/utils/frozenRecord";
import type { FFMpegEncoderOption } from "../../codecs/encoders.js";
import type { FFMpegMuxerOption } from "../../formats/muxers.js";
import type { FFMpegAVFormatContextEncoderOption } from "../../options/format.js";
import type { FFMpegAVCodecContextEncoderOption } from "../../options/codec.js";
import type {
  FFBoolean, FFInt, FFInt64, FFFloat, FFDouble, FFString,
  FFDuration, FFFunc, FFTime,
} from "@typed-ffmpeg/core/types";

/**
 * Output file URL
 *
 * @param streams - The streams to output
 * @param filename - The filename to output to
 * @param options - Output options
 * @returns The output stream
 */
export function output(
  streams: FilterableStream[],
  filename: string,
  options?: {
    f?: FFFunc;
    c?: FFFunc;
    codec?: FFFunc;
    pre?: FFFunc;
    map?: FFFunc;
    map_channel?: FFFunc;
    map_metadata?: FFFunc;
    map_chapters?: FFFunc;
    t?: FFFunc;
    to?: FFFunc;
    fs?: FFFunc;
    ss?: FFFunc;
    timestamp?: FFFunc;
    metadata?: FFFunc;
    program?: FFFunc;
    dframes?: FFFunc;
    target?: FFFunc;
    shortest?: FFFunc;
    bitexact?: FFFunc;
    apad?: FFFunc;
    copyinkf?: FFFunc;
    copypriorss?: FFFunc;
    frames?: FFFunc;
    tag?: FFFunc;
    q?: FFFunc;
    qscale?: FFFunc;
    profile?: FFFunc;
    filter?: FFFunc;
    filter_script?: FFFunc;
    attach?: FFFunc;
    disposition?: FFFunc;
    bits_per_raw_sample?: FFFunc;
    vframes?: FFFunc;
    r?: FFFunc;
    fpsmax?: FFFunc;
    s?: FFFunc;
    aspect?: FFFunc;
    pix_fmt?: FFFunc;
    vn?: FFFunc;
    rc_override?: FFFunc;
    vcodec?: FFFunc;
    timecode?: FFFunc;
    _pass?: FFFunc;
    passlogfile?: FFFunc;
    vf?: FFFunc;
    intra_matrix?: FFFunc;
    inter_matrix?: FFFunc;
    chroma_intra_matrix?: FFFunc;
    top?: FFFunc;
    vtag?: FFFunc;
    fps_mode?: FFFunc;
    force_fps?: FFFunc;
    streamid?: FFFunc;
    force_key_frames?: FFFunc;
    ab?: FFFunc;
    b?: FFFunc;
    autoscale?: FFFunc;
    aframes?: FFFunc;
    aq?: FFFunc;
    ar?: FFFunc;
    ac?: FFFunc;
    an?: FFFunc;
    acodec?: FFFunc;
    atag?: FFFunc;
    sample_fmt?: FFFunc;
    channel_layout?: FFFunc;
    ch_layout?: FFFunc;
    af?: FFFunc;
    sn?: FFFunc;
    scodec?: FFFunc;
    stag?: FFFunc;
    muxdelay?: FFFunc;
    muxpreload?: FFFunc;
    sdp_file?: FFFunc;
    time_base?: FFFunc;
    enc_time_base?: FFFunc;
    bsf?: FFFunc;
    absf?: FFFunc;
    vbsf?: FFFunc;
    apre?: FFFunc;
    vpre?: FFFunc;
    spre?: FFFunc;
    fpre?: FFFunc;
    max_muxing_queue_size?: FFFunc;
    muxing_queue_data_threshold?: FFFunc;
    dcodec?: FFFunc;
    dn?: FFFunc;
    encoderOptions?: FFMpegEncoderOption;
    muxerOptions?: FFMpegMuxerOption;
    formatOptions?: FFMpegAVFormatContextEncoderOption;
    codecOptions?: FFMpegAVCodecContextEncoderOption;
    extraOptions?: Record<string, unknown>;
  },
): OutputStream {
  return new OutputNode(
    streams,
    filename,
    merge(
      {
        "f": options?.f,
        "c": options?.c,
        "codec": options?.codec,
        "pre": options?.pre,
        "map": options?.map,
        "map_channel": options?.map_channel,
        "map_metadata": options?.map_metadata,
        "map_chapters": options?.map_chapters,
        "t": options?.t,
        "to": options?.to,
        "fs": options?.fs,
        "ss": options?.ss,
        "timestamp": options?.timestamp,
        "metadata": options?.metadata,
        "program": options?.program,
        "dframes": options?.dframes,
        "target": options?.target,
        "shortest": options?.shortest,
        "bitexact": options?.bitexact,
        "apad": options?.apad,
        "copyinkf": options?.copyinkf,
        "copypriorss": options?.copypriorss,
        "frames": options?.frames,
        "tag": options?.tag,
        "q": options?.q,
        "qscale": options?.qscale,
        "profile": options?.profile,
        "filter": options?.filter,
        "filter_script": options?.filter_script,
        "attach": options?.attach,
        "disposition": options?.disposition,
        "bits_per_raw_sample": options?.bits_per_raw_sample,
        "vframes": options?.vframes,
        "r": options?.r,
        "fpsmax": options?.fpsmax,
        "s": options?.s,
        "aspect": options?.aspect,
        "pix_fmt": options?.pix_fmt,
        "vn": options?.vn,
        "rc_override": options?.rc_override,
        "vcodec": options?.vcodec,
        "timecode": options?.timecode,
        "pass": options?._pass,
        "passlogfile": options?.passlogfile,
        "vf": options?.vf,
        "intra_matrix": options?.intra_matrix,
        "inter_matrix": options?.inter_matrix,
        "chroma_intra_matrix": options?.chroma_intra_matrix,
        "top": options?.top,
        "vtag": options?.vtag,
        "fps_mode": options?.fps_mode,
        "force_fps": options?.force_fps,
        "streamid": options?.streamid,
        "force_key_frames": options?.force_key_frames,
        "ab": options?.ab,
        "b": options?.b,
        "autoscale": options?.autoscale,
        "aframes": options?.aframes,
        "aq": options?.aq,
        "ar": options?.ar,
        "ac": options?.ac,
        "an": options?.an,
        "acodec": options?.acodec,
        "atag": options?.atag,
        "sample_fmt": options?.sample_fmt,
        "channel_layout": options?.channel_layout,
        "ch_layout": options?.ch_layout,
        "af": options?.af,
        "sn": options?.sn,
        "scodec": options?.scodec,
        "stag": options?.stag,
        "muxdelay": options?.muxdelay,
        "muxpreload": options?.muxpreload,
        "sdp_file": options?.sdp_file,
        "time_base": options?.time_base,
        "enc_time_base": options?.enc_time_base,
        "bsf": options?.bsf,
        "absf": options?.absf,
        "vbsf": options?.vbsf,
        "apre": options?.apre,
        "vpre": options?.vpre,
        "spre": options?.spre,
        "fpre": options?.fpre,
        "max_muxing_queue_size": options?.max_muxing_queue_size,
        "muxing_queue_data_threshold": options?.muxing_queue_data_threshold,
        "dcodec": options?.dcodec,
        "dn": options?.dn,
      },
      options?.encoderOptions as Record<string, unknown> | undefined,
      options?.muxerOptions as Record<string, unknown> | undefined,
      options?.formatOptions as Record<string, unknown> | undefined,
      options?.codecOptions as Record<string, unknown> | undefined,
      options?.extraOptions,
    ),
  ).stream();
}
