// NOTE: this file is auto-generated, do not modify
/**
 * Video stream with typed filter methods.
 */


import type { AudioStream } from "./audio.js";
import { StreamType, type FFMpegFilterDef } from "@typed-ffmpeg/core/common/schema";
import { Default, Auto } from "@typed-ffmpeg/core/utils/types";
import { filterNodeFactory } from "@typed-ffmpeg/core/dag/factory";
import { merge } from "@typed-ffmpeg/core/utils/frozenRecord";
import { FilterableStream } from "@typed-ffmpeg/core/dag/baseStreams";
import { VideoStream as VideoStreamBase, FilterNode } from "@typed-ffmpeg/core/dag/nodes";
import type {
  FFBoolean, FFInt, FFInt64, FFFloat, FFDouble, FFString,
  FFDuration, FFColor, FFFlags, FFDictionary, FFPixFmt,
  FFVideoRate, FFImageSize, FFRational, FFSampleFmt, FFBinary,
} from "@typed-ffmpeg/core/types";

export class VideoStream extends VideoStreamBase {






























/**
 * Add region of interest to frame.

 *
 * @param options.x - Region distance from left edge of frame. (default "0")
 * @param options.y - Region distance from top edge of frame. (default "0")
 * @param options.w - Region width. (default "0")
 * @param options.h - Region height. (default "0")
 * @param options.qoffset - Quantisation offset to apply in the region. (from -1 to 1) (default -1/10)
 * @param options.clear - Remove any existing regions of interest before adding the new one. (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#addroi
 */
  addroi(
    options?: {
    x?: FFString;
    y?: FFString;
    w?: FFString;
    h?: FFString;
    qoffset?: FFRational;
    clear?: FFBoolean;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "addroi", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "x": options?.x,
      "y": options?.y,
      "w": options?.w,
      "h": options?.h,
      "qoffset": options?.qoffset,
      "clear": options?.clear,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }














































































/**
 * Extract an alpha channel as a grayscale image component.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#alphaextract
 */
  alphaextract(
    options?: {
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "alphaextract", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Copy the luma value of the second input into the alpha channel of the first input.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#alphamerge
 */
  alphamerge(
    _alpha: VideoStream,

    options?: {
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "alphamerge", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _alpha],
      merge(
    {
      "eof_action": options?.eofAction,
      "shortest": options?.shortest,
      "repeatlast": options?.repeatlast,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }














/**
 * Amplify changes between successive video frames.

 *
 * @param options.radius - set radius (from 1 to 63) (default 2)
 * @param options.factor - set factor (from 0 to 65535) (default 2)
 * @param options.threshold - set threshold (from 0 to 65535) (default 10)
 * @param options.tolerance - set tolerance (from 0 to 65535) (default 0)
 * @param options.low - set low limit for amplification (from 0 to 65535) (default 65535)
 * @param options.high - set high limit for amplification (from 0 to 65535) (default 65535)
 * @param options.planes - set what planes to filter (default 7)
 * @see https://ffmpeg.org/ffmpeg-filters.html#amplify
 */
  amplify(
    options?: {
    radius?: FFInt;
    factor?: FFFloat;
    threshold?: FFFloat;
    tolerance?: FFFloat;
    low?: FFFloat;
    high?: FFFloat;
    planes?: FFFlags;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "amplify", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "radius": options?.radius,
      "factor": options?.factor,
      "threshold": options?.threshold,
      "tolerance": options?.tolerance,
      "low": options?.low,
      "high": options?.high,
      "planes": options?.planes,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }




























































































/**
 * Apply an Adaptive Temporal Averaging Denoiser.

 *
 * @param options._0a - set threshold A for 1st plane (from 0 to 0.3) (default 0.02)
 * @param options._0b - set threshold B for 1st plane (from 0 to 5) (default 0.04)
 * @param options._1a - set threshold A for 2nd plane (from 0 to 0.3) (default 0.02)
 * @param options._1b - set threshold B for 2nd plane (from 0 to 5) (default 0.04)
 * @param options._2a - set threshold A for 3rd plane (from 0 to 0.3) (default 0.02)
 * @param options._2b - set threshold B for 3rd plane (from 0 to 5) (default 0.04)
 * @param options.s - set how many frames to use (from 5 to 129) (default 9)
 * @param options.p - set what planes to filter (default 7)
 * @param options.a - set variant of algorithm (from 0 to 1) (default p)
 * @param options._0s - set sigma for 1st plane (from 0 to 32767) (default 32767)
 * @param options._1s - set sigma for 2nd plane (from 0 to 32767) (default 32767)
 * @param options._2s - set sigma for 3rd plane (from 0 to 32767) (default 32767)
 * @see https://ffmpeg.org/ffmpeg-filters.html#atadenoise
 */
  atadenoise(
    options?: {
    _0a?: FFFloat;
    _0b?: FFFloat;
    _1a?: FFFloat;
    _1b?: FFFloat;
    _2a?: FFFloat;
    _2b?: FFFloat;
    s?: FFInt;
    p?: FFFlags;
    a?: FFInt | "p" | "s";
    _0s?: FFFloat;
    _1s?: FFFloat;
    _2s?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "atadenoise", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "0a": options?._0a,
      "0b": options?._0b,
      "1a": options?._1a,
      "1b": options?._1b,
      "2a": options?._2a,
      "2b": options?._2b,
      "s": options?.s,
      "p": options?.p,
      "a": options?.a,
      "0s": options?._0s,
      "1s": options?._1s,
      "2s": options?._2s,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }














/**
 * Apply Average Blur filter.

 *
 * @param options.sizeX - set horizontal size (from 1 to 1024) (default 1)
 * @param options.planes - set planes to filter (from 0 to 15) (default 15)
 * @param options.sizeY - set vertical size (from 0 to 1024) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#avgblur
 */
  avgblur(
    options?: {
    sizeX?: FFInt;
    planes?: FFInt;
    sizeY?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "avgblur", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "sizeX": options?.sizeX,
      "planes": options?.planes,
      "sizeY": options?.sizeY,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }










/**
 * Turns a static background into transparency.

 *
 * @param options.threshold - set the scene change threshold (from 0 to 1) (default 0.08)
 * @param options.similarity - set the similarity (from 0 to 1) (default 0.1)
 * @param options.blend - set the blend value (from 0 to 1) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#backgroundkey
 */
  backgroundkey(
    options?: {
    threshold?: FFFloat;
    similarity?: FFFloat;
    blend?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "backgroundkey", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "threshold": options?.threshold,
      "similarity": options?.similarity,
      "blend": options?.blend,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }












/**
 * Compute bounding box for each frame.

 *
 * @param options.min_val - set minimum luminance value for bounding box (from 0 to 65535) (default 16)
 * @see https://ffmpeg.org/ffmpeg-filters.html#bbox
 */
  bbox(
    options?: {
    min_val?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "bbox", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "min_val": options?.min_val,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Benchmark part of a filtergraph.

 *
 * @param options.action - set action (from 0 to 1) (default start)
 * @see https://ffmpeg.org/ffmpeg-filters.html#bench_002c-abench
 */
  bench(
    options?: {
    action?: FFInt | "start" | "stop";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "bench", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "action": options?.action,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply Bilateral filter.

 *
 * @param options.sigmaS - set spatial sigma (from 0 to 512) (default 0.1)
 * @param options.sigmaR - set range sigma (from 0 to 1) (default 0.1)
 * @param options.planes - set planes to filter (from 0 to 15) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#bilateral
 */
  bilateral(
    options?: {
    sigmaS?: FFFloat;
    sigmaR?: FFFloat;
    planes?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "bilateral", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "sigmaS": options?.sigmaS,
      "sigmaR": options?.sigmaR,
      "planes": options?.planes,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Measure bit plane noise.

 *
 * @param options.bitplane - set bit plane to use for measuring noise (from 1 to 16) (default 1)
 * @param options.filter - show noisy pixels (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#bitplanenoise
 */
  bitplanenoise(
    options?: {
    bitplane?: FFInt;
    filter?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "bitplanenoise", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "bitplane": options?.bitplane,
      "filter": options?.filter,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Detect video intervals that are (almost) black.

 *
 * @param options.d - set minimum detected black duration in seconds (from 0 to DBL_MAX) (default 2)
 * @param options.picture_black_ratio_th - set the picture black ratio threshold (from 0 to 1) (default 0.98)
 * @param options.pixel_black_th - set the pixel black threshold (from 0 to 1) (default 0.1)
 * @param options.alpha - check alpha instead of luma (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#blackdetect_002c-blackdetect_005fvulkan
 */
  blackdetect(
    options?: {
    d?: FFDouble;
    picture_black_ratio_th?: FFDouble;
    pixel_black_th?: FFDouble;
    alpha?: FFBoolean;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "blackdetect", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "d": options?.d,
      "picture_black_ratio_th": options?.picture_black_ratio_th,
      "pixel_black_th": options?.pixel_black_th,
      "alpha": options?.alpha,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Detect frames that are (almost) black.

 *
 * @param options.amount - percentage of the pixels that have to be below the threshold for the frame to be considered black (from 0 to 100) (default 98)
 * @param options.threshold - threshold below which a pixel value is considered black (from 0 to 255) (default 32)
 * @see https://ffmpeg.org/ffmpeg-filters.html#blackframe
 */
  blackframe(
    options?: {
    amount?: FFInt;
    threshold?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "blackframe", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "amount": options?.amount,
      "threshold": options?.threshold,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Blend two video frames into each other.

 *
 * @param options.c0_mode - set component #0 blend mode (from 0 to 39) (default normal)
 * @param options.c1_mode - set component #1 blend mode (from 0 to 39) (default normal)
 * @param options.c2_mode - set component #2 blend mode (from 0 to 39) (default normal)
 * @param options.c3_mode - set component #3 blend mode (from 0 to 39) (default normal)
 * @param options.all_mode - set blend mode for all components (from -1 to 39) (default -1)
 * @param options.c0_expr - set color component #0 expression
 * @param options.c1_expr - set color component #1 expression
 * @param options.c2_expr - set color component #2 expression
 * @param options.c3_expr - set color component #3 expression
 * @param options.all_expr - set expression for all color components
 * @param options.c0_opacity - set color component #0 opacity (from 0 to 1) (default 1)
 * @param options.c1_opacity - set color component #1 opacity (from 0 to 1) (default 1)
 * @param options.c2_opacity - set color component #2 opacity (from 0 to 1) (default 1)
 * @param options.c3_opacity - set color component #3 opacity (from 0 to 1) (default 1)
 * @param options.all_opacity - set opacity for all color components (from 0 to 1) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#blend
 */
  blend(
    _bottom: VideoStream,

    options?: {
    c0_mode?: FFInt | "addition" | "addition128" | "grainmerge" | "and" | "average" | "burn" | "darken" | "difference" | "difference128" | "grainextract" | "divide" | "dodge" | "exclusion" | "extremity" | "freeze" | "glow" | "hardlight" | "hardmix" | "heat" | "lighten" | "linearlight" | "multiply" | "multiply128" | "negation" | "normal" | "or" | "overlay" | "phoenix" | "pinlight" | "reflect" | "screen" | "softlight" | "subtract" | "vividlight" | "xor" | "softdifference" | "geometric" | "harmonic" | "bleach" | "stain" | "interpolate" | "hardoverlay";
    c1_mode?: FFInt | "addition" | "addition128" | "grainmerge" | "and" | "average" | "burn" | "darken" | "difference" | "difference128" | "grainextract" | "divide" | "dodge" | "exclusion" | "extremity" | "freeze" | "glow" | "hardlight" | "hardmix" | "heat" | "lighten" | "linearlight" | "multiply" | "multiply128" | "negation" | "normal" | "or" | "overlay" | "phoenix" | "pinlight" | "reflect" | "screen" | "softlight" | "subtract" | "vividlight" | "xor" | "softdifference" | "geometric" | "harmonic" | "bleach" | "stain" | "interpolate" | "hardoverlay";
    c2_mode?: FFInt | "addition" | "addition128" | "grainmerge" | "and" | "average" | "burn" | "darken" | "difference" | "difference128" | "grainextract" | "divide" | "dodge" | "exclusion" | "extremity" | "freeze" | "glow" | "hardlight" | "hardmix" | "heat" | "lighten" | "linearlight" | "multiply" | "multiply128" | "negation" | "normal" | "or" | "overlay" | "phoenix" | "pinlight" | "reflect" | "screen" | "softlight" | "subtract" | "vividlight" | "xor" | "softdifference" | "geometric" | "harmonic" | "bleach" | "stain" | "interpolate" | "hardoverlay";
    c3_mode?: FFInt | "addition" | "addition128" | "grainmerge" | "and" | "average" | "burn" | "darken" | "difference" | "difference128" | "grainextract" | "divide" | "dodge" | "exclusion" | "extremity" | "freeze" | "glow" | "hardlight" | "hardmix" | "heat" | "lighten" | "linearlight" | "multiply" | "multiply128" | "negation" | "normal" | "or" | "overlay" | "phoenix" | "pinlight" | "reflect" | "screen" | "softlight" | "subtract" | "vividlight" | "xor" | "softdifference" | "geometric" | "harmonic" | "bleach" | "stain" | "interpolate" | "hardoverlay";
    all_mode?: FFInt | "addition" | "addition128" | "grainmerge" | "and" | "average" | "burn" | "darken" | "difference" | "difference128" | "grainextract" | "divide" | "dodge" | "exclusion" | "extremity" | "freeze" | "glow" | "hardlight" | "hardmix" | "heat" | "lighten" | "linearlight" | "multiply" | "multiply128" | "negation" | "normal" | "or" | "overlay" | "phoenix" | "pinlight" | "reflect" | "screen" | "softlight" | "subtract" | "vividlight" | "xor" | "softdifference" | "geometric" | "harmonic" | "bleach" | "stain" | "interpolate" | "hardoverlay";
    c0_expr?: FFString;
    c1_expr?: FFString;
    c2_expr?: FFString;
    c3_expr?: FFString;
    all_expr?: FFString;
    c0_opacity?: FFDouble;
    c1_opacity?: FFDouble;
    c2_opacity?: FFDouble;
    c3_opacity?: FFDouble;
    all_opacity?: FFDouble;
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "blend", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _bottom],
      merge(
    {
      "c0_mode": options?.c0_mode,
      "c1_mode": options?.c1_mode,
      "c2_mode": options?.c2_mode,
      "c3_mode": options?.c3_mode,
      "all_mode": options?.all_mode,
      "c0_expr": options?.c0_expr,
      "c1_expr": options?.c1_expr,
      "c2_expr": options?.c2_expr,
      "c3_expr": options?.c3_expr,
      "all_expr": options?.all_expr,
      "c0_opacity": options?.c0_opacity,
      "c1_opacity": options?.c1_opacity,
      "c2_opacity": options?.c2_opacity,
      "c3_opacity": options?.c3_opacity,
      "all_opacity": options?.all_opacity,
      "eof_action": options?.eofAction,
      "shortest": options?.shortest,
      "repeatlast": options?.repeatlast,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Blockdetect filter.

 *
 * @param options.period_min - Minimum period to search for (from 2 to 32) (default 3)
 * @param options.period_max - Maximum period to search for (from 2 to 64) (default 24)
 * @param options.planes - set planes to filter (from 0 to 15) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#blockdetect
 */
  blockdetect(
    options?: {
    period_min?: FFInt;
    period_max?: FFInt;
    planes?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "blockdetect", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "period_min": options?.period_min,
      "period_max": options?.period_max,
      "planes": options?.planes,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Blurdetect filter.

 *
 * @param options.high - set high threshold (from 0 to 1) (default 0.117647)
 * @param options.low - set low threshold (from 0 to 1) (default 0.0588235)
 * @param options.radius - search radius for maxima detection (from 1 to 100) (default 50)
 * @param options.block_pct - block pooling threshold when calculating blurriness (from 1 to 100) (default 80)
 * @param options.block_width - block size for block-based abbreviation of blurriness (from -1 to INT_MAX) (default -1)
 * @param options.planes - set planes to filter (from 0 to 15) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#blurdetect
 */
  blurdetect(
    options?: {
    high?: FFFloat;
    low?: FFFloat;
    radius?: FFInt;
    block_pct?: FFInt;
    block_width?: FFInt;
    planes?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "blurdetect", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "high": options?.high,
      "low": options?.low,
      "radius": options?.radius,
      "block_pct": options?.block_pct,
      "block_width": options?.block_width,
      "planes": options?.planes,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Blur the input.

 *
 * @param options.luma_radius - Radius of the luma blurring box (default "2")
 * @param options.luma_power - How many times should the boxblur be applied to luma (from 0 to INT_MAX) (default 2)
 * @param options.chroma_radius - Radius of the chroma blurring box
 * @param options.chroma_power - How many times should the boxblur be applied to chroma (from -1 to INT_MAX) (default -1)
 * @param options.alpha_radius - Radius of the alpha blurring box
 * @param options.alpha_power - How many times should the boxblur be applied to alpha (from -1 to INT_MAX) (default -1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#boxblur
 */
  boxblur(
    options?: {
    luma_radius?: FFString;
    luma_power?: FFInt;
    chroma_radius?: FFString;
    chroma_power?: FFInt;
    alpha_radius?: FFString;
    alpha_power?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "boxblur", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "luma_radius": options?.luma_radius,
      "luma_power": options?.luma_power,
      "chroma_radius": options?.chroma_radius,
      "chroma_power": options?.chroma_power,
      "alpha_radius": options?.alpha_radius,
      "alpha_power": options?.alpha_power,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }










/**
 * Deinterlace the input image.

 *
 * @param options.mode - specify the interlacing mode (from 0 to 1) (default send_field)
 * @param options.parity - specify the assumed picture field parity (from -1 to 1) (default auto)
 * @param options.deint - specify which frames to deinterlace (from 0 to 1) (default all)
 * @see https://ffmpeg.org/ffmpeg-filters.html#bwdif
 */
  bwdif(
    options?: {
    mode?: FFInt | "send_frame" | "send_field";
    parity?: FFInt | "tff" | "bff" | "auto";
    deint?: FFInt | "all" | "interlaced";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "bwdif", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "mode": options?.mode,
      "parity": options?.parity,
      "deint": options?.deint,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Contrast Adaptive Sharpen.

 *
 * @param options.strength - set the sharpening strength (from 0 to 1) (default 0)
 * @param options.planes - set what planes to filter (default 7)
 * @see https://ffmpeg.org/ffmpeg-filters.html#cas
 */
  cas(
    options?: {
    strength?: FFFloat;
    planes?: FFFlags;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "cas", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "strength": options?.strength,
      "planes": options?.planes,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Repack CEA-708 closed caption metadata

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#ccrepack
 */
  ccrepack(
    options?: {
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "ccrepack", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }














/**
 * Turns a certain color range into gray.

 *
 * @param options.color - set the chromahold key color (default "black")
 * @param options.similarity - set the chromahold similarity value (from 1e-05 to 1) (default 0.01)
 * @param options.blend - set the chromahold blend value (from 0 to 1) (default 0)
 * @param options.yuv - color parameter is in yuv instead of rgb (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#chromahold
 */
  chromahold(
    options?: {
    color?: FFColor;
    similarity?: FFFloat;
    blend?: FFFloat;
    yuv?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "chromahold", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "color": options?.color,
      "similarity": options?.similarity,
      "blend": options?.blend,
      "yuv": options?.yuv,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Turns a certain color into transparency. Operates on YUV colors.

 *
 * @param options.color - set the chromakey key color (default "black")
 * @param options.similarity - set the chromakey similarity value (from 1e-05 to 1) (default 0.01)
 * @param options.blend - set the chromakey key blend value (from 0 to 1) (default 0)
 * @param options.yuv - color parameter is in yuv instead of rgb (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#chromakey
 */
  chromakey(
    options?: {
    color?: FFColor;
    similarity?: FFFloat;
    blend?: FFFloat;
    yuv?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "chromakey", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "color": options?.color,
      "similarity": options?.similarity,
      "blend": options?.blend,
      "yuv": options?.yuv,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Reduce chrominance noise.

 *
 * @param options.thres - set y+u+v threshold (from 1 to 200) (default 30)
 * @param options.sizew - set horizontal patch size (from 1 to 100) (default 5)
 * @param options.sizeh - set vertical patch size (from 1 to 100) (default 5)
 * @param options.stepw - set horizontal step (from 1 to 50) (default 1)
 * @param options.steph - set vertical step (from 1 to 50) (default 1)
 * @param options.threy - set y threshold (from 1 to 200) (default 200)
 * @param options.threu - set u threshold (from 1 to 200) (default 200)
 * @param options.threv - set v threshold (from 1 to 200) (default 200)
 * @param options.distance - set distance type (from 0 to 1) (default manhattan)
 * @see https://ffmpeg.org/ffmpeg-filters.html#chromanr
 */
  chromanr(
    options?: {
    thres?: FFFloat;
    sizew?: FFInt;
    sizeh?: FFInt;
    stepw?: FFInt;
    steph?: FFInt;
    threy?: FFFloat;
    threu?: FFFloat;
    threv?: FFFloat;
    distance?: FFInt | "manhattan" | "euclidean";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "chromanr", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "thres": options?.thres,
      "sizew": options?.sizew,
      "sizeh": options?.sizeh,
      "stepw": options?.stepw,
      "steph": options?.steph,
      "threy": options?.threy,
      "threu": options?.threu,
      "threv": options?.threv,
      "distance": options?.distance,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Shift chroma.

 *
 * @param options.cbh - shift chroma-blue horizontally (from -255 to 255) (default 0)
 * @param options.cbv - shift chroma-blue vertically (from -255 to 255) (default 0)
 * @param options.crh - shift chroma-red horizontally (from -255 to 255) (default 0)
 * @param options.crv - shift chroma-red vertically (from -255 to 255) (default 0)
 * @param options.edge - set edge operation (from 0 to 1) (default smear)
 * @see https://ffmpeg.org/ffmpeg-filters.html#chromashift
 */
  chromashift(
    options?: {
    cbh?: FFInt;
    cbv?: FFInt;
    crh?: FFInt;
    crv?: FFInt;
    edge?: FFInt | "smear" | "wrap";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "chromashift", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "cbh": options?.cbh,
      "cbv": options?.cbv,
      "crh": options?.crh,
      "crv": options?.crv,
      "edge": options?.edge,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Video CIE scope.

 *
 * @param options.system - set color system (from 0 to 9) (default hdtv)
 * @param options.cie - set cie system (from 0 to 2) (default xyy)
 * @param options.gamuts - set what gamuts to draw (default 0)
 * @param options.size - set ciescope size (from 256 to 8192) (default 512)
 * @param options.intensity - set ciescope intensity (from 0 to 1) (default 0.001)
 * @param options.contrast - (from 0 to 1) (default 0.75)
 * @param options.corrgamma - (default true)
 * @param options.showwhite - (default false)
 * @param options.gamma - (from 0.1 to 6) (default 2.6)
 * @param options.fill - fill with CIE colors (default true)
 * @see https://ffmpeg.org/ffmpeg-filters.html#ciescope
 */
  ciescope(
    options?: {
    system?: FFInt | "ntsc" | "470m" | "ebu" | "470bg" | "smpte" | "240m" | "apple" | "widergb" | "cie1931" | "hdtv" | "rec709" | "uhdtv" | "rec2020" | "dcip3";
    cie?: FFInt | "xyy" | "ucs" | "luv";
    gamuts?: FFFlags | "ntsc" | "470m" | "ebu" | "470bg" | "smpte" | "240m" | "apple" | "widergb" | "cie1931" | "hdtv" | "rec709" | "uhdtv" | "rec2020" | "dcip3";
    size?: FFInt;
    intensity?: FFFloat;
    contrast?: FFFloat;
    corrgamma?: FFBoolean;
    showwhite?: FFBoolean;
    gamma?: FFDouble;
    fill?: FFBoolean;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "ciescope", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "system": options?.system,
      "cie": options?.cie,
      "gamuts": options?.gamuts,
      "size": options?.size,
      "intensity": options?.intensity,
      "contrast": options?.contrast,
      "corrgamma": options?.corrgamma,
      "showwhite": options?.showwhite,
      "gamma": options?.gamma,
      "fill": options?.fill,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Visualize information about some codecs.

 *
 * @param options.mv - set motion vectors to visualize (default 0)
 * @param options.qp - (default false)
 * @param options.mv_type - set motion vectors type (default 0)
 * @param options.frame_type - set frame types to visualize motion vectors of (default 0)
 * @param options.block - set block partitioning structure to visualize (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#codecview
 */
  codecview(
    options?: {
    mv?: FFFlags | "pf" | "bf" | "bb";
    qp?: FFBoolean;
    mv_type?: FFFlags | "fp" | "bp";
    frame_type?: FFFlags | "if" | "pf" | "bf";
    block?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "codecview", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "mv": options?.mv,
      "qp": options?.qp,
      "mv_type": options?.mv_type,
      "frame_type": options?.frame_type,
      "block": options?.block,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Adjust the color balance.

 *
 * @param options.rs - set red shadows (from -1 to 1) (default 0)
 * @param options.gs - set green shadows (from -1 to 1) (default 0)
 * @param options.bs - set blue shadows (from -1 to 1) (default 0)
 * @param options.rm - set red midtones (from -1 to 1) (default 0)
 * @param options.gm - set green midtones (from -1 to 1) (default 0)
 * @param options.bm - set blue midtones (from -1 to 1) (default 0)
 * @param options.rh - set red highlights (from -1 to 1) (default 0)
 * @param options.gh - set green highlights (from -1 to 1) (default 0)
 * @param options.bh - set blue highlights (from -1 to 1) (default 0)
 * @param options.pl - preserve lightness (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#colorbalance
 */
  colorbalance(
    options?: {
    rs?: FFFloat;
    gs?: FFFloat;
    bs?: FFFloat;
    rm?: FFFloat;
    gm?: FFFloat;
    bm?: FFFloat;
    rh?: FFFloat;
    gh?: FFFloat;
    bh?: FFFloat;
    pl?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "colorbalance", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "rs": options?.rs,
      "gs": options?.gs,
      "bs": options?.bs,
      "rm": options?.rm,
      "gm": options?.gm,
      "bm": options?.bm,
      "rh": options?.rh,
      "gh": options?.gh,
      "bh": options?.bh,
      "pl": options?.pl,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Adjust colors by mixing color channels.

 *
 * @param options.rr - set the red gain for the red channel (from -2 to 2) (default 1)
 * @param options.rg - set the green gain for the red channel (from -2 to 2) (default 0)
 * @param options.rb - set the blue gain for the red channel (from -2 to 2) (default 0)
 * @param options.ra - set the alpha gain for the red channel (from -2 to 2) (default 0)
 * @param options.gr - set the red gain for the green channel (from -2 to 2) (default 0)
 * @param options.gg - set the green gain for the green channel (from -2 to 2) (default 1)
 * @param options.gb - set the blue gain for the green channel (from -2 to 2) (default 0)
 * @param options.ga - set the alpha gain for the green channel (from -2 to 2) (default 0)
 * @param options.br - set the red gain for the blue channel (from -2 to 2) (default 0)
 * @param options.bg - set the green gain for the blue channel (from -2 to 2) (default 0)
 * @param options.bb - set the blue gain for the blue channel (from -2 to 2) (default 1)
 * @param options.ba - set the alpha gain for the blue channel (from -2 to 2) (default 0)
 * @param options.ar - set the red gain for the alpha channel (from -2 to 2) (default 0)
 * @param options.ag - set the green gain for the alpha channel (from -2 to 2) (default 0)
 * @param options.ab - set the blue gain for the alpha channel (from -2 to 2) (default 0)
 * @param options.aa - set the alpha gain for the alpha channel (from -2 to 2) (default 1)
 * @param options.pc - set the preserve color mode (from 0 to 6) (default none)
 * @param options.pa - set the preserve color amount (from 0 to 1) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#colorchannelmixer
 */
  colorchannelmixer(
    options?: {
    rr?: FFDouble;
    rg?: FFDouble;
    rb?: FFDouble;
    ra?: FFDouble;
    gr?: FFDouble;
    gg?: FFDouble;
    gb?: FFDouble;
    ga?: FFDouble;
    br?: FFDouble;
    bg?: FFDouble;
    bb?: FFDouble;
    ba?: FFDouble;
    ar?: FFDouble;
    ag?: FFDouble;
    ab?: FFDouble;
    aa?: FFDouble;
    pc?: FFInt | "none" | "lum" | "max" | "avg" | "sum" | "nrm" | "pwr";
    pa?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "colorchannelmixer", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "rr": options?.rr,
      "rg": options?.rg,
      "rb": options?.rb,
      "ra": options?.ra,
      "gr": options?.gr,
      "gg": options?.gg,
      "gb": options?.gb,
      "ga": options?.ga,
      "br": options?.br,
      "bg": options?.bg,
      "bb": options?.bb,
      "ba": options?.ba,
      "ar": options?.ar,
      "ag": options?.ag,
      "ab": options?.ab,
      "aa": options?.aa,
      "pc": options?.pc,
      "pa": options?.pa,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Adjust color contrast between RGB components.

 *
 * @param options.rc - set the red-cyan contrast (from -1 to 1) (default 0)
 * @param options.gm - set the green-magenta contrast (from -1 to 1) (default 0)
 * @param options.by - set the blue-yellow contrast (from -1 to 1) (default 0)
 * @param options.rcw - set the red-cyan weight (from 0 to 1) (default 0)
 * @param options.gmw - set the green-magenta weight (from 0 to 1) (default 0)
 * @param options.byw - set the blue-yellow weight (from 0 to 1) (default 0)
 * @param options.pl - set the amount of preserving lightness (from 0 to 1) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#colorcontrast
 */
  colorcontrast(
    options?: {
    rc?: FFFloat;
    gm?: FFFloat;
    by?: FFFloat;
    rcw?: FFFloat;
    gmw?: FFFloat;
    byw?: FFFloat;
    pl?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "colorcontrast", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "rc": options?.rc,
      "gm": options?.gm,
      "by": options?.by,
      "rcw": options?.rcw,
      "gmw": options?.gmw,
      "byw": options?.byw,
      "pl": options?.pl,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Adjust color white balance selectively for blacks and whites.

 *
 * @param options.rl - set the red shadow spot (from -1 to 1) (default 0)
 * @param options.bl - set the blue shadow spot (from -1 to 1) (default 0)
 * @param options.rh - set the red highlight spot (from -1 to 1) (default 0)
 * @param options.bh - set the blue highlight spot (from -1 to 1) (default 0)
 * @param options.saturation - set the amount of saturation (from -3 to 3) (default 1)
 * @param options.analyze - set the analyze mode (from 0 to 3) (default manual)
 * @see https://ffmpeg.org/ffmpeg-filters.html#colorcorrect
 */
  colorcorrect(
    options?: {
    rl?: FFFloat;
    bl?: FFFloat;
    rh?: FFFloat;
    bh?: FFFloat;
    saturation?: FFFloat;
    analyze?: FFInt | "manual" | "average" | "minmax" | "median";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "colorcorrect", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "rl": options?.rl,
      "bl": options?.bl,
      "rh": options?.rh,
      "bh": options?.bh,
      "saturation": options?.saturation,
      "analyze": options?.analyze,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Detect video color properties.
 *
 * Note: New in FFmpeg 8.0.
 *
 * @param options.mode - Image properties to detect (default color_range+alpha_mode+all)
 * @see https://ffmpeg.org/ffmpeg-filters.html#colordetect
 */
  colordetect(
    options?: {
    mode?: FFFlags | "color_range" | "alpha_mode" | "all";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "colordetect", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "mode": options?.mode,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Turns a certain color range into gray. Operates on RGB colors.

 *
 * @param options.color - set the colorhold key color (default "black")
 * @param options.similarity - set the colorhold similarity value (from 1e-05 to 1) (default 0.01)
 * @param options.blend - set the colorhold blend value (from 0 to 1) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#colorhold
 */
  colorhold(
    options?: {
    color?: FFColor;
    similarity?: FFFloat;
    blend?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "colorhold", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "color": options?.color,
      "similarity": options?.similarity,
      "blend": options?.blend,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Overlay a solid color on the video stream.

 *
 * @param options.hue - set the hue (from 0 to 360) (default 0)
 * @param options.saturation - set the saturation (from 0 to 1) (default 0.5)
 * @param options.lightness - set the lightness (from 0 to 1) (default 0.5)
 * @param options.mix - set the mix of source lightness (from 0 to 1) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#colorize
 */
  colorize(
    options?: {
    hue?: FFFloat;
    saturation?: FFFloat;
    lightness?: FFFloat;
    mix?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "colorize", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "hue": options?.hue,
      "saturation": options?.saturation,
      "lightness": options?.lightness,
      "mix": options?.mix,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Turns a certain color into transparency. Operates on RGB colors.

 *
 * @param options.color - set the colorkey key color (default "black")
 * @param options.similarity - set the colorkey similarity value (from 1e-05 to 1) (default 0.01)
 * @param options.blend - set the colorkey key blend value (from 0 to 1) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#colorkey
 */
  colorkey(
    options?: {
    color?: FFColor;
    similarity?: FFFloat;
    blend?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "colorkey", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "color": options?.color,
      "similarity": options?.similarity,
      "blend": options?.blend,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Adjust the color levels.

 *
 * @param options.rimin - set input red black point (from -1 to 1) (default 0)
 * @param options.gimin - set input green black point (from -1 to 1) (default 0)
 * @param options.bimin - set input blue black point (from -1 to 1) (default 0)
 * @param options.aimin - set input alpha black point (from -1 to 1) (default 0)
 * @param options.rimax - set input red white point (from -1 to 1) (default 1)
 * @param options.gimax - set input green white point (from -1 to 1) (default 1)
 * @param options.bimax - set input blue white point (from -1 to 1) (default 1)
 * @param options.aimax - set input alpha white point (from -1 to 1) (default 1)
 * @param options.romin - set output red black point (from 0 to 1) (default 0)
 * @param options.gomin - set output green black point (from 0 to 1) (default 0)
 * @param options.bomin - set output blue black point (from 0 to 1) (default 0)
 * @param options.aomin - set output alpha black point (from 0 to 1) (default 0)
 * @param options.romax - set output red white point (from 0 to 1) (default 1)
 * @param options.gomax - set output green white point (from 0 to 1) (default 1)
 * @param options.bomax - set output blue white point (from 0 to 1) (default 1)
 * @param options.aomax - set output alpha white point (from 0 to 1) (default 1)
 * @param options.preserve - set preserve color mode (from 0 to 6) (default none)
 * @see https://ffmpeg.org/ffmpeg-filters.html#colorlevels
 */
  colorlevels(
    options?: {
    rimin?: FFDouble;
    gimin?: FFDouble;
    bimin?: FFDouble;
    aimin?: FFDouble;
    rimax?: FFDouble;
    gimax?: FFDouble;
    bimax?: FFDouble;
    aimax?: FFDouble;
    romin?: FFDouble;
    gomin?: FFDouble;
    bomin?: FFDouble;
    aomin?: FFDouble;
    romax?: FFDouble;
    gomax?: FFDouble;
    bomax?: FFDouble;
    aomax?: FFDouble;
    preserve?: FFInt | "none" | "lum" | "max" | "avg" | "sum" | "nrm" | "pwr";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "colorlevels", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "rimin": options?.rimin,
      "gimin": options?.gimin,
      "bimin": options?.bimin,
      "aimin": options?.aimin,
      "rimax": options?.rimax,
      "gimax": options?.gimax,
      "bimax": options?.bimax,
      "aimax": options?.aimax,
      "romin": options?.romin,
      "gomin": options?.gomin,
      "bomin": options?.bomin,
      "aomin": options?.aomin,
      "romax": options?.romax,
      "gomax": options?.gomax,
      "bomax": options?.bomax,
      "aomax": options?.aomax,
      "preserve": options?.preserve,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply custom Color Maps to video stream.

 *
 * @param options.patch_size - set patch size (default "64x64")
 * @param options.nb_patches - set number of patches (from 0 to 64) (default 0)
 * @param options._type - set the target type used (from 0 to 1) (default absolute)
 * @param options.kernel - set the kernel used for measuring color difference (from 0 to 1) (default euclidean)
 * @see https://ffmpeg.org/ffmpeg-filters.html#colormap
 */
  colormap(
    _source: VideoStream,
    _target: VideoStream,

    options?: {
    patch_size?: FFImageSize;
    nb_patches?: FFInt;
    _type?: FFInt | "relative" | "absolute";
    kernel?: FFInt | "euclidean" | "weuclidean";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "colormap", typingsInput: ["video", "video", "video"], typingsOutput: ["video"] },
      [this, _source, _target],
      merge(
    {
      "patch_size": options?.patch_size,
      "nb_patches": options?.nb_patches,
      "type": options?._type,
      "kernel": options?.kernel,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Convert color matrix.

 *
 * @param options.src - set source color matrix (from -1 to 4) (default -1)
 * @param options.dst - set destination color matrix (from -1 to 4) (default -1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#colormatrix
 */
  colormatrix(
    options?: {
    src?: FFInt | "bt709" | "fcc" | "bt601" | "bt470" | "bt470bg" | "smpte170m" | "smpte240m" | "bt2020";
    dst?: FFInt | "bt709" | "fcc" | "bt601" | "bt470" | "bt470bg" | "smpte170m" | "smpte240m" | "bt2020";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "colormatrix", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "src": options?.src,
      "dst": options?.dst,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Convert between colorspaces.

 *
 * @param options.all - Set all color properties together (from 0 to 8) (default 0)
 * @param options.space - Output colorspace (from 0 to 17) (default 2)
 * @param options.range - Output color range (from 0 to 2) (default 0)
 * @param options.primaries - Output color primaries (from 0 to 256) (default 2)
 * @param options.trc - Output transfer characteristics (from 0 to 256) (default 2)
 * @param options.format - Output pixel format (from -1 to 161) (default -1)
 * @param options.fast - Ignore primary chromaticity and gamma correction (default false)
 * @param options.dither - Dithering mode (from 0 to 1) (default none)
 * @param options.wpadapt - Whitepoint adaptation method (from 0 to 2) (default bradford)
 * @param options.clipgamut - Controls how to clip out-of-gamut colors that arise as a result of colorspace conversion. (from 0 to 1) (default none)
 * @param options.iall - Set all input color properties together (from 0 to 8) (default 0)
 * @param options.ispace - Input colorspace (from 0 to 22) (default 2)
 * @param options.irange - Input color range (from 0 to 2) (default 0)
 * @param options.iprimaries - Input color primaries (from 0 to 256) (default 2)
 * @param options.itrc - Input transfer characteristics (from 0 to 256) (default 2)
 * @see https://ffmpeg.org/ffmpeg-filters.html#colorspace
 */
  colorspace(
    options?: {
    all?: FFInt | "bt470m" | "bt470bg" | "bt601-6-525" | "bt601-6-625" | "bt709" | "smpte170m" | "smpte240m" | "bt2020";
    space?: FFInt | "bt709" | "fcc" | "bt470bg" | "smpte170m" | "smpte240m" | "ycgco" | "gbr" | "bt2020nc" | "bt2020ncl";
    range?: FFInt | "tv" | "mpeg" | "pc" | "jpeg";
    primaries?: FFInt | "bt709" | "bt470m" | "bt470bg" | "smpte170m" | "smpte240m" | "smpte428" | "film" | "smpte431" | "smpte432" | "bt2020" | "jedec-p22" | "ebu3213" | "vgamut";
    trc?: FFInt | "bt709" | "bt470m" | "gamma22" | "bt470bg" | "gamma28" | "smpte170m" | "smpte240m" | "linear" | "srgb" | "iec61966-2-1" | "xvycc" | "iec61966-2-4" | "bt2020-10" | "bt2020-12" | "vlog";
    format?: FFInt | "yuv420p" | "yuv420p10" | "yuv420p12" | "yuv422p" | "yuv422p10" | "yuv422p12" | "yuv444p" | "yuv444p10" | "yuv444p12";
    fast?: FFBoolean;
    dither?: FFInt | "none" | "fsb";
    wpadapt?: FFInt | "bradford" | "vonkries" | "identity";
    clipgamut?: FFInt | "none" | "rgb";
    iall?: FFInt | "bt470m" | "bt470bg" | "bt601-6-525" | "bt601-6-625" | "bt709" | "smpte170m" | "smpte240m" | "bt2020";
    ispace?: FFInt | "bt709" | "fcc" | "bt470bg" | "smpte170m" | "smpte240m" | "ycgco" | "gbr" | "bt2020nc" | "bt2020ncl";
    irange?: FFInt | "tv" | "mpeg" | "pc" | "jpeg";
    iprimaries?: FFInt | "bt709" | "bt470m" | "bt470bg" | "smpte170m" | "smpte240m" | "smpte428" | "film" | "smpte431" | "smpte432" | "bt2020" | "jedec-p22" | "ebu3213" | "vgamut";
    itrc?: FFInt | "bt709" | "bt470m" | "gamma22" | "bt470bg" | "gamma28" | "smpte170m" | "smpte240m" | "linear" | "srgb" | "iec61966-2-1" | "xvycc" | "iec61966-2-4" | "bt2020-10" | "bt2020-12" | "vlog";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "colorspace", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "all": options?.all,
      "space": options?.space,
      "range": options?.range,
      "primaries": options?.primaries,
      "trc": options?.trc,
      "format": options?.format,
      "fast": options?.fast,
      "dither": options?.dither,
      "wpadapt": options?.wpadapt,
      "clipgamut": options?.clipgamut,
      "iall": options?.iall,
      "ispace": options?.ispace,
      "irange": options?.irange,
      "iprimaries": options?.iprimaries,
      "itrc": options?.itrc,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Adjust color temperature of video.

 *
 * @param options.temperature - set the temperature in Kelvin (from 1000 to 40000) (default 6500)
 * @param options.mix - set the mix with filtered output (from 0 to 1) (default 1)
 * @param options.pl - set the amount of preserving lightness (from 0 to 1) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#colortemperature
 */
  colortemperature(
    options?: {
    temperature?: FFFloat;
    mix?: FFFloat;
    pl?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "colortemperature", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "temperature": options?.temperature,
      "mix": options?.mix,
      "pl": options?.pl,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }












/**
 * Apply convolution filter.

 *
 * @param options._0m - set matrix for 1st plane (default "0 0 0 0 1 0 0 0 0")
 * @param options._1m - set matrix for 2nd plane (default "0 0 0 0 1 0 0 0 0")
 * @param options._2m - set matrix for 3rd plane (default "0 0 0 0 1 0 0 0 0")
 * @param options._3m - set matrix for 4th plane (default "0 0 0 0 1 0 0 0 0")
 * @param options._0rdiv - set rdiv for 1st plane (from 0 to INT_MAX) (default 0)
 * @param options._1rdiv - set rdiv for 2nd plane (from 0 to INT_MAX) (default 0)
 * @param options._2rdiv - set rdiv for 3rd plane (from 0 to INT_MAX) (default 0)
 * @param options._3rdiv - set rdiv for 4th plane (from 0 to INT_MAX) (default 0)
 * @param options._0bias - set bias for 1st plane (from 0 to INT_MAX) (default 0)
 * @param options._1bias - set bias for 2nd plane (from 0 to INT_MAX) (default 0)
 * @param options._2bias - set bias for 3rd plane (from 0 to INT_MAX) (default 0)
 * @param options._3bias - set bias for 4th plane (from 0 to INT_MAX) (default 0)
 * @param options._0mode - set matrix mode for 1st plane (from 0 to 2) (default square)
 * @param options._1mode - set matrix mode for 2nd plane (from 0 to 2) (default square)
 * @param options._2mode - set matrix mode for 3rd plane (from 0 to 2) (default square)
 * @param options._3mode - set matrix mode for 4th plane (from 0 to 2) (default square)
 * @see https://ffmpeg.org/ffmpeg-filters.html#convolution
 */
  convolution(
    options?: {
    _0m?: FFString;
    _1m?: FFString;
    _2m?: FFString;
    _3m?: FFString;
    _0rdiv?: FFFloat;
    _1rdiv?: FFFloat;
    _2rdiv?: FFFloat;
    _3rdiv?: FFFloat;
    _0bias?: FFFloat;
    _1bias?: FFFloat;
    _2bias?: FFFloat;
    _3bias?: FFFloat;
    _0mode?: FFInt | "square" | "row" | "column";
    _1mode?: FFInt | "square" | "row" | "column";
    _2mode?: FFInt | "square" | "row" | "column";
    _3mode?: FFInt | "square" | "row" | "column";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "convolution", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "0m": options?._0m,
      "1m": options?._1m,
      "2m": options?._2m,
      "3m": options?._3m,
      "0rdiv": options?._0rdiv,
      "1rdiv": options?._1rdiv,
      "2rdiv": options?._2rdiv,
      "3rdiv": options?._3rdiv,
      "0bias": options?._0bias,
      "1bias": options?._1bias,
      "2bias": options?._2bias,
      "3bias": options?._3bias,
      "0mode": options?._0mode,
      "1mode": options?._1mode,
      "2mode": options?._2mode,
      "3mode": options?._3mode,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Convolve first video stream with second video stream.

 *
 * @param options.planes - set planes to convolve (from 0 to 15) (default 7)
 * @param options.impulse - when to process impulses (from 0 to 1) (default all)
 * @param options.noise - set noise (from 0 to 1) (default 1e-07)
 * @see https://ffmpeg.org/ffmpeg-filters.html#convolve
 */
  convolve(
    _impulse: VideoStream,

    options?: {
    planes?: FFInt;
    impulse?: FFInt | "first" | "all";
    noise?: FFFloat;
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "convolve", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _impulse],
      merge(
    {
      "planes": options?.planes,
      "impulse": options?.impulse,
      "noise": options?.noise,
      "eof_action": options?.eofAction,
      "shortest": options?.shortest,
      "repeatlast": options?.repeatlast,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Copy the input video unchanged to the output.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#copy
 */
  copy(
    options?: {
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "copy", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Video filtering using CoreImage API.
 *
 * Note: New in FFmpeg 8.0.
 *
 * @param options.list_filters - list available filters (default false)
 * @param options.list_generators - list available generators (default false)
 * @param options.filter - names and options of filters to apply
 * @param options.output_rect - output rectangle within output image
 * @see https://ffmpeg.org/ffmpeg-filters.html#coreimage
 */
  coreimage(
    options?: {
    list_filters?: FFBoolean;
    list_generators?: FFBoolean;
    filter?: FFString;
    output_rect?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "coreimage", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "list_filters": options?.list_filters,
      "list_generators": options?.list_generators,
      "filter": options?.filter,
      "output_rect": options?.output_rect,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Calculate the correlation between two video streams.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#corr
 */
  corr(
    _reference: VideoStream,

    options?: {
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "corr", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _reference],
      merge(
    {
      "eof_action": options?.eofAction,
      "shortest": options?.shortest,
      "repeatlast": options?.repeatlast,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Find and cover a user specified object.

 *
 * @param options.cover - cover bitmap filename
 * @param options.mode - set removal mode (from 0 to 1) (default blur)
 * @see https://ffmpeg.org/ffmpeg-filters.html#cover_005frect
 */
  cover_rect(
    options?: {
    cover?: FFString;
    mode?: FFInt | "cover" | "blur";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "cover_rect", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "cover": options?.cover,
      "mode": options?.mode,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Crop the input video.

 *
 * @param options.out_w - set the width crop area expression (default "iw")
 * @param options.out_h - set the height crop area expression (default "ih")
 * @param options.x - set the x crop area expression (default "(in_w-out_w)/2")
 * @param options.y - set the y crop area expression (default "(in_h-out_h)/2")
 * @param options.keep_aspect - keep aspect ratio (default false)
 * @param options.exact - do exact cropping (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#crop
 */
  crop(
    options?: {
    out_w?: FFString;
    out_h?: FFString;
    x?: FFString;
    y?: FFString;
    keep_aspect?: FFBoolean;
    exact?: FFBoolean;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "crop", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "out_w": options?.out_w,
      "out_h": options?.out_h,
      "x": options?.x,
      "y": options?.y,
      "keep_aspect": options?.keep_aspect,
      "exact": options?.exact,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Auto-detect crop size.

 *
 * @param options.limit - Threshold below which the pixel is considered black (from 0 to 65535) (default 0.0941176)
 * @param options.round - Value by which the width/height should be divisible (from 0 to INT_MAX) (default 16)
 * @param options.reset - Recalculate the crop area after this many frames (from 0 to INT_MAX) (default 0)
 * @param options.skip - Number of initial frames to skip (from 0 to INT_MAX) (default 2)
 * @param options.reset_count - Recalculate the crop area after this many frames (from 0 to INT_MAX) (default 0)
 * @param options.max_outliers - Threshold count of outliers (from 0 to INT_MAX) (default 0)
 * @param options.mode - set mode (from 0 to 1) (default black)
 * @param options.high - Set high threshold for edge detection (from 0 to 1) (default 0.0980392)
 * @param options.low - Set low threshold for edge detection (from 0 to 1) (default 0.0588235)
 * @param options.mv_threshold - motion vector threshold when estimating video window size (from 0 to 100) (default 8)
 * @see https://ffmpeg.org/ffmpeg-filters.html#cropdetect
 */
  cropdetect(
    options?: {
    limit?: FFFloat;
    round?: FFInt;
    reset?: FFInt;
    skip?: FFInt;
    reset_count?: FFInt;
    max_outliers?: FFInt;
    mode?: FFInt | "black" | "mvedges";
    high?: FFFloat;
    low?: FFFloat;
    mv_threshold?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "cropdetect", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "limit": options?.limit,
      "round": options?.round,
      "reset": options?.reset,
      "skip": options?.skip,
      "reset_count": options?.reset_count,
      "max_outliers": options?.max_outliers,
      "mode": options?.mode,
      "high": options?.high,
      "low": options?.low,
      "mv_threshold": options?.mv_threshold,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }










/**
 * Delay filtering to match a cue.

 *
 * @param options.cue - cue unix timestamp in microseconds (from 0 to I64_MAX) (default 0)
 * @param options.preroll - preroll duration in seconds (default 0)
 * @param options.buffer - buffer duration in seconds (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#cue
 */
  cue(
    options?: {
    cue?: FFInt64;
    preroll?: FFDuration;
    buffer?: FFDuration;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "cue", typingsInput: ["video"], typingsOutput: ["video"] },
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
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Adjust components curves.

 *
 * @param options.preset - select a color curves preset (from 0 to 10) (default none)
 * @param options.master - set master points coordinates
 * @param options.red - set red points coordinates
 * @param options.green - set green points coordinates
 * @param options.blue - set blue points coordinates
 * @param options.all - set points coordinates for all components
 * @param options.psfile - set Photoshop curves file name
 * @param options.plot - save Gnuplot script of the curves in specified file
 * @param options.interp - specify the kind of interpolation (from 0 to 1) (default natural)
 * @see https://ffmpeg.org/ffmpeg-filters.html#curves
 */
  curves(
    options?: {
    preset?: FFInt | "none" | "color_negative" | "cross_process" | "darker" | "increase_contrast" | "lighter" | "linear_contrast" | "medium_contrast" | "negative" | "strong_contrast" | "vintage";
    master?: FFString;
    red?: FFString;
    green?: FFString;
    blue?: FFString;
    all?: FFString;
    psfile?: FFString;
    plot?: FFString;
    interp?: FFInt | "natural" | "pchip";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "curves", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "preset": options?.preset,
      "master": options?.master,
      "red": options?.red,
      "green": options?.green,
      "blue": options?.blue,
      "all": options?.all,
      "psfile": options?.psfile,
      "plot": options?.plot,
      "interp": options?.interp,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Video data analysis.

 *
 * @param options.size - set output size (default "hd720")
 * @param options.x - set x offset (from 0 to INT_MAX) (default 0)
 * @param options.y - set y offset (from 0 to INT_MAX) (default 0)
 * @param options.mode - set scope mode (from 0 to 2) (default mono)
 * @param options.axis - draw column/row numbers (default false)
 * @param options.opacity - set background opacity (from 0 to 1) (default 0.75)
 * @param options.format - set display number format (from 0 to 1) (default hex)
 * @param options.components - set components to display (from 1 to 15) (default 15)
 * @see https://ffmpeg.org/ffmpeg-filters.html#datascope
 */
  datascope(
    options?: {
    size?: FFImageSize;
    x?: FFInt;
    y?: FFInt;
    mode?: FFInt | "mono" | "color" | "color2";
    axis?: FFBoolean;
    opacity?: FFFloat;
    format?: FFInt | "hex" | "dec";
    components?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "datascope", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "size": options?.size,
      "x": options?.x,
      "y": options?.y,
      "mode": options?.mode,
      "axis": options?.axis,
      "opacity": options?.opacity,
      "format": options?.format,
      "components": options?.components,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply Directional Blur filter.

 *
 * @param options.angle - set angle (from 0 to 360) (default 45)
 * @param options.radius - set radius (from 0 to 8192) (default 5)
 * @param options.planes - set planes to filter (from 0 to 15) (default 15)
 * @see https://ffmpeg.org/ffmpeg-filters.html#dblur
 */
  dblur(
    options?: {
    angle?: FFFloat;
    radius?: FFFloat;
    planes?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "dblur", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "angle": options?.angle,
      "radius": options?.radius,
      "planes": options?.planes,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Denoise frames using 2D DCT.

 *
 * @param options.sigma - set noise sigma constant (from 0 to 999) (default 0)
 * @param options.overlap - set number of block overlapping pixels (from -1 to 15) (default -1)
 * @param options.expr - set coefficient factor expression
 * @param options.n - set the block size, expressed in bits (from 3 to 4) (default 3)
 * @see https://ffmpeg.org/ffmpeg-filters.html#dctdnoiz
 */
  dctdnoiz(
    options?: {
    sigma?: FFFloat;
    overlap?: FFInt;
    expr?: FFString;
    n?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "dctdnoiz", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "sigma": options?.sigma,
      "overlap": options?.overlap,
      "expr": options?.expr,
      "n": options?.n,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Debands video.

 *
 * @param options._1thr - set 1st plane threshold (from 3e-05 to 0.5) (default 0.02)
 * @param options._2thr - set 2nd plane threshold (from 3e-05 to 0.5) (default 0.02)
 * @param options._3thr - set 3rd plane threshold (from 3e-05 to 0.5) (default 0.02)
 * @param options._4thr - set 4th plane threshold (from 3e-05 to 0.5) (default 0.02)
 * @param options.range - set range (from INT_MIN to INT_MAX) (default 16)
 * @param options.direction - set direction (from -6.28319 to 6.28319) (default 6.28319)
 * @param options.blur - set blur (default true)
 * @param options.coupling - set plane coupling (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#deband
 */
  deband(
    options?: {
    _1thr?: FFFloat;
    _2thr?: FFFloat;
    _3thr?: FFFloat;
    _4thr?: FFFloat;
    range?: FFInt;
    direction?: FFFloat;
    blur?: FFBoolean;
    coupling?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "deband", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "1thr": options?._1thr,
      "2thr": options?._2thr,
      "3thr": options?._3thr,
      "4thr": options?._4thr,
      "range": options?.range,
      "direction": options?.direction,
      "blur": options?.blur,
      "coupling": options?.coupling,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Deblock video.

 *
 * @param options.filter - set type of filter (from 0 to 1) (default strong)
 * @param options.block - set size of block (from 4 to 512) (default 8)
 * @param options.alpha - set 1st detection threshold (from 0 to 1) (default 0.098)
 * @param options.beta - set 2nd detection threshold (from 0 to 1) (default 0.05)
 * @param options.gamma - set 3rd detection threshold (from 0 to 1) (default 0.05)
 * @param options.delta - set 4th detection threshold (from 0 to 1) (default 0.05)
 * @param options.planes - set planes to filter (from 0 to 15) (default 15)
 * @see https://ffmpeg.org/ffmpeg-filters.html#deblock
 */
  deblock(
    options?: {
    filter?: FFInt | "weak" | "strong";
    block?: FFInt;
    alpha?: FFFloat;
    beta?: FFFloat;
    gamma?: FFFloat;
    delta?: FFFloat;
    planes?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "deblock", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "filter": options?.filter,
      "block": options?.block,
      "alpha": options?.alpha,
      "beta": options?.beta,
      "gamma": options?.gamma,
      "delta": options?.delta,
      "planes": options?.planes,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Deconvolve first video stream with second video stream.

 *
 * @param options.planes - set planes to deconvolve (from 0 to 15) (default 7)
 * @param options.impulse - when to process impulses (from 0 to 1) (default all)
 * @param options.noise - set noise (from 0 to 1) (default 1e-07)
 * @see https://ffmpeg.org/ffmpeg-filters.html#deconvolve
 */
  deconvolve(
    _impulse: VideoStream,

    options?: {
    planes?: FFInt;
    impulse?: FFInt | "first" | "all";
    noise?: FFFloat;
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "deconvolve", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _impulse],
      merge(
    {
      "planes": options?.planes,
      "impulse": options?.impulse,
      "noise": options?.noise,
      "eof_action": options?.eofAction,
      "shortest": options?.shortest,
      "repeatlast": options?.repeatlast,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Reduce cross-luminance and cross-color.

 *
 * @param options.m - set filtering mode (default dotcrawl+rainbows)
 * @param options.lt - set spatial luma threshold (from 0 to 1) (default 0.079)
 * @param options.tl - set tolerance for temporal luma (from 0 to 1) (default 0.079)
 * @param options.tc - set tolerance for chroma temporal variation (from 0 to 1) (default 0.058)
 * @param options.ct - set temporal chroma threshold (from 0 to 1) (default 0.019)
 * @see https://ffmpeg.org/ffmpeg-filters.html#dedot
 */
  dedot(
    options?: {
    m?: FFFlags | "dotcrawl" | "rainbows";
    lt?: FFFloat;
    tl?: FFFloat;
    tc?: FFFloat;
    ct?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "dedot", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "m": options?.m,
      "lt": options?.lt,
      "tl": options?.tl,
      "tc": options?.tc,
      "ct": options?.ct,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Apply deflate effect.

 *
 * @param options.threshold0 - set threshold for 1st plane (from 0 to 65535) (default 65535)
 * @param options.threshold1 - set threshold for 2nd plane (from 0 to 65535) (default 65535)
 * @param options.threshold2 - set threshold for 3rd plane (from 0 to 65535) (default 65535)
 * @param options.threshold3 - set threshold for 4th plane (from 0 to 65535) (default 65535)
 * @see https://ffmpeg.org/ffmpeg-filters.html#deflate
 */
  deflate(
    options?: {
    threshold0?: FFInt;
    threshold1?: FFInt;
    threshold2?: FFInt;
    threshold3?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "deflate", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "threshold0": options?.threshold0,
      "threshold1": options?.threshold1,
      "threshold2": options?.threshold2,
      "threshold3": options?.threshold3,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Remove temporal frame luminance variations.

 *
 * @param options.size - set how many frames to use (from 2 to 129) (default 5)
 * @param options.mode - set how to smooth luminance (from 0 to 6) (default am)
 * @param options.bypass - leave frames unchanged (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#deflicker
 */
  deflicker(
    options?: {
    size?: FFInt;
    mode?: FFInt | "am" | "gm" | "hm" | "qm" | "cm" | "pm" | "median";
    bypass?: FFBoolean;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "deflicker", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "size": options?.size,
      "mode": options?.mode,
      "bypass": options?.bypass,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Remove judder produced by pullup.

 *
 * @param options.cycle - set the length of the cycle to use for dejuddering (from 2 to 240) (default 4)
 * @see https://ffmpeg.org/ffmpeg-filters.html#dejudder
 */
  dejudder(
    options?: {
    cycle?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "dejudder", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "cycle": options?.cycle,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Remove logo from input video.

 *
 * @param options.x - set logo x position (default "-1")
 * @param options.y - set logo y position (default "-1")
 * @param options.w - set logo width (default "-1")
 * @param options.h - set logo height (default "-1")
 * @param options.show - show delogo area (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#delogo
 */
  delogo(
    options?: {
    x?: FFString;
    y?: FFString;
    w?: FFString;
    h?: FFString;
    show?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "delogo", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "x": options?.x,
      "y": options?.y,
      "w": options?.w,
      "h": options?.h,
      "show": options?.show,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Stabilize shaky video.

 *
 * @param options.x - set x for the rectangular search area (from -1 to INT_MAX) (default -1)
 * @param options.y - set y for the rectangular search area (from -1 to INT_MAX) (default -1)
 * @param options.w - set width for the rectangular search area (from -1 to INT_MAX) (default -1)
 * @param options.h - set height for the rectangular search area (from -1 to INT_MAX) (default -1)
 * @param options.rx - set x for the rectangular search area (from 0 to 64) (default 16)
 * @param options.ry - set y for the rectangular search area (from 0 to 64) (default 16)
 * @param options.edge - set edge mode (from 0 to 3) (default mirror)
 * @param options.blocksize - set motion search blocksize (from 4 to 128) (default 8)
 * @param options.contrast - set contrast threshold for blocks (from 1 to 255) (default 125)
 * @param options.search - set search strategy (from 0 to 1) (default exhaustive)
 * @param options.filename - set motion search detailed log file name
 * @param options.opencl - ignored (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#deshake
 */
  deshake(
    options?: {
    x?: FFInt;
    y?: FFInt;
    w?: FFInt;
    h?: FFInt;
    rx?: FFInt;
    ry?: FFInt;
    edge?: FFInt | "blank" | "original" | "clamp" | "mirror";
    blocksize?: FFInt;
    contrast?: FFInt;
    search?: FFInt | "exhaustive" | "less";
    filename?: FFString;
    opencl?: FFBoolean;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "deshake", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "x": options?.x,
      "y": options?.y,
      "w": options?.w,
      "h": options?.h,
      "rx": options?.rx,
      "ry": options?.ry,
      "edge": options?.edge,
      "blocksize": options?.blocksize,
      "contrast": options?.contrast,
      "search": options?.search,
      "filename": options?.filename,
      "opencl": options?.opencl,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Despill video.

 *
 * @param options._type - set the screen type (from 0 to 1) (default green)
 * @param options.mix - set the spillmap mix (from 0 to 1) (default 0.5)
 * @param options.expand - set the spillmap expand (from 0 to 1) (default 0)
 * @param options.red - set red scale (from -100 to 100) (default 0)
 * @param options.green - set green scale (from -100 to 100) (default -1)
 * @param options.blue - set blue scale (from -100 to 100) (default 0)
 * @param options.brightness - set brightness (from -10 to 10) (default 0)
 * @param options.alpha - change alpha component (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#despill
 */
  despill(
    options?: {
    _type?: FFInt | "green" | "blue";
    mix?: FFFloat;
    expand?: FFFloat;
    red?: FFFloat;
    green?: FFFloat;
    blue?: FFFloat;
    brightness?: FFFloat;
    alpha?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "despill", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "type": options?._type,
      "mix": options?.mix,
      "expand": options?.expand,
      "red": options?.red,
      "green": options?.green,
      "blue": options?.blue,
      "brightness": options?.brightness,
      "alpha": options?.alpha,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply an inverse telecine pattern.

 *
 * @param options.first_field - select first field (from 0 to 1) (default top)
 * @param options.pattern - pattern that describe for how many fields a frame is to be displayed (default "23")
 * @param options.start_frame - position of first frame with respect to the pattern if stream is cut (from 0 to 13) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#detelecine
 */
  detelecine(
    options?: {
    first_field?: FFInt | "top" | "t" | "bottom" | "b";
    pattern?: FFString;
    start_frame?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "detelecine", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "first_field": options?.first_field,
      "pattern": options?.pattern,
      "start_frame": options?.start_frame,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Apply dilation effect.

 *
 * @param options.coordinates - set coordinates (from 0 to 255) (default 255)
 * @param options.threshold0 - set threshold for 1st plane (from 0 to 65535) (default 65535)
 * @param options.threshold1 - set threshold for 2nd plane (from 0 to 65535) (default 65535)
 * @param options.threshold2 - set threshold for 3rd plane (from 0 to 65535) (default 65535)
 * @param options.threshold3 - set threshold for 4th plane (from 0 to 65535) (default 65535)
 * @see https://ffmpeg.org/ffmpeg-filters.html#dilation
 */
  dilation(
    options?: {
    coordinates?: FFInt;
    threshold0?: FFInt;
    threshold1?: FFInt;
    threshold2?: FFInt;
    threshold3?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "dilation", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "coordinates": options?.coordinates,
      "threshold0": options?.threshold0,
      "threshold1": options?.threshold1,
      "threshold2": options?.threshold2,
      "threshold3": options?.threshold3,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Displace pixels.

 *
 * @param options.edge - set edge mode (from 0 to 3) (default smear)
 * @see https://ffmpeg.org/ffmpeg-filters.html#displace
 */
  displace(
    _xmap: VideoStream,
    _ymap: VideoStream,

    options?: {
    edge?: FFInt | "blank" | "smear" | "wrap" | "mirror";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "displace", typingsInput: ["video", "video", "video"], typingsOutput: ["video"] },
      [this, _xmap, _ymap],
      merge(
    {
      "edge": options?.edge,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Weave input video fields into double number of frames.

 *
 * @param options.first_field - set first field (from 0 to 1) (default top)
 * @see https://ffmpeg.org/ffmpeg-filters.html#weave_002c-doubleweave
 */
  doubleweave(
    options?: {
    first_field?: FFInt | "top" | "t" | "bottom" | "b";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "doubleweave", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "first_field": options?.first_field,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Draw a colored box on the input video.

 *
 * @param options.x - set horizontal position of the left box edge (default "0")
 * @param options.y - set vertical position of the top box edge (default "0")
 * @param options.width - set width of the box (default "0")
 * @param options.height - set height of the box (default "0")
 * @param options.color - set color of the box (default "black")
 * @param options.thickness - set the box thickness (default "3")
 * @param options.replace - replace color & alpha (default false)
 * @param options.box_source - use data from bounding box in side data
 * @see https://ffmpeg.org/ffmpeg-filters.html#drawbox
 */
  drawbox(
    options?: {
    x?: FFString;
    y?: FFString;
    width?: FFString;
    height?: FFString;
    color?: FFString;
    thickness?: FFString;
    replace?: FFBoolean;
    box_source?: FFString;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "drawbox", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "x": options?.x,
      "y": options?.y,
      "width": options?.width,
      "height": options?.height,
      "color": options?.color,
      "thickness": options?.thickness,
      "replace": options?.replace,
      "box_source": options?.box_source,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Draw a graph using input video metadata.

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
 * @see https://ffmpeg.org/ffmpeg-filters.html#drawgraph
 */
  drawgraph(
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
      { name: "drawgraph", typingsInput: ["video"], typingsOutput: ["video"] },
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
 * Draw a colored grid on the input video.

 *
 * @param options.x - set horizontal offset (default "0")
 * @param options.y - set vertical offset (default "0")
 * @param options.width - set width of grid cell (default "0")
 * @param options.height - set height of grid cell (default "0")
 * @param options.color - set color of the grid (default "black")
 * @param options.thickness - set grid line thickness (default "1")
 * @param options.replace - replace color & alpha (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#drawgrid
 */
  drawgrid(
    options?: {
    x?: FFString;
    y?: FFString;
    width?: FFString;
    height?: FFString;
    color?: FFString;
    thickness?: FFString;
    replace?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "drawgrid", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "x": options?.x,
      "y": options?.y,
      "width": options?.width,
      "height": options?.height,
      "color": options?.color,
      "thickness": options?.thickness,
      "replace": options?.replace,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }














/**
 * Detect and draw edge.

 *
 * @param options.high - set high threshold (from 0 to 1) (default 0.196078)
 * @param options.low - set low threshold (from 0 to 1) (default 0.0784314)
 * @param options.mode - set mode (from 0 to 2) (default wires)
 * @param options.planes - set planes to filter (default y+u+v+r+g+b)
 * @see https://ffmpeg.org/ffmpeg-filters.html#edgedetect
 */
  edgedetect(
    options?: {
    high?: FFDouble;
    low?: FFDouble;
    mode?: FFInt | "wires" | "colormix" | "canny";
    planes?: FFFlags | "y" | "u" | "v" | "r" | "g" | "b";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "edgedetect", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "high": options?.high,
      "low": options?.low,
      "mode": options?.mode,
      "planes": options?.planes,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply posterize effect, using the ELBG algorithm.

 *
 * @param options.codebook_length - set codebook length (from 1 to INT_MAX) (default 256)
 * @param options.nb_steps - set max number of steps used to compute the mapping (from 1 to INT_MAX) (default 1)
 * @param options.seed - set the random seed (from -1 to UINT32_MAX) (default -1)
 * @param options.pal8 - set the pal8 output (default false)
 * @param options.use_alpha - use alpha channel for mapping (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#elbg
 */
  elbg(
    options?: {
    codebook_length?: FFInt;
    nb_steps?: FFInt;
    seed?: FFInt64;
    pal8?: FFBoolean;
    use_alpha?: FFBoolean;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "elbg", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "codebook_length": options?.codebook_length,
      "nb_steps": options?.nb_steps,
      "seed": options?.seed,
      "pal8": options?.pal8,
      "use_alpha": options?.use_alpha,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Measure video frames entropy.

 *
 * @param options.mode - set kind of histogram entropy measurement (from 0 to 1) (default normal)
 * @see https://ffmpeg.org/ffmpeg-filters.html#entropy
 */
  entropy(
    options?: {
    mode?: FFInt | "normal" | "diff";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "entropy", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "mode": options?.mode,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Scale the input using EPX algorithm.

 *
 * @param options.n - set scale factor (from 2 to 3) (default 3)
 * @see https://ffmpeg.org/ffmpeg-filters.html#epx
 */
  epx(
    options?: {
    n?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "epx", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "n": options?.n,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Adjust brightness, contrast, gamma, and saturation.

 *
 * @param options.contrast - set the contrast adjustment, negative values give a negative image (default "1.0")
 * @param options.brightness - set the brightness adjustment (default "0.0")
 * @param options.saturation - set the saturation adjustment (default "1.0")
 * @param options.gamma - set the initial gamma value (default "1.0")
 * @param options.gamma_r - gamma value for red (default "1.0")
 * @param options.gamma_g - gamma value for green (default "1.0")
 * @param options.gamma_b - gamma value for blue (default "1.0")
 * @param options.gamma_weight - set the gamma weight which reduces the effect of gamma on bright areas (default "1.0")
 * @param options.eval - specify when to evaluate expressions (from 0 to 1) (default init)
 * @see https://ffmpeg.org/ffmpeg-filters.html#eq
 */
  eq(
    options?: {
    contrast?: FFString;
    brightness?: FFString;
    saturation?: FFString;
    gamma?: FFString;
    gamma_r?: FFString;
    gamma_g?: FFString;
    gamma_b?: FFString;
    gamma_weight?: FFString;
    eval?: FFInt | "init" | "frame";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "eq", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "contrast": options?.contrast,
      "brightness": options?.brightness,
      "saturation": options?.saturation,
      "gamma": options?.gamma,
      "gamma_r": options?.gamma_r,
      "gamma_g": options?.gamma_g,
      "gamma_b": options?.gamma_b,
      "gamma_weight": options?.gamma_weight,
      "eval": options?.eval,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Apply erosion effect.

 *
 * @param options.coordinates - set coordinates (from 0 to 255) (default 255)
 * @param options.threshold0 - set threshold for 1st plane (from 0 to 65535) (default 65535)
 * @param options.threshold1 - set threshold for 2nd plane (from 0 to 65535) (default 65535)
 * @param options.threshold2 - set threshold for 3rd plane (from 0 to 65535) (default 65535)
 * @param options.threshold3 - set threshold for 4th plane (from 0 to 65535) (default 65535)
 * @see https://ffmpeg.org/ffmpeg-filters.html#erosion
 */
  erosion(
    options?: {
    coordinates?: FFInt;
    threshold0?: FFInt;
    threshold1?: FFInt;
    threshold2?: FFInt;
    threshold3?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "erosion", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "coordinates": options?.coordinates,
      "threshold0": options?.threshold0,
      "threshold1": options?.threshold1,
      "threshold2": options?.threshold2,
      "threshold3": options?.threshold3,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply Edge Slope Tracing deinterlace.

 *
 * @param options.mode - specify the mode (from 0 to 1) (default field)
 * @param options.parity - specify the assumed picture field parity (from -1 to 1) (default auto)
 * @param options.deint - specify which frames to deinterlace (from 0 to 1) (default all)
 * @param options.rslope - specify the search radius for edge slope tracing (from 1 to 15) (default 1)
 * @param options.redge - specify the search radius for best edge matching (from 0 to 15) (default 2)
 * @param options.ecost - specify the edge cost for edge matching (from 0 to 50) (default 2)
 * @param options.mcost - specify the middle cost for edge matching (from 0 to 50) (default 1)
 * @param options.dcost - specify the distance cost for edge matching (from 0 to 50) (default 1)
 * @param options.interp - specify the type of interpolation (from 0 to 2) (default 4p)
 * @see https://ffmpeg.org/ffmpeg-filters.html#estdif
 */
  estdif(
    options?: {
    mode?: FFInt | "frame" | "field";
    parity?: FFInt | "tff" | "bff" | "auto";
    deint?: FFInt | "all" | "interlaced";
    rslope?: FFInt;
    redge?: FFInt;
    ecost?: FFInt;
    mcost?: FFInt;
    dcost?: FFInt;
    interp?: FFInt | "2p" | "4p" | "6p";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "estdif", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "mode": options?.mode,
      "parity": options?.parity,
      "deint": options?.deint,
      "rslope": options?.rslope,
      "redge": options?.redge,
      "ecost": options?.ecost,
      "mcost": options?.mcost,
      "dcost": options?.dcost,
      "interp": options?.interp,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Adjust exposure of the video stream.

 *
 * @param options.exposure - set the exposure correction (from -3 to 3) (default 0)
 * @param options.black - set the black level correction (from -1 to 1) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#exposure
 */
  exposure(
    options?: {
    exposure?: FFFloat;
    black?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "exposure", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "exposure": options?.exposure,
      "black": options?.black,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Extract planes as grayscale frames.

 *
 * @param options.planes - set planes (default r)
 * @see https://ffmpeg.org/ffmpeg-filters.html#extractplanes
 */
  extractplanes(
    options?: {
    planes?: FFFlags | "y" | "u" | "v" | "r" | "g" | "b" | "a";
extraOptions?: Record<string, unknown>;
    },
  ): FilterNode {
    const filterNode = filterNodeFactory(
      { name: "extractplanes", typingsInput: ["video"], typingsOutput: [] },
      [this],
      merge(
    {
      "planes": options?.planes,
},
    options?.extraOptions,
  ),
    );
return filterNode;
  }








/**
 * Fade in/out input video.

 *
 * @param options._type - set the fade direction (from 0 to 1) (default in)
 * @param options.start_frame - Number of the first frame to which to apply the effect. (from 0 to INT_MAX) (default 0)
 * @param options.nb_frames - Number of frames to which the effect should be applied. (from 1 to INT_MAX) (default 25)
 * @param options.alpha - fade alpha if it is available on the input (default false)
 * @param options.start_time - Number of seconds of the beginning of the effect. (default 0)
 * @param options.duration - Duration of the effect in seconds. (default 0)
 * @param options.color - set color (default "black")
 * @see https://ffmpeg.org/ffmpeg-filters.html#fade
 */
  fade(
    options?: {
    _type?: FFInt | "in" | "out";
    start_frame?: FFInt;
    nb_frames?: FFInt;
    alpha?: FFBoolean;
    start_time?: FFDuration;
    duration?: FFDuration;
    color?: FFColor;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "fade", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "type": options?._type,
      "start_frame": options?.start_frame,
      "nb_frames": options?.nb_frames,
      "alpha": options?.alpha,
      "start_time": options?.start_time,
      "duration": options?.duration,
      "color": options?.color,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply feedback video filter.

 *
 * @param options.x - set top left crop position (from 0 to INT_MAX) (default 0)
 * @param options.w - set crop size (from 0 to INT_MAX) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#feedback
 */
  feedback(
    _feedin: VideoStream,

    options?: {
    x?: FFInt;
    w?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): FilterNode {
    const filterNode = filterNodeFactory(
      { name: "feedback", typingsInput: ["video", "video"], typingsOutput: ["video", "video"] },
      [this, _feedin],
      merge(
    {
      "x": options?.x,
      "w": options?.w,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode;
  }






/**
 * Denoise frames using 3D FFT.

 *
 * @param options.sigma - set denoise strength (from 0 to 100) (default 1)
 * @param options.amount - set amount of denoising (from 0.01 to 1) (default 1)
 * @param options.block - set block size (from 8 to 256) (default 32)
 * @param options.overlap - set block overlap (from 0.2 to 0.8) (default 0.5)
 * @param options.method - set method of denoising (from 0 to 1) (default wiener)
 * @param options.prev - set number of previous frames for temporal denoising (from 0 to 1) (default 0)
 * @param options.next - set number of next frames for temporal denoising (from 0 to 1) (default 0)
 * @param options.planes - set planes to filter (from 0 to 15) (default 7)
 * @param options.window - set window function (from 0 to 20) (default hann)
 * @see https://ffmpeg.org/ffmpeg-filters.html#fftdnoiz
 */
  fftdnoiz(
    options?: {
    sigma?: FFFloat;
    amount?: FFFloat;
    block?: FFInt;
    overlap?: FFFloat;
    method?: FFInt | "wiener" | "hard";
    prev?: FFInt;
    next?: FFInt;
    planes?: FFInt;
    window?: FFInt | "rect" | "bartlett" | "hann" | "hanning" | "hamming" | "blackman" | "welch" | "flattop" | "bharris" | "bnuttall" | "bhann" | "sine" | "nuttall" | "lanczos" | "gauss" | "tukey" | "dolph" | "cauchy" | "parzen" | "poisson" | "bohman" | "kaiser";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "fftdnoiz", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "sigma": options?.sigma,
      "amount": options?.amount,
      "block": options?.block,
      "overlap": options?.overlap,
      "method": options?.method,
      "prev": options?.prev,
      "next": options?.next,
      "planes": options?.planes,
      "window": options?.window,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply arbitrary expressions to pixels in frequency domain.

 *
 * @param options.dc_Y - adjust gain in Y plane (from 0 to 1000) (default 0)
 * @param options.dc_U - adjust gain in U plane (from 0 to 1000) (default 0)
 * @param options.dc_V - adjust gain in V plane (from 0 to 1000) (default 0)
 * @param options.weight_Y - set luminance expression in Y plane (default "1")
 * @param options.weight_U - set chrominance expression in U plane
 * @param options.weight_V - set chrominance expression in V plane
 * @param options.eval - specify when to evaluate expressions (from 0 to 1) (default init)
 * @see https://ffmpeg.org/ffmpeg-filters.html#fftfilt
 */
  fftfilt(
    options?: {
    dc_Y?: FFInt;
    dc_U?: FFInt;
    dc_V?: FFInt;
    weight_Y?: FFString;
    weight_U?: FFString;
    weight_V?: FFString;
    eval?: FFInt | "init" | "frame";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "fftfilt", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "dc_Y": options?.dc_Y,
      "dc_U": options?.dc_U,
      "dc_V": options?.dc_V,
      "weight_Y": options?.weight_Y,
      "weight_U": options?.weight_U,
      "weight_V": options?.weight_V,
      "eval": options?.eval,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Extract a field from the input video.

 *
 * @param options._type - set field type (top or bottom) (from 0 to 1) (default top)
 * @see https://ffmpeg.org/ffmpeg-filters.html#field
 */
  field(
    options?: {
    _type?: FFInt | "top" | "bottom";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "field", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "type": options?._type,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Field matching using hints.

 *
 * @param options.hint - set hint file
 * @param options.mode - set hint mode (from 0 to 2) (default absolute)
 * @see https://ffmpeg.org/ffmpeg-filters.html#fieldhint
 */
  fieldhint(
    options?: {
    hint?: FFString;
    mode?: FFInt | "absolute" | "relative" | "pattern";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "fieldhint", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "hint": options?.hint,
      "mode": options?.mode,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Set the field order.

 *
 * @param options.order - output field order (from 0 to 1) (default tff)
 * @see https://ffmpeg.org/ffmpeg-filters.html#fieldorder
 */
  fieldorder(
    options?: {
    order?: FFInt | "bff" | "tff";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "fieldorder", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "order": options?.order,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Fill borders of the input video.

 *
 * @param options.left - set the left fill border (from 0 to INT_MAX) (default 0)
 * @param options.right - set the right fill border (from 0 to INT_MAX) (default 0)
 * @param options.top - set the top fill border (from 0 to INT_MAX) (default 0)
 * @param options.bottom - set the bottom fill border (from 0 to INT_MAX) (default 0)
 * @param options.mode - set the fill borders mode (from 0 to 6) (default smear)
 * @param options.color - set the color for the fixed/fade mode (default "black")
 * @see https://ffmpeg.org/ffmpeg-filters.html#fillborders
 */
  fillborders(
    options?: {
    left?: FFInt;
    right?: FFInt;
    top?: FFInt;
    bottom?: FFInt;
    mode?: FFInt | "smear" | "mirror" | "fixed" | "reflect" | "wrap" | "fade" | "margins";
    color?: FFColor;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "fillborders", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "left": options?.left,
      "right": options?.right,
      "top": options?.top,
      "bottom": options?.bottom,
      "mode": options?.mode,
      "color": options?.color,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Find a user specified object.

 *
 * @param options.object - object bitmap filename
 * @param options.threshold - set threshold (from 0 to 1) (default 0.5)
 * @param options.mipmaps - set mipmaps (from 1 to 5) (default 3)
 * @param options.xmin - (from 0 to INT_MAX) (default 0)
 * @param options.xmax - (from 0 to INT_MAX) (default INT_MAX)
 * @param options.discard - (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#find_005frect
 */
  find_rect(
    options?: {
    object?: FFString;
    threshold?: FFFloat;
    mipmaps?: FFInt;
    xmin?: FFInt;
    xmax?: FFInt;
    discard?: FFBoolean;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "find_rect", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "object": options?.object,
      "threshold": options?.threshold,
      "mipmaps": options?.mipmaps,
      "xmin": options?.xmin,
      "xmax": options?.xmax,
      "discard": options?.discard,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }










/**
 * Fill area with same color with another color.

 *
 * @param options.x - set pixel x coordinate (from 0 to 65535) (default 0)
 * @param options.y - set pixel y coordinate (from 0 to 65535) (default 0)
 * @param options.s0 - set source #0 component value (from -1 to 65535) (default 0)
 * @param options.s1 - set source #1 component value (from -1 to 65535) (default 0)
 * @param options.s2 - set source #2 component value (from -1 to 65535) (default 0)
 * @param options.s3 - set source #3 component value (from -1 to 65535) (default 0)
 * @param options.d0 - set destination #0 component value (from 0 to 65535) (default 0)
 * @param options.d1 - set destination #1 component value (from 0 to 65535) (default 0)
 * @param options.d2 - set destination #2 component value (from 0 to 65535) (default 0)
 * @param options.d3 - set destination #3 component value (from 0 to 65535) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#floodfill
 */
  floodfill(
    options?: {
    x?: FFInt;
    y?: FFInt;
    s0?: FFInt;
    s1?: FFInt;
    s2?: FFInt;
    s3?: FFInt;
    d0?: FFInt;
    d1?: FFInt;
    d2?: FFInt;
    d3?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "floodfill", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "x": options?.x,
      "y": options?.y,
      "s0": options?.s0,
      "s1": options?.s1,
      "s2": options?.s2,
      "s3": options?.s3,
      "d0": options?.d0,
      "d1": options?.d1,
      "d2": options?.d2,
      "d3": options?.d3,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Convert the input video to one of the specified pixel formats.

 *
 * @param options.pix_fmts - A '|'-separated list of pixel formats
 * @param options.color_spaces - A '|'-separated list of color spaces
 * @param options.color_ranges - A '|'-separated list of color ranges
 * @param options.alpha_modes - A '|'-separated list of alpha modes
 * @see https://ffmpeg.org/ffmpeg-filters.html#format
 */
  format(
    options?: {
    pix_fmts?: FFString;
    color_spaces?: FFString;
    color_ranges?: FFString;
    alpha_modes?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "format", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "pix_fmts": options?.pix_fmts,
      "color_spaces": options?.color_spaces,
      "color_ranges": options?.color_ranges,
      "alpha_modes": options?.alpha_modes,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Force constant framerate.

 *
 * @param options.fps - A string describing desired output framerate (default "25")
 * @param options.start_time - Assume the first PTS should be this value. (from -DBL_MAX to DBL_MAX) (default DBL_MAX)
 * @param options.round - set rounding method for timestamps (from 0 to 5) (default near)
 * @param options.eof_action - action performed for last frame (from 0 to 1) (default round)
 * @see https://ffmpeg.org/ffmpeg-filters.html#fps
 */
  fps(
    options?: {
    fps?: FFString;
    start_time?: FFDouble;
    round?: FFInt | "zero" | "inf" | "down" | "up" | "near";
    eof_action?: FFInt | "round" | "pass";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "fps", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "fps": options?.fps,
      "start_time": options?.start_time,
      "round": options?.round,
      "eof_action": options?.eof_action,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Generate a frame packed stereoscopic video.

 *
 * @param options.format - Frame pack output format (from 0 to INT_MAX) (default sbs)
 * @see https://ffmpeg.org/ffmpeg-filters.html#framepack
 */
  framepack(
    _right: VideoStream,

    options?: {
    format?: FFInt | "sbs" | "tab" | "frameseq" | "lines" | "columns";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "framepack", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _right],
      merge(
    {
      "format": options?.format,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Upsamples or downsamples progressive source between specified frame rates.

 *
 * @param options.fps - required output frames per second rate (default "50")
 * @param options.interp_start - point to start linear interpolation (from 0 to 255) (default 15)
 * @param options.interp_end - point to end linear interpolation (from 0 to 255) (default 240)
 * @param options.scene - scene change level (from 0 to 100) (default 8.2)
 * @param options.flags - set flags (default scene_change_detect+scd)
 * @see https://ffmpeg.org/ffmpeg-filters.html#framerate
 */
  framerate(
    options?: {
    fps?: FFVideoRate;
    interp_start?: FFInt;
    interp_end?: FFInt;
    scene?: FFDouble;
    flags?: FFFlags | "scene_change_detect" | "scd";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "framerate", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "fps": options?.fps,
      "interp_start": options?.interp_start,
      "interp_end": options?.interp_end,
      "scene": options?.scene,
      "flags": options?.flags,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Select one frame every N frames.

 *
 * @param options.step - set frame step (from 1 to INT_MAX) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#framestep
 */
  framestep(
    options?: {
    step?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "framestep", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "step": options?.step,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Detects frozen video input.

 *
 * @param options.n - set noise tolerance (from 0 to 1) (default 0.001)
 * @param options.d - set minimum duration in seconds (default 2)
 * @see https://ffmpeg.org/ffmpeg-filters.html#freezedetect
 */
  freezedetect(
    options?: {
    n?: FFDouble;
    d?: FFDuration;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "freezedetect", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "n": options?.n,
      "d": options?.d,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Freeze video frames.

 *
 * @param options.first - set first frame to freeze (from 0 to I64_MAX) (default 0)
 * @param options.last - set last frame to freeze (from 0 to I64_MAX) (default 0)
 * @param options.replace - set frame to replace (from 0 to I64_MAX) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#freezeframes
 */
  freezeframes(
    _replace: VideoStream,

    options?: {
    first?: FFInt64;
    last?: FFInt64;
    replace?: FFInt64;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "freezeframes", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _replace],
      merge(
    {
      "first": options?.first,
      "last": options?.last,
      "replace": options?.replace,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply Fast Simple Post-processing filter.

 *
 * @param options.quality - set quality (from 4 to 5) (default 4)
 * @param options.qp - force a constant quantizer parameter (from 0 to 64) (default 0)
 * @param options.strength - set filter strength (from -15 to 32) (default 0)
 * @param options.use_bframe_qp - use B-frames' QP (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#fspp
 */
  fspp(
    options?: {
    quality?: FFInt;
    qp?: FFInt;
    strength?: FFInt;
    use_bframe_qp?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "fspp", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "quality": options?.quality,
      "qp": options?.qp,
      "strength": options?.strength,
      "use_bframe_qp": options?.use_bframe_qp,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Synchronize video frames from external source.

 *
 * @param options.file - set the file name to use for frame sync (default "")
 * @see https://ffmpeg.org/ffmpeg-filters.html#fsync
 */
  fsync(
    options?: {
    file?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "fsync", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "file": options?.file,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply Gaussian Blur filter.

 *
 * @param options.sigma - set sigma (from 0 to 1024) (default 0.5)
 * @param options.steps - set number of steps (from 1 to 6) (default 1)
 * @param options.planes - set planes to filter (from 0 to 15) (default 15)
 * @param options.sigmaV - set vertical sigma (from -1 to 1024) (default -1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#gblur
 */
  gblur(
    options?: {
    sigma?: FFFloat;
    steps?: FFInt;
    planes?: FFInt;
    sigmaV?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "gblur", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "sigma": options?.sigma,
      "steps": options?.steps,
      "planes": options?.planes,
      "sigmaV": options?.sigmaV,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply generic equation to each pixel.

 *
 * @param options.lum_expr - set luminance expression
 * @param options.cb_expr - set chroma blue expression
 * @param options.cr_expr - set chroma red expression
 * @param options.alpha_expr - set alpha expression
 * @param options.red_expr - set red expression
 * @param options.green_expr - set green expression
 * @param options.blue_expr - set blue expression
 * @param options.interpolation - set interpolation method (from 0 to 1) (default bilinear)
 * @see https://ffmpeg.org/ffmpeg-filters.html#geq
 */
  geq(
    options?: {
    lum_expr?: FFString;
    cb_expr?: FFString;
    cr_expr?: FFString;
    alpha_expr?: FFString;
    red_expr?: FFString;
    green_expr?: FFString;
    blue_expr?: FFString;
    interpolation?: FFInt | "nearest" | "n" | "bilinear" | "b";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "geq", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "lum_expr": options?.lum_expr,
      "cb_expr": options?.cb_expr,
      "cr_expr": options?.cr_expr,
      "alpha_expr": options?.alpha_expr,
      "red_expr": options?.red_expr,
      "green_expr": options?.green_expr,
      "blue_expr": options?.blue_expr,
      "interpolation": options?.interpolation,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Debands video quickly using gradients.

 *
 * @param options.strength - The maximum amount by which the filter will change any one pixel. (from 0.51 to 64) (default 1.2)
 * @param options.radius - The neighborhood to fit the gradient to. (from 4 to 32) (default 16)
 * @see https://ffmpeg.org/ffmpeg-filters.html#gradfun
 */
  gradfun(
    options?: {
    strength?: FFFloat;
    radius?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "gradfun", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "strength": options?.strength,
      "radius": options?.radius,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Show various filtergraph stats.

 *
 * @param options.size - set monitor size (default "hd720")
 * @param options.opacity - set video opacity (from 0 to 1) (default 0.9)
 * @param options.mode - set mode (default 0)
 * @param options.flags - set flags (default all+queue)
 * @param options.rate - set video rate (default "25")
 * @see https://ffmpeg.org/ffmpeg-filters.html#graphmonitor
 */
  graphmonitor(
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
      { name: "graphmonitor", typingsInput: ["video"], typingsOutput: ["video"] },
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
 * Adjust white balance using LAB gray world algorithm

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#grayworld
 */
  grayworld(
    options?: {
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "grayworld", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Estimates scene illumination by grey edge assumption.

 *
 * @param options.difford - set differentiation order (from 0 to 2) (default 1)
 * @param options.minknorm - set Minkowski norm (from 0 to 20) (default 1)
 * @param options.sigma - set sigma (from 0 to 1024) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#greyedge
 */
  greyedge(
    options?: {
    difford?: FFInt;
    minknorm?: FFInt;
    sigma?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "greyedge", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "difford": options?.difford,
      "minknorm": options?.minknorm,
      "sigma": options?.sigma,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }










/**
 * Adjust colors using a Hald CLUT.

 *
 * @param options.clut - when to process CLUT (from 0 to 1) (default all)
 * @param options.interp - select interpolation mode (from 0 to 4) (default tetrahedral)
 * @see https://ffmpeg.org/ffmpeg-filters.html#haldclut
 */
  haldclut(
    _clut: VideoStream,

    options?: {
    clut?: FFInt | "first" | "all";
    interp?: FFInt | "nearest" | "trilinear" | "tetrahedral" | "pyramid" | "prism";
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "haldclut", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _clut],
      merge(
    {
      "clut": options?.clut,
      "interp": options?.interp,
      "eof_action": options?.eofAction,
      "shortest": options?.shortest,
      "repeatlast": options?.repeatlast,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }












/**
 * Horizontally flip the input video.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#hflip
 */
  hflip(
    options?: {
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "hflip", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }












/**
 * Apply global color histogram equalization.

 *
 * @param options.strength - set the strength (from 0 to 1) (default 0.2)
 * @param options.intensity - set the intensity (from 0 to 1) (default 0.21)
 * @param options.antibanding - set the antibanding level (from 0 to 2) (default none)
 * @see https://ffmpeg.org/ffmpeg-filters.html#histeq
 */
  histeq(
    options?: {
    strength?: FFFloat;
    intensity?: FFFloat;
    antibanding?: FFInt | "none" | "weak" | "strong";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "histeq", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "strength": options?.strength,
      "intensity": options?.intensity,
      "antibanding": options?.antibanding,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Compute and draw a histogram.

 *
 * @param options.level_height - set level height (from 50 to 2048) (default 200)
 * @param options.scale_height - set scale height (from 0 to 40) (default 12)
 * @param options.display_mode - set display mode (from 0 to 2) (default stack)
 * @param options.levels_mode - set levels mode (from 0 to 1) (default linear)
 * @param options.components - set color components to display (from 1 to 15) (default 7)
 * @param options.fgopacity - set foreground opacity (from 0 to 1) (default 0.7)
 * @param options.bgopacity - set background opacity (from 0 to 1) (default 0.5)
 * @param options.colors_mode - set colors mode (from 0 to 9) (default whiteonblack)
 * @see https://ffmpeg.org/ffmpeg-filters.html#histogram
 */
  histogram(
    options?: {
    level_height?: FFInt;
    scale_height?: FFInt;
    display_mode?: FFInt | "overlay" | "parade" | "stack";
    levels_mode?: FFInt | "linear" | "logarithmic";
    components?: FFInt;
    fgopacity?: FFFloat;
    bgopacity?: FFFloat;
    colors_mode?: FFInt | "whiteonblack" | "blackonwhite" | "whiteongray" | "blackongray" | "coloronblack" | "coloronwhite" | "colorongray" | "blackoncolor" | "whiteoncolor" | "grayoncolor";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "histogram", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "level_height": options?.level_height,
      "scale_height": options?.scale_height,
      "display_mode": options?.display_mode,
      "levels_mode": options?.levels_mode,
      "components": options?.components,
      "fgopacity": options?.fgopacity,
      "bgopacity": options?.bgopacity,
      "colors_mode": options?.colors_mode,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply a High Quality 3D Denoiser.

 *
 * @param options.luma_spatial - spatial luma strength (from 0 to DBL_MAX) (default 0)
 * @param options.chroma_spatial - spatial chroma strength (from 0 to DBL_MAX) (default 0)
 * @param options.luma_tmp - temporal luma strength (from 0 to DBL_MAX) (default 0)
 * @param options.chroma_tmp - temporal chroma strength (from 0 to DBL_MAX) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#hqdn3d
 */
  hqdn3d(
    options?: {
    luma_spatial?: FFDouble;
    chroma_spatial?: FFDouble;
    luma_tmp?: FFDouble;
    chroma_tmp?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "hqdn3d", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "luma_spatial": options?.luma_spatial,
      "chroma_spatial": options?.chroma_spatial,
      "luma_tmp": options?.luma_tmp,
      "chroma_tmp": options?.chroma_tmp,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Scale the input by 2, 3 or 4 using the hq*x magnification algorithm.

 *
 * @param options.n - set scale factor (from 2 to 4) (default 3)
 * @see https://ffmpeg.org/ffmpeg-filters.html#hqx
 */
  hqx(
    options?: {
    n?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "hqx", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "n": options?.n,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Turns a certain HSV range into gray.

 *
 * @param options.hue - set the hue value (from -360 to 360) (default 0)
 * @param options.sat - set the saturation value (from -1 to 1) (default 0)
 * @param options.val - set the value value (from -1 to 1) (default 0)
 * @param options.similarity - set the hsvhold similarity value (from 1e-05 to 1) (default 0.01)
 * @param options.blend - set the hsvhold blend value (from 0 to 1) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#hsvhold
 */
  hsvhold(
    options?: {
    hue?: FFFloat;
    sat?: FFFloat;
    val?: FFFloat;
    similarity?: FFFloat;
    blend?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "hsvhold", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "hue": options?.hue,
      "sat": options?.sat,
      "val": options?.val,
      "similarity": options?.similarity,
      "blend": options?.blend,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Turns a certain HSV range into transparency. Operates on YUV colors.

 *
 * @param options.hue - set the hue value (from -360 to 360) (default 0)
 * @param options.sat - set the saturation value (from -1 to 1) (default 0)
 * @param options.val - set the value value (from -1 to 1) (default 0)
 * @param options.similarity - set the hsvkey similarity value (from 1e-05 to 1) (default 0.01)
 * @param options.blend - set the hsvkey blend value (from 0 to 1) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#hsvkey
 */
  hsvkey(
    options?: {
    hue?: FFFloat;
    sat?: FFFloat;
    val?: FFFloat;
    similarity?: FFFloat;
    blend?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "hsvkey", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "hue": options?.hue,
      "sat": options?.sat,
      "val": options?.val,
      "similarity": options?.similarity,
      "blend": options?.blend,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Adjust the hue and saturation of the input video.

 *
 * @param options.h - set the hue angle degrees expression
 * @param options.s - set the saturation expression (default "1")
 * @param options.H - set the hue angle radians expression
 * @param options.b - set the brightness expression (default "0")
 * @see https://ffmpeg.org/ffmpeg-filters.html#hue
 */
  hue(
    options?: {
    h?: FFString;
    s?: FFString;
    H?: FFString;
    b?: FFString;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "hue", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "h": options?.h,
      "s": options?.s,
      "H": options?.H,
      "b": options?.b,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply hue-saturation-intensity adjustments.

 *
 * @param options.hue - set the hue shift (from -180 to 180) (default 0)
 * @param options.saturation - set the saturation shift (from -1 to 1) (default 0)
 * @param options.intensity - set the intensity shift (from -1 to 1) (default 0)
 * @param options.colors - set colors range (default r+y+g+c+b+m+a)
 * @param options.strength - set the filtering strength (from 0 to 100) (default 1)
 * @param options.rw - set the red weight (from 0 to 1) (default 0.333)
 * @param options.gw - set the green weight (from 0 to 1) (default 0.334)
 * @param options.bw - set the blue weight (from 0 to 1) (default 0.333)
 * @param options.lightness - set the preserve lightness (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#huesaturation
 */
  huesaturation(
    options?: {
    hue?: FFFloat;
    saturation?: FFFloat;
    intensity?: FFFloat;
    colors?: FFFlags | "r" | "y" | "g" | "c" | "b" | "m" | "a";
    strength?: FFFloat;
    rw?: FFFloat;
    gw?: FFFloat;
    bw?: FFFloat;
    lightness?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "huesaturation", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "hue": options?.hue,
      "saturation": options?.saturation,
      "intensity": options?.intensity,
      "colors": options?.colors,
      "strength": options?.strength,
      "rw": options?.rw,
      "gw": options?.gw,
      "bw": options?.bw,
      "lightness": options?.lightness,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Download a hardware frame to a normal frame

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#hwdownload
 */
  hwdownload(
    options?: {
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "hwdownload", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Map hardware frames

 *
 * @param options.mode - Frame mapping mode (default read+write)
 * @param options.derive_device - Derive a new device of this type
 * @param options.reverse - Map in reverse (create and allocate in the sink) (from 0 to 1) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#hwmap
 */
  hwmap(
    options?: {
    mode?: FFFlags | "read" | "write" | "overwrite" | "direct";
    derive_device?: FFString;
    reverse?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "hwmap", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "mode": options?.mode,
      "derive_device": options?.derive_device,
      "reverse": options?.reverse,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Upload a normal frame to a hardware frame

 *
 * @param options.derive_device - Derive a new device of this type
 * @see https://ffmpeg.org/ffmpeg-filters.html#hwupload
 */
  hwupload(
    options?: {
    derive_device?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "hwupload", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "derive_device": options?.derive_device,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Grow first stream into second stream by connecting components.

 *
 * @param options.planes - set planes (from 0 to 15) (default 15)
 * @param options.threshold - set threshold (from 0 to 65535) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#hysteresis
 */
  hysteresis(
    _alt: VideoStream,

    options?: {
    planes?: FFInt;
    threshold?: FFInt;
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "hysteresis", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _alt],
      merge(
    {
      "planes": options?.planes,
      "threshold": options?.threshold,
      "eof_action": options?.eofAction,
      "shortest": options?.shortest,
      "repeatlast": options?.repeatlast,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Calculate the Identity between two video streams.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#identity
 */
  identity(
    _reference: VideoStream,

    options?: {
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "identity", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _reference],
      merge(
    {
      "eof_action": options?.eofAction,
      "shortest": options?.shortest,
      "repeatlast": options?.repeatlast,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Interlace detect Filter.

 *
 * @param options.intl_thres - set interlacing threshold (from -1 to FLT_MAX) (default 1.04)
 * @param options.prog_thres - set progressive threshold (from -1 to FLT_MAX) (default 1.5)
 * @param options.rep_thres - set repeat threshold (from -1 to FLT_MAX) (default 3)
 * @param options.half_life - half life of cumulative statistics (from -1 to INT_MAX) (default 0)
 * @param options.analyze_interlaced_flag - set number of frames to use to determine if the interlace flag is accurate (from 0 to INT_MAX) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#idet
 */
  idet(
    options?: {
    intl_thres?: FFFloat;
    prog_thres?: FFFloat;
    rep_thres?: FFFloat;
    half_life?: FFFloat;
    analyze_interlaced_flag?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "idet", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "intl_thres": options?.intl_thres,
      "prog_thres": options?.prog_thres,
      "rep_thres": options?.rep_thres,
      "half_life": options?.half_life,
      "analyze_interlaced_flag": options?.analyze_interlaced_flag,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Deinterleave or interleave fields.

 *
 * @param options.luma_mode - select luma mode (from 0 to 2) (default none)
 * @param options.chroma_mode - select chroma mode (from 0 to 2) (default none)
 * @param options.alpha_mode - select alpha mode (from 0 to 2) (default none)
 * @param options.luma_swap - swap luma fields (default false)
 * @param options.chroma_swap - swap chroma fields (default false)
 * @param options.alpha_swap - swap alpha fields (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#il
 */
  il(
    options?: {
    luma_mode?: FFInt | "none" | "interleave" | "i" | "deinterleave" | "d";
    chroma_mode?: FFInt | "none" | "interleave" | "i" | "deinterleave" | "d";
    alpha_mode?: FFInt | "none" | "interleave" | "i" | "deinterleave" | "d";
    luma_swap?: FFBoolean;
    chroma_swap?: FFBoolean;
    alpha_swap?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "il", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "luma_mode": options?.luma_mode,
      "chroma_mode": options?.chroma_mode,
      "alpha_mode": options?.alpha_mode,
      "luma_swap": options?.luma_swap,
      "chroma_swap": options?.chroma_swap,
      "alpha_swap": options?.alpha_swap,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply inflate effect.

 *
 * @param options.threshold0 - set threshold for 1st plane (from 0 to 65535) (default 65535)
 * @param options.threshold1 - set threshold for 2nd plane (from 0 to 65535) (default 65535)
 * @param options.threshold2 - set threshold for 3rd plane (from 0 to 65535) (default 65535)
 * @param options.threshold3 - set threshold for 4th plane (from 0 to 65535) (default 65535)
 * @see https://ffmpeg.org/ffmpeg-filters.html#inflate
 */
  inflate(
    options?: {
    threshold0?: FFInt;
    threshold1?: FFInt;
    threshold2?: FFInt;
    threshold3?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "inflate", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "threshold0": options?.threshold0,
      "threshold1": options?.threshold1,
      "threshold2": options?.threshold2,
      "threshold3": options?.threshold3,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Convert progressive video into interlaced.

 *
 * @param options.scan - scanning mode (from 0 to 1) (default tff)
 * @param options.lowpass - set vertical low-pass filter (from 0 to 2) (default linear)
 * @see https://ffmpeg.org/ffmpeg-filters.html#interlace_002c-interlace_005fvulkan
 */
  interlace(
    options?: {
    scan?: FFInt | "tff" | "bff";
    lowpass?: FFInt | "off" | "linear" | "complex";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "interlace", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "scan": options?.scan,
      "lowpass": options?.lowpass,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }










/**
 * Apply kernel deinterlacing to the input.

 *
 * @param options.thresh - set the threshold (from 0 to 255) (default 10)
 * @param options.map - set the map (default false)
 * @param options.order - set the order (default false)
 * @param options.sharp - set sharpening (default false)
 * @param options.twoway - set twoway (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#kerndeint
 */
  kerndeint(
    options?: {
    thresh?: FFInt;
    map?: FFBoolean;
    order?: FFBoolean;
    sharp?: FFBoolean;
    twoway?: FFBoolean;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "kerndeint", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "thresh": options?.thresh,
      "map": options?.map,
      "order": options?.order,
      "sharp": options?.sharp,
      "twoway": options?.twoway,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply kirsch operator.

 *
 * @param options.planes - set planes to filter (from 0 to 15) (default 15)
 * @param options.scale - set scale (from 0 to 65535) (default 1)
 * @param options.delta - set delta (from -65535 to 65535) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#kirsch
 */
  kirsch(
    options?: {
    planes?: FFInt;
    scale?: FFFloat;
    delta?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "kirsch", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "planes": options?.planes,
      "scale": options?.scale,
      "delta": options?.delta,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Slowly update darker pixels.

 *
 * @param options.decay - set decay (from 0 to 1) (default 0.95)
 * @param options.planes - set what planes to filter (default F)
 * @see https://ffmpeg.org/ffmpeg-filters.html#lagfun
 */
  lagfun(
    options?: {
    decay?: FFFloat;
    planes?: FFFlags;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "lagfun", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "decay": options?.decay,
      "planes": options?.planes,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Report video filtering latency.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#latency_002c-alatency
 */
  latency(
    options?: {
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "latency", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Rectify the image by correcting for lens distortion.

 *
 * @param options.cx - set relative center x (from 0 to 1) (default 0.5)
 * @param options.cy - set relative center y (from 0 to 1) (default 0.5)
 * @param options.k1 - set quadratic distortion factor (from -1 to 1) (default 0)
 * @param options.k2 - set double quadratic distortion factor (from -1 to 1) (default 0)
 * @param options.i - set interpolation type (from 0 to 64) (default nearest)
 * @param options.fc - set the color of the unmapped pixels (default "black@0")
 * @see https://ffmpeg.org/ffmpeg-filters.html#lenscorrection
 */
  lenscorrection(
    options?: {
    cx?: FFDouble;
    cy?: FFDouble;
    k1?: FFDouble;
    k2?: FFDouble;
    i?: FFInt | "nearest" | "bilinear";
    fc?: FFColor;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "lenscorrection", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "cx": options?.cx,
      "cy": options?.cy,
      "k1": options?.k1,
      "k2": options?.k2,
      "i": options?.i,
      "fc": options?.fc,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }










/**
 * Limit pixels components to the specified range.

 *
 * @param options.min - set min value (from 0 to 65535) (default 0)
 * @param options.max - set max value (from 0 to 65535) (default 65535)
 * @param options.planes - set planes (from 0 to 15) (default 15)
 * @see https://ffmpeg.org/ffmpeg-filters.html#limiter
 */
  limiter(
    options?: {
    min?: FFInt;
    max?: FFInt;
    planes?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "limiter", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "min": options?.min,
      "max": options?.max,
      "planes": options?.planes,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Loop video frames.

 *
 * @param options.loop - number of loops (from -1 to INT_MAX) (default 0)
 * @param options.size - max number of frames to loop (from 0 to 32767) (default 0)
 * @param options.start - set the loop start frame (from -1 to I64_MAX) (default 0)
 * @param options.time - set the loop start time (default INT64_MAX)
 * @see https://ffmpeg.org/ffmpeg-filters.html#loop
 */
  loop(
    options?: {
    loop?: FFInt;
    size?: FFInt64;
    start?: FFInt64;
    time?: FFDuration;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "loop", typingsInput: ["video"], typingsOutput: ["video"] },
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
return filterNode.video(0) as unknown as VideoStream;
  }












/**
 * Turns a certain luma into transparency.

 *
 * @param options.threshold - set the threshold value (from 0 to 1) (default 0)
 * @param options.tolerance - set the tolerance value (from 0 to 1) (default 0.01)
 * @param options.softness - set the softness value (from 0 to 1) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#lumakey
 */
  lumakey(
    options?: {
    threshold?: FFDouble;
    tolerance?: FFDouble;
    softness?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "lumakey", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "threshold": options?.threshold,
      "tolerance": options?.tolerance,
      "softness": options?.softness,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Compute and apply a lookup table to the RGB/YUV input video.

 *
 * @param options.c0 - set component #0 expression (default "clipval")
 * @param options.c1 - set component #1 expression (default "clipval")
 * @param options.c2 - set component #2 expression (default "clipval")
 * @param options.c3 - set component #3 expression (default "clipval")
 * @param options.y - set Y expression (default "clipval")
 * @param options.u - set U expression (default "clipval")
 * @param options.v - set V expression (default "clipval")
 * @param options.r - set R expression (default "clipval")
 * @param options.g - set G expression (default "clipval")
 * @param options.b - set B expression (default "clipval")
 * @param options.a - set A expression (default "clipval")
 * @see https://ffmpeg.org/ffmpeg-filters.html#lut_002c-lutrgb_002c-lutyuv
 */
  lut(
    options?: {
    c0?: FFString;
    c1?: FFString;
    c2?: FFString;
    c3?: FFString;
    y?: FFString;
    u?: FFString;
    v?: FFString;
    r?: FFString;
    g?: FFString;
    b?: FFString;
    a?: FFString;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "lut", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "c0": options?.c0,
      "c1": options?.c1,
      "c2": options?.c2,
      "c3": options?.c3,
      "y": options?.y,
      "u": options?.u,
      "v": options?.v,
      "r": options?.r,
      "g": options?.g,
      "b": options?.b,
      "a": options?.a,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Adjust colors using a 1D LUT.

 *
 * @param options.file - set 1D LUT file name
 * @param options.interp - select interpolation mode (from 0 to 4) (default linear)
 * @see https://ffmpeg.org/ffmpeg-filters.html#lut1d
 */
  lut1d(
    options?: {
    file?: FFString;
    interp?: FFInt | "nearest" | "linear" | "cosine" | "cubic" | "spline";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "lut1d", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "file": options?.file,
      "interp": options?.interp,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Compute and apply a lookup table from two video inputs.

 *
 * @param options.c0 - set component #0 expression (default "x")
 * @param options.c1 - set component #1 expression (default "x")
 * @param options.c2 - set component #2 expression (default "x")
 * @param options.c3 - set component #3 expression (default "x")
 * @param options.d - set output depth (from 0 to 16) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#lut2_002c-tlut2
 */
  lut2(
    _srcy: VideoStream,

    options?: {
    c0?: FFString;
    c1?: FFString;
    c2?: FFString;
    c3?: FFString;
    d?: FFInt;
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "lut2", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _srcy],
      merge(
    {
      "c0": options?.c0,
      "c1": options?.c1,
      "c2": options?.c2,
      "c3": options?.c3,
      "d": options?.d,
      "eof_action": options?.eofAction,
      "shortest": options?.shortest,
      "repeatlast": options?.repeatlast,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Adjust colors using a 3D LUT.

 *
 * @param options.file - set 3D LUT file name
 * @param options.clut - when to process CLUT (from 0 to 1) (default all)
 * @param options.interp - select interpolation mode (from 0 to 4) (default tetrahedral)
 * @see https://ffmpeg.org/ffmpeg-filters.html#lut3d
 */
  lut3d(
    options?: {
    file?: FFString;
    clut?: FFInt | "first" | "all";
    interp?: FFInt | "nearest" | "trilinear" | "tetrahedral" | "pyramid" | "prism";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "lut3d", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "file": options?.file,
      "clut": options?.clut,
      "interp": options?.interp,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Compute and apply a lookup table to the RGB input video.

 *
 * @param options.c0 - set component #0 expression (default "clipval")
 * @param options.c1 - set component #1 expression (default "clipval")
 * @param options.c2 - set component #2 expression (default "clipval")
 * @param options.c3 - set component #3 expression (default "clipval")
 * @param options.y - set Y expression (default "clipval")
 * @param options.u - set U expression (default "clipval")
 * @param options.v - set V expression (default "clipval")
 * @param options.r - set R expression (default "clipval")
 * @param options.g - set G expression (default "clipval")
 * @param options.b - set B expression (default "clipval")
 * @param options.a - set A expression (default "clipval")
 * @see https://ffmpeg.org/ffmpeg-filters.html#lut_002c-lutrgb_002c-lutyuv
 */
  lutrgb(
    options?: {
    c0?: FFString;
    c1?: FFString;
    c2?: FFString;
    c3?: FFString;
    y?: FFString;
    u?: FFString;
    v?: FFString;
    r?: FFString;
    g?: FFString;
    b?: FFString;
    a?: FFString;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "lutrgb", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "c0": options?.c0,
      "c1": options?.c1,
      "c2": options?.c2,
      "c3": options?.c3,
      "y": options?.y,
      "u": options?.u,
      "v": options?.v,
      "r": options?.r,
      "g": options?.g,
      "b": options?.b,
      "a": options?.a,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Compute and apply a lookup table to the YUV input video.

 *
 * @param options.c0 - set component #0 expression (default "clipval")
 * @param options.c1 - set component #1 expression (default "clipval")
 * @param options.c2 - set component #2 expression (default "clipval")
 * @param options.c3 - set component #3 expression (default "clipval")
 * @param options.y - set Y expression (default "clipval")
 * @param options.u - set U expression (default "clipval")
 * @param options.v - set V expression (default "clipval")
 * @param options.r - set R expression (default "clipval")
 * @param options.g - set G expression (default "clipval")
 * @param options.b - set B expression (default "clipval")
 * @param options.a - set A expression (default "clipval")
 * @see https://ffmpeg.org/ffmpeg-filters.html#lut_002c-lutrgb_002c-lutyuv
 */
  lutyuv(
    options?: {
    c0?: FFString;
    c1?: FFString;
    c2?: FFString;
    c3?: FFString;
    y?: FFString;
    u?: FFString;
    v?: FFString;
    r?: FFString;
    g?: FFString;
    b?: FFString;
    a?: FFString;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "lutyuv", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "c0": options?.c0,
      "c1": options?.c1,
      "c2": options?.c2,
      "c3": options?.c3,
      "y": options?.y,
      "u": options?.u,
      "v": options?.v,
      "r": options?.r,
      "g": options?.g,
      "b": options?.b,
      "a": options?.a,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Clamp first stream with second stream and third stream.

 *
 * @param options.undershoot - set undershoot (from 0 to 65535) (default 0)
 * @param options.overshoot - set overshoot (from 0 to 65535) (default 0)
 * @param options.planes - set planes (from 0 to 15) (default 15)
 * @see https://ffmpeg.org/ffmpeg-filters.html#maskedclamp
 */
  maskedclamp(
    _dark: VideoStream,
    _bright: VideoStream,

    options?: {
    undershoot?: FFInt;
    overshoot?: FFInt;
    planes?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "maskedclamp", typingsInput: ["video", "video", "video"], typingsOutput: ["video"] },
      [this, _dark, _bright],
      merge(
    {
      "undershoot": options?.undershoot,
      "overshoot": options?.overshoot,
      "planes": options?.planes,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply filtering with maximum difference of two streams.

 *
 * @param options.planes - set planes (from 0 to 15) (default 15)
 * @see https://ffmpeg.org/ffmpeg-filters.html#maskedmax
 */
  maskedmax(
    _filter1: VideoStream,
    _filter2: VideoStream,

    options?: {
    planes?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "maskedmax", typingsInput: ["video", "video", "video"], typingsOutput: ["video"] },
      [this, _filter1, _filter2],
      merge(
    {
      "planes": options?.planes,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Merge first stream with second stream using third stream as mask.

 *
 * @param options.planes - set planes (from 0 to 15) (default 15)
 * @see https://ffmpeg.org/ffmpeg-filters.html#maskedmerge
 */
  maskedmerge(
    _overlay: VideoStream,
    _mask: VideoStream,

    options?: {
    planes?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "maskedmerge", typingsInput: ["video", "video", "video"], typingsOutput: ["video"] },
      [this, _overlay, _mask],
      merge(
    {
      "planes": options?.planes,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply filtering with minimum difference of two streams.

 *
 * @param options.planes - set planes (from 0 to 15) (default 15)
 * @see https://ffmpeg.org/ffmpeg-filters.html#maskedmin
 */
  maskedmin(
    _filter1: VideoStream,
    _filter2: VideoStream,

    options?: {
    planes?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "maskedmin", typingsInput: ["video", "video", "video"], typingsOutput: ["video"] },
      [this, _filter1, _filter2],
      merge(
    {
      "planes": options?.planes,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Pick pixels comparing absolute difference of two streams with threshold.

 *
 * @param options.threshold - set threshold (from 0 to 65535) (default 1)
 * @param options.planes - set planes (from 0 to 15) (default 15)
 * @param options.mode - set mode (from 0 to 1) (default abs)
 * @see https://ffmpeg.org/ffmpeg-filters.html#maskedthreshold
 */
  maskedthreshold(
    _reference: VideoStream,

    options?: {
    threshold?: FFInt;
    planes?: FFInt;
    mode?: FFInt | "abs" | "diff";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "maskedthreshold", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _reference],
      merge(
    {
      "threshold": options?.threshold,
      "planes": options?.planes,
      "mode": options?.mode,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Create Mask.

 *
 * @param options.low - set low threshold (from 0 to 65535) (default 10)
 * @param options.high - set high threshold (from 0 to 65535) (default 10)
 * @param options.planes - set planes (from 0 to 15) (default 15)
 * @param options.fill - set fill value (from 0 to 65535) (default 0)
 * @param options.sum - set sum value (from 0 to 65535) (default 10)
 * @see https://ffmpeg.org/ffmpeg-filters.html#maskfun
 */
  maskfun(
    options?: {
    low?: FFInt;
    high?: FFInt;
    planes?: FFInt;
    fill?: FFInt;
    sum?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "maskfun", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "low": options?.low,
      "high": options?.high,
      "planes": options?.planes,
      "fill": options?.fill,
      "sum": options?.sum,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply motion compensating deinterlacing.

 *
 * @param options.mode - set mode (from 0 to 3) (default fast)
 * @param options.parity - set the assumed picture field parity (from -1 to 1) (default bff)
 * @param options.qp - set qp (from INT_MIN to INT_MAX) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#mcdeint
 */
  mcdeint(
    options?: {
    mode?: FFInt | "fast" | "medium" | "slow" | "extra_slow";
    parity?: FFInt | "tff" | "bff";
    qp?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "mcdeint", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "mode": options?.mode,
      "parity": options?.parity,
      "qp": options?.qp,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Apply Median filter.

 *
 * @param options.radius - set median radius (from 1 to 127) (default 1)
 * @param options.planes - set planes to filter (from 0 to 15) (default 15)
 * @param options.radiusV - set median vertical radius (from 0 to 127) (default 0)
 * @param options.percentile - set median percentile (from 0 to 1) (default 0.5)
 * @see https://ffmpeg.org/ffmpeg-filters.html#median
 */
  median(
    options?: {
    radius?: FFInt;
    planes?: FFInt;
    radiusV?: FFInt;
    percentile?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "median", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "radius": options?.radius,
      "planes": options?.planes,
      "radiusV": options?.radiusV,
      "percentile": options?.percentile,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Generate motion vectors.

 *
 * @param options.method - motion estimation method (from 1 to 9) (default esa)
 * @param options.mb_size - macroblock size (from 8 to INT_MAX) (default 16)
 * @param options.search_param - search parameter (from 4 to INT_MAX) (default 7)
 * @see https://ffmpeg.org/ffmpeg-filters.html#mestimate
 */
  mestimate(
    options?: {
    method?: FFInt | "esa" | "tss" | "tdls" | "ntss" | "fss" | "ds" | "hexbs" | "epzs" | "umh";
    mb_size?: FFInt;
    search_param?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "mestimate", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "method": options?.method,
      "mb_size": options?.mb_size,
      "search_param": options?.search_param,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Manipulate video frame metadata.

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
  metadata(
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
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "metadata", typingsInput: ["video"], typingsOutput: ["video"] },
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
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply Midway Equalization.

 *
 * @param options.planes - set planes (from 0 to 15) (default 15)
 * @see https://ffmpeg.org/ffmpeg-filters.html#midequalizer
 */
  midequalizer(
    _in1: VideoStream,

    options?: {
    planes?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "midequalizer", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _in1],
      merge(
    {
      "planes": options?.planes,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Frame rate conversion using Motion Interpolation.

 *
 * @param options.fps - output's frame rate (default "60")
 * @param options.mi_mode - motion interpolation mode (from 0 to 2) (default mci)
 * @param options.mc_mode - motion compensation mode (from 0 to 1) (default obmc)
 * @param options.me_mode - motion estimation mode (from 0 to 1) (default bilat)
 * @param options.me - motion estimation method (from 1 to 9) (default epzs)
 * @param options.mb_size - macroblock size (from 4 to 16) (default 16)
 * @param options.search_param - search parameter (from 4 to INT_MAX) (default 32)
 * @param options.vsbmc - variable-size block motion compensation (from 0 to 1) (default 0)
 * @param options.scd - scene change detection method (from 0 to 1) (default fdiff)
 * @param options.scd_threshold - scene change threshold (from 0 to 100) (default 10)
 * @see https://ffmpeg.org/ffmpeg-filters.html#minterpolate
 */
  minterpolate(
    options?: {
    fps?: FFVideoRate;
    mi_mode?: FFInt | "dup" | "blend" | "mci";
    mc_mode?: FFInt | "obmc" | "aobmc";
    me_mode?: FFInt | "bidir" | "bilat";
    me?: FFInt | "esa" | "tss" | "tdls" | "ntss" | "fss" | "ds" | "hexbs" | "epzs" | "umh";
    mb_size?: FFInt;
    search_param?: FFInt;
    vsbmc?: FFInt;
    scd?: FFInt | "none" | "fdiff";
    scd_threshold?: FFDouble;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "minterpolate", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "fps": options?.fps,
      "mi_mode": options?.mi_mode,
      "mc_mode": options?.mc_mode,
      "me_mode": options?.me_mode,
      "me": options?.me,
      "mb_size": options?.mb_size,
      "search_param": options?.search_param,
      "vsbmc": options?.vsbmc,
      "scd": options?.scd,
      "scd_threshold": options?.scd_threshold,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Convert video to gray using custom color filter.

 *
 * @param options.cb - set the chroma blue spot (from -1 to 1) (default 0)
 * @param options.cr - set the chroma red spot (from -1 to 1) (default 0)
 * @param options.size - set the color filter size (from 0.1 to 10) (default 1)
 * @param options.high - set the highlights strength (from 0 to 1) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#monochrome
 */
  monochrome(
    options?: {
    cb?: FFFloat;
    cr?: FFFloat;
    size?: FFFloat;
    high?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "monochrome", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "cb": options?.cb,
      "cr": options?.cr,
      "size": options?.size,
      "high": options?.high,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply Morphological filter.

 *
 * @param options.mode - set morphological transform (from 0 to 6) (default erode)
 * @param options.planes - set planes to filter (from 0 to 15) (default 7)
 * @param options.structure - when to process structures (from 0 to 1) (default all)
 * @see https://ffmpeg.org/ffmpeg-filters.html#morpho
 */
  morpho(
    _structure: VideoStream,

    options?: {
    mode?: FFInt | "erode" | "dilate" | "open" | "close" | "gradient" | "tophat" | "blackhat";
    planes?: FFInt;
    structure?: FFInt | "first" | "all";
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "morpho", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _structure],
      merge(
    {
      "mode": options?.mode,
      "planes": options?.planes,
      "structure": options?.structure,
      "eof_action": options?.eofAction,
      "shortest": options?.shortest,
      "repeatlast": options?.repeatlast,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Remove near-duplicate frames.

 *
 * @param options.max - set the maximum number of consecutive dropped frames (positive), or the minimum interval between dropped frames (negative) (from INT_MIN to INT_MAX) (default 0)
 * @param options.keep - set the number of similar consecutive frames to be kept before starting to drop similar frames (from 0 to INT_MAX) (default 0)
 * @param options.hi - set high dropping threshold (from INT_MIN to INT_MAX) (default 768)
 * @param options.lo - set low dropping threshold (from INT_MIN to INT_MAX) (default 320)
 * @param options.frac - set fraction dropping threshold (from 0 to 1) (default 0.33)
 * @see https://ffmpeg.org/ffmpeg-filters.html#mpdecimate
 */
  mpdecimate(
    options?: {
    max?: FFInt;
    keep?: FFInt;
    hi?: FFInt;
    lo?: FFInt;
    frac?: FFFloat;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "mpdecimate", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "max": options?.max,
      "keep": options?.keep,
      "hi": options?.hi,
      "lo": options?.lo,
      "frac": options?.frac,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Calculate the MSAD between two video streams.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#msad
 */
  msad(
    _reference: VideoStream,

    options?: {
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "msad", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _reference],
      merge(
    {
      "eof_action": options?.eofAction,
      "shortest": options?.shortest,
      "repeatlast": options?.repeatlast,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Multiply first video stream with second video stream.

 *
 * @param options.scale - set scale (from 0 to 9) (default 1)
 * @param options.offset - set offset (from -1 to 1) (default 0.5)
 * @param options.planes - set planes (default F)
 * @see https://ffmpeg.org/ffmpeg-filters.html#multiply
 */
  multiply(
    _factor: VideoStream,

    options?: {
    scale?: FFFloat;
    offset?: FFFloat;
    planes?: FFFlags;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "multiply", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _factor],
      merge(
    {
      "scale": options?.scale,
      "offset": options?.offset,
      "planes": options?.planes,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Negate input video.

 *
 * @param options.components - set components to negate (default y+u+v+r+g+b)
 * @param options.negate_alpha - (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#negate
 */
  negate(
    options?: {
    components?: FFFlags | "y" | "u" | "v" | "r" | "g" | "b" | "a";
    negate_alpha?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "negate", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "components": options?.components,
      "negate_alpha": options?.negate_alpha,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Non-local means denoiser.

 *
 * @param options.s - denoising strength (from 1 to 30) (default 1)
 * @param options.p - patch size (from 0 to 99) (default 7)
 * @param options.pc - patch size for chroma planes (from 0 to 99) (default 0)
 * @param options.r - research window (from 0 to 99) (default 15)
 * @param options.rc - research window for chroma planes (from 0 to 99) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#nlmeans
 */
  nlmeans(
    options?: {
    s?: FFDouble;
    p?: FFInt;
    pc?: FFInt;
    r?: FFInt;
    rc?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "nlmeans", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "s": options?.s,
      "p": options?.p,
      "pc": options?.pc,
      "r": options?.r,
      "rc": options?.rc,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply neural network edge directed interpolation intra-only deinterlacer.

 *
 * @param options.weights - set weights file (default "nnedi3_weights.bin")
 * @param options.deint - set which frames to deinterlace (from 0 to 1) (default all)
 * @param options.field - set mode of operation (from -2 to 3) (default a)
 * @param options.planes - set which planes to process (from 0 to 15) (default 7)
 * @param options.nsize - set size of local neighborhood around each pixel, used by the predictor neural network (from 0 to 6) (default s32x4)
 * @param options.nns - set number of neurons in predictor neural network (from 0 to 4) (default n32)
 * @param options.qual - set quality (from 1 to 2) (default fast)
 * @param options.etype - set which set of weights to use in the predictor (from 0 to 1) (default a)
 * @param options.pscrn - set prescreening (from 0 to 4) (default new)
 * @see https://ffmpeg.org/ffmpeg-filters.html#nnedi
 */
  nnedi(
    options?: {
    weights?: FFString;
    deint?: FFInt | "all" | "interlaced";
    field?: FFInt | "af" | "a" | "t" | "b" | "tf" | "bf";
    planes?: FFInt;
    nsize?: FFInt | "s8x6" | "s16x6" | "s32x6" | "s48x6" | "s8x4" | "s16x4" | "s32x4";
    nns?: FFInt | "n16" | "n32" | "n64" | "n128" | "n256";
    qual?: FFInt | "fast" | "slow";
    etype?: FFInt | "a" | "abs" | "s" | "mse";
    pscrn?: FFInt | "none" | "original" | "new" | "new2" | "new3";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "nnedi", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "weights": options?.weights,
      "deint": options?.deint,
      "field": options?.field,
      "planes": options?.planes,
      "nsize": options?.nsize,
      "nns": options?.nns,
      "qual": options?.qual,
      "etype": options?.etype,
      "pscrn": options?.pscrn,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Force libavfilter not to use any of the specified pixel formats for the input to the next filter.

 *
 * @param options.pix_fmts - A '|'-separated list of pixel formats
 * @param options.color_spaces - A '|'-separated list of color spaces
 * @param options.color_ranges - A '|'-separated list of color ranges
 * @param options.alpha_modes - A '|'-separated list of alpha modes
 * @see https://ffmpeg.org/ffmpeg-filters.html#noformat
 */
  noformat(
    options?: {
    pix_fmts?: FFString;
    color_spaces?: FFString;
    color_ranges?: FFString;
    alpha_modes?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "noformat", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "pix_fmts": options?.pix_fmts,
      "color_spaces": options?.color_spaces,
      "color_ranges": options?.color_ranges,
      "alpha_modes": options?.alpha_modes,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Add noise.

 *
 * @param options.all_seed - set component #0 noise seed (from -1 to INT_MAX) (default -1)
 * @param options.all_strength - set component #0 strength (from 0 to 100) (default 0)
 * @param options.all_flags - set component #0 flags (default 0)
 * @param options.c0_seed - set component #0 noise seed (from -1 to INT_MAX) (default -1)
 * @param options.c0_strength - set component #0 strength (from 0 to 100) (default 0)
 * @param options.c0_flags - set component #0 flags (default 0)
 * @param options.c1_seed - set component #1 noise seed (from -1 to INT_MAX) (default -1)
 * @param options.c1_strength - set component #1 strength (from 0 to 100) (default 0)
 * @param options.c1_flags - set component #1 flags (default 0)
 * @param options.c2_seed - set component #2 noise seed (from -1 to INT_MAX) (default -1)
 * @param options.c2_strength - set component #2 strength (from 0 to 100) (default 0)
 * @param options.c2_flags - set component #2 flags (default 0)
 * @param options.c3_seed - set component #3 noise seed (from -1 to INT_MAX) (default -1)
 * @param options.c3_strength - set component #3 strength (from 0 to 100) (default 0)
 * @param options.c3_flags - set component #3 flags (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#noise
 */
  noise(
    options?: {
    all_seed?: FFInt;
    all_strength?: FFInt;
    all_flags?: FFFlags | "a" | "p" | "t" | "u";
    c0_seed?: FFInt;
    c0_strength?: FFInt;
    c0_flags?: FFFlags | "a" | "p" | "t" | "u";
    c1_seed?: FFInt;
    c1_strength?: FFInt;
    c1_flags?: FFFlags | "a" | "p" | "t" | "u";
    c2_seed?: FFInt;
    c2_strength?: FFInt;
    c2_flags?: FFFlags | "a" | "p" | "t" | "u";
    c3_seed?: FFInt;
    c3_strength?: FFInt;
    c3_flags?: FFFlags | "a" | "p" | "t" | "u";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "noise", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "all_seed": options?.all_seed,
      "all_strength": options?.all_strength,
      "all_flags": options?.all_flags,
      "c0_seed": options?.c0_seed,
      "c0_strength": options?.c0_strength,
      "c0_flags": options?.c0_flags,
      "c1_seed": options?.c1_seed,
      "c1_strength": options?.c1_strength,
      "c1_flags": options?.c1_flags,
      "c2_seed": options?.c2_seed,
      "c2_strength": options?.c2_strength,
      "c2_flags": options?.c2_flags,
      "c3_seed": options?.c3_seed,
      "c3_strength": options?.c3_strength,
      "c3_flags": options?.c3_flags,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Normalize RGB video.

 *
 * @param options.blackpt - output color to which darkest input color is mapped (default "black")
 * @param options.whitept - output color to which brightest input color is mapped (default "white")
 * @param options.smoothing - amount of temporal smoothing of the input range, to reduce flicker (from 0 to 2.68435e+08) (default 0)
 * @param options.independence - proportion of independent to linked channel normalization (from 0 to 1) (default 1)
 * @param options.strength - strength of filter, from no effect to full normalization (from 0 to 1) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#normalize
 */
  normalize(
    options?: {
    blackpt?: FFColor;
    whitept?: FFColor;
    smoothing?: FFInt;
    independence?: FFFloat;
    strength?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "normalize", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "blackpt": options?.blackpt,
      "whitept": options?.whitept,
      "smoothing": options?.smoothing,
      "independence": options?.independence,
      "strength": options?.strength,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Pass the source unchanged to the output.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#null
 */
  _null(
    options?: {
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "null", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }










/**
 * 2D Video Oscilloscope.

 *
 * @param options.x - set scope x position (from 0 to 1) (default 0.5)
 * @param options.y - set scope y position (from 0 to 1) (default 0.5)
 * @param options.s - set scope size (from 0 to 1) (default 0.8)
 * @param options.t - set scope tilt (from 0 to 1) (default 0.5)
 * @param options.o - set trace opacity (from 0 to 1) (default 0.8)
 * @param options.tx - set trace x position (from 0 to 1) (default 0.5)
 * @param options.ty - set trace y position (from 0 to 1) (default 0.9)
 * @param options.tw - set trace width (from 0.1 to 1) (default 0.8)
 * @param options.th - set trace height (from 0.1 to 1) (default 0.3)
 * @param options.c - set components to trace (from 0 to 15) (default 7)
 * @param options.g - draw trace grid (default true)
 * @param options.st - draw statistics (default true)
 * @param options.sc - draw scope (default true)
 * @see https://ffmpeg.org/ffmpeg-filters.html#oscilloscope
 */
  oscilloscope(
    options?: {
    x?: FFFloat;
    y?: FFFloat;
    s?: FFFloat;
    t?: FFFloat;
    o?: FFFloat;
    tx?: FFFloat;
    ty?: FFFloat;
    tw?: FFFloat;
    th?: FFFloat;
    c?: FFInt;
    g?: FFBoolean;
    st?: FFBoolean;
    sc?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "oscilloscope", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "x": options?.x,
      "y": options?.y,
      "s": options?.s,
      "t": options?.t,
      "o": options?.o,
      "tx": options?.tx,
      "ty": options?.ty,
      "tw": options?.tw,
      "th": options?.th,
      "c": options?.c,
      "g": options?.g,
      "st": options?.st,
      "sc": options?.sc,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Overlay a video source on top of the input.

 *
 * @param options.x - set the x expression (default "0")
 * @param options.y - set the y expression (default "0")
 * @param options.eof_action - Action to take when encountering EOF from secondary input (from 0 to 2) (default repeat)
 * @param options.eval - specify when to evaluate expressions (from 0 to 1) (default frame)
 * @param options.shortest - force termination when the shortest input terminates (default false)
 * @param options.format - set output format (from 0 to 8) (default yuv420)
 * @param options.repeatlast - repeat overlay of the last overlay frame (default true)
 * @param options.alpha - alpha format (from 0 to 2) (default auto)
 * @see https://ffmpeg.org/ffmpeg-filters.html#overlay
 */
  overlay(
    _overlay: VideoStream,

    options?: {
    x?: FFString;
    y?: FFString;
    eof_action?: FFInt | "repeat" | "endall" | "pass";
    eval?: FFInt | "init" | "frame";
    shortest?: FFBoolean;
    format?: FFInt | "yuv420" | "yuv420p10" | "yuv422" | "yuv422p10" | "yuv444" | "yuv444p10" | "rgb" | "gbrp" | "auto";
    repeatlast?: FFBoolean;
    alpha?: FFInt | "auto" | "unknown" | "straight" | "premultiplied";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "overlay", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _overlay],
      merge(
    {
      "x": options?.x,
      "y": options?.y,
      "eof_action": options?.eof_action,
      "eval": options?.eval,
      "shortest": options?.shortest,
      "format": options?.format,
      "repeatlast": options?.repeatlast,
      "alpha": options?.alpha,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Denoise using wavelets.

 *
 * @param options.depth - set depth (from 8 to 16) (default 8)
 * @param options.luma_strength - set luma strength (from 0 to 1000) (default 1)
 * @param options.chroma_strength - set chroma strength (from 0 to 1000) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#owdenoise
 */
  owdenoise(
    options?: {
    depth?: FFInt;
    luma_strength?: FFDouble;
    chroma_strength?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "owdenoise", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "depth": options?.depth,
      "luma_strength": options?.luma_strength,
      "chroma_strength": options?.chroma_strength,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Pad the input video.

 *
 * @param options.width - set the pad area width expression (default "iw")
 * @param options.height - set the pad area height expression (default "ih")
 * @param options.x - set the x offset expression for the input image position (default "0")
 * @param options.y - set the y offset expression for the input image position (default "0")
 * @param options.color - set the color of the padded area border (default "black")
 * @param options.eval - specify when to evaluate expressions (from 0 to 1) (default init)
 * @param options.aspect - pad to fit an aspect instead of a resolution (from 0 to DBL_MAX) (default 0/1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#pad
 */
  pad(
    options?: {
    width?: FFString;
    height?: FFString;
    x?: FFString;
    y?: FFString;
    color?: FFColor;
    eval?: FFInt | "init" | "frame";
    aspect?: FFRational;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "pad", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "width": options?.width,
      "height": options?.height,
      "x": options?.x,
      "y": options?.y,
      "color": options?.color,
      "eval": options?.eval,
      "aspect": options?.aspect,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }










/**
 * Find the optimal palette for a given stream.

 *
 * @param options.max_colors - set the maximum number of colors to use in the palette (from 2 to 256) (default 256)
 * @param options.reserve_transparent - reserve a palette entry for transparency (default true)
 * @param options.transparency_color - set a background color for transparency (default "lime")
 * @param options.stats_mode - set statistics mode (from 0 to 2) (default full)
 * @see https://ffmpeg.org/ffmpeg-filters.html#palettegen
 */
  palettegen(
    options?: {
    max_colors?: FFInt;
    reserve_transparent?: FFBoolean;
    transparency_color?: FFColor;
    stats_mode?: FFInt | "full" | "diff" | "single";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "palettegen", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "max_colors": options?.max_colors,
      "reserve_transparent": options?.reserve_transparent,
      "transparency_color": options?.transparency_color,
      "stats_mode": options?.stats_mode,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Use a palette to downsample an input video stream.

 *
 * @param options.dither - select dithering mode (from 0 to 8) (default sierra2_4a)
 * @param options.bayer_scale - set scale for bayer dithering (from 0 to 5) (default 2)
 * @param options.diff_mode - set frame difference mode (from 0 to 1) (default 0)
 * @param options._new - take new palette for each output frame (default false)
 * @param options.alpha_threshold - set the alpha threshold for transparency (from 0 to 255) (default 128)
 * @param options.debug_kdtree - save Graphviz graph of the kdtree in specified file
 * @see https://ffmpeg.org/ffmpeg-filters.html#paletteuse
 */
  paletteuse(
    _palette: VideoStream,

    options?: {
    dither?: FFInt | "bayer" | "heckbert" | "floyd_steinberg" | "sierra2" | "sierra2_4a" | "sierra3" | "burkes" | "atkinson";
    bayer_scale?: FFInt;
    diff_mode?: FFInt | "rectangle";
    _new?: FFBoolean;
    alpha_threshold?: FFInt;
    debug_kdtree?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "paletteuse", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _palette],
      merge(
    {
      "dither": options?.dither,
      "bayer_scale": options?.bayer_scale,
      "diff_mode": options?.diff_mode,
      "new": options?._new,
      "alpha_threshold": options?.alpha_threshold,
      "debug_kdtree": options?.debug_kdtree,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }










/**
 * Set permissions for the output video frame.

 *
 * @param options.mode - select permissions mode (from 0 to 4) (default none)
 * @param options.seed - set the seed for the random mode (from -1 to UINT32_MAX) (default -1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#perms_002c-aperms
 */
  perms(
    options?: {
    mode?: FFInt | "none" | "ro" | "rw" | "toggle" | "random";
    seed?: FFInt64;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "perms", typingsInput: ["video"], typingsOutput: ["video"] },
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
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Correct the perspective of video.

 *
 * @param options.x0 - set top left x coordinate (default "0")
 * @param options.y0 - set top left y coordinate (default "0")
 * @param options.x1 - set top right x coordinate (default "W")
 * @param options.y1 - set top right y coordinate (default "0")
 * @param options.x2 - set bottom left x coordinate (default "0")
 * @param options.y2 - set bottom left y coordinate (default "H")
 * @param options.x3 - set bottom right x coordinate (default "W")
 * @param options.y3 - set bottom right y coordinate (default "H")
 * @param options.interpolation - set interpolation (from 0 to 1) (default linear)
 * @param options.sense - specify the sense of the coordinates (from 0 to 1) (default source)
 * @param options.eval - specify when to evaluate expressions (from 0 to 1) (default init)
 * @see https://ffmpeg.org/ffmpeg-filters.html#perspective
 */
  perspective(
    options?: {
    x0?: FFString;
    y0?: FFString;
    x1?: FFString;
    y1?: FFString;
    x2?: FFString;
    y2?: FFString;
    x3?: FFString;
    y3?: FFString;
    interpolation?: FFInt | "linear" | "cubic";
    sense?: FFInt | "source" | "destination";
    eval?: FFInt | "init" | "frame";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "perspective", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "x0": options?.x0,
      "y0": options?.y0,
      "x1": options?.x1,
      "y1": options?.y1,
      "x2": options?.x2,
      "y2": options?.y2,
      "x3": options?.x3,
      "y3": options?.y3,
      "interpolation": options?.interpolation,
      "sense": options?.sense,
      "eval": options?.eval,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Phase shift fields.

 *
 * @param options.mode - set phase mode (from 0 to 8) (default A)
 * @see https://ffmpeg.org/ffmpeg-filters.html#phase
 */
  phase(
    options?: {
    mode?: FFInt | "p" | "t" | "b" | "T" | "B" | "u" | "U" | "a" | "A";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "phase", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "mode": options?.mode,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Filter out photosensitive epilepsy seizure-inducing flashes.

 *
 * @param options.frames - set how many frames to use (from 2 to 240) (default 30)
 * @param options.threshold - set detection threshold factor (lower is stricter) (from 0.1 to FLT_MAX) (default 1)
 * @param options.skip - set pixels to skip when sampling frames (from 1 to 1024) (default 1)
 * @param options.bypass - leave frames unchanged (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#photosensitivity
 */
  photosensitivity(
    options?: {
    frames?: FFInt;
    threshold?: FFFloat;
    skip?: FFInt;
    bypass?: FFBoolean;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "photosensitivity", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "frames": options?.frames,
      "threshold": options?.threshold,
      "skip": options?.skip,
      "bypass": options?.bypass,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Test pixel format definitions.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#pixdesctest
 */
  pixdesctest(
    options?: {
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "pixdesctest", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Pixelize video.

 *
 * @param options.width - set block width (from 1 to 1024) (default 16)
 * @param options.height - set block height (from 1 to 1024) (default 16)
 * @param options.mode - set the pixelize mode (from 0 to 2) (default avg)
 * @param options.planes - set what planes to filter (default F)
 * @see https://ffmpeg.org/ffmpeg-filters.html#pixelize
 */
  pixelize(
    options?: {
    width?: FFInt;
    height?: FFInt;
    mode?: FFInt | "avg" | "min" | "max";
    planes?: FFFlags;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "pixelize", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "width": options?.width,
      "height": options?.height,
      "mode": options?.mode,
      "planes": options?.planes,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Pixel data analysis.

 *
 * @param options.x - set scope x offset (from 0 to 1) (default 0.5)
 * @param options.y - set scope y offset (from 0 to 1) (default 0.5)
 * @param options.w - set scope width (from 1 to 80) (default 7)
 * @param options.h - set scope height (from 1 to 80) (default 7)
 * @param options.o - set window opacity (from 0 to 1) (default 0.5)
 * @param options.wx - set window x offset (from -1 to 1) (default -1)
 * @param options.wy - set window y offset (from -1 to 1) (default -1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#pixscope
 */
  pixscope(
    options?: {
    x?: FFFloat;
    y?: FFFloat;
    w?: FFInt;
    h?: FFInt;
    o?: FFFloat;
    wx?: FFFloat;
    wy?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "pixscope", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "x": options?.x,
      "y": options?.y,
      "w": options?.w,
      "h": options?.h,
      "o": options?.o,
      "wx": options?.wx,
      "wy": options?.wy,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply Postprocessing 7 filter.

 *
 * @param options.qp - force a constant quantizer parameter (from 0 to 64) (default 0)
 * @param options.mode - set thresholding mode (from 0 to 2) (default medium)
 * @see https://ffmpeg.org/ffmpeg-filters.html#pp7
 */
  pp7(
    options?: {
    qp?: FFInt;
    mode?: FFInt | "hard" | "soft" | "medium";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "pp7", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "qp": options?.qp,
      "mode": options?.mode,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Premultiply or unpremultiply an image in-place, as needed.
 *
 * Note: New in FFmpeg 8.0.
 *
 * @param options.planes - set planes (from 0 to 15) (default 15)
 * @param options.inplace - enable inplace mode (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#premultiply_005fdynamic
 */
  premultiply_dynamic(
    options?: {
    planes?: FFInt;
    inplace?: FFBoolean;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "premultiply_dynamic", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "planes": options?.planes,
      "inplace": options?.inplace,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply prewitt operator.

 *
 * @param options.planes - set planes to filter (from 0 to 15) (default 15)
 * @param options.scale - set scale (from 0 to 65535) (default 1)
 * @param options.delta - set delta (from -65535 to 65535) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#prewitt
 */
  prewitt(
    options?: {
    planes?: FFInt;
    scale?: FFFloat;
    delta?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "prewitt", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "planes": options?.planes,
      "scale": options?.scale,
      "delta": options?.delta,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Make pseudocolored video frames.

 *
 * @param options.c0 - set component #0 expression (default "val")
 * @param options.c1 - set component #1 expression (default "val")
 * @param options.c2 - set component #2 expression (default "val")
 * @param options.c3 - set component #3 expression (default "val")
 * @param options.index - set component as base (from 0 to 3) (default 0)
 * @param options.preset - set preset (from -1 to 20) (default none)
 * @param options.opacity - set pseudocolor opacity (from 0 to 1) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#pseudocolor
 */
  pseudocolor(
    options?: {
    c0?: FFString;
    c1?: FFString;
    c2?: FFString;
    c3?: FFString;
    index?: FFInt;
    preset?: FFInt | "none" | "magma" | "inferno" | "plasma" | "viridis" | "turbo" | "cividis" | "range1" | "range2" | "shadows" | "highlights" | "solar" | "nominal" | "preferred" | "total" | "spectral" | "cool" | "heat" | "fiery" | "blues" | "green" | "helix";
    opacity?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "pseudocolor", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "c0": options?.c0,
      "c1": options?.c1,
      "c2": options?.c2,
      "c3": options?.c3,
      "index": options?.index,
      "preset": options?.preset,
      "opacity": options?.opacity,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Calculate the PSNR between two video streams.

 *
 * @param options.stats_file - Set file where to store per-frame difference information
 * @param options.stats_version - Set the format version for the stats file. (from 1 to 2) (default 1)
 * @param options.output_max - Add raw stats (max values) to the output log. (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#psnr
 */
  psnr(
    _reference: VideoStream,

    options?: {
    stats_file?: FFString;
    stats_version?: FFInt;
    output_max?: FFBoolean;
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "psnr", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _reference],
      merge(
    {
      "stats_file": options?.stats_file,
      "stats_version": options?.stats_version,
      "output_max": options?.output_max,
      "eof_action": options?.eofAction,
      "shortest": options?.shortest,
      "repeatlast": options?.repeatlast,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Pullup from field sequence to frames.

 *
 * @param options.jl - set left junk size (from 0 to INT_MAX) (default 1)
 * @param options.jr - set right junk size (from 0 to INT_MAX) (default 1)
 * @param options.jt - set top junk size (from 1 to INT_MAX) (default 4)
 * @param options.jb - set bottom junk size (from 1 to INT_MAX) (default 4)
 * @param options.sb - set strict breaks (default false)
 * @param options.mp - set metric plane (from 0 to 2) (default y)
 * @see https://ffmpeg.org/ffmpeg-filters.html#pullup
 */
  pullup(
    options?: {
    jl?: FFInt;
    jr?: FFInt;
    jt?: FFInt;
    jb?: FFInt;
    sb?: FFBoolean;
    mp?: FFInt | "y" | "u" | "v";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "pullup", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "jl": options?.jl,
      "jr": options?.jr,
      "jt": options?.jt,
      "jb": options?.jb,
      "sb": options?.sb,
      "mp": options?.mp,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Change video quantization parameters.

 *
 * @param options.qp - set qp expression
 * @see https://ffmpeg.org/ffmpeg-filters.html#qp
 */
  qp(
    options?: {
    qp?: FFString;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "qp", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "qp": options?.qp,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Return random frames.

 *
 * @param options.frames - set number of frames in cache (from 2 to 512) (default 30)
 * @param options.seed - set the seed (from -1 to UINT32_MAX) (default -1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#random
 */
  random(
    options?: {
    frames?: FFInt;
    seed?: FFInt64;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "random", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "frames": options?.frames,
      "seed": options?.seed,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Read EIA-608 Closed Caption codes from input video and write them to frame metadata.

 *
 * @param options.scan_min - set from which line to scan for codes (from 0 to INT_MAX) (default 0)
 * @param options.scan_max - set to which line to scan for codes (from 0 to INT_MAX) (default 29)
 * @param options.spw - set ratio of width reserved for sync code detection (from 0.1 to 0.7) (default 0.27)
 * @param options.chp - check and apply parity bit (default false)
 * @param options.lp - lowpass line prior to processing (default true)
 * @see https://ffmpeg.org/ffmpeg-filters.html#readeia608
 */
  readeia608(
    options?: {
    scan_min?: FFInt;
    scan_max?: FFInt;
    spw?: FFFloat;
    chp?: FFBoolean;
    lp?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "readeia608", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "scan_min": options?.scan_min,
      "scan_max": options?.scan_max,
      "spw": options?.spw,
      "chp": options?.chp,
      "lp": options?.lp,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Read vertical interval timecode and write it to frame metadata.

 *
 * @param options.scan_max - maximum line numbers to scan for VITC data (from -1 to INT_MAX) (default 45)
 * @param options.thr_b - black color threshold (from 0 to 1) (default 0.2)
 * @param options.thr_w - white color threshold (from 0 to 1) (default 0.6)
 * @see https://ffmpeg.org/ffmpeg-filters.html#readvitc
 */
  readvitc(
    options?: {
    scan_max?: FFInt;
    thr_b?: FFDouble;
    thr_w?: FFDouble;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "readvitc", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "scan_max": options?.scan_max,
      "thr_b": options?.thr_b,
      "thr_w": options?.thr_w,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Slow down filtering to match realtime.

 *
 * @param options.limit - sleep time limit (default 2)
 * @param options.speed - speed factor (from DBL_MIN to DBL_MAX) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#realtime_002c-arealtime
 */
  realtime(
    options?: {
    limit?: FFDuration;
    speed?: FFDouble;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "realtime", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "limit": options?.limit,
      "speed": options?.speed,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Remap pixels.

 *
 * @param options.format - set output format (from 0 to 1) (default color)
 * @param options.fill - set the color of the unmapped pixels (default "black")
 * @see https://ffmpeg.org/ffmpeg-filters.html#remap
 */
  remap(
    _xmap: VideoStream,
    _ymap: VideoStream,

    options?: {
    format?: FFInt | "color" | "gray";
    fill?: FFColor;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "remap", typingsInput: ["video", "video", "video"], typingsOutput: ["video"] },
      [this, _xmap, _ymap],
      merge(
    {
      "format": options?.format,
      "fill": options?.fill,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Remove grain.

 *
 * @param options.m0 - set mode for 1st plane (from 0 to 24) (default 0)
 * @param options.m1 - set mode for 2nd plane (from 0 to 24) (default 0)
 * @param options.m2 - set mode for 3rd plane (from 0 to 24) (default 0)
 * @param options.m3 - set mode for 4th plane (from 0 to 24) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#removegrain
 */
  removegrain(
    options?: {
    m0?: FFInt;
    m1?: FFInt;
    m2?: FFInt;
    m3?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "removegrain", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "m0": options?.m0,
      "m1": options?.m1,
      "m2": options?.m2,
      "m3": options?.m3,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Remove a TV logo based on a mask image.

 *
 * @param options.filename - set bitmap filename
 * @see https://ffmpeg.org/ffmpeg-filters.html#removelogo
 */
  removelogo(
    options?: {
    filename?: FFString;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "removelogo", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "filename": options?.filename,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Hard repeat fields based on MPEG repeat field flag.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#repeatfields
 */
  repeatfields(
    options?: {
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "repeatfields", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Reverse a clip.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#reverse
 */
  reverse(
    options?: {
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "reverse", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Shift RGBA.

 *
 * @param options.rh - shift red horizontally (from -255 to 255) (default 0)
 * @param options.rv - shift red vertically (from -255 to 255) (default 0)
 * @param options.gh - shift green horizontally (from -255 to 255) (default 0)
 * @param options.gv - shift green vertically (from -255 to 255) (default 0)
 * @param options.bh - shift blue horizontally (from -255 to 255) (default 0)
 * @param options.bv - shift blue vertically (from -255 to 255) (default 0)
 * @param options.ah - shift alpha horizontally (from -255 to 255) (default 0)
 * @param options.av - shift alpha vertically (from -255 to 255) (default 0)
 * @param options.edge - set edge operation (from 0 to 1) (default smear)
 * @see https://ffmpeg.org/ffmpeg-filters.html#rgbashift
 */
  rgbashift(
    options?: {
    rh?: FFInt;
    rv?: FFInt;
    gh?: FFInt;
    gv?: FFInt;
    bh?: FFInt;
    bv?: FFInt;
    ah?: FFInt;
    av?: FFInt;
    edge?: FFInt | "smear" | "wrap";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "rgbashift", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "rh": options?.rh,
      "rv": options?.rv,
      "gh": options?.gh,
      "gv": options?.gv,
      "bh": options?.bh,
      "bv": options?.bv,
      "ah": options?.ah,
      "av": options?.av,
      "edge": options?.edge,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Apply roberts cross operator.

 *
 * @param options.planes - set planes to filter (from 0 to 15) (default 15)
 * @param options.scale - set scale (from 0 to 65535) (default 1)
 * @param options.delta - set delta (from -65535 to 65535) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#roberts
 */
  roberts(
    options?: {
    planes?: FFInt;
    scale?: FFFloat;
    delta?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "roberts", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "planes": options?.planes,
      "scale": options?.scale,
      "delta": options?.delta,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Rotate the input image.

 *
 * @param options.angle - set angle (in radians) (default "0")
 * @param options.out_w - set output width expression (default "iw")
 * @param options.out_h - set output height expression (default "ih")
 * @param options.fillcolor - set background fill color (default "black")
 * @param options.bilinear - use bilinear interpolation (default true)
 * @see https://ffmpeg.org/ffmpeg-filters.html#rotate
 */
  rotate(
    options?: {
    angle?: FFString;
    out_w?: FFString;
    out_h?: FFString;
    fillcolor?: FFString;
    bilinear?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "rotate", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "angle": options?.angle,
      "out_w": options?.out_w,
      "out_h": options?.out_h,
      "fillcolor": options?.fillcolor,
      "bilinear": options?.bilinear,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply shape adaptive blur.

 *
 * @param options.luma_radius - set luma radius (from 0.1 to 4) (default 1)
 * @param options.luma_pre_filter_radius - set luma pre-filter radius (from 0.1 to 2) (default 1)
 * @param options.luma_strength - set luma strength (from 0.1 to 100) (default 1)
 * @param options.chroma_radius - set chroma radius (from -0.9 to 4) (default -0.9)
 * @param options.chroma_pre_filter_radius - set chroma pre-filter radius (from -0.9 to 2) (default -0.9)
 * @param options.chroma_strength - set chroma strength (from -0.9 to 100) (default -0.9)
 * @see https://ffmpeg.org/ffmpeg-filters.html#sab
 */
  sab(
    options?: {
    luma_radius?: FFFloat;
    luma_pre_filter_radius?: FFFloat;
    luma_strength?: FFFloat;
    chroma_radius?: FFFloat;
    chroma_pre_filter_radius?: FFFloat;
    chroma_strength?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "sab", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "luma_radius": options?.luma_radius,
      "luma_pre_filter_radius": options?.luma_pre_filter_radius,
      "luma_strength": options?.luma_strength,
      "chroma_radius": options?.chroma_radius,
      "chroma_pre_filter_radius": options?.chroma_pre_filter_radius,
      "chroma_strength": options?.chroma_strength,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Scale the input video size and/or convert the image format.

 *
 * @param options.w - Output video width
 * @param options.h - Output video height
 * @param options.flags - Flags to pass to libswscale (default "")
 * @param options.interl - set interlacing (default false)
 * @param options.size - set video size
 * @param options.in_color_matrix - set input YCbCr type (from -1 to 17) (default auto)
 * @param options.out_color_matrix - set output YCbCr type (from 0 to 17) (default 2)
 * @param options.in_range - set input color range (from 0 to 2) (default auto)
 * @param options.out_range - set output color range (from 0 to 2) (default auto)
 * @param options.in_chroma_loc - set input chroma sample location (from 0 to 6) (default auto)
 * @param options.out_chroma_loc - set output chroma sample location (from 0 to 6) (default auto)
 * @param options.in_primaries - set input primaries (from -1 to 22) (default auto)
 * @param options.out_primaries - set output primaries (from -1 to 22) (default auto)
 * @param options.in_transfer - set output color transfer (from -1 to 18) (default auto)
 * @param options.in_v_chr_pos - input vertical chroma position in luma grid/256 (from -513 to 512) (default -513)
 * @param options.in_h_chr_pos - input horizontal chroma position in luma grid/256 (from -513 to 512) (default -513)
 * @param options.out_v_chr_pos - output vertical chroma position in luma grid/256 (from -513 to 512) (default -513)
 * @param options.out_h_chr_pos - output horizontal chroma position in luma grid/256 (from -513 to 512) (default -513)
 * @param options.force_original_aspect_ratio - decrease or increase w/h if necessary to keep the original AR (from 0 to 2) (default disable)
 * @param options.force_divisible_by - enforce that the output resolution is divisible by a defined integer when force_original_aspect_ratio is used (from 1 to 256) (default 1)
 * @param options.reset_sar - reset SAR to 1 and scale to square pixels if scaling proportionally (default false)
 * @param options.param0 - Scaler param 0 (from -DBL_MAX to DBL_MAX) (default DBL_MAX)
 * @param options.param1 - Scaler param 1 (from -DBL_MAX to DBL_MAX) (default DBL_MAX)
 * @param options.eval - specify when to evaluate expressions (from 0 to 1) (default init)
 * @see https://ffmpeg.org/ffmpeg-filters.html#scale
 */
  scale(
    options?: {
    w?: FFString;
    h?: FFString;
    flags?: FFString;
    interl?: FFBoolean;
    size?: FFString;
    in_color_matrix?: FFInt | "auto" | "bt601" | "bt470" | "smpte170m" | "bt470bg" | "bt709" | "fcc" | "smpte240m" | "bt2020" | "bt2020nc";
    out_color_matrix?: FFInt | "auto" | "bt601" | "bt470" | "smpte170m" | "bt470bg" | "bt709" | "fcc" | "smpte240m" | "bt2020" | "bt2020nc";
    in_range?: FFInt | "auto" | "unknown" | "full" | "limited" | "jpeg" | "mpeg" | "tv" | "pc";
    out_range?: FFInt | "auto" | "unknown" | "full" | "limited" | "jpeg" | "mpeg" | "tv" | "pc";
    in_chroma_loc?: FFInt | "auto" | "unknown" | "left" | "center" | "topleft" | "top" | "bottomleft" | "bottom";
    out_chroma_loc?: FFInt | "auto" | "unknown" | "left" | "center" | "topleft" | "top" | "bottomleft" | "bottom";
    in_primaries?: FFInt | "auto" | "bt709" | "bt470m" | "bt470bg" | "smpte170m" | "smpte240m" | "film" | "bt2020" | "smpte428" | "smpte431" | "smpte432" | "jedec-p22" | "ebu3213";
    out_primaries?: FFInt | "auto" | "bt709" | "bt470m" | "bt470bg" | "smpte170m" | "smpte240m" | "film" | "bt2020" | "smpte428" | "smpte431" | "smpte432" | "jedec-p22" | "ebu3213";
    in_transfer?: FFInt | "auto" | "bt709" | "bt470m" | "gamma22" | "bt470bg" | "gamma28" | "smpte170m" | "smpte240m" | "linear" | "iec61966-2-1" | "srgb" | "iec61966-2-4" | "xvycc" | "bt1361e" | "bt2020-10" | "bt2020-12" | "smpte2084" | "smpte428" | "arib-std-b67";
    in_v_chr_pos?: FFInt;
    in_h_chr_pos?: FFInt;
    out_v_chr_pos?: FFInt;
    out_h_chr_pos?: FFInt;
    force_original_aspect_ratio?: FFInt | "disable" | "decrease" | "increase";
    force_divisible_by?: FFInt;
    reset_sar?: FFBoolean;
    param0?: FFDouble;
    param1?: FFDouble;
    eval?: FFInt | "init" | "frame";
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "scale", typingsInput: [], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "w": options?.w,
      "h": options?.h,
      "flags": options?.flags,
      "interl": options?.interl,
      "size": options?.size,
      "in_color_matrix": options?.in_color_matrix,
      "out_color_matrix": options?.out_color_matrix,
      "in_range": options?.in_range,
      "out_range": options?.out_range,
      "in_chroma_loc": options?.in_chroma_loc,
      "out_chroma_loc": options?.out_chroma_loc,
      "in_primaries": options?.in_primaries,
      "out_primaries": options?.out_primaries,
      "in_transfer": options?.in_transfer,
      "in_v_chr_pos": options?.in_v_chr_pos,
      "in_h_chr_pos": options?.in_h_chr_pos,
      "out_v_chr_pos": options?.out_v_chr_pos,
      "out_h_chr_pos": options?.out_h_chr_pos,
      "force_original_aspect_ratio": options?.force_original_aspect_ratio,
      "force_divisible_by": options?.force_divisible_by,
      "reset_sar": options?.reset_sar,
      "param0": options?.param0,
      "param1": options?.param1,
      "eval": options?.eval,
      "eof_action": options?.eofAction,
      "shortest": options?.shortest,
      "repeatlast": options?.repeatlast,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Scale Videotoolbox frames
 *
 * Note: New in FFmpeg 8.0.
 *
 * @param options.w - Output video width (default "iw")
 * @param options.h - Output video height (default "ih")
 * @param options.color_matrix - Output colour matrix coefficient set
 * @param options.color_primaries - Output colour primaries
 * @param options.color_transfer - Output colour transfer characteristics
 * @see https://ffmpeg.org/ffmpeg-filters.html#scale_005fvt
 */
  scale_vt(
    options?: {
    w?: FFString;
    h?: FFString;
    color_matrix?: FFString;
    color_primaries?: FFString;
    color_transfer?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "scale_vt", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "w": options?.w,
      "h": options?.h,
      "color_matrix": options?.color_matrix,
      "color_primaries": options?.color_primaries,
      "color_transfer": options?.color_transfer,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Detect video scene change

 *
 * @param options.threshold - set scene change detect threshold (from 0 to 100) (default 10)
 * @param options.sc_pass - Set the flag to pass scene change frames (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#scdet
 */
  scdet(
    options?: {
    threshold?: FFDouble;
    sc_pass?: FFBoolean;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "scdet", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "threshold": options?.threshold,
      "sc_pass": options?.sc_pass,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply scharr operator.

 *
 * @param options.planes - set planes to filter (from 0 to 15) (default 15)
 * @param options.scale - set scale (from 0 to 65535) (default 1)
 * @param options.delta - set delta (from -65535 to 65535) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#scharr
 */
  scharr(
    options?: {
    planes?: FFInt;
    scale?: FFFloat;
    delta?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "scharr", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "planes": options?.planes,
      "scale": options?.scale,
      "delta": options?.delta,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Scroll input video.

 *
 * @param options.horizontal - set the horizontal scrolling speed (from -1 to 1) (default 0)
 * @param options.vertical - set the vertical scrolling speed (from -1 to 1) (default 0)
 * @param options.hpos - set initial horizontal position (from 0 to 1) (default 0)
 * @param options.vpos - set initial vertical position (from 0 to 1) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#scroll
 */
  scroll(
    options?: {
    horizontal?: FFFloat;
    vertical?: FFFloat;
    hpos?: FFFloat;
    vpos?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "scroll", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "horizontal": options?.horizontal,
      "vertical": options?.vertical,
      "hpos": options?.hpos,
      "vpos": options?.vpos,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Segment video stream.

 *
 * @param options.timestamps - timestamps of input at which to split input
 * @param options.frames - frames at which to split input
 * @see https://ffmpeg.org/ffmpeg-filters.html#segment_002c-asegment
 */
  segment(
    options?: {
    timestamps?: FFString;
    frames?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): FilterNode {
    const filterNode = filterNodeFactory(
      { name: "segment", typingsInput: ["video"], typingsOutput: [] },
      [this],
      merge(
    {
      "timestamps": options?.timestamps,
      "frames": options?.frames,
},
    options?.extraOptions,
  ),
    );
return filterNode;
  }






/**
 * Select video frames to pass in output.

 *
 * @param options.expr - set an expression to use for selecting frames (default "1")
 * @param options.outputs - set the number of outputs (from 1 to INT_MAX) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#select_002c-aselect
 */
  select(
    options?: {
    expr?: FFString;
    outputs?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): FilterNode {
    const filterNode = filterNodeFactory(
      { name: "select", typingsInput: ["video"], typingsOutput: [] },
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
 * Apply CMYK adjustments to specific color ranges.

 *
 * @param options.correction_method - select correction method (from 0 to 1) (default absolute)
 * @param options.reds - adjust red regions
 * @param options.yellows - adjust yellow regions
 * @param options.greens - adjust green regions
 * @param options.cyans - adjust cyan regions
 * @param options.blues - adjust blue regions
 * @param options.magentas - adjust magenta regions
 * @param options.whites - adjust white regions
 * @param options.neutrals - adjust neutral regions
 * @param options.blacks - adjust black regions
 * @param options.psfile - set Photoshop selectivecolor file name
 * @see https://ffmpeg.org/ffmpeg-filters.html#selectivecolor
 */
  selectivecolor(
    options?: {
    correction_method?: FFInt | "absolute" | "relative";
    reds?: FFString;
    yellows?: FFString;
    greens?: FFString;
    cyans?: FFString;
    blues?: FFString;
    magentas?: FFString;
    whites?: FFString;
    neutrals?: FFString;
    blacks?: FFString;
    psfile?: FFString;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "selectivecolor", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "correction_method": options?.correction_method,
      "reds": options?.reds,
      "yellows": options?.yellows,
      "greens": options?.greens,
      "cyans": options?.cyans,
      "blues": options?.blues,
      "magentas": options?.magentas,
      "whites": options?.whites,
      "neutrals": options?.neutrals,
      "blacks": options?.blacks,
      "psfile": options?.psfile,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Send commands to filters.

 *
 * @param options.commands - set commands
 * @param options.filename - set commands file
 * @see https://ffmpeg.org/ffmpeg-filters.html#sendcmd_002c-asendcmd
 */
  sendcmd(
    options?: {
    commands?: FFString;
    filename?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "sendcmd", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "commands": options?.commands,
      "filename": options?.filename,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Split input video frames into fields.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#separatefields
 */
  separatefields(
    options?: {
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "separatefields", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Set the frame display aspect ratio.

 *
 * @param options.dar - set display aspect ratio (default "0")
 * @param options.max - set max value for nominator or denominator in the ratio (from 1 to INT_MAX) (default 100)
 * @see https://ffmpeg.org/ffmpeg-filters.html#setdar_002c-setsar
 */
  setdar(
    options?: {
    dar?: FFString;
    max?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "setdar", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "dar": options?.dar,
      "max": options?.max,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Force field for the output video frame.

 *
 * @param options.mode - select interlace mode (from -1 to 2) (default auto)
 * @see https://ffmpeg.org/ffmpeg-filters.html#setfield
 */
  setfield(
    options?: {
    mode?: FFInt | "auto" | "bff" | "tff" | "prog";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "setfield", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "mode": options?.mode,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Force field, or color property for the output video frame.

 *
 * @param options.field_mode - select interlace mode (from -1 to 2) (default auto)
 * @param options.range - select color range (from -1 to 2) (default auto)
 * @param options.color_primaries - select color primaries (from -1 to 256) (default auto)
 * @param options.color_trc - select color transfer (from -1 to 256) (default auto)
 * @param options.colorspace - select colorspace (from -1 to 17) (default auto)
 * @param options.chroma_location - select chroma sample location (from -1 to 6) (default auto)
 * @param options.alpha_mode - select alpha moda (from -1 to 2) (default auto)
 * @see https://ffmpeg.org/ffmpeg-filters.html#setparams
 */
  setparams(
    options?: {
    field_mode?: FFInt | "auto" | "bff" | "tff" | "prog";
    range?: FFInt | "auto" | "unspecified" | "unknown" | "limited" | "tv" | "mpeg" | "full" | "pc" | "jpeg";
    color_primaries?: FFInt | "auto" | "bt709" | "unknown" | "bt470m" | "bt470bg" | "smpte170m" | "smpte240m" | "film" | "bt2020" | "smpte428" | "smpte431" | "smpte432" | "jedec-p22" | "ebu3213" | "vgamut";
    color_trc?: FFInt | "auto" | "bt709" | "unknown" | "bt470m" | "bt470bg" | "smpte170m" | "smpte240m" | "linear" | "log100" | "log316" | "iec61966-2-4" | "bt1361e" | "iec61966-2-1" | "bt2020-10" | "bt2020-12" | "smpte2084" | "smpte428" | "arib-std-b67" | "vlog";
    colorspace?: FFInt | "auto" | "gbr" | "bt709" | "unknown" | "fcc" | "bt470bg" | "smpte170m" | "smpte240m" | "ycgco" | "ycgco-re" | "ycgco-ro" | "bt2020nc" | "bt2020c" | "smpte2085" | "chroma-derived-nc" | "chroma-derived-c" | "ictcp" | "ipt-c2";
    chroma_location?: FFInt | "auto" | "unspecified" | "unknown" | "left" | "center" | "topleft" | "top" | "bottomleft" | "bottom";
    alpha_mode?: FFInt | "auto" | "unspecified" | "unknown" | "premultiplied" | "straight";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "setparams", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "field_mode": options?.field_mode,
      "range": options?.range,
      "color_primaries": options?.color_primaries,
      "color_trc": options?.color_trc,
      "colorspace": options?.colorspace,
      "chroma_location": options?.chroma_location,
      "alpha_mode": options?.alpha_mode,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Set PTS for the output video frame.

 *
 * @param options.expr - Expression determining the frame timestamp (default "PTS")
 * @param options.strip_fps - Unset framerate metadata (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#setpts_002c-asetpts
 */
  setpts(
    options?: {
    expr?: FFString;
    strip_fps?: FFBoolean;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "setpts", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "expr": options?.expr,
      "strip_fps": options?.strip_fps,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Force color range for the output video frame.

 *
 * @param options.range - select color range (from -1 to 2) (default auto)
 * @see https://ffmpeg.org/ffmpeg-filters.html#setrange
 */
  setrange(
    options?: {
    range?: FFInt | "auto" | "unspecified" | "unknown" | "limited" | "tv" | "mpeg" | "full" | "pc" | "jpeg";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "setrange", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "range": options?.range,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Set the pixel sample aspect ratio.

 *
 * @param options.sar - set sample (pixel) aspect ratio (default "0")
 * @param options.max - set max value for nominator or denominator in the ratio (from 1 to INT_MAX) (default 100)
 * @see https://ffmpeg.org/ffmpeg-filters.html#setdar_002c-setsar
 */
  setsar(
    options?: {
    sar?: FFString;
    max?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "setsar", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "sar": options?.sar,
      "max": options?.max,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Set timebase for the video output link.

 *
 * @param options.expr - set expression determining the output timebase (default "intb")
 * @see https://ffmpeg.org/ffmpeg-filters.html#settb_002c-asettb
 */
  settb(
    options?: {
    expr?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "settb", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "expr": options?.expr,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Shear transform the input image.

 *
 * @param options.shx - set x shear factor (from -2 to 2) (default 0)
 * @param options.shy - set y shear factor (from -2 to 2) (default 0)
 * @param options.fillcolor - set background fill color (default "black")
 * @param options.interp - set interpolation (from 0 to 1) (default bilinear)
 * @see https://ffmpeg.org/ffmpeg-filters.html#shear
 */
  shear(
    options?: {
    shx?: FFFloat;
    shy?: FFFloat;
    fillcolor?: FFString;
    interp?: FFInt | "nearest" | "bilinear";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "shear", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "shx": options?.shx,
      "shy": options?.shy,
      "fillcolor": options?.fillcolor,
      "interp": options?.interp,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }












/**
 * Show textual information for each video frame.

 *
 * @param options.checksum - calculate checksums (default true)
 * @param options.udu_sei_as_ascii - try to print user data unregistered SEI as ascii character when possible (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#showinfo
 */
  showinfo(
    options?: {
    checksum?: FFBoolean;
    udu_sei_as_ascii?: FFBoolean;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "showinfo", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "checksum": options?.checksum,
      "udu_sei_as_ascii": options?.udu_sei_as_ascii,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Display frame palette.

 *
 * @param options.s - set pixel box size (from 1 to 100) (default 30)
 * @see https://ffmpeg.org/ffmpeg-filters.html#showpalette
 */
  showpalette(
    options?: {
    s?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "showpalette", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "s": options?.s,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }


















/**
 * Shuffle video frames.

 *
 * @param options.mapping - set destination indexes of input frames (default "0")
 * @see https://ffmpeg.org/ffmpeg-filters.html#shuffleframes
 */
  shuffleframes(
    options?: {
    mapping?: FFString;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "shuffleframes", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "mapping": options?.mapping,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Shuffle video pixels.

 *
 * @param options.direction - set shuffle direction (from 0 to 1) (default forward)
 * @param options.mode - set shuffle mode (from 0 to 2) (default horizontal)
 * @param options.width - set block width (from 1 to 8000) (default 10)
 * @param options.height - set block height (from 1 to 8000) (default 10)
 * @param options.seed - set random seed (from -1 to UINT32_MAX) (default -1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#shufflepixels
 */
  shufflepixels(
    options?: {
    direction?: FFInt | "forward" | "inverse";
    mode?: FFInt | "horizontal" | "vertical" | "block";
    width?: FFInt;
    height?: FFInt;
    seed?: FFInt64;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "shufflepixels", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "direction": options?.direction,
      "mode": options?.mode,
      "width": options?.width,
      "height": options?.height,
      "seed": options?.seed,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Shuffle video planes.

 *
 * @param options.map0 - Index of the input plane to be used as the first output plane (from 0 to 3) (default 0)
 * @param options.map1 - Index of the input plane to be used as the second output plane (from 0 to 3) (default 1)
 * @param options.map2 - Index of the input plane to be used as the third output plane (from 0 to 3) (default 2)
 * @param options.map3 - Index of the input plane to be used as the fourth output plane (from 0 to 3) (default 3)
 * @see https://ffmpeg.org/ffmpeg-filters.html#shuffleplanes
 */
  shuffleplanes(
    options?: {
    map0?: FFInt;
    map1?: FFInt;
    map2?: FFInt;
    map3?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "shuffleplanes", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "map0": options?.map0,
      "map1": options?.map1,
      "map2": options?.map2,
      "map3": options?.map3,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }










/**
 * Manipulate video frame side data.

 *
 * @param options.mode - set a mode of operation (from 0 to 1) (default select)
 * @param options._type - set side data type (from -1 to INT_MAX) (default -1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#sidedata_002c-asidedata
 */
  sidedata(
    options?: {
    mode?: FFInt | "select" | "delete";
    _type?: FFInt | "PANSCAN" | "A53_CC" | "STEREO3D" | "MATRIXENCODING" | "DOWNMIX_INFO" | "REPLAYGAIN" | "DISPLAYMATRIX" | "AFD" | "MOTION_VECTORS" | "SKIP_SAMPLES" | "AUDIO_SERVICE_TYPE" | "MASTERING_DISPLAY_METADATA" | "GOP_TIMECODE" | "SPHERICAL" | "CONTENT_LIGHT_LEVEL" | "ICC_PROFILE" | "S12M_TIMECOD" | "S12M_TIMECODE" | "DYNAMIC_HDR_PLUS" | "REGIONS_OF_INTEREST" | "VIDEO_ENC_PARAMS" | "SEI_UNREGISTERED" | "FILM_GRAIN_PARAMS" | "DETECTION_BOUNDING_BOXES" | "DETECTION_BBOXES" | "DOVI_RPU_BUFFER" | "DOVI_METADATA" | "DYNAMIC_HDR_VIVID" | "AMBIENT_VIEWING_ENVIRONMENT" | "VIDEO_HINT";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "sidedata", typingsInput: ["video"], typingsOutput: ["video"] },
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
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Generate statistics from video analysis.

 *
 * @param options.stat - set statistics filters (default 0)
 * @param options.out - set video filter (from -1 to 2) (default -1)
 * @param options.c - set highlight color (default "yellow")
 * @see https://ffmpeg.org/ffmpeg-filters.html#signalstats
 */
  signalstats(
    options?: {
    stat?: FFFlags | "tout" | "vrep" | "brng";
    out?: FFInt | "tout" | "vrep" | "brng";
    c?: FFColor;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "signalstats", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "stat": options?.stat,
      "out": options?.out,
      "c": options?.c,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }
















/**
 * Calculate spatial information (SI) and temporal information (TI).

 *
 * @param options.print_summary - Print summary showing average values (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#siti
 */
  siti(
    options?: {
    print_summary?: FFBoolean;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "siti", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "print_summary": options?.print_summary,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Blur the input video without impacting the outlines.

 *
 * @param options.luma_radius - set luma radius (from 0.1 to 5) (default 1)
 * @param options.luma_strength - set luma strength (from -1 to 1) (default 1)
 * @param options.luma_threshold - set luma threshold (from -30 to 30) (default 0)
 * @param options.chroma_radius - set chroma radius (from -0.9 to 5) (default -0.9)
 * @param options.chroma_strength - set chroma strength (from -2 to 1) (default -2)
 * @param options.chroma_threshold - set chroma threshold (from -31 to 30) (default -31)
 * @param options.alpha_radius - set alpha radius (from -0.9 to 5) (default -0.9)
 * @param options.alpha_strength - set alpha strength (from -2 to 1) (default -2)
 * @param options.alpha_threshold - set alpha threshold (from -31 to 30) (default -31)
 * @see https://ffmpeg.org/ffmpeg-filters.html#smartblur
 */
  smartblur(
    options?: {
    luma_radius?: FFFloat;
    luma_strength?: FFFloat;
    luma_threshold?: FFInt;
    chroma_radius?: FFFloat;
    chroma_strength?: FFFloat;
    chroma_threshold?: FFInt;
    alpha_radius?: FFFloat;
    alpha_strength?: FFFloat;
    alpha_threshold?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "smartblur", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "luma_radius": options?.luma_radius,
      "luma_strength": options?.luma_strength,
      "luma_threshold": options?.luma_threshold,
      "chroma_radius": options?.chroma_radius,
      "chroma_strength": options?.chroma_strength,
      "chroma_threshold": options?.chroma_threshold,
      "alpha_radius": options?.alpha_radius,
      "alpha_strength": options?.alpha_strength,
      "alpha_threshold": options?.alpha_threshold,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }










/**
 * Apply sobel operator.

 *
 * @param options.planes - set planes to filter (from 0 to 15) (default 15)
 * @param options.scale - set scale (from 0 to 65535) (default 1)
 * @param options.delta - set delta (from -65535 to 65535) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#sobel
 */
  sobel(
    options?: {
    planes?: FFInt;
    scale?: FFFloat;
    delta?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "sobel", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "planes": options?.planes,
      "scale": options?.scale,
      "delta": options?.delta,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Convert input spectrum videos to audio output.

 *
 * @param options.sample_rate - set sample rate (from 15 to INT_MAX) (default 44100)
 * @param options.channels - set channels (from 1 to 8) (default 1)
 * @param options.scale - set input amplitude scale (from 0 to 1) (default log)
 * @param options.slide - set input sliding mode (from 0 to 3) (default fullframe)
 * @param options.win_func - set window function (from 0 to 20) (default rect)
 * @param options.overlap - set window overlap (from 0 to 1) (default 1)
 * @param options.orientation - set orientation (from 0 to 1) (default vertical)
 * @see https://ffmpeg.org/ffmpeg-filters.html#spectrumsynth
 */
  spectrumsynth(
    _phase: VideoStream,

    options?: {
    sample_rate?: FFInt;
    channels?: FFInt;
    scale?: FFInt | "lin" | "log";
    slide?: FFInt | "replace" | "scroll" | "fullframe" | "rscroll";
    win_func?: FFInt | "rect" | "bartlett" | "hann" | "hanning" | "hamming" | "blackman" | "welch" | "flattop" | "bharris" | "bnuttall" | "bhann" | "sine" | "nuttall" | "lanczos" | "gauss" | "tukey" | "dolph" | "cauchy" | "parzen" | "poisson" | "bohman" | "kaiser";
    overlap?: FFFloat;
    orientation?: FFInt | "vertical" | "horizontal";
extraOptions?: Record<string, unknown>;
    },
  ): AudioStream {
    const filterNode = filterNodeFactory(
      { name: "spectrumsynth", typingsInput: ["video", "video"], typingsOutput: ["audio"] },
      [this, _phase],
      merge(
    {
      "sample_rate": options?.sample_rate,
      "channels": options?.channels,
      "scale": options?.scale,
      "slide": options?.slide,
      "win_func": options?.win_func,
      "overlap": options?.overlap,
      "orientation": options?.orientation,
},
    options?.extraOptions,
  ),
    );
return filterNode.audio(0) as unknown as AudioStream;
  }








/**
 * Pass on the input to N video outputs.

 *
 * @param options.outputs - set number of outputs (from 1 to INT_MAX) (default 2)
 * @see https://ffmpeg.org/ffmpeg-filters.html#split_002c-asplit
 */
  split(
    options?: {
    outputs?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): FilterNode {
    const filterNode = filterNodeFactory(
      { name: "split", typingsInput: ["video"], typingsOutput: [] },
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
 * Apply a simple post processing filter.

 *
 * @param options.quality - set quality (from 0 to 6) (default 3)
 * @param options.qp - force a constant quantizer parameter (from 0 to 63) (default 0)
 * @param options.mode - set thresholding mode (from 0 to 1) (default hard)
 * @param options.use_bframe_qp - use B-frames' QP (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#spp
 */
  spp(
    options?: {
    quality?: FFInt;
    qp?: FFInt;
    mode?: FFInt | "hard" | "soft";
    use_bframe_qp?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "spp", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "quality": options?.quality,
      "qp": options?.qp,
      "mode": options?.mode,
      "use_bframe_qp": options?.use_bframe_qp,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Calculate the SSIM between two video streams.

 *
 * @param options.stats_file - Set file where to store per-frame difference information
 * @see https://ffmpeg.org/ffmpeg-filters.html#ssim
 */
  ssim(
    _reference: VideoStream,

    options?: {
    stats_file?: FFString;
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "ssim", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _reference],
      merge(
    {
      "stats_file": options?.stats_file,
      "eof_action": options?.eofAction,
      "shortest": options?.shortest,
      "repeatlast": options?.repeatlast,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Convert video stereoscopic 3D view.

 *
 * @param options._in - set input format (from 16 to 32) (default sbsl)
 * @param options.out - set output format (from 0 to 32) (default arcd)
 * @see https://ffmpeg.org/ffmpeg-filters.html#stereo3d
 */
  stereo3d(
    options?: {
    _in?: FFInt | "ab2l" | "tb2l" | "ab2r" | "tb2r" | "abl" | "tbl" | "abr" | "tbr" | "al" | "ar" | "sbs2l" | "sbs2r" | "sbsl" | "sbsr" | "irl" | "irr" | "icl" | "icr";
    out?: FFInt | "ab2l" | "tb2l" | "ab2r" | "tb2r" | "abl" | "tbl" | "abr" | "tbr" | "agmc" | "agmd" | "agmg" | "agmh" | "al" | "ar" | "arbg" | "arcc" | "arcd" | "arcg" | "arch" | "argg" | "aybc" | "aybd" | "aybg" | "aybh" | "irl" | "irr" | "ml" | "mr" | "sbs2l" | "sbs2r" | "sbsl" | "sbsr" | "chl" | "chr" | "icl" | "icr" | "hdmi";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "stereo3d", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "in": options?._in,
      "out": options?.out,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }












/**
 * Scale the input by 2x using the Super2xSaI pixel art algorithm.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#super2xsai
 */
  super2xsai(
    options?: {
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "super2xsai", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }










/**
 * Swap 2 rectangular objects in video.

 *
 * @param options.w - set rect width (default "w/2")
 * @param options.h - set rect height (default "h/2")
 * @param options.x1 - set 1st rect x top left coordinate (default "w/2")
 * @param options.y1 - set 1st rect y top left coordinate (default "h/2")
 * @param options.x2 - set 2nd rect x top left coordinate (default "0")
 * @param options.y2 - set 2nd rect y top left coordinate (default "0")
 * @see https://ffmpeg.org/ffmpeg-filters.html#swaprect
 */
  swaprect(
    options?: {
    w?: FFString;
    h?: FFString;
    x1?: FFString;
    y1?: FFString;
    x2?: FFString;
    y2?: FFString;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "swaprect", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "w": options?.w,
      "h": options?.h,
      "x1": options?.x1,
      "y1": options?.y1,
      "x2": options?.x2,
      "y2": options?.y2,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Swap U and V components.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#swapuv
 */
  swapuv(
    options?: {
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "swapuv", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Blend successive frames.

 *
 * @param options.c0_mode - set component #0 blend mode (from 0 to 39) (default normal)
 * @param options.c1_mode - set component #1 blend mode (from 0 to 39) (default normal)
 * @param options.c2_mode - set component #2 blend mode (from 0 to 39) (default normal)
 * @param options.c3_mode - set component #3 blend mode (from 0 to 39) (default normal)
 * @param options.all_mode - set blend mode for all components (from -1 to 39) (default -1)
 * @param options.c0_expr - set color component #0 expression
 * @param options.c1_expr - set color component #1 expression
 * @param options.c2_expr - set color component #2 expression
 * @param options.c3_expr - set color component #3 expression
 * @param options.all_expr - set expression for all color components
 * @param options.c0_opacity - set color component #0 opacity (from 0 to 1) (default 1)
 * @param options.c1_opacity - set color component #1 opacity (from 0 to 1) (default 1)
 * @param options.c2_opacity - set color component #2 opacity (from 0 to 1) (default 1)
 * @param options.c3_opacity - set color component #3 opacity (from 0 to 1) (default 1)
 * @param options.all_opacity - set opacity for all color components (from 0 to 1) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#tblend
 */
  tblend(
    options?: {
    c0_mode?: FFInt | "addition" | "addition128" | "grainmerge" | "and" | "average" | "burn" | "darken" | "difference" | "difference128" | "grainextract" | "divide" | "dodge" | "exclusion" | "extremity" | "freeze" | "glow" | "hardlight" | "hardmix" | "heat" | "lighten" | "linearlight" | "multiply" | "multiply128" | "negation" | "normal" | "or" | "overlay" | "phoenix" | "pinlight" | "reflect" | "screen" | "softlight" | "subtract" | "vividlight" | "xor" | "softdifference" | "geometric" | "harmonic" | "bleach" | "stain" | "interpolate" | "hardoverlay";
    c1_mode?: FFInt | "addition" | "addition128" | "grainmerge" | "and" | "average" | "burn" | "darken" | "difference" | "difference128" | "grainextract" | "divide" | "dodge" | "exclusion" | "extremity" | "freeze" | "glow" | "hardlight" | "hardmix" | "heat" | "lighten" | "linearlight" | "multiply" | "multiply128" | "negation" | "normal" | "or" | "overlay" | "phoenix" | "pinlight" | "reflect" | "screen" | "softlight" | "subtract" | "vividlight" | "xor" | "softdifference" | "geometric" | "harmonic" | "bleach" | "stain" | "interpolate" | "hardoverlay";
    c2_mode?: FFInt | "addition" | "addition128" | "grainmerge" | "and" | "average" | "burn" | "darken" | "difference" | "difference128" | "grainextract" | "divide" | "dodge" | "exclusion" | "extremity" | "freeze" | "glow" | "hardlight" | "hardmix" | "heat" | "lighten" | "linearlight" | "multiply" | "multiply128" | "negation" | "normal" | "or" | "overlay" | "phoenix" | "pinlight" | "reflect" | "screen" | "softlight" | "subtract" | "vividlight" | "xor" | "softdifference" | "geometric" | "harmonic" | "bleach" | "stain" | "interpolate" | "hardoverlay";
    c3_mode?: FFInt | "addition" | "addition128" | "grainmerge" | "and" | "average" | "burn" | "darken" | "difference" | "difference128" | "grainextract" | "divide" | "dodge" | "exclusion" | "extremity" | "freeze" | "glow" | "hardlight" | "hardmix" | "heat" | "lighten" | "linearlight" | "multiply" | "multiply128" | "negation" | "normal" | "or" | "overlay" | "phoenix" | "pinlight" | "reflect" | "screen" | "softlight" | "subtract" | "vividlight" | "xor" | "softdifference" | "geometric" | "harmonic" | "bleach" | "stain" | "interpolate" | "hardoverlay";
    all_mode?: FFInt | "addition" | "addition128" | "grainmerge" | "and" | "average" | "burn" | "darken" | "difference" | "difference128" | "grainextract" | "divide" | "dodge" | "exclusion" | "extremity" | "freeze" | "glow" | "hardlight" | "hardmix" | "heat" | "lighten" | "linearlight" | "multiply" | "multiply128" | "negation" | "normal" | "or" | "overlay" | "phoenix" | "pinlight" | "reflect" | "screen" | "softlight" | "subtract" | "vividlight" | "xor" | "softdifference" | "geometric" | "harmonic" | "bleach" | "stain" | "interpolate" | "hardoverlay";
    c0_expr?: FFString;
    c1_expr?: FFString;
    c2_expr?: FFString;
    c3_expr?: FFString;
    all_expr?: FFString;
    c0_opacity?: FFDouble;
    c1_opacity?: FFDouble;
    c2_opacity?: FFDouble;
    c3_opacity?: FFDouble;
    all_opacity?: FFDouble;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "tblend", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "c0_mode": options?.c0_mode,
      "c1_mode": options?.c1_mode,
      "c2_mode": options?.c2_mode,
      "c3_mode": options?.c3_mode,
      "all_mode": options?.all_mode,
      "c0_expr": options?.c0_expr,
      "c1_expr": options?.c1_expr,
      "c2_expr": options?.c2_expr,
      "c3_expr": options?.c3_expr,
      "all_expr": options?.all_expr,
      "c0_opacity": options?.c0_opacity,
      "c1_opacity": options?.c1_opacity,
      "c2_opacity": options?.c2_opacity,
      "c3_opacity": options?.c3_opacity,
      "all_opacity": options?.all_opacity,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply a telecine pattern.

 *
 * @param options.first_field - select first field (from 0 to 1) (default top)
 * @param options.pattern - pattern that describe for how many fields a frame is to be displayed (default "23")
 * @see https://ffmpeg.org/ffmpeg-filters.html#telecine
 */
  telecine(
    options?: {
    first_field?: FFInt | "top" | "t" | "bottom" | "b";
    pattern?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "telecine", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "first_field": options?.first_field,
      "pattern": options?.pattern,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }










/**
 * Compute and draw a temporal histogram.

 *
 * @param options.width - set width (from 0 to 8192) (default 0)
 * @param options.display_mode - set display mode (from 0 to 2) (default stack)
 * @param options.levels_mode - set levels mode (from 0 to 1) (default linear)
 * @param options.components - set color components to display (from 1 to 15) (default 7)
 * @param options.bgopacity - set background opacity (from 0 to 1) (default 0.9)
 * @param options.envelope - display envelope (default false)
 * @param options.ecolor - set envelope color (default "gold")
 * @param options.slide - set slide mode (from 0 to 4) (default replace)
 * @see https://ffmpeg.org/ffmpeg-filters.html#thistogram
 */
  thistogram(
    options?: {
    width?: FFInt;
    display_mode?: FFInt | "overlay" | "parade" | "stack";
    levels_mode?: FFInt | "linear" | "logarithmic";
    components?: FFInt;
    bgopacity?: FFFloat;
    envelope?: FFBoolean;
    ecolor?: FFColor;
    slide?: FFInt | "frame" | "replace" | "scroll" | "rscroll" | "picture";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "thistogram", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "width": options?.width,
      "display_mode": options?.display_mode,
      "levels_mode": options?.levels_mode,
      "components": options?.components,
      "bgopacity": options?.bgopacity,
      "envelope": options?.envelope,
      "ecolor": options?.ecolor,
      "slide": options?.slide,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Threshold first video stream using other video streams.

 *
 * @param options.planes - set planes to filter (from 0 to 15) (default 15)
 * @see https://ffmpeg.org/ffmpeg-filters.html#threshold
 */
  threshold(
    _threshold: VideoStream,
    _min: VideoStream,
    _max: VideoStream,

    options?: {
    planes?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "threshold", typingsInput: ["video", "video", "video", "video"], typingsOutput: ["video"] },
      [this, _threshold, _min, _max],
      merge(
    {
      "planes": options?.planes,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Select the most representative frame in a given sequence of consecutive frames.

 *
 * @param options.n - set the frames batch size (from 2 to INT_MAX) (default 100)
 * @param options.log - force stats logging level (from INT_MIN to INT_MAX) (default info)
 * @see https://ffmpeg.org/ffmpeg-filters.html#thumbnail
 */
  thumbnail(
    options?: {
    n?: FFInt;
    log?: FFInt | "quiet" | "info" | "verbose";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "thumbnail", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "n": options?.n,
      "log": options?.log,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Tile several successive frames together.

 *
 * @param options.layout - set grid size (default "6x5")
 * @param options.nb_frames - set maximum number of frame to render (from 0 to INT_MAX) (default 0)
 * @param options.margin - set outer border margin in pixels (from 0 to 1024) (default 0)
 * @param options.padding - set inner border thickness in pixels (from 0 to 1024) (default 0)
 * @param options.color - set the color of the unused area (default "black")
 * @param options.overlap - set how many frames to overlap for each render (from 0 to INT_MAX) (default 0)
 * @param options.init_padding - set how many frames to initially pad (from 0 to INT_MAX) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#tile
 */
  tile(
    options?: {
    layout?: FFImageSize;
    nb_frames?: FFInt;
    margin?: FFInt;
    padding?: FFInt;
    color?: FFColor;
    overlap?: FFInt;
    init_padding?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "tile", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "layout": options?.layout,
      "nb_frames": options?.nb_frames,
      "margin": options?.margin,
      "padding": options?.padding,
      "color": options?.color,
      "overlap": options?.overlap,
      "init_padding": options?.init_padding,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Generate a tilt-and-shift'd video.

 *
 * @param options.tilt - Tilt the video horizontally while shifting (from 0 to 1) (default 1)
 * @param options.start - Action at the start of input (from 0 to 3) (default none)
 * @param options.end - Action at the end of input (from 0 to 3) (default none)
 * @param options.hold - Number of columns to hold at the start of the video (from 0 to INT_MAX) (default 0)
 * @param options.pad - Number of columns to pad at the end of the video (from 0 to INT_MAX) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#tiltandshift
 */
  tiltandshift(
    options?: {
    tilt?: FFInt;
    start?: FFInt | "none" | "frame" | "black";
    end?: FFInt | "none" | "frame" | "black";
    hold?: FFInt;
    pad?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "tiltandshift", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "tilt": options?.tilt,
      "start": options?.start,
      "end": options?.end,
      "hold": options?.hold,
      "pad": options?.pad,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Perform temporal field interlacing.

 *
 * @param options.mode - select interlace mode (from 0 to 7) (default merge)
 * @see https://ffmpeg.org/ffmpeg-filters.html#tinterlace
 */
  tinterlace(
    options?: {
    mode?: FFInt | "merge" | "drop_even" | "drop_odd" | "pad" | "interleave_top" | "interleave_bottom" | "interlacex2" | "mergex2";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "tinterlace", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "mode": options?.mode,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Compute and apply a lookup table from two successive frames.

 *
 * @param options.c0 - set component #0 expression (default "x")
 * @param options.c1 - set component #1 expression (default "x")
 * @param options.c2 - set component #2 expression (default "x")
 * @param options.c3 - set component #3 expression (default "x")
 * @see https://ffmpeg.org/ffmpeg-filters.html#lut2_002c-tlut2
 */
  tlut2(
    options?: {
    c0?: FFString;
    c1?: FFString;
    c2?: FFString;
    c3?: FFString;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "tlut2", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "c0": options?.c0,
      "c1": options?.c1,
      "c2": options?.c2,
      "c3": options?.c3,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Pick median pixels from successive frames.

 *
 * @param options.radius - set median filter radius (from 1 to 127) (default 1)
 * @param options.planes - set planes to filter (from 0 to 15) (default 15)
 * @param options.percentile - set percentile (from 0 to 1) (default 0.5)
 * @see https://ffmpeg.org/ffmpeg-filters.html#tmedian
 */
  tmedian(
    options?: {
    radius?: FFInt;
    planes?: FFInt;
    percentile?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "tmedian", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "radius": options?.radius,
      "planes": options?.planes,
      "percentile": options?.percentile,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply Temporal Midway Equalization.

 *
 * @param options.radius - set radius (from 1 to 127) (default 5)
 * @param options.sigma - set sigma (from 0 to 1) (default 0.5)
 * @param options.planes - set planes (from 0 to 15) (default 15)
 * @see https://ffmpeg.org/ffmpeg-filters.html#tmidequalizer
 */
  tmidequalizer(
    options?: {
    radius?: FFInt;
    sigma?: FFFloat;
    planes?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "tmidequalizer", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "radius": options?.radius,
      "sigma": options?.sigma,
      "planes": options?.planes,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Mix successive video frames.

 *
 * @param options.frames - set number of successive frames to mix (from 1 to 1024) (default 3)
 * @param options.weights - set weight for each frame (default "1 1 1")
 * @param options.scale - set scale (from 0 to 32767) (default 0)
 * @param options.planes - set what planes to filter (default F)
 * @see https://ffmpeg.org/ffmpeg-filters.html#tmix
 */
  tmix(
    options?: {
    frames?: FFInt;
    weights?: FFString;
    scale?: FFFloat;
    planes?: FFFlags;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "tmix", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "frames": options?.frames,
      "weights": options?.weights,
      "scale": options?.scale,
      "planes": options?.planes,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Conversion to/from different dynamic ranges.

 *
 * @param options.tonemap - tonemap algorithm selection (from 0 to 6) (default none)
 * @param options.param - tonemap parameter (from DBL_MIN to DBL_MAX) (default nan)
 * @param options.desat - desaturation strength (from 0 to DBL_MAX) (default 2)
 * @param options.peak - signal peak override (from 0 to DBL_MAX) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#tonemap
 */
  tonemap(
    options?: {
    tonemap?: FFInt | "none" | "linear" | "gamma" | "clip" | "reinhard" | "hable" | "mobius";
    param?: FFDouble;
    desat?: FFDouble;
    peak?: FFDouble;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "tonemap", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "tonemap": options?.tonemap,
      "param": options?.param,
      "desat": options?.desat,
      "peak": options?.peak,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Temporarily pad video frames.

 *
 * @param options.start - set the number of frames to delay input (from 0 to INT_MAX) (default 0)
 * @param options.stop - set the number of frames to add after input finished (from -1 to INT_MAX) (default 0)
 * @param options.start_mode - set the mode of added frames to start (from 0 to 1) (default add)
 * @param options.stop_mode - set the mode of added frames to end (from 0 to 1) (default add)
 * @param options.start_duration - set the duration to delay input (default 0)
 * @param options.stop_duration - set the duration to pad input (default 0)
 * @param options.color - set the color of the added frames (default "black")
 * @see https://ffmpeg.org/ffmpeg-filters.html#tpad
 */
  tpad(
    options?: {
    start?: FFInt;
    stop?: FFInt;
    start_mode?: FFInt | "add" | "clone";
    stop_mode?: FFInt | "add" | "clone";
    start_duration?: FFDuration;
    stop_duration?: FFDuration;
    color?: FFColor;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "tpad", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "start": options?.start,
      "stop": options?.stop,
      "start_mode": options?.start_mode,
      "stop_mode": options?.stop_mode,
      "start_duration": options?.start_duration,
      "stop_duration": options?.stop_duration,
      "color": options?.color,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Transpose input video.

 *
 * @param options.dir - set transpose direction (from 0 to 7) (default cclock_flip)
 * @param options.passthrough - do not apply transposition if the input matches the specified geometry (from 0 to INT_MAX) (default none)
 * @see https://ffmpeg.org/ffmpeg-filters.html#transpose
 */
  transpose(
    options?: {
    dir?: FFInt | "cclock_flip" | "clock" | "cclock" | "clock_flip";
    passthrough?: FFInt | "none" | "portrait" | "landscape";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "transpose", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "dir": options?.dir,
      "passthrough": options?.passthrough,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Transpose Videotoolbox frames
 *
 * Note: New in FFmpeg 8.0.
 *
 * @param options.dir - set transpose direction (from 0 to 6) (default cclock_flip)
 * @param options.passthrough - do not apply transposition if the input matches the specified geometry (from 0 to INT_MAX) (default none)
 * @see https://ffmpeg.org/ffmpeg-filters.html#transpose_005fvt
 */
  transpose_vt(
    options?: {
    dir?: FFInt | "cclock_flip" | "clock" | "cclock" | "clock_flip" | "reversal" | "hflip" | "vflip";
    passthrough?: FFInt | "none" | "portrait" | "landscape";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "transpose_vt", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "dir": options?.dir,
      "passthrough": options?.passthrough,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }










/**
 * Pick one continuous section from the input, drop the rest.

 *
 * @param options.start - Timestamp of the first frame that should be passed (default INT64_MAX)
 * @param options.end - Timestamp of the first frame that should be dropped again (default INT64_MAX)
 * @param options.start_pts - Timestamp of the first frame that should be passed (from I64_MIN to I64_MAX) (default I64_MIN)
 * @param options.end_pts - Timestamp of the first frame that should be dropped again (from I64_MIN to I64_MAX) (default I64_MIN)
 * @param options.duration - Maximum duration of the output (default 0)
 * @param options.start_frame - Number of the first frame that should be passed to the output (from -1 to I64_MAX) (default -1)
 * @param options.end_frame - Number of the first frame that should be dropped again (from 0 to I64_MAX) (default I64_MAX)
 * @see https://ffmpeg.org/ffmpeg-filters.html#trim
 */
  trim(
    options?: {
    start?: FFDuration;
    end?: FFDuration;
    start_pts?: FFInt64;
    end_pts?: FFInt64;
    duration?: FFDuration;
    start_frame?: FFInt64;
    end_frame?: FFInt64;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "trim", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "start": options?.start,
      "end": options?.end,
      "start_pts": options?.start_pts,
      "end_pts": options?.end_pts,
      "duration": options?.duration,
      "start_frame": options?.start_frame,
      "end_frame": options?.end_frame,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Sharpen or blur the input video.

 *
 * @param options.luma_msize_x - set luma matrix horizontal size (from 3 to 23) (default 5)
 * @param options.luma_msize_y - set luma matrix vertical size (from 3 to 23) (default 5)
 * @param options.luma_amount - set luma effect strength (from -2 to 5) (default 1)
 * @param options.chroma_msize_x - set chroma matrix horizontal size (from 3 to 23) (default 5)
 * @param options.chroma_msize_y - set chroma matrix vertical size (from 3 to 23) (default 5)
 * @param options.chroma_amount - set chroma effect strength (from -2 to 5) (default 0)
 * @param options.alpha_msize_x - set alpha matrix horizontal size (from 3 to 23) (default 5)
 * @param options.alpha_msize_y - set alpha matrix vertical size (from 3 to 23) (default 5)
 * @param options.alpha_amount - set alpha effect strength (from -2 to 5) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#unsharp
 */
  unsharp(
    options?: {
    luma_msize_x?: FFInt;
    luma_msize_y?: FFInt;
    luma_amount?: FFFloat;
    chroma_msize_x?: FFInt;
    chroma_msize_y?: FFInt;
    chroma_amount?: FFFloat;
    alpha_msize_x?: FFInt;
    alpha_msize_y?: FFInt;
    alpha_amount?: FFFloat;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "unsharp", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "luma_msize_x": options?.luma_msize_x,
      "luma_msize_y": options?.luma_msize_y,
      "luma_amount": options?.luma_amount,
      "chroma_msize_x": options?.chroma_msize_x,
      "chroma_msize_y": options?.chroma_msize_y,
      "chroma_amount": options?.chroma_amount,
      "alpha_msize_x": options?.alpha_msize_x,
      "alpha_msize_y": options?.alpha_msize_y,
      "alpha_amount": options?.alpha_amount,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Untile a frame into a sequence of frames.

 *
 * @param options.layout - set grid size (default "6x5")
 * @see https://ffmpeg.org/ffmpeg-filters.html#untile
 */
  untile(
    options?: {
    layout?: FFImageSize;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "untile", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "layout": options?.layout,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply Ultra Simple / Slow Post-processing filter.

 *
 * @param options.quality - set quality (from 0 to 8) (default 3)
 * @param options.qp - force a constant quantizer parameter (from 0 to 63) (default 0)
 * @param options.use_bframe_qp - use B-frames' QP (default false)
 * @param options.codec - Codec name (default "snow")
 * @see https://ffmpeg.org/ffmpeg-filters.html#uspp
 */
  uspp(
    options?: {
    quality?: FFInt;
    qp?: FFInt;
    use_bframe_qp?: FFBoolean;
    codec?: FFString;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "uspp", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "quality": options?.quality,
      "qp": options?.qp,
      "use_bframe_qp": options?.use_bframe_qp,
      "codec": options?.codec,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Convert 360 projection of video.

 *
 * @param options.input - set input projection (from 0 to 24) (default e)
 * @param options.output - set output projection (from 0 to 24) (default c3x2)
 * @param options.interp - set interpolation method (from 0 to 7) (default line)
 * @param options.w - output width (from 0 to 32767) (default 0)
 * @param options.h - output height (from 0 to 32767) (default 0)
 * @param options.in_stereo - input stereo format (from 0 to 2) (default 2d)
 * @param options.out_stereo - output stereo format (from 0 to 2) (default 2d)
 * @param options.in_forder - input cubemap face order (default "rludfb")
 * @param options.out_forder - output cubemap face order (default "rludfb")
 * @param options.in_frot - input cubemap face rotation (default "000000")
 * @param options.out_frot - output cubemap face rotation (default "000000")
 * @param options.in_pad - percent input cubemap pads (from 0 to 0.1) (default 0)
 * @param options.out_pad - percent output cubemap pads (from 0 to 0.1) (default 0)
 * @param options.fin_pad - fixed input cubemap pads (from 0 to 100) (default 0)
 * @param options.fout_pad - fixed output cubemap pads (from 0 to 100) (default 0)
 * @param options.yaw - yaw rotation (from -180 to 180) (default 0)
 * @param options.pitch - pitch rotation (from -180 to 180) (default 0)
 * @param options.roll - roll rotation (from -180 to 180) (default 0)
 * @param options.rorder - rotation order (default "ypr")
 * @param options.h_fov - output horizontal field of view (from 0 to 360) (default 0)
 * @param options.v_fov - output vertical field of view (from 0 to 360) (default 0)
 * @param options.d_fov - output diagonal field of view (from 0 to 360) (default 0)
 * @param options.h_flip - flip out video horizontally (default false)
 * @param options.v_flip - flip out video vertically (default false)
 * @param options.d_flip - flip out video indepth (default false)
 * @param options.ih_flip - flip in video horizontally (default false)
 * @param options.iv_flip - flip in video vertically (default false)
 * @param options.in_trans - transpose video input (default false)
 * @param options.out_trans - transpose video output (default false)
 * @param options.ih_fov - input horizontal field of view (from 0 to 360) (default 0)
 * @param options.iv_fov - input vertical field of view (from 0 to 360) (default 0)
 * @param options.id_fov - input diagonal field of view (from 0 to 360) (default 0)
 * @param options.h_offset - output horizontal off-axis offset (from -1 to 1) (default 0)
 * @param options.v_offset - output vertical off-axis offset (from -1 to 1) (default 0)
 * @param options.alpha_mask - build mask in alpha plane (default false)
 * @param options.reset_rot - reset rotation (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#v360
 */
  v360(
    options?: {
    input?: FFInt | "e" | "equirect" | "c3x2" | "c6x1" | "eac" | "dfisheye" | "flat" | "rectilinear" | "gnomonic" | "barrel" | "fb" | "c1x6" | "sg" | "mercator" | "ball" | "hammer" | "sinusoidal" | "fisheye" | "pannini" | "cylindrical" | "tetrahedron" | "barrelsplit" | "tsp" | "hequirect" | "he" | "equisolid" | "og" | "octahedron" | "cylindricalea";
    output?: FFInt | "e" | "equirect" | "c3x2" | "c6x1" | "eac" | "dfisheye" | "flat" | "rectilinear" | "gnomonic" | "barrel" | "fb" | "c1x6" | "sg" | "mercator" | "ball" | "hammer" | "sinusoidal" | "fisheye" | "pannini" | "cylindrical" | "perspective" | "tetrahedron" | "barrelsplit" | "tsp" | "hequirect" | "he" | "equisolid" | "og" | "octahedron" | "cylindricalea";
    interp?: FFInt | "near" | "nearest" | "line" | "linear" | "lagrange9" | "cube" | "cubic" | "lanc" | "lanczos" | "sp16" | "spline16" | "gauss" | "gaussian" | "mitchell";
    w?: FFInt;
    h?: FFInt;
    in_stereo?: FFInt | "2d" | "sbs" | "tb";
    out_stereo?: FFInt | "2d" | "sbs" | "tb";
    in_forder?: FFString;
    out_forder?: FFString;
    in_frot?: FFString;
    out_frot?: FFString;
    in_pad?: FFFloat;
    out_pad?: FFFloat;
    fin_pad?: FFInt;
    fout_pad?: FFInt;
    yaw?: FFFloat;
    pitch?: FFFloat;
    roll?: FFFloat;
    rorder?: FFString;
    h_fov?: FFFloat;
    v_fov?: FFFloat;
    d_fov?: FFFloat;
    h_flip?: FFBoolean;
    v_flip?: FFBoolean;
    d_flip?: FFBoolean;
    ih_flip?: FFBoolean;
    iv_flip?: FFBoolean;
    in_trans?: FFBoolean;
    out_trans?: FFBoolean;
    ih_fov?: FFFloat;
    iv_fov?: FFFloat;
    id_fov?: FFFloat;
    h_offset?: FFFloat;
    v_offset?: FFFloat;
    alpha_mask?: FFBoolean;
    reset_rot?: FFBoolean;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "v360", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "input": options?.input,
      "output": options?.output,
      "interp": options?.interp,
      "w": options?.w,
      "h": options?.h,
      "in_stereo": options?.in_stereo,
      "out_stereo": options?.out_stereo,
      "in_forder": options?.in_forder,
      "out_forder": options?.out_forder,
      "in_frot": options?.in_frot,
      "out_frot": options?.out_frot,
      "in_pad": options?.in_pad,
      "out_pad": options?.out_pad,
      "fin_pad": options?.fin_pad,
      "fout_pad": options?.fout_pad,
      "yaw": options?.yaw,
      "pitch": options?.pitch,
      "roll": options?.roll,
      "rorder": options?.rorder,
      "h_fov": options?.h_fov,
      "v_fov": options?.v_fov,
      "d_fov": options?.d_fov,
      "h_flip": options?.h_flip,
      "v_flip": options?.v_flip,
      "d_flip": options?.d_flip,
      "ih_flip": options?.ih_flip,
      "iv_flip": options?.iv_flip,
      "in_trans": options?.in_trans,
      "out_trans": options?.out_trans,
      "ih_fov": options?.ih_fov,
      "iv_fov": options?.iv_fov,
      "id_fov": options?.id_fov,
      "h_offset": options?.h_offset,
      "v_offset": options?.v_offset,
      "alpha_mask": options?.alpha_mask,
      "reset_rot": options?.reset_rot,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply a Wavelet based Denoiser.

 *
 * @param options.threshold - set filtering strength (from 0 to DBL_MAX) (default 2)
 * @param options.method - set filtering method (from 0 to 2) (default garrote)
 * @param options.nsteps - set number of steps (from 1 to 32) (default 6)
 * @param options.percent - set percent of full denoising (from 0 to 100) (default 85)
 * @param options.planes - set planes to filter (from 0 to 15) (default 15)
 * @param options._type - set threshold type (from 0 to 1) (default universal)
 * @see https://ffmpeg.org/ffmpeg-filters.html#vaguedenoiser
 */
  vaguedenoiser(
    options?: {
    threshold?: FFFloat;
    method?: FFInt | "hard" | "soft" | "garrote";
    nsteps?: FFInt;
    percent?: FFFloat;
    planes?: FFInt;
    _type?: FFInt | "universal" | "bayes";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "vaguedenoiser", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "threshold": options?.threshold,
      "method": options?.method,
      "nsteps": options?.nsteps,
      "percent": options?.percent,
      "planes": options?.planes,
      "type": options?._type,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Apply Variable Blur filter.

 *
 * @param options.min_r - set min blur radius (from 0 to 254) (default 0)
 * @param options.max_r - set max blur radius (from 1 to 255) (default 8)
 * @param options.planes - set planes to filter (from 0 to 15) (default 15)
 * @see https://ffmpeg.org/ffmpeg-filters.html#varblur
 */
  varblur(
    _radius: VideoStream,

    options?: {
    min_r?: FFInt;
    max_r?: FFInt;
    planes?: FFInt;
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "varblur", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _radius],
      merge(
    {
      "min_r": options?.min_r,
      "max_r": options?.max_r,
      "planes": options?.planes,
      "eof_action": options?.eofAction,
      "shortest": options?.shortest,
      "repeatlast": options?.repeatlast,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Video vectorscope.

 *
 * @param options.mode - set vectorscope mode (from 0 to 5) (default gray)
 * @param options.x - set color component on X axis (from 0 to 2) (default 1)
 * @param options.y - set color component on Y axis (from 0 to 2) (default 2)
 * @param options.intensity - set intensity (from 0 to 1) (default 0.004)
 * @param options.envelope - set envelope (from 0 to 3) (default none)
 * @param options.graticule - set graticule (from 0 to 3) (default none)
 * @param options.opacity - set graticule opacity (from 0 to 1) (default 0.75)
 * @param options.flags - set graticule flags (default name)
 * @param options.bgopacity - set background opacity (from 0 to 1) (default 0.3)
 * @param options.lthreshold - set low threshold (from 0 to 1) (default 0)
 * @param options.hthreshold - set high threshold (from 0 to 1) (default 1)
 * @param options.colorspace - set colorspace (from 0 to 2) (default auto)
 * @param options.tint0 - set 1st tint (from -1 to 1) (default 0)
 * @param options.tint1 - set 2nd tint (from -1 to 1) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#vectorscope
 */
  vectorscope(
    options?: {
    mode?: FFInt | "gray" | "tint" | "color" | "color2" | "color3" | "color4" | "color5";
    x?: FFInt;
    y?: FFInt;
    intensity?: FFFloat;
    envelope?: FFInt | "none" | "instant" | "peak" | "peak+instant";
    graticule?: FFInt | "none" | "green" | "color" | "invert";
    opacity?: FFFloat;
    flags?: FFFlags | "white" | "black" | "name";
    bgopacity?: FFFloat;
    lthreshold?: FFFloat;
    hthreshold?: FFFloat;
    colorspace?: FFInt | "auto" | "601" | "709";
    tint0?: FFFloat;
    tint1?: FFFloat;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "vectorscope", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "mode": options?.mode,
      "x": options?.x,
      "y": options?.y,
      "intensity": options?.intensity,
      "envelope": options?.envelope,
      "graticule": options?.graticule,
      "opacity": options?.opacity,
      "flags": options?.flags,
      "bgopacity": options?.bgopacity,
      "lthreshold": options?.lthreshold,
      "hthreshold": options?.hthreshold,
      "colorspace": options?.colorspace,
      "tint0": options?.tint0,
      "tint1": options?.tint1,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Flip the input video vertically.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#vflip
 */
  vflip(
    options?: {
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "vflip", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Variable frame rate detect filter.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#vfrdet
 */
  vfrdet(
    options?: {
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "vfrdet", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Boost or alter saturation.

 *
 * @param options.intensity - set the intensity value (from -2 to 2) (default 0)
 * @param options.rbal - set the red balance value (from -10 to 10) (default 1)
 * @param options.gbal - set the green balance value (from -10 to 10) (default 1)
 * @param options.bbal - set the blue balance value (from -10 to 10) (default 1)
 * @param options.rlum - set the red luma coefficient (from 0 to 1) (default 0.212656)
 * @param options.glum - set the green luma coefficient (from 0 to 1) (default 0.715158)
 * @param options.blum - set the blue luma coefficient (from 0 to 1) (default 0.072186)
 * @param options.alternate - use alternate colors (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#vibrance
 */
  vibrance(
    options?: {
    intensity?: FFFloat;
    rbal?: FFFloat;
    gbal?: FFFloat;
    bbal?: FFFloat;
    rlum?: FFFloat;
    glum?: FFFloat;
    blum?: FFFloat;
    alternate?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "vibrance", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "intensity": options?.intensity,
      "rbal": options?.rbal,
      "gbal": options?.gbal,
      "bbal": options?.bbal,
      "rlum": options?.rlum,
      "glum": options?.glum,
      "blum": options?.blum,
      "alternate": options?.alternate,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Calculate the VIF between two video streams.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#vif
 */
  vif(
    _reference: VideoStream,

    options?: {
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "vif", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _reference],
      merge(
    {
      "eof_action": options?.eofAction,
      "shortest": options?.shortest,
      "repeatlast": options?.repeatlast,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Make or reverse a vignette effect.

 *
 * @param options.angle - set lens angle (default "PI/5")
 * @param options.x0 - set circle center position on x-axis (default "w/2")
 * @param options.y0 - set circle center position on y-axis (default "h/2")
 * @param options.mode - set forward/backward mode (from 0 to 1) (default forward)
 * @param options.eval - specify when to evaluate expressions (from 0 to 1) (default init)
 * @param options.dither - set dithering (default true)
 * @param options.aspect - set aspect ratio (from 0 to DBL_MAX) (default 1/1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#vignette
 */
  vignette(
    options?: {
    angle?: FFString;
    x0?: FFString;
    y0?: FFString;
    mode?: FFInt | "forward" | "backward";
    eval?: FFInt | "init" | "frame";
    dither?: FFBoolean;
    aspect?: FFRational;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "vignette", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "angle": options?.angle,
      "x0": options?.x0,
      "y0": options?.y0,
      "mode": options?.mode,
      "eval": options?.eval,
      "dither": options?.dither,
      "aspect": options?.aspect,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Calculate the VMAF Motion score.

 *
 * @param options.stats_file - Set file where to store per-frame difference information
 * @see https://ffmpeg.org/ffmpeg-filters.html#vmafmotion
 */
  vmafmotion(
    options?: {
    stats_file?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "vmafmotion", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "stats_file": options?.stats_file,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }












/**
 * Apply Martin Weston three field deinterlace.

 *
 * @param options.filter - specify the filter (from 0 to 1) (default complex)
 * @param options.mode - specify the interlacing mode (from 0 to 1) (default field)
 * @param options.parity - specify the assumed picture field parity (from -1 to 1) (default auto)
 * @param options.deint - specify which frames to deinterlace (from 0 to 1) (default all)
 * @see https://ffmpeg.org/ffmpeg-filters.html#w3fdif
 */
  w3fdif(
    options?: {
    filter?: FFInt | "simple" | "complex";
    mode?: FFInt | "frame" | "field";
    parity?: FFInt | "tff" | "bff" | "auto";
    deint?: FFInt | "all" | "interlaced";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "w3fdif", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "filter": options?.filter,
      "mode": options?.mode,
      "parity": options?.parity,
      "deint": options?.deint,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Video waveform monitor.

 *
 * @param options.mode - set mode (from 0 to 1) (default column)
 * @param options.intensity - set intensity (from 0 to 1) (default 0.04)
 * @param options.mirror - set mirroring (default true)
 * @param options.display - set display mode (from 0 to 2) (default stack)
 * @param options.components - set components to display (from 1 to 15) (default 1)
 * @param options.envelope - set envelope to display (from 0 to 3) (default none)
 * @param options.filter - set filter (from 0 to 7) (default lowpass)
 * @param options.graticule - set graticule (from 0 to 3) (default none)
 * @param options.opacity - set graticule opacity (from 0 to 1) (default 0.75)
 * @param options.flags - set graticule flags (default numbers)
 * @param options.scale - set scale (from 0 to 2) (default digital)
 * @param options.bgopacity - set background opacity (from 0 to 1) (default 0.75)
 * @param options.tint0 - set 1st tint (from -1 to 1) (default 0)
 * @param options.tint1 - set 2nd tint (from -1 to 1) (default 0)
 * @param options.fitmode - set fit mode (from 0 to 1) (default none)
 * @param options.input - set input formats selection (from 0 to 1) (default first)
 * @see https://ffmpeg.org/ffmpeg-filters.html#waveform
 */
  waveform(
    options?: {
    mode?: FFInt | "row" | "column";
    intensity?: FFFloat;
    mirror?: FFBoolean;
    display?: FFInt | "overlay" | "stack" | "parade";
    components?: FFInt;
    envelope?: FFInt | "none" | "instant" | "peak" | "peak+instant";
    filter?: FFInt | "lowpass" | "flat" | "aflat" | "chroma" | "color" | "acolor" | "xflat" | "yflat";
    graticule?: FFInt | "none" | "green" | "orange" | "invert";
    opacity?: FFFloat;
    flags?: FFFlags | "numbers" | "dots";
    scale?: FFInt | "digital" | "millivolts" | "ire";
    bgopacity?: FFFloat;
    tint0?: FFFloat;
    tint1?: FFFloat;
    fitmode?: FFInt | "none" | "size";
    input?: FFInt | "all" | "first";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "waveform", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "mode": options?.mode,
      "intensity": options?.intensity,
      "mirror": options?.mirror,
      "display": options?.display,
      "components": options?.components,
      "envelope": options?.envelope,
      "filter": options?.filter,
      "graticule": options?.graticule,
      "opacity": options?.opacity,
      "flags": options?.flags,
      "scale": options?.scale,
      "bgopacity": options?.bgopacity,
      "tint0": options?.tint0,
      "tint1": options?.tint1,
      "fitmode": options?.fitmode,
      "input": options?.input,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Weave input video fields into frames.

 *
 * @param options.first_field - set first field (from 0 to 1) (default top)
 * @see https://ffmpeg.org/ffmpeg-filters.html#weave_002c-doubleweave
 */
  weave(
    options?: {
    first_field?: FFInt | "top" | "t" | "bottom" | "b";
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "weave", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "first_field": options?.first_field,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Scale the input using xBR algorithm.

 *
 * @param options.n - set scale factor (from 2 to 4) (default 3)
 * @see https://ffmpeg.org/ffmpeg-filters.html#xbr
 */
  xbr(
    options?: {
    n?: FFInt;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "xbr", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "n": options?.n,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Cross-correlate first video stream with second video stream.

 *
 * @param options.planes - set planes to cross-correlate (from 0 to 15) (default 7)
 * @param options.secondary - when to process secondary frame (from 0 to 1) (default all)
 * @see https://ffmpeg.org/ffmpeg-filters.html#xcorrelate
 */
  xcorrelate(
    _secondary: VideoStream,

    options?: {
    planes?: FFInt;
    secondary?: FFInt | "first" | "all";
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "xcorrelate", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _secondary],
      merge(
    {
      "planes": options?.planes,
      "secondary": options?.secondary,
      "eof_action": options?.eofAction,
      "shortest": options?.shortest,
      "repeatlast": options?.repeatlast,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Cross fade one video with another video.

 *
 * @param options.transition - set cross fade transition (from -1 to 57) (default fade)
 * @param options.duration - set cross fade duration (default 1)
 * @param options.offset - set cross fade start relative to first input stream (default 0)
 * @param options.expr - set expression for custom transition
 * @see https://ffmpeg.org/ffmpeg-filters.html#xfade
 */
  xfade(
    _xfade: VideoStream,

    options?: {
    transition?: FFInt | "custom" | "fade" | "wipeleft" | "wiperight" | "wipeup" | "wipedown" | "slideleft" | "slideright" | "slideup" | "slidedown" | "circlecrop" | "rectcrop" | "distance" | "fadeblack" | "fadewhite" | "radial" | "smoothleft" | "smoothright" | "smoothup" | "smoothdown" | "circleopen" | "circleclose" | "vertopen" | "vertclose" | "horzopen" | "horzclose" | "dissolve" | "pixelize" | "diagtl" | "diagtr" | "diagbl" | "diagbr" | "hlslice" | "hrslice" | "vuslice" | "vdslice" | "hblur" | "fadegrays" | "wipetl" | "wipetr" | "wipebl" | "wipebr" | "squeezeh" | "squeezev" | "zoomin" | "fadefast" | "fadeslow" | "hlwind" | "hrwind" | "vuwind" | "vdwind" | "coverleft" | "coverright" | "coverup" | "coverdown" | "revealleft" | "revealright" | "revealup" | "revealdown";
    duration?: FFDuration;
    offset?: FFDuration;
    expr?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "xfade", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _xfade],
      merge(
    {
      "transition": options?.transition,
      "duration": options?.duration,
      "offset": options?.offset,
      "expr": options?.expr,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Calculate the extended perceptually weighted peak signal-to-noise ratio (XPSNR) between two video streams.

 *
 * @param options.stats_file - Set file where to store per-frame XPSNR information
 * @see https://ffmpeg.org/ffmpeg-filters.html#xpsnr
 */
  xpsnr(
    _reference: VideoStream,

    options?: {
    stats_file?: FFString;
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "xpsnr", typingsInput: ["video", "video"], typingsOutput: ["video"] },
      [this, _reference],
      merge(
    {
      "stats_file": options?.stats_file,
      "eof_action": options?.eofAction,
      "shortest": options?.shortest,
      "repeatlast": options?.repeatlast,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }








/**
 * Deinterlace the input image.

 *
 * @param options.mode - specify the interlacing mode (from 0 to 3) (default send_frame)
 * @param options.parity - specify the assumed picture field parity (from -1 to 1) (default auto)
 * @param options.deint - specify which frames to deinterlace (from 0 to 1) (default all)
 * @see https://ffmpeg.org/ffmpeg-filters.html#yadif
 */
  yadif(
    options?: {
    mode?: FFInt | "send_frame" | "send_field" | "send_frame_nospatial" | "send_field_nospatial";
    parity?: FFInt | "tff" | "bff" | "auto";
    deint?: FFInt | "all" | "interlaced";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "yadif", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "mode": options?.mode,
      "parity": options?.parity,
      "deint": options?.deint,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }






/**
 * Yet another edge preserving blur filter.

 *
 * @param options.radius - set window radius (from 0 to INT_MAX) (default 3)
 * @param options.planes - set planes to filter (from 0 to 15) (default 1)
 * @param options.sigma - set blur strength (from 1 to INT_MAX) (default 128)
 * @see https://ffmpeg.org/ffmpeg-filters.html#yaepblur
 */
  yaepblur(
    options?: {
    radius?: FFInt;
    planes?: FFInt;
    sigma?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "yaepblur", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "radius": options?.radius,
      "planes": options?.planes,
      "sigma": options?.sigma,
      "enable": options?.enable,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }










/**
 * Apply Zoom & Pan effect.

 *
 * @param options.zoom - set the zoom expression (default "1")
 * @param options.x - set the x expression (default "0")
 * @param options.y - set the y expression (default "0")
 * @param options.d - set the duration expression (default "90")
 * @param options.s - set the output image size (default "hd720")
 * @param options.fps - set the output framerate (default "25")
 * @see https://ffmpeg.org/ffmpeg-filters.html#zoompan
 */
  zoompan(
    options?: {
    zoom?: FFString;
    x?: FFString;
    y?: FFString;
    d?: FFString;
    s?: FFImageSize;
    fps?: FFVideoRate;
extraOptions?: Record<string, unknown>;
    },
  ): VideoStream {
    const filterNode = filterNodeFactory(
      { name: "zoompan", typingsInput: ["video"], typingsOutput: ["video"] },
      [this],
      merge(
    {
      "zoom": options?.zoom,
      "x": options?.x,
      "y": options?.y,
      "d": options?.d,
      "s": options?.s,
      "fps": options?.fps,
},
    options?.extraOptions,
  ),
    );
return filterNode.video(0) as unknown as VideoStream;
  }



}
