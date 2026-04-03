// NOTE: this file is auto-generated, do not modify
/**
 * Audio stream with typed filter methods.
 */


import type { VideoStream } from "./video.js";
import { StreamType, type FFMpegFilterDef } from "@typed-ffmpeg/core/common/schema";
import { Default, Auto } from "@typed-ffmpeg/core/utils/types";
import { filterNodeFactory } from "@typed-ffmpeg/core/dag/factory";
import { merge } from "@typed-ffmpeg/core/utils/frozenRecord";
import { FilterableStream } from "@typed-ffmpeg/core/dag/baseStreams";
import { AudioStream as AudioStreamBase, FilterNode } from "@typed-ffmpeg/core/dag/nodes";
import type {
  FFBoolean, FFInt, FFInt64, FFFloat, FFDouble, FFString,
  FFDuration, FFColor, FFFlags, FFDictionary, FFPixFmt,
  FFVideoRate, FFImageSize, FFRational, FFSampleFmt, FFBinary,
} from "@typed-ffmpeg/core/types";

export class AudioStream extends AudioStreamBase {




/**
 * Convert input audio to 3d scope video output.

 *
 * @param options.rate - set video rate (default "25")
 * @param options.size - set video size (default "hd720")
 * @param options.fov - set camera FoV (from 40 to 150) (default 90)
 * @param options.roll - set camera roll (from -180 to 180) (default 0)
 * @param options.pitch - set camera pitch (from -180 to 180) (default 0)
 * @param options.yaw - set camera yaw (from -180 to 180) (default 0)
 * @param options.xzoom - set camera zoom (from 0.01 to 10) (default 1)
 * @param options.xpos - set camera position (from -60 to 60) (default 0)
 * @param options.length - set length (from 1 to 60) (default 15)
 * @see https://ffmpeg.org/ffmpeg-filters.html#a3dscope
 */
  a3dscope(
    options?: {
    rate?: FFVideoRate;
    size?: FFImageSize;
    fov?: FFFloat;
    roll?: FFFloat;
    pitch?: FFFloat;
    yaw?: FFFloat;
    xzoom?: FFFloat;
    xpos?: FFFloat;
    length?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "a3dscope", typingsInput: ["audio"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "rate": options?.rate,
      "size": options?.size,
      "fov": options?.fov,
      "roll": options?.roll,
      "pitch": options?.pitch,
      "yaw": options?.yaw,
      "xzoom": options?.xzoom,
      "xpos": options?.xpos,
      "length": options?.length,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply Affine Projection algorithm to first audio stream.

 *
 * @param options.order - set the filter order (from 1 to 32767) (default 16)
 * @param options.projection - set the filter projection (from 1 to 256) (default 2)
 * @param options.mu - set the filter mu (from 0 to 1) (default 0.0001)
 * @param options.delta - set the filter delta (from 0 to 1) (default 0.001)
 * @param options.out_mode - set output mode (from 0 to 4) (default o)
 * @param options.precision - set processing precision (from 0 to 2) (default auto)
 * @see https://ffmpeg.org/ffmpeg-filters.html#aap
 */
  aap(
    _desired: AudioStream,

    options?: {
    order?: FFInt;
    projection?: FFInt;
    mu?: FFFloat;
    delta?: FFFloat;
    out_mode?: FFInt | "i" | "d" | "o" | "n" | "e";
    precision?: FFInt | "auto" | "float" | "double";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "aap", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
      [this, _desired],
      merge(
    {
      "order": options?.order,
      "projection": options?.projection,
      "mu": options?.mu,
      "delta": options?.delta,
      "out_mode": options?.out_mode,
      "precision": options?.precision,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Benchmark part of a filtergraph.

 *
 * @param options.action - set action (from 0 to 1) (default start)
 * @see https://ffmpeg.org/ffmpeg-filters.html#bench_002c-abench
 */
  abench(
    options?: {
    action?: FFInt | "start" | "stop";
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "abench", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "action": options?.action,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Convert input audio to audio bit scope video output.

 *
 * @param options.rate - set video rate (default "25")
 * @param options.size - set video size (default "1024x256")
 * @param options.colors - set channels colors (default "red|green|blue|yellow|orange|lime|pink|magenta|brown")
 * @param options.mode - set output mode (from 0 to 1) (default bars)
 * @see https://ffmpeg.org/ffmpeg-filters.html#abitscope
 */
  abitscope(
    options?: {
    rate?: FFVideoRate;
    size?: FFImageSize;
    colors?: FFString;
    mode?: FFInt | "bars" | "trace";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "abitscope", typingsInput: ["audio"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "rate": options?.rate,
      "size": options?.size,
      "colors": options?.colors,
      "mode": options?.mode,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }










/**
 * Audio compressor.

 *
 * @param options.level_in - set input gain (from 0.015625 to 64) (default 1)
 * @param options.mode - set mode (from 0 to 1) (default downward)
 * @param options.threshold - set threshold (from 0.000976563 to 1) (default 0.125)
 * @param options.ratio - set ratio (from 1 to 20) (default 2)
 * @param options.attack - set attack (from 0.01 to 2000) (default 20)
 * @param options.release - set release (from 0.01 to 9000) (default 250)
 * @param options.makeup - set make up gain (from 1 to 64) (default 1)
 * @param options.knee - set knee (from 1 to 8) (default 2.82843)
 * @param options.link - set link type (from 0 to 1) (default average)
 * @param options.detection - set detection (from 0 to 1) (default rms)
 * @param options.level_sc - set sidechain gain (from 0.015625 to 64) (default 1)
 * @param options.mix - set mix (from 0 to 1) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#acompressor
 */
  acompressor(
    options?: {
    level_in?: FFDouble;
    mode?: FFInt | "downward" | "upward";
    threshold?: FFDouble;
    ratio?: FFDouble;
    attack?: FFDouble;
    release?: FFDouble;
    makeup?: FFDouble;
    knee?: FFDouble;
    link?: FFInt | "average" | "maximum";
    detection?: FFInt | "peak" | "rms";
    level_sc?: FFDouble;
    mix?: FFDouble;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "acompressor", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "level_in": options?.level_in,
      "mode": options?.mode,
      "threshold": options?.threshold,
      "ratio": options?.ratio,
      "attack": options?.attack,
      "release": options?.release,
      "makeup": options?.makeup,
      "knee": options?.knee,
      "link": options?.link,
      "detection": options?.detection,
      "level_sc": options?.level_sc,
      "mix": options?.mix,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Simple audio dynamic range compression/expansion filter.

 *
 * @param options.contrast - set contrast (from 0 to 100) (default 33)
 * @see https://ffmpeg.org/ffmpeg-filters.html#acontrast
 */
  acontrast(
    options?: {
    contrast?: FFFloat;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "acontrast", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "contrast": options?.contrast,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Copy the input audio unchanged to the output.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#acopy
 */
  acopy(
    options?: {
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "acopy", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }








/**
 * Split audio into per-bands streams.

 *
 * @param options.split - set split frequencies (default "500")
 * @param options.order - set filter order (from 0 to 9) (default 4th)
 * @param options.level - set input gain (from 0 to 1) (default 1)
 * @param options.gain - set output bands gain (default "1.f")
 * @param options.precision - set processing precision (from 0 to 2) (default auto)
 * @see https://ffmpeg.org/ffmpeg-filters.html#acrossover
 */
  acrossover(
    options?: {
    split?: FFString;
    order?: FFInt | "2nd" | "4th" | "6th" | "8th" | "10th" | "12th" | "14th" | "16th" | "18th" | "20th";
    level?: FFFloat;
    gain?: FFString;
    precision?: FFInt | "auto" | "float" | "double";
extraOptions?: Record<string, unknown>;
    },
  ): FilterNode {
    const filterNode = filterNodeFactory(
      { name: "acrossover", typingsInput: ["audio"], typingsOutput: [] },
      [this],
      merge(
    {
      "split": options?.split,
      "order": options?.order,
      "level": options?.level,
      "gain": options?.gain,
      "precision": options?.precision,
},
    options?.extraOptions,
  ),
    );
return filterNode;
  }






/**
 * Reduce audio bit resolution.

 *
 * @param options.level_in - set level in (from 0.015625 to 64) (default 1)
 * @param options.level_out - set level out (from 0.015625 to 64) (default 1)
 * @param options.bits - set bit reduction (from 1 to 64) (default 8)
 * @param options.mix - set mix (from 0 to 1) (default 0.5)
 * @param options.mode - set mode (from 0 to 1) (default lin)
 * @param options.dc - set DC (from 0.25 to 4) (default 1)
 * @param options.aa - set anti-aliasing (from 0 to 1) (default 0.5)
 * @param options.samples - set sample reduction (from 1 to 250) (default 1)
 * @param options.lfo - enable LFO (default false)
 * @param options.lforange - set LFO depth (from 1 to 250) (default 20)
 * @param options.lforate - set LFO rate (from 0.01 to 200) (default 0.3)
 * @see https://ffmpeg.org/ffmpeg-filters.html#acrusher
 */
  acrusher(
    options?: {
    level_in?: FFDouble;
    level_out?: FFDouble;
    bits?: FFDouble;
    mix?: FFDouble;
    mode?: FFInt | "lin" | "log";
    dc?: FFDouble;
    aa?: FFDouble;
    samples?: FFDouble;
    lfo?: FFBoolean;
    lforange?: FFDouble;
    lforate?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "acrusher", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "level_in": options?.level_in,
      "level_out": options?.level_out,
      "bits": options?.bits,
      "mix": options?.mix,
      "mode": options?.mode,
      "dc": options?.dc,
      "aa": options?.aa,
      "samples": options?.samples,
      "lfo": options?.lfo,
      "lforange": options?.lforange,
      "lforate": options?.lforate,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Delay filtering to match a cue.

 *
 * @param options.cue - cue unix timestamp in microseconds (from 0 to I64_MAX) (default 0)
 * @param options.preroll - preroll duration in seconds (default 0)
 * @param options.buffer - buffer duration in seconds (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#acue
 */
  acue(
    options?: {
    cue?: FFInt64;
    preroll?: FFDuration;
    buffer?: FFDuration;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "acue", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "cue": options?.cue,
      "preroll": options?.preroll,
      "buffer": options?.buffer,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }








/**
 * Remove impulsive noise from input audio.

 *
 * @param options.window - set window size (from 10 to 100) (default 55)
 * @param options.overlap - set window overlap (from 50 to 95) (default 75)
 * @param options.arorder - set autoregression order (from 0 to 25) (default 2)
 * @param options.threshold - set threshold (from 1 to 100) (default 2)
 * @param options.burst - set burst fusion (from 0 to 10) (default 2)
 * @param options.method - set overlap method (from 0 to 1) (default add)
 * @see https://ffmpeg.org/ffmpeg-filters.html#adeclick
 */
  adeclick(
    options?: {
    window?: FFDouble;
    overlap?: FFDouble;
    arorder?: FFDouble;
    threshold?: FFDouble;
    burst?: FFDouble;
    method?: FFInt | "add" | "a" | "save" | "s";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "adeclick", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "window": options?.window,
      "overlap": options?.overlap,
      "arorder": options?.arorder,
      "threshold": options?.threshold,
      "burst": options?.burst,
      "method": options?.method,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Remove clipping from input audio.

 *
 * @param options.window - set window size (from 10 to 100) (default 55)
 * @param options.overlap - set window overlap (from 50 to 95) (default 75)
 * @param options.arorder - set autoregression order (from 0 to 25) (default 8)
 * @param options.threshold - set threshold (from 1 to 100) (default 10)
 * @param options.hsize - set histogram size (from 100 to 9999) (default 1000)
 * @param options.method - set overlap method (from 0 to 1) (default add)
 * @see https://ffmpeg.org/ffmpeg-filters.html#adeclip
 */
  adeclip(
    options?: {
    window?: FFDouble;
    overlap?: FFDouble;
    arorder?: FFDouble;
    threshold?: FFDouble;
    hsize?: FFInt;
    method?: FFInt | "add" | "a" | "save" | "s";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "adeclip", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "window": options?.window,
      "overlap": options?.overlap,
      "arorder": options?.arorder,
      "threshold": options?.threshold,
      "hsize": options?.hsize,
      "method": options?.method,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply decorrelation to input audio.

 *
 * @param options.stages - set filtering stages (from 1 to 16) (default 6)
 * @param options.seed - set random seed (from -1 to UINT32_MAX) (default -1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#adecorrelate
 */
  adecorrelate(
    options?: {
    stages?: FFInt;
    seed?: FFInt64;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "adecorrelate", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "stages": options?.stages,
      "seed": options?.seed,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Delay one or more audio channels.

 *
 * @param options.delays - set list of delays for each channel
 * @param options.all - use last available delay for remained channels (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#adelay
 */
  adelay(
    options?: {
    delays?: FFString;
    all?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "adelay", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "delays": options?.delays,
      "all": options?.all,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Remedy denormals by adding extremely low-level noise.

 *
 * @param options.level - set level (from -451 to -90) (default -351)
 * @param options._type - set type (from 0 to 3) (default dc)
 * @see https://ffmpeg.org/ffmpeg-filters.html#adenorm
 */
  adenorm(
    options?: {
    level?: FFDouble;
    _type?: FFInt | "dc" | "ac" | "square" | "pulse";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "adenorm", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "level": options?.level,
      "type": options?._type,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Compute derivative of input audio.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#aderivative_002c-aintegral
 */
  aderivative(
    options?: {
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "aderivative", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Draw a graph using input audio metadata.

 *
 * @param options.m1 - set 1st metadata key (default "")
 * @param options.fg1 - set 1st foreground color expression (default "0xffff0000")
 * @param options.m2 - set 2nd metadata key (default "")
 * @param options.fg2 - set 2nd foreground color expression (default "0xff00ff00")
 * @param options.m3 - set 3rd metadata key (default "")
 * @param options.fg3 - set 3rd foreground color expression (default "0xffff00ff")
 * @param options.m4 - set 4th metadata key (default "")
 * @param options.fg4 - set 4th foreground color expression (default "0xffffff00")
 * @param options.bg - set background color (default "white")
 * @param options.min - set minimal value (from INT_MIN to INT_MAX) (default -1)
 * @param options.max - set maximal value (from INT_MIN to INT_MAX) (default 1)
 * @param options.mode - set graph mode (from 0 to 2) (default line)
 * @param options.slide - set slide mode (from 0 to 4) (default frame)
 * @param options.size - set graph size (default "900x256")
 * @param options.rate - set video rate (default "25")
 * @see https://ffmpeg.org/ffmpeg-filters.html#adrawgraph
 */
  adrawgraph(
    options?: {
    m1?: FFString;
    fg1?: FFString;
    m2?: FFString;
    fg2?: FFString;
    m3?: FFString;
    fg3?: FFString;
    m4?: FFString;
    fg4?: FFString;
    bg?: FFColor;
    min?: FFFloat;
    max?: FFFloat;
    mode?: FFInt | "bar" | "dot" | "line";
    slide?: FFInt | "frame" | "replace" | "scroll" | "rscroll" | "picture";
    size?: FFImageSize;
    rate?: FFVideoRate;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "adrawgraph", typingsInput: ["audio"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "m1": options?.m1,
      "fg1": options?.fg1,
      "m2": options?.m2,
      "fg2": options?.fg2,
      "m3": options?.m3,
      "fg3": options?.fg3,
      "m4": options?.m4,
      "fg4": options?.fg4,
      "bg": options?.bg,
      "min": options?.min,
      "max": options?.max,
      "mode": options?.mode,
      "slide": options?.slide,
      "size": options?.size,
      "rate": options?.rate,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Audio Spectral Dynamic Range Controller.

 *
 * @param options.transfer - set the transfer expression (default "p")
 * @param options.attack - set the attack (from 1 to 1000) (default 50)
 * @param options.release - set the release (from 5 to 2000) (default 100)
 * @param options.channels - set channels to filter (default "all")
 * @see https://ffmpeg.org/ffmpeg-filters.html#adrc
 */
  adrc(
    options?: {
    transfer?: FFString;
    attack?: FFDouble;
    release?: FFDouble;
    channels?: FFString;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "adrc", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "transfer": options?.transfer,
      "attack": options?.attack,
      "release": options?.release,
      "channels": options?.channels,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply Dynamic Equalization of input audio.

 *
 * @param options.threshold - set detection threshold (from 0 to 100) (default 0)
 * @param options.dfrequency - set detection frequency (from 2 to 1e+06) (default 1000)
 * @param options.dqfactor - set detection Q factor (from 0.001 to 1000) (default 1)
 * @param options.tfrequency - set target frequency (from 2 to 1e+06) (default 1000)
 * @param options.tqfactor - set target Q factor (from 0.001 to 1000) (default 1)
 * @param options.attack - set detection attack duration (from 0.01 to 2000) (default 20)
 * @param options.release - set detection release duration (from 0.01 to 2000) (default 200)
 * @param options.ratio - set ratio factor (from 0 to 30) (default 1)
 * @param options.makeup - set makeup gain (from 0 to 1000) (default 0)
 * @param options.range - set max gain (from 1 to 2000) (default 50)
 * @param options.mode - set mode (from -1 to 3) (default cutbelow)
 * @param options.dftype - set detection filter type (from 0 to 3) (default bandpass)
 * @param options.tftype - set target filter type (from 0 to 2) (default bell)
 * @param options.auto - set auto threshold (from 1 to 4) (default off)
 * @param options.precision - set processing precision (from 0 to 2) (default auto)
 * @see https://ffmpeg.org/ffmpeg-filters.html#adynamicequalizer
 */
  adynamicequalizer(
    options?: {
    threshold?: FFDouble;
    dfrequency?: FFDouble;
    dqfactor?: FFDouble;
    tfrequency?: FFDouble;
    tqfactor?: FFDouble;
    attack?: FFDouble;
    release?: FFDouble;
    ratio?: FFDouble;
    makeup?: FFDouble;
    range?: FFDouble;
    mode?: FFInt | "listen" | "cutbelow" | "cutabove" | "boostbelow" | "boostabove";
    dftype?: FFInt | "bandpass" | "lowpass" | "highpass" | "peak";
    tftype?: FFInt | "bell" | "lowshelf" | "highshelf";
    auto?: FFInt | "disabled" | "off" | "on" | "adaptive";
    precision?: FFInt | "auto" | "float" | "double";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "adynamicequalizer", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "threshold": options?.threshold,
      "dfrequency": options?.dfrequency,
      "dqfactor": options?.dqfactor,
      "tfrequency": options?.tfrequency,
      "tqfactor": options?.tqfactor,
      "attack": options?.attack,
      "release": options?.release,
      "ratio": options?.ratio,
      "makeup": options?.makeup,
      "range": options?.range,
      "mode": options?.mode,
      "dftype": options?.dftype,
      "tftype": options?.tftype,
      "auto": options?.auto,
      "precision": options?.precision,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply Dynamic Smoothing of input audio.

 *
 * @param options.sensitivity - set smooth sensitivity (from 0 to 1e+06) (default 2)
 * @param options.basefreq - set base frequency (from 2 to 1e+06) (default 22050)
 * @see https://ffmpeg.org/ffmpeg-filters.html#adynamicsmooth
 */
  adynamicsmooth(
    options?: {
    sensitivity?: FFDouble;
    basefreq?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "adynamicsmooth", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "sensitivity": options?.sensitivity,
      "basefreq": options?.basefreq,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Add echoing to the audio.

 *
 * @param options.in_gain - set signal input gain (from 0 to 1) (default 0.6)
 * @param options.out_gain - set signal output gain (from 0 to 1) (default 0.3)
 * @param options.delays - set list of signal delays (default "1000")
 * @param options.decays - set list of signal decays (default "0.5")
 * @see https://ffmpeg.org/ffmpeg-filters.html#aecho
 */
  aecho(
    options?: {
    in_gain?: FFFloat;
    out_gain?: FFFloat;
    delays?: FFString;
    decays?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "aecho", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "in_gain": options?.in_gain,
      "out_gain": options?.out_gain,
      "delays": options?.delays,
      "decays": options?.decays,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Audio emphasis.

 *
 * @param options.level_in - set input gain (from 0 to 64) (default 1)
 * @param options.level_out - set output gain (from 0 to 64) (default 1)
 * @param options.mode - set filter mode (from 0 to 1) (default reproduction)
 * @param options._type - set filter type (from 0 to 8) (default cd)
 * @see https://ffmpeg.org/ffmpeg-filters.html#aemphasis
 */
  aemphasis(
    options?: {
    level_in?: FFDouble;
    level_out?: FFDouble;
    mode?: FFInt | "reproduction" | "production";
    _type?: FFInt | "col" | "emi" | "bsi" | "riaa" | "cd" | "50fm" | "75fm" | "50kf" | "75kf";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "aemphasis", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "level_in": options?.level_in,
      "level_out": options?.level_out,
      "mode": options?.mode,
      "type": options?._type,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Filter audio signal according to a specified expression.

 *
 * @param options.exprs - set the '|'-separated list of channels expressions
 * @param options.channel_layout - set channel layout
 * @see https://ffmpeg.org/ffmpeg-filters.html#aeval
 */
  aeval(
    options?: {
    exprs?: FFString;
    channel_layout?: FFString;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "aeval", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "exprs": options?.exprs,
      "channel_layout": options?.channel_layout,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }








/**
 * Enhance high frequency part of audio.

 *
 * @param options.level_in - set level in (from 0 to 64) (default 1)
 * @param options.level_out - set level out (from 0 to 64) (default 1)
 * @param options.amount - set amount (from 0 to 64) (default 1)
 * @param options.drive - set harmonics (from 0.1 to 10) (default 8.5)
 * @param options.blend - set blend harmonics (from -10 to 10) (default 0)
 * @param options.freq - set scope (from 2000 to 12000) (default 7500)
 * @param options.ceil - set ceiling (from 9999 to 20000) (default 9999)
 * @param options.listen - enable listen mode (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#aexciter
 */
  aexciter(
    options?: {
    level_in?: FFDouble;
    level_out?: FFDouble;
    amount?: FFDouble;
    drive?: FFDouble;
    blend?: FFDouble;
    freq?: FFDouble;
    ceil?: FFDouble;
    listen?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "aexciter", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "level_in": options?.level_in,
      "level_out": options?.level_out,
      "amount": options?.amount,
      "drive": options?.drive,
      "blend": options?.blend,
      "freq": options?.freq,
      "ceil": options?.ceil,
      "listen": options?.listen,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Fade in/out input audio.

 *
 * @param options._type - set the fade direction (from 0 to 1) (default in)
 * @param options.start_sample - set number of first sample to start fading (from 0 to I64_MAX) (default 0)
 * @param options.nb_samples - set number of samples for fade duration (from 1 to I64_MAX) (default 44100)
 * @param options.start_time - set time to start fading (default 0)
 * @param options.duration - set fade duration (default 0)
 * @param options.curve - set fade curve type (from -1 to 22) (default tri)
 * @param options.silence - set the silence gain (from 0 to 1) (default 0)
 * @param options.unity - set the unity gain (from 0 to 1) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#afade
 */
  afade(
    options?: {
    _type?: FFInt | "in" | "out";
    start_sample?: FFInt64;
    nb_samples?: FFInt64;
    start_time?: FFDuration;
    duration?: FFDuration;
    curve?: FFInt | "nofade" | "tri" | "qsin" | "esin" | "hsin" | "log" | "ipar" | "qua" | "cub" | "squ" | "cbr" | "par" | "exp" | "iqsin" | "ihsin" | "dese" | "desi" | "losi" | "sinc" | "isinc" | "quat" | "quatr" | "qsin2" | "hsin2";
    silence?: FFDouble;
    unity?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "afade", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "type": options?._type,
      "start_sample": options?.start_sample,
      "nb_samples": options?.nb_samples,
      "start_time": options?.start_time,
      "duration": options?.duration,
      "curve": options?.curve,
      "silence": options?.silence,
      "unity": options?.unity,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }








/**
 * Denoise audio samples using FFT.

 *
 * @param options.noise_reduction - set the noise reduction (from 0.01 to 97) (default 12)
 * @param options.noise_floor - set the noise floor (from -80 to -20) (default -50)
 * @param options.noise_type - set the noise type (from 0 to 3) (default white)
 * @param options.band_noise - set the custom bands noise
 * @param options.residual_floor - set the residual floor (from -80 to -20) (default -38)
 * @param options.track_noise - track noise (default false)
 * @param options.track_residual - track residual (default false)
 * @param options.output_mode - set output mode (from 0 to 2) (default output)
 * @param options.adaptivity - set adaptivity factor (from 0 to 1) (default 0.5)
 * @param options.floor_offset - set noise floor offset factor (from -2 to 2) (default 1)
 * @param options.noise_link - set the noise floor link (from 0 to 3) (default min)
 * @param options.band_multiplier - set band multiplier (from 0.2 to 5) (default 1.25)
 * @param options.sample_noise - set sample noise mode (from 0 to 2) (default none)
 * @param options.gain_smooth - set gain smooth radius (from 0 to 50) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#afftdn
 */
  afftdn(
    options?: {
    noise_reduction?: FFFloat;
    noise_floor?: FFFloat;
    noise_type?: FFInt | "white" | "w" | "vinyl" | "v" | "shellac" | "s" | "custom" | "c";
    band_noise?: FFString;
    residual_floor?: FFFloat;
    track_noise?: FFBoolean;
    track_residual?: FFBoolean;
    output_mode?: FFInt | "input" | "i" | "output" | "o" | "noise" | "n";
    adaptivity?: FFFloat;
    floor_offset?: FFFloat;
    noise_link?: FFInt | "none" | "min" | "max" | "average";
    band_multiplier?: FFFloat;
    sample_noise?: FFInt | "none" | "start" | "begin" | "stop" | "end";
    gain_smooth?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "afftdn", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "noise_reduction": options?.noise_reduction,
      "noise_floor": options?.noise_floor,
      "noise_type": options?.noise_type,
      "band_noise": options?.band_noise,
      "residual_floor": options?.residual_floor,
      "track_noise": options?.track_noise,
      "track_residual": options?.track_residual,
      "output_mode": options?.output_mode,
      "adaptivity": options?.adaptivity,
      "floor_offset": options?.floor_offset,
      "noise_link": options?.noise_link,
      "band_multiplier": options?.band_multiplier,
      "sample_noise": options?.sample_noise,
      "gain_smooth": options?.gain_smooth,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply arbitrary expressions to samples in frequency domain.

 *
 * @param options.real - set channels real expressions (default "re")
 * @param options.imag - set channels imaginary expressions (default "im")
 * @param options.win_size - set window size (from 16 to 131072) (default 4096)
 * @param options.win_func - set window function (from 0 to 20) (default hann)
 * @param options.overlap - set window overlap (from 0 to 1) (default 0.75)
 * @see https://ffmpeg.org/ffmpeg-filters.html#afftfilt
 */
  afftfilt(
    options?: {
    real?: FFString;
    imag?: FFString;
    win_size?: FFInt;
    win_func?: FFInt | "rect" | "bartlett" | "hann" | "hanning" | "hamming" | "blackman" | "welch" | "flattop" | "bharris" | "bnuttall" | "bhann" | "sine" | "nuttall" | "lanczos" | "gauss" | "tukey" | "dolph" | "cauchy" | "parzen" | "poisson" | "bohman" | "kaiser";
    overlap?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "afftfilt", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "real": options?.real,
      "imag": options?.imag,
      "win_size": options?.win_size,
      "win_func": options?.win_func,
      "overlap": options?.overlap,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }










/**
 * Convert the input audio to one of the specified formats.

 *
 * @param options.sample_fmts - A '|'-separated list of sample formats.
 * @param options.sample_rates - A '|'-separated list of sample rates.
 * @param options.channel_layouts - A '|'-separated list of channel layouts.
 * @see https://ffmpeg.org/ffmpeg-filters.html#aformat
 */
  aformat(
    options?: {
    sample_fmts?: FFSampleFmt;
    sample_rates?: FFInt;
    channel_layouts?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "aformat", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "sample_fmts": options?.sample_fmts,
      "sample_rates": options?.sample_rates,
      "channel_layouts": options?.channel_layouts,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply frequency shifting to input audio.

 *
 * @param options.shift - set frequency shift (from -2.14748e+09 to INT_MAX) (default 0)
 * @param options.level - set output level (from 0 to 1) (default 1)
 * @param options.order - set filter order (from 1 to 16) (default 8)
 * @see https://ffmpeg.org/ffmpeg-filters.html#afreqshift
 */
  afreqshift(
    options?: {
    shift?: FFDouble;
    level?: FFDouble;
    order?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "afreqshift", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "shift": options?.shift,
      "level": options?.level,
      "order": options?.order,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Denoise audio stream using Wavelets.

 *
 * @param options.sigma - set noise sigma (from 0 to 1) (default 0)
 * @param options.levels - set number of wavelet levels (from 1 to 12) (default 10)
 * @param options.wavet - set wavelet type (from 0 to 6) (default sym10)
 * @param options.percent - set percent of full denoising (from 0 to 100) (default 85)
 * @param options.profile - profile noise (default false)
 * @param options.adaptive - adaptive profiling of noise (default false)
 * @param options.samples - set frame size in number of samples (from 512 to 65536) (default 8192)
 * @param options.softness - set thresholding softness (from 0 to 10) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#afwtdn
 */
  afwtdn(
    options?: {
    sigma?: FFDouble;
    levels?: FFInt;
    wavet?: FFInt | "sym2" | "sym4" | "rbior68" | "deb10" | "sym10" | "coif5" | "bl3";
    percent?: FFDouble;
    profile?: FFBoolean;
    adaptive?: FFBoolean;
    samples?: FFInt;
    softness?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "afwtdn", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "sigma": options?.sigma,
      "levels": options?.levels,
      "wavet": options?.wavet,
      "percent": options?.percent,
      "profile": options?.profile,
      "adaptive": options?.adaptive,
      "samples": options?.samples,
      "softness": options?.softness,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Audio gate.

 *
 * @param options.level_in - set input level (from 0.015625 to 64) (default 1)
 * @param options.mode - set mode (from 0 to 1) (default downward)
 * @param options.range - set max gain reduction (from 0 to 1) (default 0.06125)
 * @param options.threshold - set threshold (from 0 to 1) (default 0.125)
 * @param options.ratio - set ratio (from 1 to 9000) (default 2)
 * @param options.attack - set attack (from 0.01 to 9000) (default 20)
 * @param options.release - set release (from 0.01 to 9000) (default 250)
 * @param options.makeup - set makeup gain (from 1 to 64) (default 1)
 * @param options.knee - set knee (from 1 to 8) (default 2.82843)
 * @param options.detection - set detection (from 0 to 1) (default rms)
 * @param options.link - set link (from 0 to 1) (default average)
 * @param options.level_sc - set sidechain gain (from 0.015625 to 64) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#agate
 */
  agate(
    options?: {
    level_in?: FFDouble;
    mode?: FFInt | "downward" | "upward";
    range?: FFDouble;
    threshold?: FFDouble;
    ratio?: FFDouble;
    attack?: FFDouble;
    release?: FFDouble;
    makeup?: FFDouble;
    knee?: FFDouble;
    detection?: FFInt | "peak" | "rms";
    link?: FFInt | "average" | "maximum";
    level_sc?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "agate", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "level_in": options?.level_in,
      "mode": options?.mode,
      "range": options?.range,
      "threshold": options?.threshold,
      "ratio": options?.ratio,
      "attack": options?.attack,
      "release": options?.release,
      "makeup": options?.makeup,
      "knee": options?.knee,
      "detection": options?.detection,
      "link": options?.link,
      "level_sc": options?.level_sc,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Show various filtergraph stats.

 *
 * @param options.size - set monitor size (default "hd720")
 * @param options.opacity - set video opacity (from 0 to 1) (default 0.9)
 * @param options.mode - set mode (default 0)
 * @param options.flags - set flags (default all+queue)
 * @param options.rate - set video rate (default "25")
 * @see https://ffmpeg.org/ffmpeg-filters.html#agraphmonitor
 */
  agraphmonitor(
    options?: {
    size?: FFImageSize;
    opacity?: FFFloat;
    mode?: FFFlags | "full" | "compact" | "nozero" | "noeof" | "nodisabled";
    flags?: FFFlags | "none" | "all" | "queue" | "frame_count_in" | "frame_count_out" | "frame_count_delta" | "pts" | "pts_delta" | "time" | "time_delta" | "timebase" | "format" | "size" | "rate" | "eof" | "sample_count_in" | "sample_count_out" | "sample_count_delta" | "disabled";
    rate?: FFVideoRate;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "agraphmonitor", typingsInput: ["audio"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "size": options?.size,
      "opacity": options?.opacity,
      "mode": options?.mode,
      "flags": options?.flags,
      "rate": options?.rate,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Convert input audio to histogram video output.

 *
 * @param options.dmode - set method to display channels (from 0 to 1) (default single)
 * @param options.rate - set video rate (default "25")
 * @param options.size - set video size (default "hd720")
 * @param options.scale - set display scale (from 0 to 4) (default log)
 * @param options.ascale - set amplitude scale (from 0 to 1) (default log)
 * @param options.acount - how much frames to accumulate (from -1 to 100) (default 1)
 * @param options.rheight - set histogram ratio of window height (from 0 to 1) (default 0.1)
 * @param options.slide - set sonogram sliding (from 0 to 1) (default replace)
 * @param options.hmode - set histograms mode (from 0 to 1) (default abs)
 * @see https://ffmpeg.org/ffmpeg-filters.html#ahistogram
 */
  ahistogram(
    options?: {
    dmode?: FFInt | "single" | "separate";
    rate?: FFVideoRate;
    size?: FFImageSize;
    scale?: FFInt | "log" | "sqrt" | "cbrt" | "lin" | "rlog";
    ascale?: FFInt | "log" | "lin";
    acount?: FFInt;
    rheight?: FFFloat;
    slide?: FFInt | "replace" | "scroll";
    hmode?: FFInt | "abs" | "sign";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "ahistogram", typingsInput: ["audio"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "dmode": options?.dmode,
      "rate": options?.rate,
      "size": options?.size,
      "scale": options?.scale,
      "ascale": options?.ascale,
      "acount": options?.acount,
      "rheight": options?.rheight,
      "slide": options?.slide,
      "hmode": options?.hmode,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply Infinite Impulse Response filter with supplied coefficients.

 *
 * @param options.zeros - set B/numerator/zeros/reflection coefficients (default "1+0i 1-0i")
 * @param options.poles - set A/denominator/poles/ladder coefficients (default "1+0i 1-0i")
 * @param options.gains - set channels gains (default "1|1")
 * @param options.dry - set dry gain (from 0 to 1) (default 1)
 * @param options.wet - set wet gain (from 0 to 1) (default 1)
 * @param options.format - set coefficients format (from -2 to 4) (default zp)
 * @param options.process - set kind of processing (from 0 to 2) (default s)
 * @param options.precision - set filtering precision (from 0 to 3) (default dbl)
 * @param options.e - set precision (from 0 to 3) (default dbl)
 * @param options.normalize - normalize coefficients (default true)
 * @param options.mix - set mix (from 0 to 1) (default 1)
 * @param options.response - show IR frequency response (default false)
 * @param options.channel - set IR channel to display frequency response (from 0 to 1024) (default 0)
 * @param options.size - set video size (default "hd720")
 * @param options.rate - set video rate (default "25")
 * @see https://ffmpeg.org/ffmpeg-filters.html#aiir
 */
  aiir(
    options?: {
    zeros?: FFString;
    poles?: FFString;
    gains?: FFString;
    dry?: FFDouble;
    wet?: FFDouble;
    format?: FFInt | "ll" | "sf" | "tf" | "zp" | "pr" | "pd" | "sp";
    process?: FFInt | "d" | "s" | "p";
    precision?: FFInt | "dbl" | "flt" | "i32" | "i16";
    e?: FFInt | "dbl" | "flt" | "i32" | "i16";
    normalize?: FFBoolean;
    mix?: FFDouble;
    response?: FFBoolean;
    channel?: FFInt;
    size?: FFImageSize;
    rate?: FFVideoRate;
extraOptions?: Record<string, unknown>;
    },
  ): FilterNode {
    const filterNode = filterNodeFactory(
      { name: "aiir", typingsInput: ["audio"], typingsOutput: [] },
      [this],
      merge(
    {
      "zeros": options?.zeros,
      "poles": options?.poles,
      "gains": options?.gains,
      "dry": options?.dry,
      "wet": options?.wet,
      "format": options?.format,
      "process": options?.process,
      "precision": options?.precision,
      "e": options?.e,
      "normalize": options?.normalize,
      "mix": options?.mix,
      "response": options?.response,
      "channel": options?.channel,
      "size": options?.size,
      "rate": options?.rate,
},
    options?.extraOptions,
  ),
    );
return filterNode;
  }






/**
 * Compute integral of input audio.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#aderivative_002c-aintegral
 */
  aintegral(
    options?: {
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "aintegral", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }








/**
 * Report audio filtering latency.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#latency_002c-alatency
 */
  alatency(
    options?: {
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "alatency", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Audio lookahead limiter.

 *
 * @param options.level_in - set input level (from 0.015625 to 64) (default 1)
 * @param options.level_out - set output level (from 0.015625 to 64) (default 1)
 * @param options.limit - set limit (from 0.0625 to 1) (default 1)
 * @param options.attack - set attack (from 0.1 to 80) (default 5)
 * @param options.release - set release (from 1 to 8000) (default 50)
 * @param options.asc - enable asc (default false)
 * @param options.asc_level - set asc level (from 0 to 1) (default 0.5)
 * @param options.level - auto level (default true)
 * @param options.latency - compensate delay (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#alimiter
 */
  alimiter(
    options?: {
    level_in?: FFDouble;
    level_out?: FFDouble;
    limit?: FFDouble;
    attack?: FFDouble;
    release?: FFDouble;
    asc?: FFBoolean;
    asc_level?: FFDouble;
    level?: FFBoolean;
    latency?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "alimiter", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "level_in": options?.level_in,
      "level_out": options?.level_out,
      "limit": options?.limit,
      "attack": options?.attack,
      "release": options?.release,
      "asc": options?.asc,
      "asc_level": options?.asc_level,
      "level": options?.level,
      "latency": options?.latency,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply a two-pole all-pass filter.

 *
 * @param options.frequency - set central frequency (from 0 to 999999) (default 3000)
 * @param options.width_type - set filter-width type (from 1 to 5) (default q)
 * @param options.width - set width (from 0 to 99999) (default 0.707)
 * @param options.mix - set mix (from 0 to 1) (default 1)
 * @param options.channels - set channels to filter (default "all")
 * @param options.normalize - normalize coefficients (default false)
 * @param options.order - set filter order (from 1 to 2) (default 2)
 * @param options.transform - set transform type (from 0 to 6) (default di)
 * @param options.precision - set filtering precision (from -1 to 3) (default auto)
 * @see https://ffmpeg.org/ffmpeg-filters.html#allpass
 */
  allpass(
    options?: {
    frequency?: FFDouble;
    width_type?: FFInt | "h" | "q" | "o" | "s" | "k";
    width?: FFDouble;
    mix?: FFDouble;
    channels?: FFString;
    normalize?: FFBoolean;
    order?: FFInt;
    transform?: FFInt | "di" | "dii" | "tdi" | "tdii" | "latt" | "svf" | "zdf";
    precision?: FFInt | "auto" | "s16" | "s32" | "f32" | "f64";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "allpass", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "frequency": options?.frequency,
      "width_type": options?.width_type,
      "width": options?.width,
      "mix": options?.mix,
      "channels": options?.channels,
      "normalize": options?.normalize,
      "order": options?.order,
      "transform": options?.transform,
      "precision": options?.precision,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }










/**
 * Loop audio samples.

 *
 * @param options.loop - number of loops (from -1 to INT_MAX) (default 0)
 * @param options.size - max number of samples to loop (from 0 to INT_MAX) (default 0)
 * @param options.start - set the loop start sample (from -1 to I64_MAX) (default 0)
 * @param options.time - set the loop start time (default INT64_MAX)
 * @see https://ffmpeg.org/ffmpeg-filters.html#aloop
 */
  aloop(
    options?: {
    loop?: FFInt;
    size?: FFInt64;
    start?: FFInt64;
    time?: FFDuration;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "aloop", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "loop": options?.loop,
      "size": options?.size,
      "start": options?.start,
      "time": options?.time,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }












/**
 * Manipulate audio frame metadata.

 *
 * @param options.mode - set a mode of operation (from 0 to 4) (default select)
 * @param options.key - set metadata key
 * @param options.value - set metadata value
 * @param options._function - function for comparing values (from 0 to 6) (default same_str)
 * @param options.expr - set expression for expr function
 * @param options.file - set file where to print metadata information
 * @param options.direct - reduce buffering when printing to user-set file or pipe (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#metadata_002c-ametadata
 */
  ametadata(
    options?: {
    mode?: FFInt | "select" | "add" | "modify" | "delete" | "print";
    key?: FFString;
    value?: FFString;
    _function?: FFInt | "same_str" | "starts_with" | "less" | "equal" | "greater" | "expr" | "ends_with";
    expr?: FFString;
    file?: FFString;
    direct?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "ametadata", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "mode": options?.mode,
      "key": options?.key,
      "value": options?.value,
      "function": options?._function,
      "expr": options?.expr,
      "file": options?.file,
      "direct": options?.direct,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }












/**
 * Multiply two audio streams.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#amultiply
 */
  amultiply(
    _multiply1: AudioStream,

    options?: {
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "amultiply", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
      [this, _multiply1],
      merge(
    {
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply high-order audio parametric multi band equalizer.

 *
 * @param options.params - (default "")
 * @param options.curves - draw frequency response curves (default false)
 * @param options.size - set video size (default "hd720")
 * @param options.mgain - set max gain (from -900 to 900) (default 60)
 * @param options.fscale - set frequency scale (from 0 to 1) (default log)
 * @param options.colors - set channels curves colors (default "red|green|blue|yellow|orange|lime|pink|magenta|brown")
 * @see https://ffmpeg.org/ffmpeg-filters.html#anequalizer
 */
  anequalizer(
    options?: {
    params?: FFString;
    curves?: FFBoolean;
    size?: FFImageSize;
    mgain?: FFDouble;
    fscale?: FFInt | "lin" | "log";
    colors?: FFString;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): FilterNode {
    const filterNode = filterNodeFactory(
      { name: "anequalizer", typingsInput: ["audio"], typingsOutput: [] },
      [this],
      merge(
    {
      "params": options?.params,
      "curves": options?.curves,
      "size": options?.size,
      "mgain": options?.mgain,
      "fscale": options?.fscale,
      "colors": options?.colors,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode;
  }






/**
 * Reduce broadband noise from stream using Non-Local Means.

 *
 * @param options.strength - set denoising strength (from 1e-05 to 10000) (default 1e-05)
 * @param options.patch - set patch duration (default 0.002)
 * @param options.research - set research duration (default 0.006)
 * @param options.output - set output mode (from 0 to 2) (default o)
 * @param options.smooth - set smooth factor (from 1 to 1000) (default 11)
 * @see https://ffmpeg.org/ffmpeg-filters.html#anlmdn
 */
  anlmdn(
    options?: {
    strength?: FFFloat;
    patch?: FFDuration;
    research?: FFDuration;
    output?: FFInt | "i" | "o" | "n";
    smooth?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "anlmdn", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "strength": options?.strength,
      "patch": options?.patch,
      "research": options?.research,
      "output": options?.output,
      "smooth": options?.smooth,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply Normalized Least-Mean-Fourth algorithm to first audio stream.

 *
 * @param options.order - set the filter order (from 1 to 32767) (default 256)
 * @param options.mu - set the filter mu (from 0 to 2) (default 0.75)
 * @param options.eps - set the filter eps (from 0 to 1) (default 1)
 * @param options.leakage - set the filter leakage (from 0 to 1) (default 0)
 * @param options.out_mode - set output mode (from 0 to 4) (default o)
 * @param options.precision - set processing precision (from 0 to 2) (default auto)
 * @see https://ffmpeg.org/ffmpeg-filters.html#anlmf_002c-anlms
 */
  anlmf(
    _desired: AudioStream,

    options?: {
    order?: FFInt;
    mu?: FFFloat;
    eps?: FFFloat;
    leakage?: FFFloat;
    out_mode?: FFInt | "i" | "d" | "o" | "n" | "e";
    precision?: FFInt | "auto" | "float" | "double";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "anlmf", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
      [this, _desired],
      merge(
    {
      "order": options?.order,
      "mu": options?.mu,
      "eps": options?.eps,
      "leakage": options?.leakage,
      "out_mode": options?.out_mode,
      "precision": options?.precision,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply Normalized Least-Mean-Squares algorithm to first audio stream.

 *
 * @param options.order - set the filter order (from 1 to 32767) (default 256)
 * @param options.mu - set the filter mu (from 0 to 2) (default 0.75)
 * @param options.eps - set the filter eps (from 0 to 1) (default 1)
 * @param options.leakage - set the filter leakage (from 0 to 1) (default 0)
 * @param options.out_mode - set output mode (from 0 to 4) (default o)
 * @param options.precision - set processing precision (from 0 to 2) (default auto)
 * @see https://ffmpeg.org/ffmpeg-filters.html#anlmf_002c-anlms
 */
  anlms(
    _desired: AudioStream,

    options?: {
    order?: FFInt;
    mu?: FFFloat;
    eps?: FFFloat;
    leakage?: FFFloat;
    out_mode?: FFInt | "i" | "d" | "o" | "n" | "e";
    precision?: FFInt | "auto" | "float" | "double";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "anlms", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
      [this, _desired],
      merge(
    {
      "order": options?.order,
      "mu": options?.mu,
      "eps": options?.eps,
      "leakage": options?.leakage,
      "out_mode": options?.out_mode,
      "precision": options?.precision,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }








/**
 * Pass the source unchanged to the output.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#anull
 */
  anull(
    options?: {
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "anull", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }










/**
 * Pad audio with silence.

 *
 * @param options.packet_size - set silence packet size (from 0 to INT_MAX) (default 4096)
 * @param options.pad_len - set number of samples of silence to add (from -1 to I64_MAX) (default -1)
 * @param options.whole_len - set minimum target number of samples in the audio stream (from -1 to I64_MAX) (default -1)
 * @param options.pad_dur - set duration of silence to add (default -0.000001)
 * @param options.whole_dur - set minimum target duration in the audio stream (default -0.000001)
 * @see https://ffmpeg.org/ffmpeg-filters.html#apad
 */
  apad(
    options?: {
    packet_size?: FFInt;
    pad_len?: FFInt64;
    whole_len?: FFInt64;
    pad_dur?: FFDuration;
    whole_dur?: FFDuration;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "apad", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "packet_size": options?.packet_size,
      "pad_len": options?.pad_len,
      "whole_len": options?.whole_len,
      "pad_dur": options?.pad_dur,
      "whole_dur": options?.whole_dur,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Set permissions for the output audio frame.

 *
 * @param options.mode - select permissions mode (from 0 to 4) (default none)
 * @param options.seed - set the seed for the random mode (from -1 to UINT32_MAX) (default -1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#perms_002c-aperms
 */
  aperms(
    options?: {
    mode?: FFInt | "none" | "ro" | "rw" | "toggle" | "random";
    seed?: FFInt64;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "aperms", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "mode": options?.mode,
      "seed": options?.seed,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Convert input audio to phase meter video output.

 *
 * @param options.rate - set video rate (default "25")
 * @param options.size - set video size (default "800x400")
 * @param options.rc - set red contrast (from 0 to 255) (default 2)
 * @param options.gc - set green contrast (from 0 to 255) (default 7)
 * @param options.bc - set blue contrast (from 0 to 255) (default 1)
 * @param options.mpc - set median phase color (default "none")
 * @param options.video - set video output (default true)
 * @param options.phasing - set mono and out-of-phase detection output (default false)
 * @param options.tolerance - set phase tolerance for mono detection (from 0 to 1) (default 0)
 * @param options.angle - set angle threshold for out-of-phase detection (from 90 to 180) (default 170)
 * @param options.duration - set minimum mono or out-of-phase duration in seconds (default 2)
 * @see https://ffmpeg.org/ffmpeg-filters.html#aphasemeter
 */
  aphasemeter(
    options?: {
    rate?: FFVideoRate;
    size?: FFImageSize;
    rc?: FFInt;
    gc?: FFInt;
    bc?: FFInt;
    mpc?: FFString;
    video?: FFBoolean;
    phasing?: FFBoolean;
    tolerance?: FFFloat;
    angle?: FFFloat;
    duration?: FFDuration;
extraOptions?: Record<string, unknown>;
    },
  ): FilterNode {
    const filterNode = filterNodeFactory(
      { name: "aphasemeter", typingsInput: ["audio"], typingsOutput: [] },
      [this],
      merge(
    {
      "rate": options?.rate,
      "size": options?.size,
      "rc": options?.rc,
      "gc": options?.gc,
      "bc": options?.bc,
      "mpc": options?.mpc,
      "video": options?.video,
      "phasing": options?.phasing,
      "tolerance": options?.tolerance,
      "angle": options?.angle,
      "duration": options?.duration,
},
    options?.extraOptions,
  ),
    );
return filterNode;
  }






/**
 * Add a phasing effect to the audio.

 *
 * @param options.in_gain - set input gain (from 0 to 1) (default 0.4)
 * @param options.out_gain - set output gain (from 0 to 1e+09) (default 0.74)
 * @param options.delay - set delay in milliseconds (from 0 to 5) (default 3)
 * @param options.decay - set decay (from 0 to 0.99) (default 0.4)
 * @param options.speed - set modulation speed (from 0.1 to 2) (default 0.5)
 * @param options._type - set modulation type (from 0 to 1) (default triangular)
 * @see https://ffmpeg.org/ffmpeg-filters.html#aphaser
 */
  aphaser(
    options?: {
    in_gain?: FFDouble;
    out_gain?: FFDouble;
    delay?: FFDouble;
    decay?: FFDouble;
    speed?: FFDouble;
    _type?: FFInt | "triangular" | "t" | "sinusoidal" | "s";
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "aphaser", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "in_gain": options?.in_gain,
      "out_gain": options?.out_gain,
      "delay": options?.delay,
      "decay": options?.decay,
      "speed": options?.speed,
      "type": options?._type,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply phase shifting to input audio.

 *
 * @param options.shift - set phase shift (from -1 to 1) (default 0)
 * @param options.level - set output level (from 0 to 1) (default 1)
 * @param options.order - set filter order (from 1 to 16) (default 8)
 * @see https://ffmpeg.org/ffmpeg-filters.html#aphaseshift
 */
  aphaseshift(
    options?: {
    shift?: FFDouble;
    level?: FFDouble;
    order?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "aphaseshift", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "shift": options?.shift,
      "level": options?.level,
      "order": options?.order,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Measure Audio Peak Signal-to-Noise Ratio.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#apsnr
 */
  apsnr(
    _input1: AudioStream,

    options?: {
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "apsnr", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
      [this, _input1],
      merge(
    {
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Audio Psychoacoustic Clipper.

 *
 * @param options.level_in - set input level (from 0.015625 to 64) (default 1)
 * @param options.level_out - set output level (from 0.015625 to 64) (default 1)
 * @param options.clip - set clip level (from 0.015625 to 1) (default 1)
 * @param options.diff - enable difference (default false)
 * @param options.adaptive - set adaptive distortion (from 0 to 1) (default 0.5)
 * @param options.iterations - set iterations (from 1 to 20) (default 10)
 * @param options.level - set auto level (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#apsyclip
 */
  apsyclip(
    options?: {
    level_in?: FFDouble;
    level_out?: FFDouble;
    clip?: FFDouble;
    diff?: FFBoolean;
    adaptive?: FFDouble;
    iterations?: FFInt;
    level?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "apsyclip", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "level_in": options?.level_in,
      "level_out": options?.level_out,
      "clip": options?.clip,
      "diff": options?.diff,
      "adaptive": options?.adaptive,
      "iterations": options?.iterations,
      "level": options?.level,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Audio pulsator.

 *
 * @param options.level_in - set input gain (from 0.015625 to 64) (default 1)
 * @param options.level_out - set output gain (from 0.015625 to 64) (default 1)
 * @param options.mode - set mode (from 0 to 4) (default sine)
 * @param options.amount - set modulation (from 0 to 1) (default 1)
 * @param options.offset_l - set offset L (from 0 to 1) (default 0)
 * @param options.offset_r - set offset R (from 0 to 1) (default 0.5)
 * @param options.width - set pulse width (from 0 to 2) (default 1)
 * @param options.timing - set timing (from 0 to 2) (default hz)
 * @param options.bpm - set BPM (from 30 to 300) (default 120)
 * @param options.ms - set ms (from 10 to 2000) (default 500)
 * @param options.hz - set frequency (from 0.01 to 100) (default 2)
 * @see https://ffmpeg.org/ffmpeg-filters.html#apulsator
 */
  apulsator(
    options?: {
    level_in?: FFDouble;
    level_out?: FFDouble;
    mode?: FFInt | "sine" | "triangle" | "square" | "sawup" | "sawdown";
    amount?: FFDouble;
    offset_l?: FFDouble;
    offset_r?: FFDouble;
    width?: FFDouble;
    timing?: FFInt | "bpm" | "ms" | "hz";
    bpm?: FFDouble;
    ms?: FFInt;
    hz?: FFDouble;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "apulsator", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "level_in": options?.level_in,
      "level_out": options?.level_out,
      "mode": options?.mode,
      "amount": options?.amount,
      "offset_l": options?.offset_l,
      "offset_r": options?.offset_r,
      "width": options?.width,
      "timing": options?.timing,
      "bpm": options?.bpm,
      "ms": options?.ms,
      "hz": options?.hz,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Slow down filtering to match realtime.

 *
 * @param options.limit - sleep time limit (default 2)
 * @param options.speed - speed factor (from DBL_MIN to DBL_MAX) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#realtime_002c-arealtime
 */
  arealtime(
    options?: {
    limit?: FFDuration;
    speed?: FFDouble;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "arealtime", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "limit": options?.limit,
      "speed": options?.speed,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Resample audio data.

 *
 * @param options.sample_rate - (from 0 to INT_MAX) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#aresample
 */
  aresample(
    options?: {
    sample_rate?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "aresample", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "sample_rate": options?.sample_rate,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Reverse an audio clip.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#areverse
 */
  areverse(
    options?: {
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "areverse", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply Recursive Least Squares algorithm to first audio stream.

 *
 * @param options.order - set the filter order (from 1 to 32767) (default 16)
 * @param options._lambda - set the filter lambda (from 0 to 1) (default 1)
 * @param options.delta - set the filter delta (from 0 to 32767) (default 2)
 * @param options.out_mode - set output mode (from 0 to 4) (default o)
 * @param options.precision - set processing precision (from 0 to 2) (default auto)
 * @see https://ffmpeg.org/ffmpeg-filters.html#arls
 */
  arls(
    _desired: AudioStream,

    options?: {
    order?: FFInt;
    _lambda?: FFFloat;
    delta?: FFFloat;
    out_mode?: FFInt | "i" | "d" | "o" | "n" | "e";
    precision?: FFInt | "auto" | "float" | "double";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "arls", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
      [this, _desired],
      merge(
    {
      "order": options?.order,
      "lambda": options?._lambda,
      "delta": options?.delta,
      "out_mode": options?.out_mode,
      "precision": options?.precision,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Reduce noise from speech using Recurrent Neural Networks.

 *
 * @param options.model - set model name
 * @param options.mix - set output vs input mix (from -1 to 1) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#arnndn
 */
  arnndn(
    options?: {
    model?: FFString;
    mix?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "arnndn", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "model": options?.model,
      "mix": options?.mix,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Measure Audio Signal-to-Distortion Ratio.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#asdr
 */
  asdr(
    _input1: AudioStream,

    options?: {
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "asdr", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
      [this, _input1],
      merge(
    {
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Segment audio stream.

 *
 * @param options.timestamps - timestamps of input at which to split input
 * @param options.samples - samples at which to split input
 * @see https://ffmpeg.org/ffmpeg-filters.html#segment_002c-asegment
 */
  asegment(
    options?: {
    timestamps?: FFString;
    samples?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): FilterNode {
    const filterNode = filterNodeFactory(
      { name: "asegment", typingsInput: ["audio"], typingsOutput: [] },
      [this],
      merge(
    {
      "timestamps": options?.timestamps,
      "samples": options?.samples,
},
    options?.extraOptions,
  ),
    );
return filterNode;
  }






/**
 * Select audio frames to pass in output.

 *
 * @param options.expr - set an expression to use for selecting frames (default "1")
 * @param options.outputs - set the number of outputs (from 1 to INT_MAX) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#select_002c-aselect
 */
  aselect(
    options?: {
    expr?: FFString;
    outputs?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): FilterNode {
    const filterNode = filterNodeFactory(
      { name: "aselect", typingsInput: ["audio"], typingsOutput: [] },
      [this],
      merge(
    {
      "expr": options?.expr,
      "outputs": options?.outputs,
},
    options?.extraOptions,
  ),
    );
return filterNode;
  }






/**
 * Send commands to filters.

 *
 * @param options.commands - set commands
 * @param options.filename - set commands file
 * @see https://ffmpeg.org/ffmpeg-filters.html#sendcmd_002c-asendcmd
 */
  asendcmd(
    options?: {
    commands?: FFString;
    filename?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "asendcmd", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "commands": options?.commands,
      "filename": options?.filename,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Set the number of samples for each output audio frames.

 *
 * @param options.nb_out_samples - set the number of per-frame output samples (from 1 to INT_MAX) (default 1024)
 * @param options.pad - pad last frame with zeros (default true)
 * @see https://ffmpeg.org/ffmpeg-filters.html#asetnsamples
 */
  asetnsamples(
    options?: {
    nb_out_samples?: FFInt;
    pad?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "asetnsamples", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "nb_out_samples": options?.nb_out_samples,
      "pad": options?.pad,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Set PTS for the output audio frame.

 *
 * @param options.expr - Expression determining the frame timestamp (default "PTS")
 * @see https://ffmpeg.org/ffmpeg-filters.html#setpts_002c-asetpts
 */
  asetpts(
    options?: {
    expr?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "asetpts", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "expr": options?.expr,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Change the sample rate without altering the data.

 *
 * @param options.sample_rate - set the sample rate (from 1 to INT_MAX) (default 44100)
 * @see https://ffmpeg.org/ffmpeg-filters.html#asetrate
 */
  asetrate(
    options?: {
    sample_rate?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "asetrate", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "sample_rate": options?.sample_rate,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Set timebase for the audio output link.

 *
 * @param options.expr - set expression determining the output timebase (default "intb")
 * @see https://ffmpeg.org/ffmpeg-filters.html#settb_002c-asettb
 */
  asettb(
    options?: {
    expr?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "asettb", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "expr": options?.expr,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Show textual information for each audio frame.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#ashowinfo
 */
  ashowinfo(
    options?: {
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "ashowinfo", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Manipulate audio frame side data.

 *
 * @param options.mode - set a mode of operation (from 0 to 1) (default select)
 * @param options._type - set side data type (from -1 to INT_MAX) (default -1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#sidedata_002c-asidedata
 */
  asidedata(
    options?: {
    mode?: FFInt | "select" | "delete";
    _type?: FFInt | "PANSCAN" | "A53_CC" | "STEREO3D" | "MATRIXENCODING" | "DOWNMIX_INFO" | "REPLAYGAIN" | "DISPLAYMATRIX" | "AFD" | "MOTION_VECTORS" | "SKIP_SAMPLES" | "AUDIO_SERVICE_TYPE" | "MASTERING_DISPLAY_METADATA" | "GOP_TIMECODE" | "SPHERICAL" | "CONTENT_LIGHT_LEVEL" | "ICC_PROFILE" | "S12M_TIMECOD" | "S12M_TIMECODE" | "DYNAMIC_HDR_PLUS" | "REGIONS_OF_INTEREST" | "VIDEO_ENC_PARAMS" | "SEI_UNREGISTERED" | "FILM_GRAIN_PARAMS" | "DETECTION_BOUNDING_BOXES" | "DETECTION_BBOXES" | "DOVI_RPU_BUFFER" | "DOVI_METADATA" | "DYNAMIC_HDR_VIVID" | "AMBIENT_VIEWING_ENVIRONMENT" | "VIDEO_HINT";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "asidedata", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "mode": options?.mode,
      "type": options?._type,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Measure Audio Scale-Invariant Signal-to-Distortion Ratio.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#asisdr
 */
  asisdr(
    _input1: AudioStream,

    options?: {
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "asisdr", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
      [this, _input1],
      merge(
    {
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Audio Soft Clipper.

 *
 * @param options._type - set softclip type (from -1 to 7) (default tanh)
 * @param options.threshold - set softclip threshold (from 1e-06 to 1) (default 1)
 * @param options.output - set softclip output gain (from 1e-06 to 16) (default 1)
 * @param options.param - set softclip parameter (from 0.01 to 3) (default 1)
 * @param options.oversample - set oversample factor (from 1 to 64) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#asoftclip
 */
  asoftclip(
    options?: {
    _type?: FFInt | "hard" | "tanh" | "atan" | "cubic" | "exp" | "alg" | "quintic" | "sin" | "erf";
    threshold?: FFDouble;
    output?: FFDouble;
    param?: FFDouble;
    oversample?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "asoftclip", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "type": options?._type,
      "threshold": options?.threshold,
      "output": options?.output,
      "param": options?.param,
      "oversample": options?.oversample,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Show frequency domain statistics about audio frames.

 *
 * @param options.win_size - set the window size (from 32 to 65536) (default 2048)
 * @param options.win_func - set window function (from 0 to 20) (default hann)
 * @param options.overlap - set window overlap (from 0 to 1) (default 0.5)
 * @param options.measure - select the parameters which are measured (default all+mean+variance+centroid+spread+skewness+kurtosis+entropy+flatness+crest+flux+slope+decrease+rolloff)
 * @see https://ffmpeg.org/ffmpeg-filters.html#aspectralstats
 */
  aspectralstats(
    options?: {
    win_size?: FFInt;
    win_func?: FFInt | "rect" | "bartlett" | "hann" | "hanning" | "hamming" | "blackman" | "welch" | "flattop" | "bharris" | "bnuttall" | "bhann" | "sine" | "nuttall" | "lanczos" | "gauss" | "tukey" | "dolph" | "cauchy" | "parzen" | "poisson" | "bohman" | "kaiser";
    overlap?: FFFloat;
    measure?: FFFlags | "none" | "all" | "mean" | "variance" | "centroid" | "spread" | "skewness" | "kurtosis" | "entropy" | "flatness" | "crest" | "flux" | "slope" | "decrease" | "rolloff";
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "aspectralstats", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "win_size": options?.win_size,
      "win_func": options?.win_func,
      "overlap": options?.overlap,
      "measure": options?.measure,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Pass on the audio input to N audio outputs.

 *
 * @param options.outputs - set number of outputs (from 1 to INT_MAX) (default 2)
 * @see https://ffmpeg.org/ffmpeg-filters.html#split_002c-asplit
 */
  asplit(
    options?: {
    outputs?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): FilterNode {
    const filterNode = filterNodeFactory(
      { name: "asplit", typingsInput: ["audio"], typingsOutput: [] },
      [this],
      merge(
    {
      "outputs": options?.outputs,
},
    options?.extraOptions,
  ),
    );
return filterNode;
  }






/**
 * Show time domain statistics about audio frames.

 *
 * @param options.length - set the window length (from 0 to 10) (default 0.05)
 * @param options.metadata - inject metadata in the filtergraph (default false)
 * @param options.reset - Set the number of frames over which cumulative stats are calculated before being reset (from 0 to INT_MAX) (default 0)
 * @param options.measure_perchannel - Select the parameters which are measured per channel (default all+Bit_depth+Crest_factor+DC_offset+Dynamic_range+Entropy+Flat_factor+Max_difference+Max_level+Mean_difference+Min_difference+Min_level+Noise_floor+Noise_floor_count+Number_of_Infs+Number_of_NaNs+Number_of_denormals+Number_of_samples+Peak_count+Peak_level+RMS_difference+RMS_level+RMS_peak+RMS_trough+Zero_crossings+Zero_crossings_rate+Abs_Peak_count)
 * @param options.measure_overall - Select the parameters which are measured overall (default all+Bit_depth+Crest_factor+DC_offset+Dynamic_range+Entropy+Flat_factor+Max_difference+Max_level+Mean_difference+Min_difference+Min_level+Noise_floor+Noise_floor_count+Number_of_Infs+Number_of_NaNs+Number_of_denormals+Number_of_samples+Peak_count+Peak_level+RMS_difference+RMS_level+RMS_peak+RMS_trough+Zero_crossings+Zero_crossings_rate+Abs_Peak_count)
 * @see https://ffmpeg.org/ffmpeg-filters.html#astats
 */
  astats(
    options?: {
    length?: FFDouble;
    metadata?: FFBoolean;
    reset?: FFInt;
    measure_perchannel?: FFFlags | "none" | "all" | "Bit_depth" | "Crest_factor" | "DC_offset" | "Dynamic_range" | "Entropy" | "Flat_factor" | "Max_difference" | "Max_level" | "Mean_difference" | "Min_difference" | "Min_level" | "Noise_floor" | "Noise_floor_count" | "Number_of_Infs" | "Number_of_NaNs" | "Number_of_denormals" | "Number_of_samples" | "Peak_count" | "Peak_level" | "RMS_difference" | "RMS_level" | "RMS_peak" | "RMS_trough" | "Zero_crossings" | "Zero_crossings_rate" | "Abs_Peak_count";
    measure_overall?: FFFlags | "none" | "all" | "Bit_depth" | "Crest_factor" | "DC_offset" | "Dynamic_range" | "Entropy" | "Flat_factor" | "Max_difference" | "Max_level" | "Mean_difference" | "Min_difference" | "Min_level" | "Noise_floor" | "Noise_floor_count" | "Number_of_Infs" | "Number_of_NaNs" | "Number_of_denormals" | "Number_of_samples" | "Peak_count" | "Peak_level" | "RMS_difference" | "RMS_level" | "RMS_peak" | "RMS_trough" | "Zero_crossings" | "Zero_crossings_rate" | "Abs_Peak_count";
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "astats", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "length": options?.length,
      "metadata": options?.metadata,
      "reset": options?.reset,
      "measure_perchannel": options?.measure_perchannel,
      "measure_overall": options?.measure_overall,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }








/**
 * Boost subwoofer frequencies.

 *
 * @param options.dry - set dry gain (from 0 to 1) (default 1)
 * @param options.wet - set wet gain (from 0 to 1) (default 1)
 * @param options.boost - set max boost (from 1 to 12) (default 2)
 * @param options.decay - set decay (from 0 to 1) (default 0)
 * @param options.feedback - set feedback (from 0 to 1) (default 0.9)
 * @param options.cutoff - set cutoff (from 50 to 900) (default 100)
 * @param options.slope - set slope (from 0.0001 to 1) (default 0.5)
 * @param options.delay - set delay (from 1 to 100) (default 20)
 * @param options.channels - set channels to filter (default "all")
 * @see https://ffmpeg.org/ffmpeg-filters.html#asubboost
 */
  asubboost(
    options?: {
    dry?: FFDouble;
    wet?: FFDouble;
    boost?: FFDouble;
    decay?: FFDouble;
    feedback?: FFDouble;
    cutoff?: FFDouble;
    slope?: FFDouble;
    delay?: FFDouble;
    channels?: FFString;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "asubboost", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "dry": options?.dry,
      "wet": options?.wet,
      "boost": options?.boost,
      "decay": options?.decay,
      "feedback": options?.feedback,
      "cutoff": options?.cutoff,
      "slope": options?.slope,
      "delay": options?.delay,
      "channels": options?.channels,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Cut subwoofer frequencies.

 *
 * @param options.cutoff - set cutoff frequency (from 2 to 200) (default 20)
 * @param options.order - set filter order (from 3 to 20) (default 10)
 * @param options.level - set input level (from 0 to 1) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#asubcut
 */
  asubcut(
    options?: {
    cutoff?: FFDouble;
    order?: FFInt;
    level?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "asubcut", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "cutoff": options?.cutoff,
      "order": options?.order,
      "level": options?.level,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Cut super frequencies.

 *
 * @param options.cutoff - set cutoff frequency (from 20000 to 192000) (default 20000)
 * @param options.order - set filter order (from 3 to 20) (default 10)
 * @param options.level - set input level (from 0 to 1) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#asupercut
 */
  asupercut(
    options?: {
    cutoff?: FFDouble;
    order?: FFInt;
    level?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "asupercut", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "cutoff": options?.cutoff,
      "order": options?.order,
      "level": options?.level,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply high order Butterworth band-pass filter.

 *
 * @param options.centerf - set center frequency (from 2 to 999999) (default 1000)
 * @param options.order - set filter order (from 4 to 20) (default 4)
 * @param options.qfactor - set Q-factor (from 0.01 to 100) (default 1)
 * @param options.level - set input level (from 0 to 2) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#asuperpass
 */
  asuperpass(
    options?: {
    centerf?: FFDouble;
    order?: FFInt;
    qfactor?: FFDouble;
    level?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "asuperpass", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "centerf": options?.centerf,
      "order": options?.order,
      "qfactor": options?.qfactor,
      "level": options?.level,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply high order Butterworth band-stop filter.

 *
 * @param options.centerf - set center frequency (from 2 to 999999) (default 1000)
 * @param options.order - set filter order (from 4 to 20) (default 4)
 * @param options.qfactor - set Q-factor (from 0.01 to 100) (default 1)
 * @param options.level - set input level (from 0 to 2) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#asuperstop
 */
  asuperstop(
    options?: {
    centerf?: FFDouble;
    order?: FFInt;
    qfactor?: FFDouble;
    level?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "asuperstop", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "centerf": options?.centerf,
      "order": options?.order,
      "qfactor": options?.qfactor,
      "level": options?.level,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }








/**
 * Adjust audio tempo.

 *
 * @param options.tempo - set tempo scale factor (from 0.5 to 100) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#atempo
 */
  atempo(
    options?: {
    tempo?: FFDouble;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "atempo", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "tempo": options?.tempo,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply spectral tilt to audio.

 *
 * @param options.freq - set central frequency (from 20 to 192000) (default 10000)
 * @param options.slope - set filter slope (from -1 to 1) (default 0)
 * @param options.width - set filter width (from 100 to 10000) (default 1000)
 * @param options.order - set filter order (from 2 to 30) (default 5)
 * @param options.level - set input level (from 0 to 4) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#atilt
 */
  atilt(
    options?: {
    freq?: FFDouble;
    slope?: FFDouble;
    width?: FFDouble;
    order?: FFInt;
    level?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "atilt", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "freq": options?.freq,
      "slope": options?.slope,
      "width": options?.width,
      "order": options?.order,
      "level": options?.level,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Pick one continuous section from the input, drop the rest.

 *
 * @param options.start - Timestamp of the first frame that should be passed (default INT64_MAX)
 * @param options.end - Timestamp of the first frame that should be dropped again (default INT64_MAX)
 * @param options.start_pts - Timestamp of the first frame that should be passed (from I64_MIN to I64_MAX) (default I64_MIN)
 * @param options.end_pts - Timestamp of the first frame that should be dropped again (from I64_MIN to I64_MAX) (default I64_MIN)
 * @param options.duration - Maximum duration of the output (default 0)
 * @param options.start_sample - Number of the first audio sample that should be passed to the output (from -1 to I64_MAX) (default -1)
 * @param options.end_sample - Number of the first audio sample that should be dropped again (from 0 to I64_MAX) (default I64_MAX)
 * @see https://ffmpeg.org/ffmpeg-filters.html#atrim
 */
  atrim(
    options?: {
    start?: FFDuration;
    end?: FFDuration;
    start_pts?: FFInt64;
    end_pts?: FFInt64;
    duration?: FFDuration;
    start_sample?: FFInt64;
    end_sample?: FFInt64;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "atrim", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "start": options?.start,
      "end": options?.end,
      "start_pts": options?.start_pts,
      "end_pts": options?.end_pts,
      "duration": options?.duration,
      "start_sample": options?.start_sample,
      "end_sample": options?.end_sample,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Convert input audio to vectorscope video output.

 *
 * @param options.mode - set mode (from 0 to 2) (default lissajous)
 * @param options.rate - set video rate (default "25")
 * @param options.size - set video size (default "400x400")
 * @param options.rc - set red contrast (from 0 to 255) (default 40)
 * @param options.gc - set green contrast (from 0 to 255) (default 160)
 * @param options.bc - set blue contrast (from 0 to 255) (default 80)
 * @param options.ac - set alpha contrast (from 0 to 255) (default 255)
 * @param options.rf - set red fade (from 0 to 255) (default 15)
 * @param options.gf - set green fade (from 0 to 255) (default 10)
 * @param options.bf - set blue fade (from 0 to 255) (default 5)
 * @param options.af - set alpha fade (from 0 to 255) (default 5)
 * @param options.zoom - set zoom factor (from 0 to 10) (default 1)
 * @param options.draw - set draw mode (from 0 to 2) (default dot)
 * @param options.scale - set amplitude scale mode (from 0 to 3) (default lin)
 * @param options.swap - swap x axis with y axis (default true)
 * @param options.mirror - mirror axis (from 0 to 3) (default none)
 * @see https://ffmpeg.org/ffmpeg-filters.html#avectorscope
 */
  avectorscope(
    options?: {
    mode?: FFInt | "lissajous" | "lissajous_xy" | "polar";
    rate?: FFVideoRate;
    size?: FFImageSize;
    rc?: FFInt;
    gc?: FFInt;
    bc?: FFInt;
    ac?: FFInt;
    rf?: FFInt;
    gf?: FFInt;
    bf?: FFInt;
    af?: FFInt;
    zoom?: FFDouble;
    draw?: FFInt | "dot" | "line" | "aaline";
    scale?: FFInt | "lin" | "sqrt" | "cbrt" | "log";
    swap?: FFBoolean;
    mirror?: FFInt | "none" | "x" | "y" | "xy";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "avectorscope", typingsInput: ["audio"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "mode": options?.mode,
      "rate": options?.rate,
      "size": options?.size,
      "rc": options?.rc,
      "gc": options?.gc,
      "bc": options?.bc,
      "ac": options?.ac,
      "rf": options?.rf,
      "gf": options?.gf,
      "bf": options?.bf,
      "af": options?.af,
      "zoom": options?.zoom,
      "draw": options?.draw,
      "scale": options?.scale,
      "swap": options?.swap,
      "mirror": options?.mirror,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }










/**
 * Cross-correlate two audio streams.

 *
 * @param options.size - set the segment size (from 2 to 131072) (default 256)
 * @param options.algo - set the algorithm (from 0 to 2) (default best)
 * @see https://ffmpeg.org/ffmpeg-filters.html#axcorrelate
 */
  axcorrelate(
    _axcorrelate1: AudioStream,

    options?: {
    size?: FFInt;
    algo?: FFInt | "slow" | "fast" | "best";
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "axcorrelate", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
      [this, _axcorrelate1],
      merge(
    {
      "size": options?.size,
      "algo": options?.algo,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }








/**
 * Apply a two-pole Butterworth band-pass filter.

 *
 * @param options.frequency - set central frequency (from 0 to 999999) (default 3000)
 * @param options.width_type - set filter-width type (from 1 to 5) (default q)
 * @param options.width - set width (from 0 to 99999) (default 0.5)
 * @param options.csg - use constant skirt gain (default false)
 * @param options.mix - set mix (from 0 to 1) (default 1)
 * @param options.channels - set channels to filter (default "all")
 * @param options.normalize - normalize coefficients (default false)
 * @param options.transform - set transform type (from 0 to 6) (default di)
 * @param options.precision - set filtering precision (from -1 to 3) (default auto)
 * @param options.blocksize - set the block size (from 0 to 32768) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#bandpass
 */
  bandpass(
    options?: {
    frequency?: FFDouble;
    width_type?: FFInt | "h" | "q" | "o" | "s" | "k";
    width?: FFDouble;
    csg?: FFBoolean;
    mix?: FFDouble;
    channels?: FFString;
    normalize?: FFBoolean;
    transform?: FFInt | "di" | "dii" | "tdi" | "tdii" | "latt" | "svf" | "zdf";
    precision?: FFInt | "auto" | "s16" | "s32" | "f32" | "f64";
    blocksize?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "bandpass", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "frequency": options?.frequency,
      "width_type": options?.width_type,
      "width": options?.width,
      "csg": options?.csg,
      "mix": options?.mix,
      "channels": options?.channels,
      "normalize": options?.normalize,
      "transform": options?.transform,
      "precision": options?.precision,
      "blocksize": options?.blocksize,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply a two-pole Butterworth band-reject filter.

 *
 * @param options.frequency - set central frequency (from 0 to 999999) (default 3000)
 * @param options.width_type - set filter-width type (from 1 to 5) (default q)
 * @param options.width - set width (from 0 to 99999) (default 0.5)
 * @param options.mix - set mix (from 0 to 1) (default 1)
 * @param options.channels - set channels to filter (default "all")
 * @param options.normalize - normalize coefficients (default false)
 * @param options.transform - set transform type (from 0 to 6) (default di)
 * @param options.precision - set filtering precision (from -1 to 3) (default auto)
 * @param options.blocksize - set the block size (from 0 to 32768) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#bandreject
 */
  bandreject(
    options?: {
    frequency?: FFDouble;
    width_type?: FFInt | "h" | "q" | "o" | "s" | "k";
    width?: FFDouble;
    mix?: FFDouble;
    channels?: FFString;
    normalize?: FFBoolean;
    transform?: FFInt | "di" | "dii" | "tdi" | "tdii" | "latt" | "svf" | "zdf";
    precision?: FFInt | "auto" | "s16" | "s32" | "f32" | "f64";
    blocksize?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "bandreject", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "frequency": options?.frequency,
      "width_type": options?.width_type,
      "width": options?.width,
      "mix": options?.mix,
      "channels": options?.channels,
      "normalize": options?.normalize,
      "transform": options?.transform,
      "precision": options?.precision,
      "blocksize": options?.blocksize,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Boost or cut lower frequencies.

 *
 * @param options.frequency - set central frequency (from 0 to 999999) (default 100)
 * @param options.width_type - set filter-width type (from 1 to 5) (default q)
 * @param options.width - set width (from 0 to 99999) (default 0.5)
 * @param options.gain - set gain (from -900 to 900) (default 0)
 * @param options.poles - set number of poles (from 1 to 2) (default 2)
 * @param options.mix - set mix (from 0 to 1) (default 1)
 * @param options.channels - set channels to filter (default "all")
 * @param options.normalize - normalize coefficients (default false)
 * @param options.transform - set transform type (from 0 to 6) (default di)
 * @param options.precision - set filtering precision (from -1 to 3) (default auto)
 * @param options.blocksize - set the block size (from 0 to 32768) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#bass_002c-lowshelf
 */
  bass(
    options?: {
    frequency?: FFDouble;
    width_type?: FFInt | "h" | "q" | "o" | "s" | "k";
    width?: FFDouble;
    gain?: FFDouble;
    poles?: FFInt;
    mix?: FFDouble;
    channels?: FFString;
    normalize?: FFBoolean;
    transform?: FFInt | "di" | "dii" | "tdi" | "tdii" | "latt" | "svf" | "zdf";
    precision?: FFInt | "auto" | "s16" | "s32" | "f32" | "f64";
    blocksize?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "bass", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "frequency": options?.frequency,
      "width_type": options?.width_type,
      "width": options?.width,
      "gain": options?.gain,
      "poles": options?.poles,
      "mix": options?.mix,
      "channels": options?.channels,
      "normalize": options?.normalize,
      "transform": options?.transform,
      "precision": options?.precision,
      "blocksize": options?.blocksize,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }












/**
 * Apply a biquad IIR filter with the given coefficients.

 *
 * @param options.a0 - (from INT_MIN to INT_MAX) (default 1)
 * @param options.a1 - (from INT_MIN to INT_MAX) (default 0)
 * @param options.mix - set mix (from 0 to 1) (default 1)
 * @param options.channels - set channels to filter (default "all")
 * @param options.normalize - normalize coefficients (default false)
 * @param options.transform - set transform type (from 0 to 6) (default di)
 * @param options.precision - set filtering precision (from -1 to 3) (default auto)
 * @param options.blocksize - set the block size (from 0 to 32768) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#biquad
 */
  biquad(
    options?: {
    a0?: FFDouble;
    a1?: FFDouble;
    mix?: FFDouble;
    channels?: FFString;
    normalize?: FFBoolean;
    transform?: FFInt | "di" | "dii" | "tdi" | "tdii" | "latt" | "svf" | "zdf";
    precision?: FFInt | "auto" | "s16" | "s32" | "f32" | "f64";
    blocksize?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "biquad", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "a0": options?.a0,
      "a1": options?.a1,
      "mix": options?.mix,
      "channels": options?.channels,
      "normalize": options?.normalize,
      "transform": options?.transform,
      "precision": options?.precision,
      "blocksize": options?.blocksize,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }


































/**
 * Remap audio channels.

 *
 * @param options.map - A comma-separated list of input channel numbers in output order.
 * @param options.channel_layout - Output channel layout.
 * @see https://ffmpeg.org/ffmpeg-filters.html#channelmap
 */
  channelmap(
    options?: {
    map?: FFString;
    channel_layout?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "channelmap", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "map": options?.map,
      "channel_layout": options?.channel_layout,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Split audio into per-channel streams.

 *
 * @param options.channel_layout - Input channel layout. (default "stereo")
 * @param options.channels - Channels to extract. (default "all")
 * @see https://ffmpeg.org/ffmpeg-filters.html#channelsplit
 */
  channelsplit(
    options?: {
    channel_layout?: FFString;
    channels?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): FilterNode {
    const filterNode = filterNodeFactory(
      { name: "channelsplit", typingsInput: ["audio"], typingsOutput: [] },
      [this],
      merge(
    {
      "channel_layout": options?.channel_layout,
      "channels": options?.channels,
},
    options?.extraOptions,
  ),
    );
return filterNode;
  }






/**
 * Add a chorus effect to the audio.

 *
 * @param options.in_gain - set input gain (from 0 to 1) (default 0.4)
 * @param options.out_gain - set output gain (from 0 to 1) (default 0.4)
 * @param options.delays - set delays
 * @param options.decays - set decays
 * @param options.speeds - set speeds
 * @param options.depths - set depths
 * @see https://ffmpeg.org/ffmpeg-filters.html#chorus
 */
  chorus(
    options?: {
    in_gain?: FFFloat;
    out_gain?: FFFloat;
    delays?: FFString;
    decays?: FFString;
    speeds?: FFString;
    depths?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "chorus", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "in_gain": options?.in_gain,
      "out_gain": options?.out_gain,
      "delays": options?.delays,
      "decays": options?.decays,
      "speeds": options?.speeds,
      "depths": options?.depths,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }


















































/**
 * Compress or expand audio dynamic range.

 *
 * @param options.attacks - set time over which increase of volume is determined (default "0")
 * @param options.decays - set time over which decrease of volume is determined (default "0.8")
 * @param options.points - set points of transfer function (default "-70/-70|-60/-20|1/0")
 * @param options.soft_knee - set soft-knee (from 0.01 to 900) (default 0.01)
 * @param options.gain - set output gain (from -900 to 900) (default 0)
 * @param options.volume - set initial volume (from -900 to 0) (default 0)
 * @param options.delay - set delay for samples before sending them to volume adjuster (from 0 to 20) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#compand
 */
  compand(
    options?: {
    attacks?: FFString;
    decays?: FFString;
    points?: FFString;
    soft_knee?: FFDouble;
    gain?: FFDouble;
    volume?: FFDouble;
    delay?: FFDouble;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "compand", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "attacks": options?.attacks,
      "decays": options?.decays,
      "points": options?.points,
      "soft-knee": options?.soft_knee,
      "gain": options?.gain,
      "volume": options?.volume,
      "delay": options?.delay,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Audio Compensation Delay Line.

 *
 * @param options.mm - set mm distance (from 0 to 10) (default 0)
 * @param options.cm - set cm distance (from 0 to 100) (default 0)
 * @param options.m - set meter distance (from 0 to 100) (default 0)
 * @param options.dry - set dry amount (from 0 to 1) (default 0)
 * @param options.wet - set wet amount (from 0 to 1) (default 1)
 * @param options.temp - set temperature °C (from -50 to 50) (default 20)
 * @see https://ffmpeg.org/ffmpeg-filters.html#compensationdelay
 */
  compensationdelay(
    options?: {
    mm?: FFInt;
    cm?: FFInt;
    m?: FFInt;
    dry?: FFDouble;
    wet?: FFDouble;
    temp?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "compensationdelay", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "mm": options?.mm,
      "cm": options?.cm,
      "m": options?.m,
      "dry": options?.dry,
      "wet": options?.wet,
      "temp": options?.temp,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }


























/**
 * Apply headphone crossfeed filter.

 *
 * @param options.strength - set crossfeed strength (from 0 to 1) (default 0.2)
 * @param options.range - set soundstage wideness (from 0 to 1) (default 0.5)
 * @param options.slope - set curve slope (from 0.01 to 1) (default 0.5)
 * @param options.level_in - set level in (from 0 to 1) (default 0.9)
 * @param options.level_out - set level out (from 0 to 1) (default 1)
 * @param options.block_size - set the block size (from 0 to 32768) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#crossfeed
 */
  crossfeed(
    options?: {
    strength?: FFDouble;
    range?: FFDouble;
    slope?: FFDouble;
    level_in?: FFDouble;
    level_out?: FFDouble;
    block_size?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "crossfeed", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "strength": options?.strength,
      "range": options?.range,
      "slope": options?.slope,
      "level_in": options?.level_in,
      "level_out": options?.level_out,
      "block_size": options?.block_size,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Simple audio noise sharpening filter.

 *
 * @param options.i - set intensity (from -10 to 10) (default 2)
 * @param options.c - enable clipping (default true)
 * @see https://ffmpeg.org/ffmpeg-filters.html#crystalizer
 */
  crystalizer(
    options?: {
    i?: FFFloat;
    c?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "crystalizer", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "i": options?.i,
      "c": options?.c,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }














/**
 * Apply a DC shift to the audio.

 *
 * @param options.shift - set DC shift (from -1 to 1) (default 0)
 * @param options.limitergain - set limiter gain (from 0 to 1) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#dcshift
 */
  dcshift(
    options?: {
    shift?: FFDouble;
    limitergain?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "dcshift", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "shift": options?.shift,
      "limitergain": options?.limitergain,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }


















/**
 * Apply de-essing to the audio.

 *
 * @param options.i - set intensity (from 0 to 1) (default 0)
 * @param options.m - set max deessing (from 0 to 1) (default 0.5)
 * @param options.f - set frequency (from 0 to 1) (default 0.5)
 * @param options.s - set output mode (from 0 to 2) (default o)
 * @see https://ffmpeg.org/ffmpeg-filters.html#deesser
 */
  deesser(
    options?: {
    i?: FFDouble;
    m?: FFDouble;
    f?: FFDouble;
    s?: FFInt | "i" | "o" | "e";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "deesser", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "i": options?.i,
      "m": options?.m,
      "f": options?.f,
      "s": options?.s,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }




















/**
 * Audio Dialogue Enhancement.

 *
 * @param options.original - set original center factor (from 0 to 1) (default 1)
 * @param options.enhance - set dialogue enhance factor (from 0 to 3) (default 1)
 * @param options.voice - set voice detection factor (from 2 to 32) (default 2)
 * @see https://ffmpeg.org/ffmpeg-filters.html#dialoguenhance
 */
  dialoguenhance(
    options?: {
    original?: FFDouble;
    enhance?: FFDouble;
    voice?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "dialoguenhance", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "original": options?.original,
      "enhance": options?.enhance,
      "voice": options?.voice,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }


















/**
 * Measure audio dynamic range.

 *
 * @param options.length - set the window length (from 0.01 to 10) (default 3)
 * @see https://ffmpeg.org/ffmpeg-filters.html#drmeter
 */
  drmeter(
    options?: {
    length?: FFDouble;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "drmeter", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "length": options?.length,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Dynamic Audio Normalizer.

 *
 * @param options.framelen - set the frame length in msec (from 10 to 8000) (default 500)
 * @param options.gausssize - set the filter size (from 3 to 301) (default 31)
 * @param options.peak - set the peak value (from 0 to 1) (default 0.95)
 * @param options.maxgain - set the max amplification (from 1 to 100) (default 10)
 * @param options.targetrms - set the target RMS (from 0 to 1) (default 0)
 * @param options.coupling - set channel coupling (default true)
 * @param options.correctdc - set DC correction (default false)
 * @param options.altboundary - set alternative boundary mode (default false)
 * @param options.compress - set the compress factor (from 0 to 30) (default 0)
 * @param options.threshold - set the threshold value (from 0 to 1) (default 0)
 * @param options.channels - set channels to filter (default "all")
 * @param options.overlap - set the frame overlap (from 0 to 1) (default 0)
 * @param options.curve - set the custom peak mapping curve
 * @see https://ffmpeg.org/ffmpeg-filters.html#dynaudnorm
 */
  dynaudnorm(
    options?: {
    framelen?: FFInt;
    gausssize?: FFInt;
    peak?: FFDouble;
    maxgain?: FFDouble;
    targetrms?: FFDouble;
    coupling?: FFBoolean;
    correctdc?: FFBoolean;
    altboundary?: FFBoolean;
    compress?: FFDouble;
    threshold?: FFDouble;
    channels?: FFString;
    overlap?: FFDouble;
    curve?: FFString;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "dynaudnorm", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "framelen": options?.framelen,
      "gausssize": options?.gausssize,
      "peak": options?.peak,
      "maxgain": options?.maxgain,
      "targetrms": options?.targetrms,
      "coupling": options?.coupling,
      "correctdc": options?.correctdc,
      "altboundary": options?.altboundary,
      "compress": options?.compress,
      "threshold": options?.threshold,
      "channels": options?.channels,
      "overlap": options?.overlap,
      "curve": options?.curve,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Widen the stereo image.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#earwax
 */
  earwax(
    options?: {
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "earwax", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * EBU R128 scanner.

 *
 * @param options.video - set video output (default false)
 * @param options.size - set video size (default "640x480")
 * @param options.meter - set scale meter (+9 to +18) (from 9 to 18) (default 9)
 * @param options.framelog - force frame logging level (from INT_MIN to INT_MAX) (default -1)
 * @param options.metadata - inject metadata in the filtergraph (default false)
 * @param options.peak - set peak mode (default 0)
 * @param options.dualmono - treat mono input files as dual-mono (default false)
 * @param options.panlaw - set a specific pan law for dual-mono files (from -10 to 0) (default -3.0103)
 * @param options.target - set a specific target level in LUFS (-23 to 0) (from -23 to 0) (default -23)
 * @param options.gauge - set gauge display type (from 0 to 1) (default momentary)
 * @param options.scale - sets display method for the stats (from 0 to 1) (default absolute)
 * @param options.integrated - integrated loudness (LUFS) (from -DBL_MAX to DBL_MAX) (default 0)
 * @param options.range - loudness range (LU) (from -DBL_MAX to DBL_MAX) (default 0)
 * @param options.lra_low - LRA low (LUFS) (from -DBL_MAX to DBL_MAX) (default 0)
 * @param options.lra_high - LRA high (LUFS) (from -DBL_MAX to DBL_MAX) (default 0)
 * @param options.sample_peak - sample peak (dBFS) (from -DBL_MAX to DBL_MAX) (default 0)
 * @param options.true_peak - true peak (dBFS) (from -DBL_MAX to DBL_MAX) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#ebur128
 */
  ebur128(
    options?: {
    video?: FFBoolean;
    size?: FFImageSize;
    meter?: FFInt;
    framelog?: FFInt | "quiet" | "info" | "verbose";
    metadata?: FFBoolean;
    peak?: FFFlags | "none" | "sample" | "true";
    dualmono?: FFBoolean;
    panlaw?: FFDouble;
    target?: FFInt;
    gauge?: FFInt | "momentary" | "m" | "shortterm" | "s";
    scale?: FFInt | "absolute" | "LUFS" | "relative" | "LU";
    integrated?: FFDouble;
    range?: FFDouble;
    lra_low?: FFDouble;
    lra_high?: FFDouble;
    sample_peak?: FFDouble;
    true_peak?: FFDouble;
extraOptions?: Record<string, unknown>;
    },
  ): FilterNode {
    const filterNode = filterNodeFactory(
      { name: "ebur128", typingsInput: ["audio"], typingsOutput: [] },
      [this],
      merge(
    {
      "video": options?.video,
      "size": options?.size,
      "meter": options?.meter,
      "framelog": options?.framelog,
      "metadata": options?.metadata,
      "peak": options?.peak,
      "dualmono": options?.dualmono,
      "panlaw": options?.panlaw,
      "target": options?.target,
      "gauge": options?.gauge,
      "scale": options?.scale,
      "integrated": options?.integrated,
      "range": options?.range,
      "lra_low": options?.lra_low,
      "lra_high": options?.lra_high,
      "sample_peak": options?.sample_peak,
      "true_peak": options?.true_peak,
},
    options?.extraOptions,
  ),
    );
return filterNode;
  }
















/**
 * Apply two-pole peaking equalization (EQ) filter.

 *
 * @param options.frequency - set central frequency (from 0 to 999999) (default 0)
 * @param options.width_type - set filter-width type (from 1 to 5) (default q)
 * @param options.width - set width (from 0 to 99999) (default 1)
 * @param options.gain - set gain (from -900 to 900) (default 0)
 * @param options.mix - set mix (from 0 to 1) (default 1)
 * @param options.channels - set channels to filter (default "all")
 * @param options.normalize - normalize coefficients (default false)
 * @param options.transform - set transform type (from 0 to 6) (default di)
 * @param options.precision - set filtering precision (from -1 to 3) (default auto)
 * @param options.blocksize - set the block size (from 0 to 32768) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#equalizer
 */
  equalizer(
    options?: {
    frequency?: FFDouble;
    width_type?: FFInt | "h" | "q" | "o" | "s" | "k";
    width?: FFDouble;
    gain?: FFDouble;
    mix?: FFDouble;
    channels?: FFString;
    normalize?: FFBoolean;
    transform?: FFInt | "di" | "dii" | "tdi" | "tdii" | "latt" | "svf" | "zdf";
    precision?: FFInt | "auto" | "s16" | "s32" | "f32" | "f64";
    blocksize?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "equalizer", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "frequency": options?.frequency,
      "width_type": options?.width_type,
      "width": options?.width,
      "gain": options?.gain,
      "mix": options?.mix,
      "channels": options?.channels,
      "normalize": options?.normalize,
      "transform": options?.transform,
      "precision": options?.precision,
      "blocksize": options?.blocksize,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }














/**
 * Increase difference between stereo audio channels.

 *
 * @param options.m - set the difference coefficient (from -10 to 10) (default 2.5)
 * @param options.c - enable clipping (default true)
 * @see https://ffmpeg.org/ffmpeg-filters.html#extrastereo
 */
  extrastereo(
    options?: {
    m?: FFFloat;
    c?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "extrastereo", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "m": options?.m,
      "c": options?.c,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }


























/**
 * Finite Impulse Response Equalizer.

 *
 * @param options.gain - set gain curve (default "gain_interpolate(f)")
 * @param options.gain_entry - set gain entry
 * @param options.delay - set delay (from 0 to 1e+10) (default 0.01)
 * @param options.accuracy - set accuracy (from 0 to 1e+10) (default 5)
 * @param options.wfunc - set window function (from 0 to 9) (default hann)
 * @param options.fixed - set fixed frame samples (default false)
 * @param options.multi - set multi channels mode (default false)
 * @param options.zero_phase - set zero phase mode (default false)
 * @param options.scale - set gain scale (from 0 to 3) (default linlog)
 * @param options.dumpfile - set dump file
 * @param options.dumpscale - set dump scale (from 0 to 3) (default linlog)
 * @param options.fft2 - set 2-channels fft (default false)
 * @param options.min_phase - set minimum phase mode (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#firequalizer
 */
  firequalizer(
    options?: {
    gain?: FFString;
    gain_entry?: FFString;
    delay?: FFDouble;
    accuracy?: FFDouble;
    wfunc?: FFInt | "rectangular" | "hann" | "hamming" | "blackman" | "nuttall3" | "mnuttall3" | "nuttall" | "bnuttall" | "bharris" | "tukey";
    fixed?: FFBoolean;
    multi?: FFBoolean;
    zero_phase?: FFBoolean;
    scale?: FFInt | "linlin" | "linlog" | "loglin" | "loglog";
    dumpfile?: FFString;
    dumpscale?: FFInt | "linlin" | "linlog" | "loglin" | "loglog";
    fft2?: FFBoolean;
    min_phase?: FFBoolean;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "firequalizer", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "gain": options?.gain,
      "gain_entry": options?.gain_entry,
      "delay": options?.delay,
      "accuracy": options?.accuracy,
      "wfunc": options?.wfunc,
      "fixed": options?.fixed,
      "multi": options?.multi,
      "zero_phase": options?.zero_phase,
      "scale": options?.scale,
      "dumpfile": options?.dumpfile,
      "dumpscale": options?.dumpscale,
      "fft2": options?.fft2,
      "min_phase": options?.min_phase,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply a flanging effect to the audio.

 *
 * @param options.delay - base delay in milliseconds (from 0 to 30) (default 0)
 * @param options.depth - added swept delay in milliseconds (from 0 to 10) (default 2)
 * @param options.regen - percentage regeneration (delayed signal feedback) (from -95 to 95) (default 0)
 * @param options.width - percentage of delayed signal mixed with original (from 0 to 100) (default 71)
 * @param options.speed - sweeps per second (Hz) (from 0.1 to 10) (default 0.5)
 * @param options.shape - swept wave shape (from 0 to 1) (default sinusoidal)
 * @param options.phase - swept wave percentage phase-shift for multi-channel (from 0 to 100) (default 25)
 * @param options.interp - delay-line interpolation (from 0 to 1) (default linear)
 * @see https://ffmpeg.org/ffmpeg-filters.html#flanger
 */
  flanger(
    options?: {
    delay?: FFDouble;
    depth?: FFDouble;
    regen?: FFDouble;
    width?: FFDouble;
    speed?: FFDouble;
    shape?: FFInt | "triangular" | "t" | "sinusoidal" | "s";
    phase?: FFDouble;
    interp?: FFInt | "linear" | "quadratic";
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "flanger", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "delay": options?.delay,
      "depth": options?.depth,
      "regen": options?.regen,
      "width": options?.width,
      "speed": options?.speed,
      "shape": options?.shape,
      "phase": options?.phase,
      "interp": options?.interp,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }










































/**
 * Apply Haas Stereo Enhancer.

 *
 * @param options.level_in - set level in (from 0.015625 to 64) (default 1)
 * @param options.level_out - set level out (from 0.015625 to 64) (default 1)
 * @param options.side_gain - set side gain (from 0.015625 to 64) (default 1)
 * @param options.middle_source - set middle source (from 0 to 3) (default mid)
 * @param options.middle_phase - set middle phase (default false)
 * @param options.left_delay - set left delay (from 0 to 40) (default 2.05)
 * @param options.left_balance - set left balance (from -1 to 1) (default -1)
 * @param options.left_gain - set left gain (from 0.015625 to 64) (default 1)
 * @param options.left_phase - set left phase (default false)
 * @param options.right_delay - set right delay (from 0 to 40) (default 2.12)
 * @param options.right_balance - set right balance (from -1 to 1) (default 1)
 * @param options.right_gain - set right gain (from 0.015625 to 64) (default 1)
 * @param options.right_phase - set right phase (default true)
 * @see https://ffmpeg.org/ffmpeg-filters.html#haas
 */
  haas(
    options?: {
    level_in?: FFDouble;
    level_out?: FFDouble;
    side_gain?: FFDouble;
    middle_source?: FFInt | "left" | "right" | "mid" | "side";
    middle_phase?: FFBoolean;
    left_delay?: FFDouble;
    left_balance?: FFDouble;
    left_gain?: FFDouble;
    left_phase?: FFBoolean;
    right_delay?: FFDouble;
    right_balance?: FFDouble;
    right_gain?: FFDouble;
    right_phase?: FFBoolean;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "haas", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "level_in": options?.level_in,
      "level_out": options?.level_out,
      "side_gain": options?.side_gain,
      "middle_source": options?.middle_source,
      "middle_phase": options?.middle_phase,
      "left_delay": options?.left_delay,
      "left_balance": options?.left_balance,
      "left_gain": options?.left_gain,
      "left_phase": options?.left_phase,
      "right_delay": options?.right_delay,
      "right_balance": options?.right_balance,
      "right_gain": options?.right_gain,
      "right_phase": options?.right_phase,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }










/**
 * Apply High Definition Compatible Digital (HDCD) decoding.

 *
 * @param options.disable_autoconvert - Disable any format conversion or resampling in the filter graph. (default true)
 * @param options.process_stereo - Process stereo channels together. Only apply target_gain when both channels match. (default true)
 * @param options.cdt_ms - Code detect timer period in ms. (from 100 to 60000) (default 2000)
 * @param options.force_pe - Always extend peaks above -3dBFS even when PE is not signaled. (default false)
 * @param options.analyze_mode - Replace audio with solid tone and signal some processing aspect in the amplitude. (from 0 to 4) (default off)
 * @param options.bits_per_sample - Valid bits per sample (location of the true LSB). (from 16 to 24) (default 16)
 * @see https://ffmpeg.org/ffmpeg-filters.html#hdcd
 */
  hdcd(
    options?: {
    disable_autoconvert?: FFBoolean;
    process_stereo?: FFBoolean;
    cdt_ms?: FFInt;
    force_pe?: FFBoolean;
    analyze_mode?: FFInt | "off" | "lle" | "pe" | "cdt" | "tgm";
    bits_per_sample?: FFInt | "16" | "20" | "24";
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "hdcd", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "disable_autoconvert": options?.disable_autoconvert,
      "process_stereo": options?.process_stereo,
      "cdt_ms": options?.cdt_ms,
      "force_pe": options?.force_pe,
      "analyze_mode": options?.analyze_mode,
      "bits_per_sample": options?.bits_per_sample,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }










/**
 * Apply a high-pass filter with 3dB point frequency.

 *
 * @param options.frequency - set frequency (from 0 to 999999) (default 3000)
 * @param options.width_type - set filter-width type (from 1 to 5) (default q)
 * @param options.width - set width (from 0 to 99999) (default 0.707)
 * @param options.poles - set number of poles (from 1 to 2) (default 2)
 * @param options.mix - set mix (from 0 to 1) (default 1)
 * @param options.channels - set channels to filter (default "all")
 * @param options.normalize - normalize coefficients (default false)
 * @param options.transform - set transform type (from 0 to 6) (default di)
 * @param options.precision - set filtering precision (from -1 to 3) (default auto)
 * @param options.blocksize - set the block size (from 0 to 32768) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#highpass
 */
  highpass(
    options?: {
    frequency?: FFDouble;
    width_type?: FFInt | "h" | "q" | "o" | "s" | "k";
    width?: FFDouble;
    poles?: FFInt;
    mix?: FFDouble;
    channels?: FFString;
    normalize?: FFBoolean;
    transform?: FFInt | "di" | "dii" | "tdi" | "tdii" | "latt" | "svf" | "zdf";
    precision?: FFInt | "auto" | "s16" | "s32" | "f32" | "f64";
    blocksize?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "highpass", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "frequency": options?.frequency,
      "width_type": options?.width_type,
      "width": options?.width,
      "poles": options?.poles,
      "mix": options?.mix,
      "channels": options?.channels,
      "normalize": options?.normalize,
      "transform": options?.transform,
      "precision": options?.precision,
      "blocksize": options?.blocksize,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply a high shelf filter.

 *
 * @param options.frequency - set central frequency (from 0 to 999999) (default 3000)
 * @param options.width_type - set filter-width type (from 1 to 5) (default q)
 * @param options.width - set width (from 0 to 99999) (default 0.5)
 * @param options.gain - set gain (from -900 to 900) (default 0)
 * @param options.poles - set number of poles (from 1 to 2) (default 2)
 * @param options.mix - set mix (from 0 to 1) (default 1)
 * @param options.channels - set channels to filter (default "all")
 * @param options.normalize - normalize coefficients (default false)
 * @param options.transform - set transform type (from 0 to 6) (default di)
 * @param options.precision - set filtering precision (from -1 to 3) (default auto)
 * @param options.blocksize - set the block size (from 0 to 32768) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#treble_002c-highshelf
 */
  highshelf(
    options?: {
    frequency?: FFDouble;
    width_type?: FFInt | "h" | "q" | "o" | "s" | "k";
    width?: FFDouble;
    gain?: FFDouble;
    poles?: FFInt;
    mix?: FFDouble;
    channels?: FFString;
    normalize?: FFBoolean;
    transform?: FFInt | "di" | "dii" | "tdi" | "tdii" | "latt" | "svf" | "zdf";
    precision?: FFInt | "auto" | "s16" | "s32" | "f32" | "f64";
    blocksize?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "highshelf", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "frequency": options?.frequency,
      "width_type": options?.width_type,
      "width": options?.width,
      "gain": options?.gain,
      "poles": options?.poles,
      "mix": options?.mix,
      "channels": options?.channels,
      "normalize": options?.normalize,
      "transform": options?.transform,
      "precision": options?.precision,
      "blocksize": options?.blocksize,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }


































































/**
 * EBU R128 loudness normalization

 *
 * @param options.I - set integrated loudness target (from -70 to -5) (default -24)
 * @param options.LRA - set loudness range target (from 1 to 50) (default 7)
 * @param options.TP - set maximum true peak (from -9 to 0) (default -2)
 * @param options.measured_I - measured IL of input file (from -99 to 0) (default 0)
 * @param options.measured_LRA - measured LRA of input file (from 0 to 99) (default 0)
 * @param options.measured_TP - measured true peak of input file (from -99 to 99) (default 99)
 * @param options.measured_thresh - measured threshold of input file (from -99 to 0) (default -70)
 * @param options.offset - set offset gain (from -99 to 99) (default 0)
 * @param options.linear - normalize linearly if possible (default true)
 * @param options.dual_mono - treat mono input as dual-mono (default false)
 * @param options.print_format - set print format for stats (from 0 to 2) (default none)
 * @param options.stats_file - set stats output file
 * @see https://ffmpeg.org/ffmpeg-filters.html#loudnorm
 */
  loudnorm(
    options?: {
    I?: FFDouble;
    LRA?: FFDouble;
    TP?: FFDouble;
    measured_I?: FFDouble;
    measured_LRA?: FFDouble;
    measured_TP?: FFDouble;
    measured_thresh?: FFDouble;
    offset?: FFDouble;
    linear?: FFBoolean;
    dual_mono?: FFBoolean;
    print_format?: FFInt | "none" | "json" | "summary";
    stats_file?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "loudnorm", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "I": options?.I,
      "LRA": options?.LRA,
      "TP": options?.TP,
      "measured_I": options?.measured_I,
      "measured_LRA": options?.measured_LRA,
      "measured_TP": options?.measured_TP,
      "measured_thresh": options?.measured_thresh,
      "offset": options?.offset,
      "linear": options?.linear,
      "dual_mono": options?.dual_mono,
      "print_format": options?.print_format,
      "stats_file": options?.stats_file,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply a low-pass filter with 3dB point frequency.

 *
 * @param options.frequency - set frequency (from 0 to 999999) (default 500)
 * @param options.width_type - set filter-width type (from 1 to 5) (default q)
 * @param options.width - set width (from 0 to 99999) (default 0.707)
 * @param options.poles - set number of poles (from 1 to 2) (default 2)
 * @param options.mix - set mix (from 0 to 1) (default 1)
 * @param options.channels - set channels to filter (default "all")
 * @param options.normalize - normalize coefficients (default false)
 * @param options.transform - set transform type (from 0 to 6) (default di)
 * @param options.precision - set filtering precision (from -1 to 3) (default auto)
 * @param options.blocksize - set the block size (from 0 to 32768) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#lowpass
 */
  lowpass(
    options?: {
    frequency?: FFDouble;
    width_type?: FFInt | "h" | "q" | "o" | "s" | "k";
    width?: FFDouble;
    poles?: FFInt;
    mix?: FFDouble;
    channels?: FFString;
    normalize?: FFBoolean;
    transform?: FFInt | "di" | "dii" | "tdi" | "tdii" | "latt" | "svf" | "zdf";
    precision?: FFInt | "auto" | "s16" | "s32" | "f32" | "f64";
    blocksize?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "lowpass", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "frequency": options?.frequency,
      "width_type": options?.width_type,
      "width": options?.width,
      "poles": options?.poles,
      "mix": options?.mix,
      "channels": options?.channels,
      "normalize": options?.normalize,
      "transform": options?.transform,
      "precision": options?.precision,
      "blocksize": options?.blocksize,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply a low shelf filter.

 *
 * @param options.frequency - set central frequency (from 0 to 999999) (default 100)
 * @param options.width_type - set filter-width type (from 1 to 5) (default q)
 * @param options.width - set width (from 0 to 99999) (default 0.5)
 * @param options.gain - set gain (from -900 to 900) (default 0)
 * @param options.poles - set number of poles (from 1 to 2) (default 2)
 * @param options.mix - set mix (from 0 to 1) (default 1)
 * @param options.channels - set channels to filter (default "all")
 * @param options.normalize - normalize coefficients (default false)
 * @param options.transform - set transform type (from 0 to 6) (default di)
 * @param options.precision - set filtering precision (from -1 to 3) (default auto)
 * @param options.blocksize - set the block size (from 0 to 32768) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#bass_002c-lowshelf
 */
  lowshelf(
    options?: {
    frequency?: FFDouble;
    width_type?: FFInt | "h" | "q" | "o" | "s" | "k";
    width?: FFDouble;
    gain?: FFDouble;
    poles?: FFInt;
    mix?: FFDouble;
    channels?: FFString;
    normalize?: FFBoolean;
    transform?: FFInt | "di" | "dii" | "tdi" | "tdii" | "latt" | "svf" | "zdf";
    precision?: FFInt | "auto" | "s16" | "s32" | "f32" | "f64";
    blocksize?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "lowshelf", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "frequency": options?.frequency,
      "width_type": options?.width_type,
      "width": options?.width,
      "gain": options?.gain,
      "poles": options?.poles,
      "mix": options?.mix,
      "channels": options?.channels,
      "normalize": options?.normalize,
      "transform": options?.transform,
      "precision": options?.precision,
      "blocksize": options?.blocksize,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }




































/**
 * Multiband Compress or expand audio dynamic range.

 *
 * @param options.args - set parameters for each band (default "0.005,0.1 6 -47/-40,-34/-34,-17/-33 100 | 0.003,0.05 6 -47/-40,-34/-34,-17/-33 400 | 0.000625,0.0125 6 -47/-40,-34/-34,-15/-33 1600 | 0.0001,0.025 6 -47/-40,-34/-34,-31/-31,-0/-30 6400 | 0,0.025 6 -38/-31,-28/-28,-0/-25 22000")
 * @see https://ffmpeg.org/ffmpeg-filters.html#mcompand
 */
  mcompand(
    options?: {
    args?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "mcompand", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "args": options?.args,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }




































































/**
 * Remix channels with coefficients (panning).

 *
 * @param options.args -
 * @see https://ffmpeg.org/ffmpeg-filters.html#pan
 */
  pan(
    options?: {
    args?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "pan", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "args": options?.args,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






















































/**
 * ReplayGain scanner.

 *
 * @param options.track_gain - track gain (dB) (from -FLT_MAX to FLT_MAX) (default 0)
 * @param options.track_peak - track peak (from -FLT_MAX to FLT_MAX) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#replaygain
 */
  replaygain(
    options?: {
    track_gain?: FFFloat;
    track_peak?: FFFloat;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "replaygain", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "track_gain": options?.track_gain,
      "track_peak": options?.track_peak,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






















































/**
 * Convert input audio to a CQT (Constant/Clamped Q Transform) spectrum video output.

 *
 * @param options.size - set video size (default "1920x1080")
 * @param options.fps - set video rate (default "25")
 * @param options.bar_h - set bargraph height (from -1 to INT_MAX) (default -1)
 * @param options.axis_h - set axis height (from -1 to INT_MAX) (default -1)
 * @param options.sono_h - set sonogram height (from -1 to INT_MAX) (default -1)
 * @param options.fullhd - set fullhd size (default true)
 * @param options.sono_v - set sonogram volume (default "16")
 * @param options.bar_v - set bargraph volume (default "sono_v")
 * @param options.sono_g - set sonogram gamma (from 1 to 7) (default 3)
 * @param options.bar_g - set bargraph gamma (from 1 to 7) (default 1)
 * @param options.bar_t - set bar transparency (from 0 to 1) (default 1)
 * @param options.timeclamp - set timeclamp (from 0.002 to 1) (default 0.17)
 * @param options.attack - set attack time (from 0 to 1) (default 0)
 * @param options.basefreq - set base frequency (from 10 to 100000) (default 20.0152)
 * @param options.endfreq - set end frequency (from 10 to 100000) (default 20495.6)
 * @param options.coeffclamp - set coeffclamp (from 0.1 to 10) (default 1)
 * @param options.tlength - set tlength (default "384*tc/(384+tc*f)")
 * @param options.count - set transform count (from 1 to 30) (default 6)
 * @param options.fcount - set frequency count (from 0 to 10) (default 0)
 * @param options.fontfile - set axis font file
 * @param options.font - set axis font
 * @param options.fontcolor - set font color (default "st(0, (midi(f)-59.5)/12);st(1, if(between(ld(0),0,1), 0.5-0.5*cos(2*PI*ld(0)), 0));r(1-ld(1)) + b(ld(1))")
 * @param options.axisfile - set axis image
 * @param options.axis - draw axis (default true)
 * @param options.csp - set color space (from 0 to INT_MAX) (default unspecified)
 * @param options.cscheme - set color scheme (default "1|0.5|0|0|0.5|1")
 * @see https://ffmpeg.org/ffmpeg-filters.html#showcqt
 */
  showcqt(
    options?: {
    size?: FFImageSize;
    fps?: FFVideoRate;
    bar_h?: FFInt;
    axis_h?: FFInt;
    sono_h?: FFInt;
    fullhd?: FFBoolean;
    sono_v?: FFString;
    bar_v?: FFString;
    sono_g?: FFFloat;
    bar_g?: FFFloat;
    bar_t?: FFFloat;
    timeclamp?: FFDouble;
    attack?: FFDouble;
    basefreq?: FFDouble;
    endfreq?: FFDouble;
    coeffclamp?: FFFloat;
    tlength?: FFString;
    count?: FFInt;
    fcount?: FFInt;
    fontfile?: FFString;
    font?: FFString;
    fontcolor?: FFString;
    axisfile?: FFString;
    axis?: FFBoolean;
    csp?: FFInt | "unspecified" | "bt709" | "fcc" | "bt470bg" | "smpte170m" | "smpte240m" | "bt2020ncl";
    cscheme?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "showcqt", typingsInput: ["audio"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "size": options?.size,
      "fps": options?.fps,
      "bar_h": options?.bar_h,
      "axis_h": options?.axis_h,
      "sono_h": options?.sono_h,
      "fullhd": options?.fullhd,
      "sono_v": options?.sono_v,
      "bar_v": options?.bar_v,
      "sono_g": options?.sono_g,
      "bar_g": options?.bar_g,
      "bar_t": options?.bar_t,
      "timeclamp": options?.timeclamp,
      "attack": options?.attack,
      "basefreq": options?.basefreq,
      "endfreq": options?.endfreq,
      "coeffclamp": options?.coeffclamp,
      "tlength": options?.tlength,
      "count": options?.count,
      "fcount": options?.fcount,
      "fontfile": options?.fontfile,
      "font": options?.font,
      "fontcolor": options?.fontcolor,
      "axisfile": options?.axisfile,
      "axis": options?.axis,
      "csp": options?.csp,
      "cscheme": options?.cscheme,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Convert input audio to a CWT (Continuous Wavelet Transform) spectrum video output.

 *
 * @param options.size - set video size (default "640x512")
 * @param options.rate - set video rate (default "25")
 * @param options.scale - set frequency scale (from 0 to 8) (default linear)
 * @param options.iscale - set intensity scale (from 0 to 4) (default log)
 * @param options.min - set minimum frequency (from 1 to 192000) (default 20)
 * @param options.max - set maximum frequency (from 1 to 192000) (default 20000)
 * @param options.imin - set minimum intensity (from 0 to 1) (default 0)
 * @param options.imax - set maximum intensity (from 0 to 1) (default 1)
 * @param options.logb - set logarithmic basis (from 0 to 1) (default 0.0001)
 * @param options.deviation - set frequency deviation (from 0 to 100) (default 1)
 * @param options.pps - set pixels per second (from 1 to 1024) (default 64)
 * @param options.mode - set output mode (from 0 to 4) (default magnitude)
 * @param options.slide - set slide mode (from 0 to 2) (default replace)
 * @param options.direction - set direction mode (from 0 to 3) (default lr)
 * @param options.bar - set bargraph ratio (from 0 to 1) (default 0)
 * @param options.rotation - set color rotation (from -1 to 1) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#showcwt
 */
  showcwt(
    options?: {
    size?: FFImageSize;
    rate?: FFString;
    scale?: FFInt | "linear" | "log" | "bark" | "mel" | "erbs" | "sqrt" | "cbrt" | "qdrt" | "fm";
    iscale?: FFInt | "linear" | "log" | "sqrt" | "cbrt" | "qdrt";
    min?: FFFloat;
    max?: FFFloat;
    imin?: FFFloat;
    imax?: FFFloat;
    logb?: FFFloat;
    deviation?: FFFloat;
    pps?: FFInt;
    mode?: FFInt | "magnitude" | "phase" | "magphase" | "channel" | "stereo";
    slide?: FFInt | "replace" | "scroll" | "frame";
    direction?: FFInt | "lr" | "rl" | "ud" | "du";
    bar?: FFFloat;
    rotation?: FFFloat;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "showcwt", typingsInput: ["audio"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "size": options?.size,
      "rate": options?.rate,
      "scale": options?.scale,
      "iscale": options?.iscale,
      "min": options?.min,
      "max": options?.max,
      "imin": options?.imin,
      "imax": options?.imax,
      "logb": options?.logb,
      "deviation": options?.deviation,
      "pps": options?.pps,
      "mode": options?.mode,
      "slide": options?.slide,
      "direction": options?.direction,
      "bar": options?.bar,
      "rotation": options?.rotation,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Convert input audio to a frequencies video output.

 *
 * @param options.size - set video size (default "1024x512")
 * @param options.rate - set video rate (default "25")
 * @param options.mode - set display mode (from 0 to 2) (default bar)
 * @param options.ascale - set amplitude scale (from 0 to 3) (default log)
 * @param options.fscale - set frequency scale (from 0 to 2) (default lin)
 * @param options.win_size - set window size (from 16 to 65536) (default 2048)
 * @param options.win_func - set window function (from 0 to 20) (default hann)
 * @param options.overlap - set window overlap (from 0 to 1) (default 1)
 * @param options.averaging - set time averaging (from 0 to INT_MAX) (default 1)
 * @param options.colors - set channels colors (default "red|green|blue|yellow|orange|lime|pink|magenta|brown")
 * @param options.cmode - set channel mode (from 0 to 1) (default combined)
 * @param options.minamp - set minimum amplitude (from FLT_MIN to 1e-06) (default 1e-06)
 * @param options.data - set data mode (from 0 to 2) (default magnitude)
 * @param options.channels - set channels to draw (default "all")
 * @see https://ffmpeg.org/ffmpeg-filters.html#showfreqs
 */
  showfreqs(
    options?: {
    size?: FFImageSize;
    rate?: FFVideoRate;
    mode?: FFInt | "line" | "bar" | "dot";
    ascale?: FFInt | "lin" | "sqrt" | "cbrt" | "log";
    fscale?: FFInt | "lin" | "log" | "rlog";
    win_size?: FFInt;
    win_func?: FFInt | "rect" | "bartlett" | "hann" | "hanning" | "hamming" | "blackman" | "welch" | "flattop" | "bharris" | "bnuttall" | "bhann" | "sine" | "nuttall" | "lanczos" | "gauss" | "tukey" | "dolph" | "cauchy" | "parzen" | "poisson" | "bohman" | "kaiser";
    overlap?: FFFloat;
    averaging?: FFInt;
    colors?: FFString;
    cmode?: FFInt | "combined" | "separate";
    minamp?: FFFloat;
    data?: FFInt | "magnitude" | "phase" | "delay";
    channels?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "showfreqs", typingsInput: ["audio"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "size": options?.size,
      "rate": options?.rate,
      "mode": options?.mode,
      "ascale": options?.ascale,
      "fscale": options?.fscale,
      "win_size": options?.win_size,
      "win_func": options?.win_func,
      "overlap": options?.overlap,
      "averaging": options?.averaging,
      "colors": options?.colors,
      "cmode": options?.cmode,
      "minamp": options?.minamp,
      "data": options?.data,
      "channels": options?.channels,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }










/**
 * Convert input audio to a spatial video output.

 *
 * @param options.size - set video size (default "512x512")
 * @param options.win_size - set window size (from 1024 to 65536) (default 4096)
 * @param options.win_func - set window function (from 0 to 20) (default hann)
 * @param options.rate - set video rate (default "25")
 * @see https://ffmpeg.org/ffmpeg-filters.html#showspatial
 */
  showspatial(
    options?: {
    size?: FFImageSize;
    win_size?: FFInt;
    win_func?: FFInt | "rect" | "bartlett" | "hann" | "hanning" | "hamming" | "blackman" | "welch" | "flattop" | "bharris" | "bnuttall" | "bhann" | "sine" | "nuttall" | "lanczos" | "gauss" | "tukey" | "dolph" | "cauchy" | "parzen" | "poisson" | "bohman" | "kaiser";
    rate?: FFVideoRate;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "showspatial", typingsInput: ["audio"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "size": options?.size,
      "win_size": options?.win_size,
      "win_func": options?.win_func,
      "rate": options?.rate,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Convert input audio to a spectrum video output.

 *
 * @param options.size - set video size (default "640x512")
 * @param options.slide - set sliding mode (from 0 to 4) (default replace)
 * @param options.mode - set channel display mode (from 0 to 1) (default combined)
 * @param options.color - set channel coloring (from 0 to 14) (default channel)
 * @param options.scale - set display scale (from 0 to 5) (default sqrt)
 * @param options.fscale - set frequency scale (from 0 to 1) (default lin)
 * @param options.saturation - color saturation multiplier (from -10 to 10) (default 1)
 * @param options.win_func - set window function (from 0 to 20) (default hann)
 * @param options.orientation - set orientation (from 0 to 1) (default vertical)
 * @param options.overlap - set window overlap (from 0 to 1) (default 0)
 * @param options.gain - set scale gain (from 0 to 128) (default 1)
 * @param options.data - set data mode (from 0 to 2) (default magnitude)
 * @param options.rotation - color rotation (from -1 to 1) (default 0)
 * @param options.start - start frequency (from 0 to INT_MAX) (default 0)
 * @param options.stop - stop frequency (from 0 to INT_MAX) (default 0)
 * @param options.fps - set video rate (default "auto")
 * @param options.legend - draw legend (default false)
 * @param options.drange - set dynamic range in dBFS (from 10 to 200) (default 120)
 * @param options.limit - set upper limit in dBFS (from -100 to 100) (default 0)
 * @param options.opacity - set opacity strength (from 0 to 10) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#showspectrum
 */
  showspectrum(
    options?: {
    size?: FFImageSize;
    slide?: FFInt | "replace" | "scroll" | "fullframe" | "rscroll" | "lreplace";
    mode?: FFInt | "combined" | "separate";
    color?: FFInt | "channel" | "intensity" | "rainbow" | "moreland" | "nebulae" | "fire" | "fiery" | "fruit" | "cool" | "magma" | "green" | "viridis" | "plasma" | "cividis" | "terrain";
    scale?: FFInt | "lin" | "sqrt" | "cbrt" | "log" | "4thrt" | "5thrt";
    fscale?: FFInt | "lin" | "log";
    saturation?: FFFloat;
    win_func?: FFInt | "rect" | "bartlett" | "hann" | "hanning" | "hamming" | "blackman" | "welch" | "flattop" | "bharris" | "bnuttall" | "bhann" | "sine" | "nuttall" | "lanczos" | "gauss" | "tukey" | "dolph" | "cauchy" | "parzen" | "poisson" | "bohman" | "kaiser";
    orientation?: FFInt | "vertical" | "horizontal";
    overlap?: FFFloat;
    gain?: FFFloat;
    data?: FFInt | "magnitude" | "phase" | "uphase";
    rotation?: FFFloat;
    start?: FFInt;
    stop?: FFInt;
    fps?: FFString;
    legend?: FFBoolean;
    drange?: FFFloat;
    limit?: FFFloat;
    opacity?: FFFloat;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "showspectrum", typingsInput: ["audio"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "size": options?.size,
      "slide": options?.slide,
      "mode": options?.mode,
      "color": options?.color,
      "scale": options?.scale,
      "fscale": options?.fscale,
      "saturation": options?.saturation,
      "win_func": options?.win_func,
      "orientation": options?.orientation,
      "overlap": options?.overlap,
      "gain": options?.gain,
      "data": options?.data,
      "rotation": options?.rotation,
      "start": options?.start,
      "stop": options?.stop,
      "fps": options?.fps,
      "legend": options?.legend,
      "drange": options?.drange,
      "limit": options?.limit,
      "opacity": options?.opacity,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Convert input audio to a spectrum video output single picture.

 *
 * @param options.size - set video size (default "4096x2048")
 * @param options.mode - set channel display mode (from 0 to 1) (default combined)
 * @param options.color - set channel coloring (from 0 to 14) (default intensity)
 * @param options.scale - set display scale (from 0 to 5) (default log)
 * @param options.fscale - set frequency scale (from 0 to 1) (default lin)
 * @param options.saturation - color saturation multiplier (from -10 to 10) (default 1)
 * @param options.win_func - set window function (from 0 to 20) (default hann)
 * @param options.orientation - set orientation (from 0 to 1) (default vertical)
 * @param options.gain - set scale gain (from 0 to 128) (default 1)
 * @param options.legend - draw legend (default true)
 * @param options.rotation - color rotation (from -1 to 1) (default 0)
 * @param options.start - start frequency (from 0 to INT_MAX) (default 0)
 * @param options.stop - stop frequency (from 0 to INT_MAX) (default 0)
 * @param options.drange - set dynamic range in dBFS (from 10 to 200) (default 120)
 * @param options.limit - set upper limit in dBFS (from -100 to 100) (default 0)
 * @param options.opacity - set opacity strength (from 0 to 10) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#showspectrumpic
 */
  showspectrumpic(
    options?: {
    size?: FFImageSize;
    mode?: FFInt | "combined" | "separate";
    color?: FFInt | "channel" | "intensity" | "rainbow" | "moreland" | "nebulae" | "fire" | "fiery" | "fruit" | "cool" | "magma" | "green" | "viridis" | "plasma" | "cividis" | "terrain";
    scale?: FFInt | "lin" | "sqrt" | "cbrt" | "log" | "4thrt" | "5thrt";
    fscale?: FFInt | "lin" | "log";
    saturation?: FFFloat;
    win_func?: FFInt | "rect" | "bartlett" | "hann" | "hanning" | "hamming" | "blackman" | "welch" | "flattop" | "bharris" | "bnuttall" | "bhann" | "sine" | "nuttall" | "lanczos" | "gauss" | "tukey" | "dolph" | "cauchy" | "parzen" | "poisson" | "bohman" | "kaiser";
    orientation?: FFInt | "vertical" | "horizontal";
    gain?: FFFloat;
    legend?: FFBoolean;
    rotation?: FFFloat;
    start?: FFInt;
    stop?: FFInt;
    drange?: FFFloat;
    limit?: FFFloat;
    opacity?: FFFloat;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "showspectrumpic", typingsInput: ["audio"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "size": options?.size,
      "mode": options?.mode,
      "color": options?.color,
      "scale": options?.scale,
      "fscale": options?.fscale,
      "saturation": options?.saturation,
      "win_func": options?.win_func,
      "orientation": options?.orientation,
      "gain": options?.gain,
      "legend": options?.legend,
      "rotation": options?.rotation,
      "start": options?.start,
      "stop": options?.stop,
      "drange": options?.drange,
      "limit": options?.limit,
      "opacity": options?.opacity,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Convert input audio volume to video output.

 *
 * @param options.rate - set video rate (default "25")
 * @param options.b - set border width (from 0 to 5) (default 1)
 * @param options.w - set channel width (from 80 to 8192) (default 400)
 * @param options.h - set channel height (from 1 to 900) (default 20)
 * @param options.f - set fade (from 0 to 1) (default 0.95)
 * @param options.c - set volume color expression (default "PEAK*255+floor((1-PEAK)*255)*256+0xff000000")
 * @param options.t - display channel names (default true)
 * @param options.v - display volume value (default true)
 * @param options.dm - duration for max value display (from 0 to 9000) (default 0)
 * @param options.dmc - set color of the max value line (default "orange")
 * @param options.o - set orientation (from 0 to 1) (default h)
 * @param options.s - set step size (from 0 to 5) (default 0)
 * @param options.p - set background opacity (from 0 to 1) (default 0)
 * @param options.m - set mode (from 0 to 1) (default p)
 * @param options.ds - set display scale (from 0 to 1) (default lin)
 * @see https://ffmpeg.org/ffmpeg-filters.html#showvolume
 */
  showvolume(
    options?: {
    rate?: FFVideoRate;
    b?: FFInt;
    w?: FFInt;
    h?: FFInt;
    f?: FFDouble;
    c?: FFString;
    t?: FFBoolean;
    v?: FFBoolean;
    dm?: FFDouble;
    dmc?: FFColor;
    o?: FFInt | "h" | "v";
    s?: FFInt;
    p?: FFFloat;
    m?: FFInt | "p" | "r";
    ds?: FFInt | "lin" | "log";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "showvolume", typingsInput: ["audio"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "rate": options?.rate,
      "b": options?.b,
      "w": options?.w,
      "h": options?.h,
      "f": options?.f,
      "c": options?.c,
      "t": options?.t,
      "v": options?.v,
      "dm": options?.dm,
      "dmc": options?.dmc,
      "o": options?.o,
      "s": options?.s,
      "p": options?.p,
      "m": options?.m,
      "ds": options?.ds,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Convert input audio to a video output.

 *
 * @param options.size - set video size (default "600x240")
 * @param options.mode - select display mode (from 0 to 3) (default point)
 * @param options.n - set how many samples to show in the same point (from 0 to INT_MAX) (default 0/1)
 * @param options.rate - set video rate (default "25")
 * @param options.split_channels - draw channels separately (default false)
 * @param options.colors - set channels colors (default "red|green|blue|yellow|orange|lime|pink|magenta|brown")
 * @param options.scale - set amplitude scale (from 0 to 3) (default lin)
 * @param options.draw - set draw mode (from 0 to 1) (default scale)
 * @see https://ffmpeg.org/ffmpeg-filters.html#showwaves
 */
  showwaves(
    options?: {
    size?: FFImageSize;
    mode?: FFInt | "point" | "line" | "p2p" | "cline";
    n?: FFRational;
    rate?: FFVideoRate;
    split_channels?: FFBoolean;
    colors?: FFString;
    scale?: FFInt | "lin" | "log" | "sqrt" | "cbrt";
    draw?: FFInt | "scale" | "full";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "showwaves", typingsInput: ["audio"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "size": options?.size,
      "mode": options?.mode,
      "n": options?.n,
      "rate": options?.rate,
      "split_channels": options?.split_channels,
      "colors": options?.colors,
      "scale": options?.scale,
      "draw": options?.draw,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Convert input audio to a video output single picture.

 *
 * @param options.size - set video size (default "600x240")
 * @param options.split_channels - draw channels separately (default false)
 * @param options.colors - set channels colors (default "red|green|blue|yellow|orange|lime|pink|magenta|brown")
 * @param options.scale - set amplitude scale (from 0 to 3) (default lin)
 * @param options.draw - set draw mode (from 0 to 1) (default scale)
 * @param options.filter - set filter mode (from 0 to 1) (default average)
 * @see https://ffmpeg.org/ffmpeg-filters.html#showwavespic
 */
  showwavespic(
    options?: {
    size?: FFImageSize;
    split_channels?: FFBoolean;
    colors?: FFString;
    scale?: FFInt | "lin" | "log" | "sqrt" | "cbrt";
    draw?: FFInt | "scale" | "full";
    filter?: FFInt | "average" | "peak";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "showwavespic", typingsInput: ["audio"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "size": options?.size,
      "split_channels": options?.split_channels,
      "colors": options?.colors,
      "scale": options?.scale,
      "draw": options?.draw,
      "filter": options?.filter,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }












/**
 * Sidechain compressor.

 *
 * @param options.level_in - set input gain (from 0.015625 to 64) (default 1)
 * @param options.mode - set mode (from 0 to 1) (default downward)
 * @param options.threshold - set threshold (from 0.000976563 to 1) (default 0.125)
 * @param options.ratio - set ratio (from 1 to 20) (default 2)
 * @param options.attack - set attack (from 0.01 to 2000) (default 20)
 * @param options.release - set release (from 0.01 to 9000) (default 250)
 * @param options.makeup - set make up gain (from 1 to 64) (default 1)
 * @param options.knee - set knee (from 1 to 8) (default 2.82843)
 * @param options.link - set link type (from 0 to 1) (default average)
 * @param options.detection - set detection (from 0 to 1) (default rms)
 * @param options.level_sc - set sidechain gain (from 0.015625 to 64) (default 1)
 * @param options.mix - set mix (from 0 to 1) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#sidechaincompress
 */
  sidechaincompress(
    _sidechain: AudioStream,

    options?: {
    level_in?: FFDouble;
    mode?: FFInt | "downward" | "upward";
    threshold?: FFDouble;
    ratio?: FFDouble;
    attack?: FFDouble;
    release?: FFDouble;
    makeup?: FFDouble;
    knee?: FFDouble;
    link?: FFInt | "average" | "maximum";
    detection?: FFInt | "peak" | "rms";
    level_sc?: FFDouble;
    mix?: FFDouble;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "sidechaincompress", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
      [this, _sidechain],
      merge(
    {
      "level_in": options?.level_in,
      "mode": options?.mode,
      "threshold": options?.threshold,
      "ratio": options?.ratio,
      "attack": options?.attack,
      "release": options?.release,
      "makeup": options?.makeup,
      "knee": options?.knee,
      "link": options?.link,
      "detection": options?.detection,
      "level_sc": options?.level_sc,
      "mix": options?.mix,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Audio sidechain gate.

 *
 * @param options.level_in - set input level (from 0.015625 to 64) (default 1)
 * @param options.mode - set mode (from 0 to 1) (default downward)
 * @param options.range - set max gain reduction (from 0 to 1) (default 0.06125)
 * @param options.threshold - set threshold (from 0 to 1) (default 0.125)
 * @param options.ratio - set ratio (from 1 to 9000) (default 2)
 * @param options.attack - set attack (from 0.01 to 9000) (default 20)
 * @param options.release - set release (from 0.01 to 9000) (default 250)
 * @param options.makeup - set makeup gain (from 1 to 64) (default 1)
 * @param options.knee - set knee (from 1 to 8) (default 2.82843)
 * @param options.detection - set detection (from 0 to 1) (default rms)
 * @param options.link - set link (from 0 to 1) (default average)
 * @param options.level_sc - set sidechain gain (from 0.015625 to 64) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#sidechaingate
 */
  sidechaingate(
    _sidechain: AudioStream,

    options?: {
    level_in?: FFDouble;
    mode?: FFInt | "downward" | "upward";
    range?: FFDouble;
    threshold?: FFDouble;
    ratio?: FFDouble;
    attack?: FFDouble;
    release?: FFDouble;
    makeup?: FFDouble;
    knee?: FFDouble;
    detection?: FFInt | "peak" | "rms";
    link?: FFInt | "average" | "maximum";
    level_sc?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "sidechaingate", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
      [this, _sidechain],
      merge(
    {
      "level_in": options?.level_in,
      "mode": options?.mode,
      "range": options?.range,
      "threshold": options?.threshold,
      "ratio": options?.ratio,
      "attack": options?.attack,
      "release": options?.release,
      "makeup": options?.makeup,
      "knee": options?.knee,
      "detection": options?.detection,
      "link": options?.link,
      "level_sc": options?.level_sc,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }














/**
 * Detect silence.

 *
 * @param options.n - set noise tolerance (from 0 to DBL_MAX) (default 0.001)
 * @param options.d - set minimum duration in seconds (default 2)
 * @param options.mono - check each channel separately (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#silencedetect
 */
  silencedetect(
    options?: {
    n?: FFDouble;
    d?: FFDuration;
    mono?: FFBoolean;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "silencedetect", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "n": options?.n,
      "d": options?.d,
      "mono": options?.mono,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Remove silence.

 *
 * @param options.start_periods - set periods of silence parts to skip from start (from 0 to 9000) (default 0)
 * @param options.start_duration - set start duration of non-silence part (default 0)
 * @param options.start_threshold - set threshold for start silence detection (from 0 to DBL_MAX) (default 0)
 * @param options.start_silence - set start duration of silence part to keep (default 0)
 * @param options.start_mode - set which channel will trigger trimming from start (from 0 to 1) (default any)
 * @param options.stop_periods - set periods of silence parts to skip from end (from -9000 to 9000) (default 0)
 * @param options.stop_duration - set stop duration of silence part (default 0)
 * @param options.stop_threshold - set threshold for stop silence detection (from 0 to DBL_MAX) (default 0)
 * @param options.stop_silence - set stop duration of silence part to keep (default 0)
 * @param options.stop_mode - set which channel will trigger trimming from end (from 0 to 1) (default all)
 * @param options.detection - set how silence is detected (from 0 to 5) (default rms)
 * @param options.window - set duration of window for silence detection (default 0.02)
 * @param options.timestamp - set how every output frame timestamp is processed (from 0 to 1) (default write)
 * @see https://ffmpeg.org/ffmpeg-filters.html#silenceremove
 */
  silenceremove(
    options?: {
    start_periods?: FFInt;
    start_duration?: FFDuration;
    start_threshold?: FFDouble;
    start_silence?: FFDuration;
    start_mode?: FFInt | "any" | "all";
    stop_periods?: FFInt;
    stop_duration?: FFDuration;
    stop_threshold?: FFDouble;
    stop_silence?: FFDuration;
    stop_mode?: FFInt | "any" | "all";
    detection?: FFInt | "avg" | "rms" | "peak" | "median" | "ptp" | "dev";
    window?: FFDuration;
    timestamp?: FFInt | "write" | "copy";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "silenceremove", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "start_periods": options?.start_periods,
      "start_duration": options?.start_duration,
      "start_threshold": options?.start_threshold,
      "start_silence": options?.start_silence,
      "start_mode": options?.start_mode,
      "stop_periods": options?.stop_periods,
      "stop_duration": options?.stop_duration,
      "stop_threshold": options?.stop_threshold,
      "stop_silence": options?.stop_silence,
      "stop_mode": options?.stop_mode,
      "detection": options?.detection,
      "window": options?.window,
      "timestamp": options?.timestamp,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






















/**
 * Speech Normalizer.

 *
 * @param options.peak - set the peak value (from 0 to 1) (default 0.95)
 * @param options.expansion - set the max expansion factor (from 1 to 50) (default 2)
 * @param options.compression - set the max compression factor (from 1 to 50) (default 2)
 * @param options.threshold - set the threshold value (from 0 to 1) (default 0)
 * @param options._raise - set the expansion raising amount (from 0 to 1) (default 0.001)
 * @param options.fall - set the compression raising amount (from 0 to 1) (default 0.001)
 * @param options.channels - set channels to filter (default "all")
 * @param options.invert - set inverted filtering (default false)
 * @param options.link - set linked channels filtering (default false)
 * @param options.rms - set the RMS value (from 0 to 1) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#speechnorm
 */
  speechnorm(
    options?: {
    peak?: FFDouble;
    expansion?: FFDouble;
    compression?: FFDouble;
    threshold?: FFDouble;
    _raise?: FFDouble;
    fall?: FFDouble;
    channels?: FFString;
    invert?: FFBoolean;
    link?: FFBoolean;
    rms?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "speechnorm", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "peak": options?.peak,
      "expansion": options?.expansion,
      "compression": options?.compression,
      "threshold": options?.threshold,
      "raise": options?._raise,
      "fall": options?.fall,
      "channels": options?.channels,
      "invert": options?.invert,
      "link": options?.link,
      "rms": options?.rms,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }














/**
 * Apply various stereo tools.

 *
 * @param options.level_in - set level in (from 0.015625 to 64) (default 1)
 * @param options.level_out - set level out (from 0.015625 to 64) (default 1)
 * @param options.balance_in - set balance in (from -1 to 1) (default 0)
 * @param options.balance_out - set balance out (from -1 to 1) (default 0)
 * @param options.softclip - enable softclip (default false)
 * @param options.mutel - mute L (default false)
 * @param options.muter - mute R (default false)
 * @param options.phasel - phase L (default false)
 * @param options.phaser - phase R (default false)
 * @param options.mode - set stereo mode (from 0 to 10) (default lr>lr)
 * @param options.slev - set side level (from 0.015625 to 64) (default 1)
 * @param options.sbal - set side balance (from -1 to 1) (default 0)
 * @param options.mlev - set middle level (from 0.015625 to 64) (default 1)
 * @param options.mpan - set middle pan (from -1 to 1) (default 0)
 * @param options.base - set stereo base (from -1 to 1) (default 0)
 * @param options.delay - set delay (from -20 to 20) (default 0)
 * @param options.sclevel - set S/C level (from 1 to 100) (default 1)
 * @param options.phase - set stereo phase (from 0 to 360) (default 0)
 * @param options.bmode_in - set balance in mode (from 0 to 2) (default balance)
 * @param options.bmode_out - set balance out mode (from 0 to 2) (default balance)
 * @see https://ffmpeg.org/ffmpeg-filters.html#stereotools
 */
  stereotools(
    options?: {
    level_in?: FFDouble;
    level_out?: FFDouble;
    balance_in?: FFDouble;
    balance_out?: FFDouble;
    softclip?: FFBoolean;
    mutel?: FFBoolean;
    muter?: FFBoolean;
    phasel?: FFBoolean;
    phaser?: FFBoolean;
    mode?: FFInt | "lr\u003elr" | "lr\u003ems" | "ms\u003elr" | "lr\u003ell" | "lr\u003err" | "lr\u003el+r" | "lr\u003erl" | "ms\u003ell" | "ms\u003err" | "ms\u003erl" | "lr\u003el-r";
    slev?: FFDouble;
    sbal?: FFDouble;
    mlev?: FFDouble;
    mpan?: FFDouble;
    base?: FFDouble;
    delay?: FFDouble;
    sclevel?: FFDouble;
    phase?: FFDouble;
    bmode_in?: FFInt | "balance" | "amplitude" | "power";
    bmode_out?: FFInt | "balance" | "amplitude" | "power";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "stereotools", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "level_in": options?.level_in,
      "level_out": options?.level_out,
      "balance_in": options?.balance_in,
      "balance_out": options?.balance_out,
      "softclip": options?.softclip,
      "mutel": options?.mutel,
      "muter": options?.muter,
      "phasel": options?.phasel,
      "phaser": options?.phaser,
      "mode": options?.mode,
      "slev": options?.slev,
      "sbal": options?.sbal,
      "mlev": options?.mlev,
      "mpan": options?.mpan,
      "base": options?.base,
      "delay": options?.delay,
      "sclevel": options?.sclevel,
      "phase": options?.phase,
      "bmode_in": options?.bmode_in,
      "bmode_out": options?.bmode_out,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply stereo widening effect.

 *
 * @param options.delay - set delay time (from 1 to 100) (default 20)
 * @param options.feedback - set feedback gain (from 0 to 0.9) (default 0.3)
 * @param options.crossfeed - set cross feed (from 0 to 0.8) (default 0.3)
 * @param options.drymix - set dry-mix (from 0 to 1) (default 0.8)
 * @see https://ffmpeg.org/ffmpeg-filters.html#stereowiden
 */
  stereowiden(
    options?: {
    delay?: FFFloat;
    feedback?: FFFloat;
    crossfeed?: FFFloat;
    drymix?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "stereowiden", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "delay": options?.delay,
      "feedback": options?.feedback,
      "crossfeed": options?.crossfeed,
      "drymix": options?.drymix,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }










/**
 * Apply 18 band equalization filter.

 *
 * @param options._1b - set 65Hz band gain (from 0 to 20) (default 1)
 * @param options._2b - set 92Hz band gain (from 0 to 20) (default 1)
 * @param options._3b - set 131Hz band gain (from 0 to 20) (default 1)
 * @param options._4b - set 185Hz band gain (from 0 to 20) (default 1)
 * @param options._5b - set 262Hz band gain (from 0 to 20) (default 1)
 * @param options._6b - set 370Hz band gain (from 0 to 20) (default 1)
 * @param options._7b - set 523Hz band gain (from 0 to 20) (default 1)
 * @param options._8b - set 740Hz band gain (from 0 to 20) (default 1)
 * @param options._9b - set 1047Hz band gain (from 0 to 20) (default 1)
 * @param options._10b - set 1480Hz band gain (from 0 to 20) (default 1)
 * @param options._11b - set 2093Hz band gain (from 0 to 20) (default 1)
 * @param options._12b - set 2960Hz band gain (from 0 to 20) (default 1)
 * @param options._13b - set 4186Hz band gain (from 0 to 20) (default 1)
 * @param options._14b - set 5920Hz band gain (from 0 to 20) (default 1)
 * @param options._15b - set 8372Hz band gain (from 0 to 20) (default 1)
 * @param options._16b - set 11840Hz band gain (from 0 to 20) (default 1)
 * @param options._17b - set 16744Hz band gain (from 0 to 20) (default 1)
 * @param options._18b - set 20000Hz band gain (from 0 to 20) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#superequalizer
 */
  superequalizer(
    options?: {
    _1b?: FFFloat;
    _2b?: FFFloat;
    _3b?: FFFloat;
    _4b?: FFFloat;
    _5b?: FFFloat;
    _6b?: FFFloat;
    _7b?: FFFloat;
    _8b?: FFFloat;
    _9b?: FFFloat;
    _10b?: FFFloat;
    _11b?: FFFloat;
    _12b?: FFFloat;
    _13b?: FFFloat;
    _14b?: FFFloat;
    _15b?: FFFloat;
    _16b?: FFFloat;
    _17b?: FFFloat;
    _18b?: FFFloat;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "superequalizer", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "1b": options?._1b,
      "2b": options?._2b,
      "3b": options?._3b,
      "4b": options?._4b,
      "5b": options?._5b,
      "6b": options?._6b,
      "7b": options?._7b,
      "8b": options?._8b,
      "9b": options?._9b,
      "10b": options?._10b,
      "11b": options?._11b,
      "12b": options?._12b,
      "13b": options?._13b,
      "14b": options?._14b,
      "15b": options?._15b,
      "16b": options?._16b,
      "17b": options?._17b,
      "18b": options?._18b,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply audio surround upmix filter.

 *
 * @param options.chl_out - set output channel layout (default "5.1")
 * @param options.chl_in - set input channel layout (default "stereo")
 * @param options.level_in - set input level (from 0 to 10) (default 1)
 * @param options.level_out - set output level (from 0 to 10) (default 1)
 * @param options.lfe - output LFE (default true)
 * @param options.lfe_low - LFE low cut off (from 0 to 256) (default 128)
 * @param options.lfe_high - LFE high cut off (from 0 to 512) (default 256)
 * @param options.lfe_mode - set LFE channel mode (from 0 to 1) (default add)
 * @param options.smooth - set temporal smoothness strength (from 0 to 1) (default 0)
 * @param options.angle - set soundfield transform angle (from 0 to 360) (default 90)
 * @param options.focus - set soundfield transform focus (from -1 to 1) (default 0)
 * @param options.fc_in - set front center channel input level (from 0 to 10) (default 1)
 * @param options.fc_out - set front center channel output level (from 0 to 10) (default 1)
 * @param options.fl_in - set front left channel input level (from 0 to 10) (default 1)
 * @param options.fl_out - set front left channel output level (from 0 to 10) (default 1)
 * @param options.fr_in - set front right channel input level (from 0 to 10) (default 1)
 * @param options.fr_out - set front right channel output level (from 0 to 10) (default 1)
 * @param options.sl_in - set side left channel input level (from 0 to 10) (default 1)
 * @param options.sl_out - set side left channel output level (from 0 to 10) (default 1)
 * @param options.sr_in - set side right channel input level (from 0 to 10) (default 1)
 * @param options.sr_out - set side right channel output level (from 0 to 10) (default 1)
 * @param options.bl_in - set back left channel input level (from 0 to 10) (default 1)
 * @param options.bl_out - set back left channel output level (from 0 to 10) (default 1)
 * @param options.br_in - set back right channel input level (from 0 to 10) (default 1)
 * @param options.br_out - set back right channel output level (from 0 to 10) (default 1)
 * @param options.bc_in - set back center channel input level (from 0 to 10) (default 1)
 * @param options.bc_out - set back center channel output level (from 0 to 10) (default 1)
 * @param options.lfe_in - set lfe channel input level (from 0 to 10) (default 1)
 * @param options.lfe_out - set lfe channel output level (from 0 to 10) (default 1)
 * @param options.allx - set all channel's x spread (from -1 to 15) (default -1)
 * @param options.ally - set all channel's y spread (from -1 to 15) (default -1)
 * @param options.fcx - set front center channel x spread (from 0.06 to 15) (default 0.5)
 * @param options.flx - set front left channel x spread (from 0.06 to 15) (default 0.5)
 * @param options.frx - set front right channel x spread (from 0.06 to 15) (default 0.5)
 * @param options.blx - set back left channel x spread (from 0.06 to 15) (default 0.5)
 * @param options.brx - set back right channel x spread (from 0.06 to 15) (default 0.5)
 * @param options.slx - set side left channel x spread (from 0.06 to 15) (default 0.5)
 * @param options.srx - set side right channel x spread (from 0.06 to 15) (default 0.5)
 * @param options.bcx - set back center channel x spread (from 0.06 to 15) (default 0.5)
 * @param options.fcy - set front center channel y spread (from 0.06 to 15) (default 0.5)
 * @param options.fly - set front left channel y spread (from 0.06 to 15) (default 0.5)
 * @param options.fry - set front right channel y spread (from 0.06 to 15) (default 0.5)
 * @param options.bly - set back left channel y spread (from 0.06 to 15) (default 0.5)
 * @param options.bry - set back right channel y spread (from 0.06 to 15) (default 0.5)
 * @param options.sly - set side left channel y spread (from 0.06 to 15) (default 0.5)
 * @param options.sry - set side right channel y spread (from 0.06 to 15) (default 0.5)
 * @param options.bcy - set back center channel y spread (from 0.06 to 15) (default 0.5)
 * @param options.win_size - set window size (from 1024 to 65536) (default 4096)
 * @param options.win_func - set window function (from 0 to 20) (default hann)
 * @param options.overlap - set window overlap (from 0 to 1) (default 0.5)
 * @see https://ffmpeg.org/ffmpeg-filters.html#surround
 */
  surround(
    options?: {
    chl_out?: FFString;
    chl_in?: FFString;
    level_in?: FFFloat;
    level_out?: FFFloat;
    lfe?: FFBoolean;
    lfe_low?: FFInt;
    lfe_high?: FFInt;
    lfe_mode?: FFInt | "add" | "sub";
    smooth?: FFFloat;
    angle?: FFFloat;
    focus?: FFFloat;
    fc_in?: FFFloat;
    fc_out?: FFFloat;
    fl_in?: FFFloat;
    fl_out?: FFFloat;
    fr_in?: FFFloat;
    fr_out?: FFFloat;
    sl_in?: FFFloat;
    sl_out?: FFFloat;
    sr_in?: FFFloat;
    sr_out?: FFFloat;
    bl_in?: FFFloat;
    bl_out?: FFFloat;
    br_in?: FFFloat;
    br_out?: FFFloat;
    bc_in?: FFFloat;
    bc_out?: FFFloat;
    lfe_in?: FFFloat;
    lfe_out?: FFFloat;
    allx?: FFFloat;
    ally?: FFFloat;
    fcx?: FFFloat;
    flx?: FFFloat;
    frx?: FFFloat;
    blx?: FFFloat;
    brx?: FFFloat;
    slx?: FFFloat;
    srx?: FFFloat;
    bcx?: FFFloat;
    fcy?: FFFloat;
    fly?: FFFloat;
    fry?: FFFloat;
    bly?: FFFloat;
    bry?: FFFloat;
    sly?: FFFloat;
    sry?: FFFloat;
    bcy?: FFFloat;
    win_size?: FFInt;
    win_func?: FFInt | "rect" | "bartlett" | "hann" | "hanning" | "hamming" | "blackman" | "welch" | "flattop" | "bharris" | "bnuttall" | "bhann" | "sine" | "nuttall" | "lanczos" | "gauss" | "tukey" | "dolph" | "cauchy" | "parzen" | "poisson" | "bohman" | "kaiser";
    overlap?: FFFloat;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "surround", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "chl_out": options?.chl_out,
      "chl_in": options?.chl_in,
      "level_in": options?.level_in,
      "level_out": options?.level_out,
      "lfe": options?.lfe,
      "lfe_low": options?.lfe_low,
      "lfe_high": options?.lfe_high,
      "lfe_mode": options?.lfe_mode,
      "smooth": options?.smooth,
      "angle": options?.angle,
      "focus": options?.focus,
      "fc_in": options?.fc_in,
      "fc_out": options?.fc_out,
      "fl_in": options?.fl_in,
      "fl_out": options?.fl_out,
      "fr_in": options?.fr_in,
      "fr_out": options?.fr_out,
      "sl_in": options?.sl_in,
      "sl_out": options?.sl_out,
      "sr_in": options?.sr_in,
      "sr_out": options?.sr_out,
      "bl_in": options?.bl_in,
      "bl_out": options?.bl_out,
      "br_in": options?.br_in,
      "br_out": options?.br_out,
      "bc_in": options?.bc_in,
      "bc_out": options?.bc_out,
      "lfe_in": options?.lfe_in,
      "lfe_out": options?.lfe_out,
      "allx": options?.allx,
      "ally": options?.ally,
      "fcx": options?.fcx,
      "flx": options?.flx,
      "frx": options?.frx,
      "blx": options?.blx,
      "brx": options?.brx,
      "slx": options?.slx,
      "srx": options?.srx,
      "bcx": options?.bcx,
      "fcy": options?.fcy,
      "fly": options?.fly,
      "fry": options?.fry,
      "bly": options?.bly,
      "bry": options?.bry,
      "sly": options?.sly,
      "sry": options?.sry,
      "bcy": options?.bcy,
      "win_size": options?.win_size,
      "win_func": options?.win_func,
      "overlap": options?.overlap,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }




























/**
 * Apply a tilt shelf filter.

 *
 * @param options.frequency - set central frequency (from 0 to 999999) (default 3000)
 * @param options.width_type - set filter-width type (from 1 to 5) (default q)
 * @param options.width - set width (from 0 to 99999) (default 0.5)
 * @param options.gain - set gain (from -900 to 900) (default 0)
 * @param options.poles - set number of poles (from 1 to 2) (default 2)
 * @param options.mix - set mix (from 0 to 1) (default 1)
 * @param options.channels - set channels to filter (default "all")
 * @param options.normalize - normalize coefficients (default false)
 * @param options.transform - set transform type (from 0 to 6) (default di)
 * @param options.precision - set filtering precision (from -1 to 3) (default auto)
 * @param options.blocksize - set the block size (from 0 to 32768) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#tiltshelf
 */
  tiltshelf(
    options?: {
    frequency?: FFDouble;
    width_type?: FFInt | "h" | "q" | "o" | "s" | "k";
    width?: FFDouble;
    gain?: FFDouble;
    poles?: FFInt;
    mix?: FFDouble;
    channels?: FFString;
    normalize?: FFBoolean;
    transform?: FFInt | "di" | "dii" | "tdi" | "tdii" | "latt" | "svf" | "zdf";
    precision?: FFInt | "auto" | "s16" | "s32" | "f32" | "f64";
    blocksize?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "tiltshelf", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "frequency": options?.frequency,
      "width_type": options?.width_type,
      "width": options?.width,
      "gain": options?.gain,
      "poles": options?.poles,
      "mix": options?.mix,
      "channels": options?.channels,
      "normalize": options?.normalize,
      "transform": options?.transform,
      "precision": options?.precision,
      "blocksize": options?.blocksize,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }
























/**
 * Boost or cut upper frequencies.

 *
 * @param options.frequency - set central frequency (from 0 to 999999) (default 3000)
 * @param options.width_type - set filter-width type (from 1 to 5) (default q)
 * @param options.width - set width (from 0 to 99999) (default 0.5)
 * @param options.gain - set gain (from -900 to 900) (default 0)
 * @param options.poles - set number of poles (from 1 to 2) (default 2)
 * @param options.mix - set mix (from 0 to 1) (default 1)
 * @param options.channels - set channels to filter (default "all")
 * @param options.normalize - normalize coefficients (default false)
 * @param options.transform - set transform type (from 0 to 6) (default di)
 * @param options.precision - set filtering precision (from -1 to 3) (default auto)
 * @param options.blocksize - set the block size (from 0 to 32768) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#treble_002c-highshelf
 */
  treble(
    options?: {
    frequency?: FFDouble;
    width_type?: FFInt | "h" | "q" | "o" | "s" | "k";
    width?: FFDouble;
    gain?: FFDouble;
    poles?: FFInt;
    mix?: FFDouble;
    channels?: FFString;
    normalize?: FFBoolean;
    transform?: FFInt | "di" | "dii" | "tdi" | "tdii" | "latt" | "svf" | "zdf";
    precision?: FFInt | "auto" | "s16" | "s32" | "f32" | "f64";
    blocksize?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "treble", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "frequency": options?.frequency,
      "width_type": options?.width_type,
      "width": options?.width,
      "gain": options?.gain,
      "poles": options?.poles,
      "mix": options?.mix,
      "channels": options?.channels,
      "normalize": options?.normalize,
      "transform": options?.transform,
      "precision": options?.precision,
      "blocksize": options?.blocksize,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Apply tremolo effect.

 *
 * @param options.f - set frequency in hertz (from 0.1 to 20000) (default 5)
 * @param options.d - set depth as percentage (from 0 to 1) (default 0.5)
 * @see https://ffmpeg.org/ffmpeg-filters.html#tremolo
 */
  tremolo(
    options?: {
    f?: FFDouble;
    d?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "tremolo", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "f": options?.f,
      "d": options?.d,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






























/**
 * Apply vibrato effect.

 *
 * @param options.f - set frequency in hertz (from 0.1 to 20000) (default 5)
 * @param options.d - set depth as percentage (from 0 to 1) (default 0.5)
 * @see https://ffmpeg.org/ffmpeg-filters.html#vibrato
 */
  vibrato(
    options?: {
    f?: FFDouble;
    d?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "vibrato", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "f": options?.f,
      "d": options?.d,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }










/**
 * Audio Virtual Bass.

 *
 * @param options.cutoff - set virtual bass cutoff (from 100 to 500) (default 250)
 * @param options.strength - set virtual bass strength (from 0.5 to 3) (default 3)
 * @see https://ffmpeg.org/ffmpeg-filters.html#virtualbass
 */
  virtualbass(
    options?: {
    cutoff?: FFDouble;
    strength?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "virtualbass", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "cutoff": options?.cutoff,
      "strength": options?.strength,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }








/**
 * Change input volume.

 *
 * @param options.volume - set volume adjustment expression (default "1.0")
 * @param options.precision - select mathematical precision (from 0 to 2) (default float)
 * @param options.eval - specify when to evaluate expressions (from 0 to 1) (default once)
 * @param options.replaygain - Apply replaygain side data when present (from 0 to 3) (default drop)
 * @param options.replaygain_preamp - Apply replaygain pre-amplification (from -15 to 15) (default 0)
 * @param options.replaygain_noclip - Apply replaygain clipping prevention (default true)
 * @see https://ffmpeg.org/ffmpeg-filters.html#volume
 */
  volume(
    options?: {
    volume?: FFString;
    precision?: FFInt | "fixed" | "float" | "double";
    eval?: FFInt | "once" | "frame";
    replaygain?: FFInt | "drop" | "ignore" | "track" | "album";
    replaygain_preamp?: FFDouble;
    replaygain_noclip?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "volume", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
      "volume": options?.volume,
      "precision": options?.precision,
      "eval": options?.eval,
      "replaygain": options?.replaygain,
      "replaygain_preamp": options?.replaygain_preamp,
      "replaygain_noclip": options?.replaygain_noclip,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }






/**
 * Detect audio volume.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#volumedetect
 */
  volumedetect(
    options?: {
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "volumedetect", typingsInput: ["audio"], typingsOutput: ["audio"] },
      [this],
      merge(
    {
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }

































}
