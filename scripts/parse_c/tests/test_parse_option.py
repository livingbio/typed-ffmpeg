import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..parse_option import parse_av_option, parse_option_str


@pytest.mark.parametrize(
    "text",
    [
        pytest.param(
            """
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
}""",
            id="libavfilter/af_aspectralstats.c",
        ),
        pytest.param(
            """
    {
    {
        "derive_device", "Derive a new device of this type",
        OFFSET(device_type), AV_OPT_TYPE_STRING,
        { .str = NULL }, 0, 0, FLAGS
    },
    {
        NULL
    }
    }""",
            id="libavfilter/vf_hwupload.c",
        ),
        pytest.param(
            """{
    { "split", "set split frequencies", OFFSET(splits_str), AV_OPT_TYPE_STRING, {.str="500"}, 0, 0, AF },
    { "order", "set filter order",      OFFSET(order_opt),  AV_OPT_TYPE_INT,    {.i64=1},     0, 9, AF, "m" },
    { "2nd",   "2nd order (12 dB/8ve)", 0,                  AV_OPT_TYPE_CONST,  {.i64=0},     0, 0, AF, "m" },
    { "4th",   "4th order (24 dB/8ve)", 0,                  AV_OPT_TYPE_CONST,  {.i64=1},     0, 0, AF, "m" },
    { "6th",   "6th order (36 dB/8ve)", 0,                  AV_OPT_TYPE_CONST,  {.i64=2},     0, 0, AF, "m" },
    { "8th",   "8th order (48 dB/8ve)", 0,                  AV_OPT_TYPE_CONST,  {.i64=3},     0, 0, AF, "m" },
    { "10th",  "10th order (60 dB/8ve)",0,                  AV_OPT_TYPE_CONST,  {.i64=4},     0, 0, AF, "m" },
    { "12th",  "12th order (72 dB/8ve)",0,                  AV_OPT_TYPE_CONST,  {.i64=5},     0, 0, AF, "m" },
    { "14th",  "14th order (84 dB/8ve)",0,                  AV_OPT_TYPE_CONST,  {.i64=6},     0, 0, AF, "m" },
    { "16th",  "16th order (96 dB/8ve)",0,                  AV_OPT_TYPE_CONST,  {.i64=7},     0, 0, AF, "m" },
    { "18th",  "18th order (108 dB/8ve)",0,                 AV_OPT_TYPE_CONST,  {.i64=8},     0, 0, AF, "m" },
    { "20th",  "20th order (120 dB/8ve)",0,                 AV_OPT_TYPE_CONST,  {.i64=9},     0, 0, AF, "m" },
    { "level", "set input gain",        OFFSET(level_in),   AV_OPT_TYPE_FLOAT,  {.dbl=1},     0, 1, AF },
    { "gain",  "set output bands gain", OFFSET(gains_str),  AV_OPT_TYPE_STRING, {.str="1.f"}, 0, 0, AF },
    { "precision",  "set processing precision", OFFSET(precision),   AV_OPT_TYPE_INT,   {.i64=0}, 0, 2, AF, "precision" },
    {  "auto",  "set auto processing precision",                  0, AV_OPT_TYPE_CONST, {.i64=0}, 0, 0, AF, "precision" },
    {  "float", "set single-floating point processing precision", 0, AV_OPT_TYPE_CONST, {.i64=1}, 0, 0, AF, "precision" },
    {  "double","set double-floating point processing precision", 0, AV_OPT_TYPE_CONST, {.i64=2}, 0, 0, AF, "precision" },
    { NULL }
}""",
            id="libavfilter/af_acrossover.c",
        ),
    ],
)
def test_parse_option(snapshot: SnapshotAssertion, text: str) -> None:
    assert snapshot(extension_class=JSONSnapshotExtension) == parse_option_str(text)
    assert snapshot(extension_class=JSONSnapshotExtension) == parse_av_option(text)
