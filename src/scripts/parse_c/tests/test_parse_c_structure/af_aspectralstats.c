{
    { "win_size", "set the window size", OFFSET(win_size), AV_OPT_TYPE_INT, {.i64=2048}, 32, 65536, A },
    { win_func, "set window function", OFFSET(win_func), AV_OPT_TYPE_INT, {.i64 = WFUNC_HANNING}, 0, NB_WFUNC-1, A, "win_func" },
{ "rect",     "Rectangular",      0, AV_OPT_TYPE_CONST, {.i64=WFUNC_RECT},     0, 0, A, "win_func" },
{ "bartlett", "Bartlett",         0, AV_OPT_TYPE_CONST, {.i64=WFUNC_BARTLETT}, 0, 0, A, "win_func" },
{ "hann",     "Hann",             0, AV_OPT_TYPE_CONST, {.i64=WFUNC_HANNING},  0, 0, A, "win_func" },
{ "hanning",  "Hanning",          0, AV_OPT_TYPE_CONST, {.i64=WFUNC_HANNING},  0, 0, A, "win_func" },
{ "hamming",  "Hamming",          0, AV_OPT_TYPE_CONST, {.i64=WFUNC_HAMMING},  0, 0, A, "win_func" },
{ "blackman", "Blackman",         0, AV_OPT_TYPE_CONST, {.i64=WFUNC_BLACKMAN}, 0, 0, A, "win_func" },
{ "welch",    "Welch",            0, AV_OPT_TYPE_CONST, {.i64=WFUNC_WELCH},    0, 0, A, "win_func" },
{ "flattop",  "Flat-top",         0, AV_OPT_TYPE_CONST, {.i64=WFUNC_FLATTOP},  0, 0, A, "win_func" },
{ "bharris",  "Blackman-Harris",  0, AV_OPT_TYPE_CONST, {.i64=WFUNC_BHARRIS},  0, 0, A, "win_func" },
{ "bnuttall", "Blackman-Nuttall", 0, AV_OPT_TYPE_CONST, {.i64=WFUNC_BNUTTALL}, 0, 0, A, "win_func" },
{ "bhann",    "Bartlett-Hann",    0, AV_OPT_TYPE_CONST, {.i64=WFUNC_BHANN},    0, 0, A, "win_func" },
{ "sine",     "Sine",             0, AV_OPT_TYPE_CONST, {.i64=WFUNC_SINE},     0, 0, A, "win_func" },
{ "nuttall",  "Nuttall",          0, AV_OPT_TYPE_CONST, {.i64=WFUNC_NUTTALL},  0, 0, A, "win_func" },
{ "lanczos",  "Lanczos",          0, AV_OPT_TYPE_CONST, {.i64=WFUNC_LANCZOS},  0, 0, A, "win_func" },
{ "gauss",    "Gauss",            0, AV_OPT_TYPE_CONST, {.i64=WFUNC_GAUSS},    0, 0, A, "win_func" },
{ "tukey",    "Tukey",            0, AV_OPT_TYPE_CONST, {.i64=WFUNC_TUKEY},    0, 0, A, "win_func" },
{ "dolph",    "Dolph-Chebyshev",  0, AV_OPT_TYPE_CONST, {.i64=WFUNC_DOLPH},    0, 0, A, "win_func" },
{ "cauchy",   "Cauchy",           0, AV_OPT_TYPE_CONST, {.i64=WFUNC_CAUCHY},   0, 0, A, "win_func" },
{ "parzen",   "Parzen",           0, AV_OPT_TYPE_CONST, {.i64=WFUNC_PARZEN},   0, 0, A, "win_func" },
{ "poisson",  "Poisson",          0, AV_OPT_TYPE_CONST, {.i64=WFUNC_POISSON},  0, 0, A, "win_func" },
{ "bohman",   "Bohman",           0, AV_OPT_TYPE_CONST, {.i64=WFUNC_BOHMAN},   0, 0, A, "win_func" },
{ "kaiser",   "Kaiser",           0, AV_OPT_TYPE_CONST, {.i64=WFUNC_KAISER},   0, 0, A, "win_func" },
    { "overlap", "set window overlap", OFFSET(overlap), AV_OPT_TYPE_FLOAT, {.dbl=0.5}, 0,  1, A },
    { "measure", "select the parameters which are measured", OFFSET(measure), AV_OPT_TYPE_FLAGS, {.i64=MEASURE_ALL}, 0, UINT_MAX, A, "measure" },
    { "none",     "", 0, AV_OPT_TYPE_CONST, {.i64=MEASURE_NONE    }, 0, 0, A, "measure" },
    { "all",      "", 0, AV_OPT_TYPE_CONST, {.i64=MEASURE_ALL     }, 0, 0, A, "measure" },
    { "mean",     "", 0, AV_OPT_TYPE_CONST, {.i64=MEASURE_MEAN    }, 0, 0, A, "measure" },
    { "variance", "", 0, AV_OPT_TYPE_CONST, {.i64=MEASURE_VARIANCE}, 0, 0, A, "measure" },
    { "centroid", "", 0, AV_OPT_TYPE_CONST, {.i64=MEASURE_CENTROID}, 0, 0, A, "measure" },
    { "spread",   "", 0, AV_OPT_TYPE_CONST, {.i64=MEASURE_SPREAD  }, 0, 0, A, "measure" },
    { "skewness", "", 0, AV_OPT_TYPE_CONST, {.i64=MEASURE_SKEWNESS}, 0, 0, A, "measure" },
    { "kurtosis", "", 0, AV_OPT_TYPE_CONST, {.i64=MEASURE_KURTOSIS}, 0, 0, A, "measure" },
    { "entropy",  "", 0, AV_OPT_TYPE_CONST, {.i64=MEASURE_ENTROPY }, 0, 0, A, "measure" },
    { "flatness", "", 0, AV_OPT_TYPE_CONST, {.i64=MEASURE_FLATNESS}, 0, 0, A, "measure" },
    { "crest",    "", 0, AV_OPT_TYPE_CONST, {.i64=MEASURE_CREST   }, 0, 0, A, "measure" },
    { "flux",     "", 0, AV_OPT_TYPE_CONST, {.i64=MEASURE_FLUX    }, 0, 0, A, "measure" },
    { "slope",    "", 0, AV_OPT_TYPE_CONST, {.i64=MEASURE_SLOPE   }, 0, 0, A, "measure" },
    { "decrease", "", 0, AV_OPT_TYPE_CONST, {.i64=MEASURE_DECREASE}, 0, 0, A, "measure" },
    { "rolloff",  "", 0, AV_OPT_TYPE_CONST, {.i64=MEASURE_ROLLOFF }, 0, 0, A, "measure" },
    { NULL }
}
