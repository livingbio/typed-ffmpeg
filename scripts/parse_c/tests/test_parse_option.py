import pytest
from syrupy.assertion import SnapshotAssertion
from syrupy.extensions.json import JSONSnapshotExtension

from ..parse_option import parse_option_str


@pytest.mark.parametrize(
    "text",
    [
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
def parse_option_str(snapshot: SnapshotAssertion, text: str) -> None:
    assert snapshot(extension_class=JSONSnapshotExtension) == parse_option_str(text)