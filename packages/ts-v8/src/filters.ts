// NOTE: this file is auto-generated, do not modify
/**
 * FFmpeg filter functions (multi-input and dynamic-input filters).
 */


import { StreamType, type FFMpegFilterDef } from "@typed-ffmpeg/core/common/schema";
import { Default, Auto } from "@typed-ffmpeg/core/utils/types";
import { filterNodeFactory } from "@typed-ffmpeg/core/dag/factory";
import { merge } from "@typed-ffmpeg/core/utils/frozenRecord";
import { FilterableStream } from "@typed-ffmpeg/core/dag/baseStreams";
import { FilterNode, VideoStream, AudioStream } from "@typed-ffmpeg/core/dag/nodes";
import type {
  FFBoolean, FFInt, FFInt64, FFFloat, FFDouble, FFString,
  FFDuration, FFColor, FFFlags, FFDictionary, FFPixFmt,
  FFVideoRate, FFImageSize, FFRational, FFSampleFmt, FFBinary,
} from "@typed-ffmpeg/core/types";







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
export function aap(


  _input: AudioStream,

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

  const inputStreams: FilterableStream[] = [_input, _desired];

  const filterNode = filterNodeFactory(
    { name: "aap", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
    inputStreams,
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
 * Cross fade two input audio streams.

 *
 * @param options.inputs - set number of input files to cross fade (from 1 to INT_MAX) (default 2)
 * @param options.nb_samples - set number of samples for cross fade duration (from 1 to 2.14748e+08) (default 44100)
 * @param options.duration - set cross fade duration (default 0)
 * @param options.overlap - overlap 1st stream end with 2nd stream start (default true)
 * @param options.curve1 - set fade curve type for 1st stream (from -1 to 22) (default tri)
 * @param options.curve2 - set fade curve type for 2nd stream (from -1 to 22) (default tri)
 * @see https://ffmpeg.org/ffmpeg-filters.html#acrossfade
 */
export function acrossfade(

  streams: FilterableStream[],

  options?: {
    inputs?: FFInt;
    nb_samples?: FFInt64;
    duration?: FFDuration;
    overlap?: FFBoolean;
    curve1?: FFInt | "nofade" | "tri" | "qsin" | "esin" | "hsin" | "log" | "ipar" | "qua" | "cub" | "squ" | "cbr" | "par" | "exp" | "iqsin" | "ihsin" | "dese" | "desi" | "losi" | "sinc" | "isinc" | "quat" | "quatr" | "qsin2" | "hsin2";
    curve2?: FFInt | "nofade" | "tri" | "qsin" | "esin" | "hsin" | "log" | "ipar" | "qua" | "cub" | "squ" | "cbr" | "par" | "exp" | "iqsin" | "ihsin" | "dese" | "desi" | "losi" | "sinc" | "isinc" | "quat" | "quatr" | "qsin2" | "hsin2";
extraOptions?: Record<string, unknown>;
  },
): AudioStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "acrossfade", typingsInput: [], typingsOutput: ["audio"] },
    inputStreams,
    merge(
    {
      "inputs": options?.inputs,
      "nb_samples": options?.nb_samples,
      "duration": options?.duration,
      "overlap": options?.overlap,
      "curve1": options?.curve1,
      "curve2": options?.curve2,
},
    options?.extraOptions,
  ),
  );
return filterNode.audio(0) as unknown as AudioStream;
}








































































/**
 * Temporally interleave audio inputs.

 *
 * @param options.nb_inputs - set number of inputs (from 1 to INT_MAX) (default 2)
 * @param options.duration - how to determine the end-of-stream (from 0 to 2) (default longest)
 * @see https://ffmpeg.org/ffmpeg-filters.html#interleave_002c-ainterleave
 */
export function ainterleave(

  streams: FilterableStream[],

  options?: {
    nb_inputs?: FFInt;
    duration?: FFInt | "longest" | "shortest" | "first";
extraOptions?: Record<string, unknown>;
  },
): AudioStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "ainterleave", typingsInput: [], typingsOutput: ["audio"] },
    inputStreams,
    merge(
    {
      "nb_inputs": options?.nb_inputs,
      "duration": options?.duration,
},
    options?.extraOptions,
  ),
  );
return filterNode.audio(0) as unknown as AudioStream;
}




















/**
 * Copy the luma value of the second input into the alpha channel of the first input.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#alphamerge
 */
