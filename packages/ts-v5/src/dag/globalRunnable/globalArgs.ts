// NOTE: this file is auto-generated, do not modify
/**
 * Typed globalArgs() function with all FFmpeg global options.
 */

import { merge } from "@typed-ffmpeg/core/utils/frozenRecord";
import type { GlobalStream, OutputStream, GlobalNode } from "@typed-ffmpeg/core/dag/nodes";
import type {
  FFBoolean, FFInt, FFInt64, FFFloat, FFDouble, FFString,
  FFDuration, FFFunc, FFTime,
} from "@typed-ffmpeg/core/types";

export interface GlobalArgsOptions {
  /** set logging level */
  loglevel?: FFFunc;
  /** set logging level */
  v?: FFFunc;
  /** generate a report */
  report?: FFFunc;
  /** set maximum size of a single allocated block */
  max_alloc?: FFFunc;
  /** force specific cpu flags */
  cpuflags?: FFFunc;
  /** force specific cpu count */
  cpucount?: FFFunc;
  /** do not show program banner */
  hide_banner?: FFFunc;
  /** overwrite output files */
  y?: FFFunc;
  /** never overwrite output files */
  n?: FFFunc;
  /** Ignore unknown stream types */
  ignore_unknown?: FFFunc;
  /** Copy unknown stream types */
  copy_unknown?: FFFunc;
  /** allow recasting stream type in order to force a decoder of different media type */
  recast_media?: FFFunc;
  /** add timings for benchmarking */
  benchmark?: FFFunc;
  /** add timings for each task */
  benchmark_all?: FFFunc;
  /** write program-readable progress information */
  progress?: FFFunc;
  /** enable or disable interaction on standard input */
  stdin?: FFFunc;
  /** set max runtime in seconds in CPU user time */
  timelimit?: FFFunc;
  /** dump each input packet */
  dump?: FFFunc;
  /** when dumping packets, also dump the payload */
  hex?: FFFunc;
  /** set video sync method globally; deprecated, use -fps_mode */
  vsync?: FFFunc;
  /** frame drop threshold */
  frame_drop_threshold?: FFFunc;
  /** audio sync method */
  _async?: FFFunc;
  /** audio drift threshold */
  adrift_threshold?: FFFunc;
  /** copy timestamps */
  copyts?: FFFunc;
  /** shift input timestamps to start at 0 when using copyts */
  start_at_zero?: FFFunc;
  /** copy input stream time base when stream copying */
  copytb?: FFFunc;
  /** timestamp discontinuity delta threshold */
  dts_delta_threshold?: FFFunc;
  /** timestamp error delta threshold */
  dts_error_threshold?: FFFunc;
  /** exit on error */
  xerror?: FFFunc;
  /** abort on the specified condition flags */
  abort_on?: FFFunc;
  /** number of non-complex filter threads */
  filter_threads?: FFFunc;
  /** create a complex filtergraph */
  filter_complex?: FFFunc;
  /** number of threads for -filter_complex */
  filter_complex_threads?: FFFunc;
  /** create a complex filtergraph */
  lavfi?: FFFunc;
  /** read complex filtergraph description from a file */
  filter_complex_script?: FFFunc;
  /** enable automatic conversion filters globally */
  auto_conversion_filters?: FFFunc;
  /** print progress report during encoding */
  stats?: FFFunc;
  /** set the period at which ffmpeg updates stats and -progress output */
  stats_period?: FFFunc;
  /** print timestamp debugging info */
  debug_ts?: FFFunc;
  /** ratio of decoding errors (0.0: no errors, 1.0: 100% errors) above which ffmpeg returns an error instead of success. */
  max_error_rate?: FFFunc;
  /** calculate PSNR of compressed frames */
  psnr?: FFFunc;
  /** dump video coding statistics to file */
  vstats?: FFFunc;
  /** dump video coding statistics to file */
  vstats_file?: FFFunc;
  /** Version of the vstats format to use. */
  vstats_version?: FFFunc;
  /** show QP histogram */
  qphist?: FFFunc;
  /** change audio volume (256=normal) */
  vol?: FFFunc;
  /** set VAAPI hardware device (DRM path or X11 display name) */
  vaapi_device?: FFFunc;
  /** initialise hardware device */
  init_hw_device?: FFFunc;
  /** set hardware device used when filtering */
  filter_hw_device?: FFFunc;
  extraOptions?: Record<string, unknown>;
}

/**
 * Build global args kwargs from typed options.
 */
export function buildGlobalArgsKwargs(options?: GlobalArgsOptions): Record<string, unknown> {
  return merge(
    {
      "loglevel": options?.loglevel,
      "v": options?.v,
      "report": options?.report,
      "max_alloc": options?.max_alloc,
      "cpuflags": options?.cpuflags,
      "cpucount": options?.cpucount,
      "hide_banner": options?.hide_banner,
      "y": options?.y,
      "n": options?.n,
      "ignore_unknown": options?.ignore_unknown,
      "copy_unknown": options?.copy_unknown,
      "recast_media": options?.recast_media,
      "benchmark": options?.benchmark,
      "benchmark_all": options?.benchmark_all,
      "progress": options?.progress,
      "stdin": options?.stdin,
      "timelimit": options?.timelimit,
      "dump": options?.dump,
      "hex": options?.hex,
      "vsync": options?.vsync,
      "frame_drop_threshold": options?.frame_drop_threshold,
      "async": options?._async,
      "adrift_threshold": options?.adrift_threshold,
      "copyts": options?.copyts,
      "start_at_zero": options?.start_at_zero,
      "copytb": options?.copytb,
      "dts_delta_threshold": options?.dts_delta_threshold,
      "dts_error_threshold": options?.dts_error_threshold,
      "xerror": options?.xerror,
      "abort_on": options?.abort_on,
      "filter_threads": options?.filter_threads,
      "filter_complex": options?.filter_complex,
      "filter_complex_threads": options?.filter_complex_threads,
      "lavfi": options?.lavfi,
      "filter_complex_script": options?.filter_complex_script,
      "auto_conversion_filters": options?.auto_conversion_filters,
      "stats": options?.stats,
      "stats_period": options?.stats_period,
      "debug_ts": options?.debug_ts,
      "max_error_rate": options?.max_error_rate,
      "psnr": options?.psnr,
      "vstats": options?.vstats,
      "vstats_file": options?.vstats_file,
      "vstats_version": options?.vstats_version,
      "qphist": options?.qphist,
      "vol": options?.vol,
      "vaapi_device": options?.vaapi_device,
      "init_hw_device": options?.init_hw_device,
      "filter_hw_device": options?.filter_hw_device,
    },
    options?.extraOptions,
  ) as Record<string, unknown>;
}