export function alphamerge(


  _main: VideoStream,

  _alpha: VideoStream,


  options?: {
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams: FilterableStream[] = [_main, _alpha];

  const filterNode = filterNodeFactory(
    { name: "alphamerge", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Merge two or more audio streams into a single multi-channel stream.

 *
 * @param options.inputs - specify the number of inputs (from 1 to 64) (default 2)
 * @param options.layout_mode - method used to determine the output channel layout (from 0 to 2) (default legacy)
 * @see https://ffmpeg.org/ffmpeg-filters.html#amerge
 */
export function amerge(

  streams: FilterableStream[],

  options?: {
    inputs?: FFInt;
    layout_mode?: FFInt | "legacy" | "reset" | "normal";
extraOptions?: Record<string, unknown>;
  },
): AudioStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "amerge", typingsInput: [], typingsOutput: ["audio"] },
    inputStreams,
    merge(
    {
      "inputs": options?.inputs,
      "layout_mode": options?.layout_mode,
},
    options?.extraOptions,
  ),
  );
return filterNode.audio(0) as unknown as AudioStream;
}








/**
 * Audio mixing.

 *
 * @param options.inputs - Number of inputs. (from 1 to 32767) (default 2)
 * @param options.duration - How to determine the end-of-stream. (from 0 to 2) (default longest)
 * @param options.dropout_transition - Transition time, in seconds, for volume renormalization when an input stream ends. (from 0 to INT_MAX) (default 2)
 * @param options.weights - Set weight for each input. (default "1 1")
 * @param options.normalize - Scale inputs (default true)
 * @see https://ffmpeg.org/ffmpeg-filters.html#amix
 */
export function amix(

  streams: FilterableStream[],

  options?: {
    inputs?: FFInt;
    duration?: FFInt | "longest" | "shortest" | "first";
    dropout_transition?: FFFloat;
    weights?: FFString;
    normalize?: FFBoolean;
extraOptions?: Record<string, unknown>;
  },
): AudioStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "amix", typingsInput: [], typingsOutput: ["audio"] },
    inputStreams,
    merge(
    {
      "inputs": options?.inputs,
      "duration": options?.duration,
      "dropout_transition": options?.dropout_transition,
      "weights": options?.weights,
      "normalize": options?.normalize,
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
export function amultiply(


  _multiply0: AudioStream,

  _multiply1: AudioStream,


  options?: {
extraOptions?: Record<string, unknown>;
  },
): AudioStream {

  const inputStreams: FilterableStream[] = [_multiply0, _multiply1];

  const filterNode = filterNodeFactory(
    { name: "amultiply", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
    inputStreams,
    merge(
    {
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
export function anlmf(


  _input: AudioStream,

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

  const inputStreams: FilterableStream[] = [_input, _desired];

  const filterNode = filterNodeFactory(
    { name: "anlmf", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
    inputStreams,
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
export function anlms(


  _input: AudioStream,

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

  const inputStreams: FilterableStream[] = [_input, _desired];

  const filterNode = filterNodeFactory(
    { name: "anlms", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
    inputStreams,
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
 * Measure Audio Peak Signal-to-Noise Ratio.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#apsnr
 */
export function apsnr(


  _input0: AudioStream,

  _input1: AudioStream,


  options?: {
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): AudioStream {

  const inputStreams: FilterableStream[] = [_input0, _input1];

  const filterNode = filterNodeFactory(
    { name: "apsnr", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
    inputStreams,
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
 * Apply Recursive Least Squares algorithm to first audio stream.

 *
 * @param options.order - set the filter order (from 1 to 32767) (default 16)
 * @param options._lambda - set the filter lambda (from 0 to 1) (default 1)
 * @param options.delta - set the filter delta (from 0 to 32767) (default 2)
 * @param options.out_mode - set output mode (from 0 to 4) (default o)
 * @param options.precision - set processing precision (from 0 to 2) (default auto)
 * @see https://ffmpeg.org/ffmpeg-filters.html#arls
 */
export function arls(


  _input: AudioStream,

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

  const inputStreams: FilterableStream[] = [_input, _desired];

  const filterNode = filterNodeFactory(
    { name: "arls", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
    inputStreams,
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
 * Measure Audio Signal-to-Distortion Ratio.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#asdr
 */
export function asdr(


  _input0: AudioStream,

  _input1: AudioStream,


  options?: {
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): AudioStream {

  const inputStreams: FilterableStream[] = [_input0, _input1];

  const filterNode = filterNodeFactory(
    { name: "asdr", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
    inputStreams,
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
 * Measure Audio Scale-Invariant Signal-to-Distortion Ratio.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#asisdr
 */
export function asisdr(


  _input0: AudioStream,

  _input1: AudioStream,


  options?: {
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): AudioStream {

  const inputStreams: FilterableStream[] = [_input0, _input1];

  const filterNode = filterNodeFactory(
    { name: "asisdr", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
    inputStreams,
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
 * Select audio streams

 *
 * @param options.inputs - number of input streams (from 2 to INT_MAX) (default 2)
 * @param options.map - input indexes to remap to outputs
 * @see https://ffmpeg.org/ffmpeg-filters.html#streamselect_002c-astreamselect
 */
export function astreamselect(

  streams: FilterableStream[],

  options?: {
    inputs?: FFInt;
    map?: FFString;
extraOptions?: Record<string, unknown>;
  },
): FilterNode {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "astreamselect", typingsInput: [], typingsOutput: [] },
    inputStreams,
    merge(
    {
      "inputs": options?.inputs,
      "map": options?.map,
},
    options?.extraOptions,
  ),
  );
return filterNode;
}






























/**
 * Cross-correlate two audio streams.

 *
 * @param options.size - set the segment size (from 2 to 131072) (default 256)
 * @param options.algo - set the algorithm (from 0 to 2) (default best)
 * @see https://ffmpeg.org/ffmpeg-filters.html#axcorrelate
 */
export function axcorrelate(


  _axcorrelate0: AudioStream,

  _axcorrelate1: AudioStream,


  options?: {
    size?: FFInt;
    algo?: FFInt | "slow" | "fast" | "best";
extraOptions?: Record<string, unknown>;
  },
): AudioStream {

  const inputStreams: FilterableStream[] = [_axcorrelate0, _axcorrelate1];

  const filterNode = filterNodeFactory(
    { name: "axcorrelate", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
    inputStreams,
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
export function blend(


  _top: VideoStream,

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

  const inputStreams: FilterableStream[] = [_top, _bottom];

  const filterNode = filterNodeFactory(
    { name: "blend", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Block-Matching 3D denoiser.

 *
 * @param options.sigma - set denoising strength (from 0 to 99999.9) (default 1)
 * @param options.block - set size of local patch (from 8 to 64) (default 16)
 * @param options.bstep - set sliding step for processing blocks (from 1 to 64) (default 4)
 * @param options.group - set maximal number of similar blocks (from 1 to 256) (default 1)
 * @param options.range - set block matching range (from 1 to INT_MAX) (default 9)
 * @param options.mstep - set step for block matching (from 1 to 64) (default 1)
 * @param options.thmse - set threshold of mean square error for block matching (from 0 to INT_MAX) (default 0)
 * @param options.hdthr - set hard threshold for 3D transfer domain (from 0 to INT_MAX) (default 2.7)
 * @param options.estim - set filtering estimation mode (from 0 to 1) (default basic)
 * @param options.ref - have reference stream (default false)
 * @param options.planes - set planes to filter (from 0 to 15) (default 7)
 * @see https://ffmpeg.org/ffmpeg-filters.html#bm3d
 */
export function bm3d(

  streams: FilterableStream[],

  options?: {
    sigma?: FFFloat;
    block?: FFInt;
    bstep?: FFInt;
    group?: FFInt;
    range?: FFInt;
    mstep?: FFInt;
    thmse?: FFFloat;
    hdthr?: FFFloat;
    estim?: FFInt | "basic" | "final";
    ref?: FFBoolean;
    planes?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "bm3d", typingsInput: [], typingsOutput: ["video"] },
    inputStreams,
    merge(
    {
      "sigma": options?.sigma,
      "block": options?.block,
      "bstep": options?.bstep,
      "group": options?.group,
      "range": options?.range,
      "mstep": options?.mstep,
      "thmse": options?.thmse,
      "hdthr": options?.hdthr,
      "estim": options?.estim,
      "ref": options?.ref,
      "planes": options?.planes,
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
export function colormap(


  __default: VideoStream,

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

  const inputStreams: FilterableStream[] = [__default, _source, _target];

  const filterNode = filterNodeFactory(
    { name: "colormap", typingsInput: ["video", "video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Concatenate audio and video streams.

 *
 * @param options.n - specify the number of segments (from 1 to INT_MAX) (default 2)
 * @param options.v - specify the number of video streams (from 0 to INT_MAX) (default 1)
 * @param options.a - specify the number of audio streams (from 0 to INT_MAX) (default 0)
 * @param options.unsafe - enable unsafe mode (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#concat
 */
export function concat(

  streams: FilterableStream[],

  options?: {
    n?: FFInt;
    v?: FFInt;
    a?: FFInt;
    unsafe?: FFBoolean;
extraOptions?: Record<string, unknown>;
  },
): FilterNode {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "concat", typingsInput: [], typingsOutput: [] },
    inputStreams,
    merge(
    {
      "n": options?.n,
      "v": options?.v,
      "a": options?.a,
      "unsafe": options?.unsafe,
},
    options?.extraOptions,
  ),
  );
return filterNode;
}








/**
 * Convolve first video stream with second video stream.

 *
 * @param options.planes - set planes to convolve (from 0 to 15) (default 7)
 * @param options.impulse - when to process impulses (from 0 to 1) (default all)
 * @param options.noise - set noise (from 0 to 1) (default 1e-07)
 * @see https://ffmpeg.org/ffmpeg-filters.html#convolve
 */
export function convolve(


  _main: VideoStream,

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

  const inputStreams: FilterableStream[] = [_main, _impulse];

  const filterNode = filterNodeFactory(
    { name: "convolve", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Calculate the correlation between two video streams.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#corr
 */
export function corr(


  _main: VideoStream,

  _reference: VideoStream,


  options?: {
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams: FilterableStream[] = [_main, _reference];

  const filterNode = filterNodeFactory(
    { name: "corr", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Decimate frames (post field matching filter).

 *
 * @param options.cycle - set the number of frame from which one will be dropped (from 2 to 25) (default 5)
 * @param options.dupthresh - set duplicate threshold (from 0 to 100) (default 1.1)
 * @param options.scthresh - set scene change threshold (from 0 to 100) (default 15)
 * @param options.blockx - set the size of the x-axis blocks used during metric calculations (from 4 to 512) (default 32)
 * @param options.blocky - set the size of the y-axis blocks used during metric calculations (from 4 to 512) (default 32)
 * @param options.ppsrc - mark main input as a pre-processed input and activate clean source input stream (default false)
 * @param options.chroma - set whether or not chroma is considered in the metric calculations (default true)
 * @param options.mixed - set whether or not the input only partially contains content to be decimated (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#decimate
 */
export function decimate(

  streams: FilterableStream[],

  options?: {
    cycle?: FFInt;
    dupthresh?: FFDouble;
    scthresh?: FFDouble;
    blockx?: FFInt;
    blocky?: FFInt;
    ppsrc?: FFBoolean;
    chroma?: FFBoolean;
    mixed?: FFBoolean;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "decimate", typingsInput: [], typingsOutput: ["video"] },
    inputStreams,
    merge(
    {
      "cycle": options?.cycle,
      "dupthresh": options?.dupthresh,
      "scthresh": options?.scthresh,
      "blockx": options?.blockx,
      "blocky": options?.blocky,
      "ppsrc": options?.ppsrc,
      "chroma": options?.chroma,
      "mixed": options?.mixed,
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
export function deconvolve(


  _main: VideoStream,

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

  const inputStreams: FilterableStream[] = [_main, _impulse];

  const filterNode = filterNodeFactory(
    { name: "deconvolve", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Displace pixels.

 *
 * @param options.edge - set edge mode (from 0 to 3) (default smear)
 * @see https://ffmpeg.org/ffmpeg-filters.html#displace
 */
export function displace(


  _source: VideoStream,

  _xmap: VideoStream,

  _ymap: VideoStream,


  options?: {
    edge?: FFInt | "blank" | "smear" | "wrap" | "mirror";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams: FilterableStream[] = [_source, _xmap, _ymap];

  const filterNode = filterNodeFactory(
    { name: "displace", typingsInput: ["video", "video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Apply feedback video filter.

 *
 * @param options.x - set top left crop position (from 0 to INT_MAX) (default 0)
 * @param options.w - set crop size (from 0 to INT_MAX) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#feedback
 */
export function feedback(


  __default: VideoStream,

  _feedin: VideoStream,


  options?: {
    x?: FFInt;
    w?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): FilterNode {

  const inputStreams: FilterableStream[] = [__default, _feedin];

  const filterNode = filterNodeFactory(
    { name: "feedback", typingsInput: ["video", "video"], typingsOutput: ["video", "video"] },
    inputStreams,
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
 * Field matching for inverse telecine.

 *
 * @param options.order - specify the assumed field order (from -1 to 1) (default auto)
 * @param options.mode - set the matching mode or strategy to use (from 0 to 5) (default pc_n)
 * @param options.ppsrc - mark main input as a pre-processed input and activate clean source input stream (default false)
 * @param options.field - set the field to match from (from -1 to 1) (default auto)
 * @param options.mchroma - set whether or not chroma is included during the match comparisons (default true)
 * @param options.y0 - define an exclusion band which excludes the lines between y0 and y1 from the field matching decision (from 0 to INT_MAX) (default 0)
 * @param options.scthresh - set scene change detection threshold (from 0 to 100) (default 12)
 * @param options.combmatch - set combmatching mode (from 0 to 2) (default sc)
 * @param options.combdbg - enable comb debug (from 0 to 2) (default none)
 * @param options.cthresh - set the area combing threshold used for combed frame detection (from -1 to 255) (default 9)
 * @param options.chroma - set whether or not chroma is considered in the combed frame decision (default false)
 * @param options.blockx - set the x-axis size of the window used during combed frame detection (from 4 to 512) (default 16)
 * @param options.blocky - set the y-axis size of the window used during combed frame detection (from 4 to 512) (default 16)
 * @param options.combpel - set the number of combed pixels inside any of the blocky by blockx size blocks on the frame for the frame to be detected as combed (from 0 to INT_MAX) (default 80)
 * @see https://ffmpeg.org/ffmpeg-filters.html#fieldmatch
 */
export function fieldmatch(

  streams: FilterableStream[],

  options?: {
    order?: FFInt | "auto" | "bff" | "tff";
    mode?: FFInt | "pc" | "pc_n" | "pc_u" | "pc_n_ub" | "pcn" | "pcn_ub";
    ppsrc?: FFBoolean;
    field?: FFInt | "auto" | "bottom" | "top";
    mchroma?: FFBoolean;
    y0?: FFInt;
    scthresh?: FFDouble;
    combmatch?: FFInt | "none" | "sc" | "full";
    combdbg?: FFInt | "none" | "pcn" | "pcnub";
    cthresh?: FFInt;
    chroma?: FFBoolean;
    blockx?: FFInt;
    blocky?: FFInt;
    combpel?: FFInt;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "fieldmatch", typingsInput: [], typingsOutput: ["video"] },
    inputStreams,
    merge(
    {
      "order": options?.order,
      "mode": options?.mode,
      "ppsrc": options?.ppsrc,
      "field": options?.field,
      "mchroma": options?.mchroma,
      "y0": options?.y0,
      "scthresh": options?.scthresh,
      "combmatch": options?.combmatch,
      "combdbg": options?.combdbg,
      "cthresh": options?.cthresh,
      "chroma": options?.chroma,
      "blockx": options?.blockx,
      "blocky": options?.blocky,
      "combpel": options?.combpel,
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
export function framepack(


  _left: VideoStream,

  _right: VideoStream,


  options?: {
    format?: FFInt | "sbs" | "tab" | "frameseq" | "lines" | "columns";
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams: FilterableStream[] = [_left, _right];

  const filterNode = filterNodeFactory(
    { name: "framepack", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Freeze video frames.

 *
 * @param options.first - set first frame to freeze (from 0 to I64_MAX) (default 0)
 * @param options.last - set last frame to freeze (from 0 to I64_MAX) (default 0)
 * @param options.replace - set frame to replace (from 0 to I64_MAX) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#freezeframes
 */
export function freezeframes(


  _source: VideoStream,

  _replace: VideoStream,


  options?: {
    first?: FFInt64;
    last?: FFInt64;
    replace?: FFInt64;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams: FilterableStream[] = [_source, _replace];

  const filterNode = filterNodeFactory(
    { name: "freezeframes", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Apply Guided filter.

 *
 * @param options.radius - set the box radius (from 1 to 20) (default 3)
 * @param options.eps - set the regularization parameter (with square) (from 0 to 1) (default 0.01)
 * @param options.mode - set filtering mode (0: basic mode; 1: fast mode) (from 0 to 1) (default basic)
 * @param options.sub - subsampling ratio for fast mode (from 2 to 64) (default 4)
 * @param options.guidance - set guidance mode (0: off mode; 1: on mode) (from 0 to 1) (default off)
 * @param options.planes - set planes to filter (from 0 to 15) (default 1)
 * @see https://ffmpeg.org/ffmpeg-filters.html#guided
 */
export function guided(

  streams: FilterableStream[],

  options?: {
    radius?: FFInt;
    eps?: FFFloat;
    mode?: FFInt | "basic" | "fast";
    sub?: FFInt;
    guidance?: FFInt | "off" | "on";
    planes?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "guided", typingsInput: [], typingsOutput: ["video"] },
    inputStreams,
    merge(
    {
      "radius": options?.radius,
      "eps": options?.eps,
      "mode": options?.mode,
      "sub": options?.sub,
      "guidance": options?.guidance,
      "planes": options?.planes,
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
export function haldclut(


  _main: VideoStream,

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

  const inputStreams: FilterableStream[] = [_main, _clut];

  const filterNode = filterNodeFactory(
    { name: "haldclut", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Apply headphone binaural spatialization with HRTFs in additional streams.

 *
 * @param options.map - set channels convolution mappings
 * @param options.gain - set gain in dB (from -20 to 40) (default 0)
 * @param options.lfe - set lfe gain in dB (from -20 to 40) (default 0)
 * @param options._type - set processing (from 0 to 1) (default freq)
 * @param options.size - set frame size (from 1024 to 96000) (default 1024)
 * @param options.hrir - set hrir format (from 0 to 1) (default stereo)
 * @see https://ffmpeg.org/ffmpeg-filters.html#headphone
 */
export function headphone(

  streams: FilterableStream[],

  options?: {
    map?: FFString;
    gain?: FFFloat;
    lfe?: FFFloat;
    _type?: FFInt | "time" | "freq";
    size?: FFInt;
    hrir?: FFInt | "stereo" | "multich";
extraOptions?: Record<string, unknown>;
  },
): AudioStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "headphone", typingsInput: [], typingsOutput: ["audio"] },
    inputStreams,
    merge(
    {
      "map": options?.map,
      "gain": options?.gain,
      "lfe": options?.lfe,
      "type": options?._type,
      "size": options?.size,
      "hrir": options?.hrir,
},
    options?.extraOptions,
  ),
  );
return filterNode.audio(0) as unknown as AudioStream;
}






















/**
 * Stack video inputs horizontally.

 *
 * @param options.inputs - set number of inputs (from 2 to INT_MAX) (default 2)
 * @param options.shortest - force termination when the shortest input terminates (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#hstack
 */
export function hstack(

  streams: FilterableStream[],

  options?: {
    inputs?: FFInt;
    shortest?: FFBoolean;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "hstack", typingsInput: [], typingsOutput: ["video"] },
    inputStreams,
    merge(
    {
      "inputs": options?.inputs,
      "shortest": options?.shortest,
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
export function hysteresis(


  _base: VideoStream,

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

  const inputStreams: FilterableStream[] = [_base, _alt];

  const filterNode = filterNodeFactory(
    { name: "hysteresis", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
export function identity(


  _main: VideoStream,

  _reference: VideoStream,


  options?: {
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams: FilterableStream[] = [_main, _reference];

  const filterNode = filterNodeFactory(
    { name: "identity", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Temporally interleave video inputs.

 *
 * @param options.nb_inputs - set number of inputs (from 1 to INT_MAX) (default 2)
 * @param options.duration - how to determine the end-of-stream (from 0 to 2) (default longest)
 * @see https://ffmpeg.org/ffmpeg-filters.html#interleave_002c-ainterleave
 */
export function interleave(

  streams: FilterableStream[],

  options?: {
    nb_inputs?: FFInt;
    duration?: FFInt | "longest" | "shortest" | "first";
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "interleave", typingsInput: [], typingsOutput: ["video"] },
    inputStreams,
    merge(
    {
      "nb_inputs": options?.nb_inputs,
      "duration": options?.duration,
},
    options?.extraOptions,
  ),
  );
return filterNode.video(0) as unknown as VideoStream;
}






/**
 * Join multiple audio streams into multi-channel output.

 *
 * @param options.inputs - Number of input streams. (from 1 to INT_MAX) (default 2)
 * @param options.channel_layout - Channel layout of the output stream. (default "stereo")
 * @param options.map - A comma-separated list of channels maps in the format 'input_stream.input_channel-output_channel.
 * @see https://ffmpeg.org/ffmpeg-filters.html#join
 */
export function join(

  streams: FilterableStream[],

  options?: {
    inputs?: FFInt;
    channel_layout?: FFString;
    map?: FFString;
extraOptions?: Record<string, unknown>;
  },
): AudioStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "join", typingsInput: [], typingsOutput: ["audio"] },
    inputStreams,
    merge(
    {
      "inputs": options?.inputs,
      "channel_layout": options?.channel_layout,
      "map": options?.map,
},
    options?.extraOptions,
  ),
  );
return filterNode.audio(0) as unknown as AudioStream;
}


















/**
 * Apply filtering with limiting difference.

 *
 * @param options.threshold - set the threshold (from 0 to 1) (default 0.00392157)
 * @param options.elasticity - set the elasticity (from 0 to 10) (default 2)
 * @param options.reference - enable reference stream (default false)
 * @param options.planes - set the planes to filter (from 0 to 15) (default 15)
 * @see https://ffmpeg.org/ffmpeg-filters.html#limitdiff
 */
export function limitdiff(

  streams: FilterableStream[],

  options?: {
    threshold?: FFFloat;
    elasticity?: FFFloat;
    reference?: FFBoolean;
    planes?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "limitdiff", typingsInput: [], typingsOutput: ["video"] },
    inputStreams,
    merge(
    {
      "threshold": options?.threshold,
      "elasticity": options?.elasticity,
      "reference": options?.reference,
      "planes": options?.planes,
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
export function lut2(


  _srcx: VideoStream,

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

  const inputStreams: FilterableStream[] = [_srcx, _srcy];

  const filterNode = filterNodeFactory(
    { name: "lut2", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Clamp first stream with second stream and third stream.

 *
 * @param options.undershoot - set undershoot (from 0 to 65535) (default 0)
 * @param options.overshoot - set overshoot (from 0 to 65535) (default 0)
 * @param options.planes - set planes (from 0 to 15) (default 15)
 * @see https://ffmpeg.org/ffmpeg-filters.html#maskedclamp
 */
export function maskedclamp(


  _base: VideoStream,

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

  const inputStreams: FilterableStream[] = [_base, _dark, _bright];

  const filterNode = filterNodeFactory(
    { name: "maskedclamp", typingsInput: ["video", "video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
export function maskedmax(


  _source: VideoStream,

  _filter1: VideoStream,

  _filter2: VideoStream,


  options?: {
    planes?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams: FilterableStream[] = [_source, _filter1, _filter2];

  const filterNode = filterNodeFactory(
    { name: "maskedmax", typingsInput: ["video", "video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
export function maskedmerge(


  _base: VideoStream,

  _overlay: VideoStream,

  _mask: VideoStream,


  options?: {
    planes?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams: FilterableStream[] = [_base, _overlay, _mask];

  const filterNode = filterNodeFactory(
    { name: "maskedmerge", typingsInput: ["video", "video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
export function maskedmin(


  _source: VideoStream,

  _filter1: VideoStream,

  _filter2: VideoStream,


  options?: {
    planes?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams: FilterableStream[] = [_source, _filter1, _filter2];

  const filterNode = filterNodeFactory(
    { name: "maskedmin", typingsInput: ["video", "video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
export function maskedthreshold(


  _source: VideoStream,

  _reference: VideoStream,


  options?: {
    threshold?: FFInt;
    planes?: FFInt;
    mode?: FFInt | "abs" | "diff";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams: FilterableStream[] = [_source, _reference];

  const filterNode = filterNodeFactory(
    { name: "maskedthreshold", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Merge planes.

 *
 * @param options.mapping - set input to output plane mapping (from -1 to 8.58993e+08) (default -1)
 * @param options.format - set output pixel format (default yuva444p)
 * @param options.map0s - set 1st input to output stream mapping (from 0 to 3) (default 0)
 * @param options.map0p - set 1st input to output plane mapping (from 0 to 3) (default 0)
 * @param options.map1s - set 2nd input to output stream mapping (from 0 to 3) (default 0)
 * @param options.map1p - set 2nd input to output plane mapping (from 0 to 3) (default 0)
 * @param options.map2s - set 3rd input to output stream mapping (from 0 to 3) (default 0)
 * @param options.map2p - set 3rd input to output plane mapping (from 0 to 3) (default 0)
 * @param options.map3s - set 4th input to output stream mapping (from 0 to 3) (default 0)
 * @param options.map3p - set 4th input to output plane mapping (from 0 to 3) (default 0)
 * @see https://ffmpeg.org/ffmpeg-filters.html#mergeplanes
 */
export function mergeplanes(

  streams: FilterableStream[],

  options?: {
    mapping?: FFInt;
    format?: FFPixFmt;
    map0s?: FFInt;
    map0p?: FFInt;
    map1s?: FFInt;
    map1p?: FFInt;
    map2s?: FFInt;
    map2p?: FFInt;
    map3s?: FFInt;
    map3p?: FFInt;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "mergeplanes", typingsInput: [], typingsOutput: ["video"] },
    inputStreams,
    merge(
    {
      "mapping": options?.mapping,
      "format": options?.format,
      "map0s": options?.map0s,
      "map0p": options?.map0p,
      "map1s": options?.map1s,
      "map1p": options?.map1p,
      "map2s": options?.map2s,
      "map2p": options?.map2p,
      "map3s": options?.map3s,
      "map3p": options?.map3p,
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
export function midequalizer(


  _in0: VideoStream,

  _in1: VideoStream,


  options?: {
    planes?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams: FilterableStream[] = [_in0, _in1];

  const filterNode = filterNodeFactory(
    { name: "midequalizer", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Mix video inputs.

 *
 * @param options.inputs - set number of inputs (from 2 to 32767) (default 2)
 * @param options.weights - set weight for each input (default "1 1")
 * @param options.scale - set scale (from 0 to 32767) (default 0)
 * @param options.planes - set what planes to filter (default F)
 * @param options.duration - how to determine end of stream (from 0 to 2) (default longest)
 * @see https://ffmpeg.org/ffmpeg-filters.html#mix
 */
export function mix(

  streams: FilterableStream[],

  options?: {
    inputs?: FFInt;
    weights?: FFString;
    scale?: FFFloat;
    planes?: FFFlags;
    duration?: FFInt | "longest" | "shortest" | "first";
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "mix", typingsInput: [], typingsOutput: ["video"] },
    inputStreams,
    merge(
    {
      "inputs": options?.inputs,
      "weights": options?.weights,
      "scale": options?.scale,
      "planes": options?.planes,
      "duration": options?.duration,
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
export function morpho(


  __default: VideoStream,

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

  const inputStreams: FilterableStream[] = [__default, _structure];

  const filterNode = filterNodeFactory(
    { name: "morpho", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Calculate the MSAD between two video streams.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#msad
 */
export function msad(


  _main: VideoStream,

  _reference: VideoStream,


  options?: {
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams: FilterableStream[] = [_main, _reference];

  const filterNode = filterNodeFactory(
    { name: "msad", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
export function multiply(


  _source: VideoStream,

  _factor: VideoStream,


  options?: {
    scale?: FFFloat;
    offset?: FFFloat;
    planes?: FFFlags;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams: FilterableStream[] = [_source, _factor];

  const filterNode = filterNodeFactory(
    { name: "multiply", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
export function overlay(


  _main: VideoStream,

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

  const inputStreams: FilterableStream[] = [_main, _overlay];

  const filterNode = filterNodeFactory(
    { name: "overlay", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
export function paletteuse(


  __default: VideoStream,

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

  const inputStreams: FilterableStream[] = [__default, _palette];

  const filterNode = filterNodeFactory(
    { name: "paletteuse", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * PreMultiply first stream with first plane of second stream.

 *
 * @param options.planes - set planes (from 0 to 15) (default 15)
 * @param options.inplace - enable inplace mode (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#premultiply
 */
export function premultiply(

  streams: FilterableStream[],

  options?: {
    planes?: FFInt;
    inplace?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "premultiply", typingsInput: [], typingsOutput: ["video"] },
    inputStreams,
    merge(
    {
      "planes": options?.planes,
      "inplace": options?.inplace,
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
export function psnr(


  _main: VideoStream,

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

  const inputStreams: FilterableStream[] = [_main, _reference];

  const filterNode = filterNodeFactory(
    { name: "psnr", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Remap pixels.

 *
 * @param options.format - set output format (from 0 to 1) (default color)
 * @param options.fill - set the color of the unmapped pixels (default "black")
 * @see https://ffmpeg.org/ffmpeg-filters.html#remap
 */
export function remap(


  _source: VideoStream,

  _xmap: VideoStream,

  _ymap: VideoStream,


  options?: {
    format?: FFInt | "color" | "gray";
    fill?: FFColor;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams: FilterableStream[] = [_source, _xmap, _ymap];

  const filterNode = filterNodeFactory(
    { name: "remap", typingsInput: ["video", "video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
export function sidechaincompress(


  _main: AudioStream,

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

  const inputStreams: FilterableStream[] = [_main, _sidechain];

  const filterNode = filterNodeFactory(
    { name: "sidechaincompress", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
    inputStreams,
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
export function sidechaingate(


  _main: AudioStream,

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

  const inputStreams: FilterableStream[] = [_main, _sidechain];

  const filterNode = filterNodeFactory(
    { name: "sidechaingate", typingsInput: ["audio", "audio"], typingsOutput: ["audio"] },
    inputStreams,
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
 * Calculate the MPEG-7 video signature

 *
 * @param options.detectmode - set the detectmode (from 0 to 2) (default off)
 * @param options.nb_inputs - number of inputs (from 1 to INT_MAX) (default 1)
 * @param options.filename - filename for output files (default "")
 * @param options.format - set output format (from 0 to 1) (default binary)
 * @param options.th_d - threshold to detect one word as similar (from 1 to INT_MAX) (default 9000)
 * @param options.th_dc - threshold to detect all words as similar (from 1 to INT_MAX) (default 60000)
 * @param options.th_xh - threshold to detect frames as similar (from 1 to INT_MAX) (default 116)
 * @param options.th_di - minimum length of matching sequence in frames (from 0 to INT_MAX) (default 0)
 * @param options.th_it - threshold for relation of good to all frames (from 0 to 1) (default 0.5)
 * @see https://ffmpeg.org/ffmpeg-filters.html#signature
 */
export function signature(

  streams: FilterableStream[],

  options?: {
    detectmode?: FFInt | "off" | "full" | "fast";
    nb_inputs?: FFInt;
    filename?: FFString;
    format?: FFInt | "binary" | "xml";
    th_d?: FFInt;
    th_dc?: FFInt;
    th_xh?: FFInt;
    th_di?: FFInt;
    th_it?: FFDouble;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "signature", typingsInput: [], typingsOutput: ["video"] },
    inputStreams,
    merge(
    {
      "detectmode": options?.detectmode,
      "nb_inputs": options?.nb_inputs,
      "filename": options?.filename,
      "format": options?.format,
      "th_d": options?.th_d,
      "th_dc": options?.th_dc,
      "th_xh": options?.th_xh,
      "th_di": options?.th_di,
      "th_it": options?.th_it,
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
export function spectrumsynth(


  _magnitude: VideoStream,

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

  const inputStreams: FilterableStream[] = [_magnitude, _phase];

  const filterNode = filterNodeFactory(
    { name: "spectrumsynth", typingsInput: ["video", "video"], typingsOutput: ["audio"] },
    inputStreams,
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
 * Calculate the SSIM between two video streams.

 *
 * @param options.stats_file - Set file where to store per-frame difference information
 * @see https://ffmpeg.org/ffmpeg-filters.html#ssim
 */
export function ssim(


  _main: VideoStream,

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

  const inputStreams: FilterableStream[] = [_main, _reference];

  const filterNode = filterNodeFactory(
    { name: "ssim", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Select video streams

 *
 * @param options.inputs - number of input streams (from 2 to INT_MAX) (default 2)
 * @param options.map - input indexes to remap to outputs
 * @see https://ffmpeg.org/ffmpeg-filters.html#streamselect_002c-astreamselect
 */
export function streamselect(

  streams: FilterableStream[],

  options?: {
    inputs?: FFInt;
    map?: FFString;
extraOptions?: Record<string, unknown>;
  },
): FilterNode {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "streamselect", typingsInput: [], typingsOutput: [] },
    inputStreams,
    merge(
    {
      "inputs": options?.inputs,
      "map": options?.map,
},
    options?.extraOptions,
  ),
  );
return filterNode;
}


























/**
 * Threshold first video stream using other video streams.

 *
 * @param options.planes - set planes to filter (from 0 to 15) (default 15)
 * @see https://ffmpeg.org/ffmpeg-filters.html#threshold
 */
export function threshold(


  __default: VideoStream,

  _threshold: VideoStream,

  _min: VideoStream,

  _max: VideoStream,


  options?: {
    planes?: FFInt;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams: FilterableStream[] = [__default, _threshold, _min, _max];

  const filterNode = filterNodeFactory(
    { name: "threshold", typingsInput: ["video", "video", "video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * UnPreMultiply first stream with first plane of second stream.

 *
 * @param options.planes - set planes (from 0 to 15) (default 15)
 * @param options.inplace - enable inplace mode (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#unpremultiply
 */
export function unpremultiply(

  streams: FilterableStream[],

  options?: {
    planes?: FFInt;
    inplace?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "unpremultiply", typingsInput: [], typingsOutput: ["video"] },
    inputStreams,
    merge(
    {
      "planes": options?.planes,
      "inplace": options?.inplace,
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
export function varblur(


  __default: VideoStream,

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

  const inputStreams: FilterableStream[] = [__default, _radius];

  const filterNode = filterNodeFactory(
    { name: "varblur", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Calculate the VIF between two video streams.

 *
 * @see https://ffmpeg.org/ffmpeg-filters.html#vif
 */
export function vif(


  _main: VideoStream,

  _reference: VideoStream,


  options?: {
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams: FilterableStream[] = [_main, _reference];

  const filterNode = filterNodeFactory(
    { name: "vif", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Stack video inputs vertically.

 *
 * @param options.inputs - set number of inputs (from 2 to INT_MAX) (default 2)
 * @param options.shortest - force termination when the shortest input terminates (default false)
 * @see https://ffmpeg.org/ffmpeg-filters.html#vstack
 */
export function vstack(

  streams: FilterableStream[],

  options?: {
    inputs?: FFInt;
    shortest?: FFBoolean;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "vstack", typingsInput: [], typingsOutput: ["video"] },
    inputStreams,
    merge(
    {
      "inputs": options?.inputs,
      "shortest": options?.shortest,
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
export function xcorrelate(


  _primary: VideoStream,

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

  const inputStreams: FilterableStream[] = [_primary, _secondary];

  const filterNode = filterNodeFactory(
    { name: "xcorrelate", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
export function xfade(


  _main: VideoStream,

  _xfade: VideoStream,


  options?: {
    transition?: FFInt | "custom" | "fade" | "wipeleft" | "wiperight" | "wipeup" | "wipedown" | "slideleft" | "slideright" | "slideup" | "slidedown" | "circlecrop" | "rectcrop" | "distance" | "fadeblack" | "fadewhite" | "radial" | "smoothleft" | "smoothright" | "smoothup" | "smoothdown" | "circleopen" | "circleclose" | "vertopen" | "vertclose" | "horzopen" | "horzclose" | "dissolve" | "pixelize" | "diagtl" | "diagtr" | "diagbl" | "diagbr" | "hlslice" | "hrslice" | "vuslice" | "vdslice" | "hblur" | "fadegrays" | "wipetl" | "wipetr" | "wipebl" | "wipebr" | "squeezeh" | "squeezev" | "zoomin" | "fadefast" | "fadeslow" | "hlwind" | "hrwind" | "vuwind" | "vdwind" | "coverleft" | "coverright" | "coverup" | "coverdown" | "revealleft" | "revealright" | "revealup" | "revealdown";
    duration?: FFDuration;
    offset?: FFDuration;
    expr?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams: FilterableStream[] = [_main, _xfade];

  const filterNode = filterNodeFactory(
    { name: "xfade", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Pick median pixels from several video inputs.

 *
 * @param options.inputs - set number of inputs (from 3 to 255) (default 3)
 * @param options.planes - set planes to filter (from 0 to 15) (default 15)
 * @param options.percentile - set percentile (from 0 to 1) (default 0.5)
 * @see https://ffmpeg.org/ffmpeg-filters.html#xmedian
 */
export function xmedian(

  streams: FilterableStream[],

  options?: {
    inputs?: FFInt;
    planes?: FFInt;
    percentile?: FFFloat;
    eofAction?: FFString;
    shortest?: FFBoolean;
    repeatlast?: FFBoolean;
    enable?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "xmedian", typingsInput: [], typingsOutput: ["video"] },
    inputStreams,
    merge(
    {
      "inputs": options?.inputs,
      "planes": options?.planes,
      "percentile": options?.percentile,
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
 * Calculate the extended perceptually weighted peak signal-to-noise ratio (XPSNR) between two video streams.

 *
 * @param options.stats_file - Set file where to store per-frame XPSNR information
 * @see https://ffmpeg.org/ffmpeg-filters.html#xpsnr
 */
export function xpsnr(


  _main: VideoStream,

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

  const inputStreams: FilterableStream[] = [_main, _reference];

  const filterNode = filterNodeFactory(
    { name: "xpsnr", typingsInput: ["video", "video"], typingsOutput: ["video"] },
    inputStreams,
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
 * Stack video inputs into custom layout.

 *
 * @param options.inputs - set number of inputs (from 2 to INT_MAX) (default 2)
 * @param options.layout - set custom layout
 * @param options.grid - set fixed size grid layout
 * @param options.shortest - force termination when the shortest input terminates (default false)
 * @param options.fill - set the color for unused pixels (default "none")
 * @see https://ffmpeg.org/ffmpeg-filters.html#xstack
 */
export function xstack(

  streams: FilterableStream[],

  options?: {
    inputs?: FFInt;
    layout?: FFString;
    grid?: FFImageSize;
    shortest?: FFBoolean;
    fill?: FFString;
extraOptions?: Record<string, unknown>;
  },
): VideoStream {

  const inputStreams = streams;

  const filterNode = filterNodeFactory(
    { name: "xstack", typingsInput: [], typingsOutput: ["video"] },
    inputStreams,
    merge(
    {
      "inputs": options?.inputs,
      "layout": options?.layout,
      "grid": options?.grid,
      "shortest": options?.shortest,
      "fill": options?.fill,
},
    options?.extraOptions,
  ),
  );
return filterNode.video(0) as unknown as VideoStream;
}











