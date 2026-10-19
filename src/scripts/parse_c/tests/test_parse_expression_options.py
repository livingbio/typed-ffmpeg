from pathlib import Path

from ..parse_expression_options import (
    extract_expression_options,
    parse_expression_options,
)

DRAWBOX = r"""
typedef struct DrawBoxContext {
    char *x_expr, *y_expr;
    char *w_expr, *h_expr;
    char *color_str;
} DrawBoxContext;

#define OFFSET(x) offsetof(DrawBoxContext, x)
static const AVOption drawbox_options[] = {
    { "x",      "set horizontal position of the left box edge", OFFSET(x_expr), AV_OPT_TYPE_STRING, { .str="0" }, 0, 0, FLAGS },
    { "y",      "set vertical position of the top box edge",    OFFSET(y_expr), AV_OPT_TYPE_STRING, { .str="0" }, 0, 0, FLAGS },
    { "width",  "set width of the box",                         OFFSET(w_expr), AV_OPT_TYPE_STRING, { .str="0" }, 0, 0, FLAGS },
    { "w",      "set width of the box",                         OFFSET(w_expr), AV_OPT_TYPE_STRING, { .str="0" }, 0, 0, FLAGS },
    { "color",  "set color of the box",                         OFFSET(color_str), AV_OPT_TYPE_STRING, { .str="black" }, 0, 0, FLAGS },
    { "thickness", "set the box thickness",                     OFFSET(thickness), AV_OPT_TYPE_INT, { .i64=3 }, 0, INT_MAX, FLAGS },
    { NULL }
};

static int config_input(AVFilterLink *inlink)
{
    DrawBoxContext *s = inlink->dst->priv;
    double res;
    /* evaluate expressions, fail on last iteration */
    av_expr_parse_and_eval(&res, s->x_expr,
                           var_names, s->var_values,
                           NULL, NULL, NULL, NULL, NULL, 0, ctx);
    av_expr_parse_and_eval(&res, s->w_expr, var_names, s->var_values,
                           NULL, NULL, NULL, NULL, NULL, 0, ctx);
    av_parse_color(s->rgba_color, s->color_str, -1, ctx);
    return 0;
}

const FFFilter ff_vf_drawbox = {
    .p.name        = "drawbox",
    .p.description = NULL_IF_CONFIG_SMALL("Draw a colored box on the input video."),
};
"""


def test_parse_expression_options_direct_call() -> None:
    names, options = parse_expression_options(DRAWBOX)
    assert names == {"drawbox"}
    # aliases sharing a field are both expressions; y is never parsed here
    assert options == {"x", "width", "w"}


def test_parse_expression_options_helper_and_array_field() -> None:
    text = r"""
#define OFFSET(x) offsetof(GEQContext, x)
static const AVOption geq_options[] = {
    { "lum_expr", "set luminance expression", OFFSET(expr_str[Y]), AV_OPT_TYPE_STRING, {.str=NULL}, 0, 0, FLAGS },
    { "x",        "set x",                    OFFSET(x_str),       AV_OPT_TYPE_STRING, {.str=NULL}, 0, 0, FLAGS },
    { NULL },
};

static int set_expr(AVExpr **pexpr, const char *expr, AVFilterContext *ctx)
{
    return av_expr_parse(pexpr, expr, var_names, NULL, NULL, NULL, NULL, 0, ctx);
}

static av_cold int geq_init(AVFilterContext *ctx)
{
    GEQContext *geq = ctx->priv;
    for (int plane = 0; plane < 4; plane++)
        set_expr(&geq->e[plane], geq->expr_str[plane], ctx);
    return 0;
}
"""
    assert parse_expression_options(text)[1] == {"lum_expr"}


def test_parse_expression_options_token_pasting_macro() -> None:
    text = r"""
static const AVOption rotate_options[] = {
    { "out_w", "set output width expression",  OFFSET(outw_expr_str), AV_OPT_TYPE_STRING, {.str="iw"}, 0, 0, FLAGS },
    { "out_h", "set output height expression", OFFSET(outh_expr_str), AV_OPT_TYPE_STRING, {.str="ih"}, 0, 0, FLAGS },
    { "fillcolor", "set background fill color", OFFSET(fillcolor_str), AV_OPT_TYPE_STRING, {.str="black"}, 0, 0, FLAGS },
    { NULL }
};

#define SET_SIZE_EXPR(name, opt_name) do {                                         \
    ret = av_expr_parse_and_eval(&res, expr = rot->name##_expr_str,                \
                                 var_names, rot->var_values,                       \
                                 NULL, NULL, NULL, NULL, rot, 0, ctx);             \
} while (0)

static int config_props(AVFilterLink *outlink)
{
    SET_SIZE_EXPR(outh, "out_h");
    SET_SIZE_EXPR(outw, "out_w");
    return 0;
}
"""
    assert parse_expression_options(text)[1] == {"out_w", "out_h"}


def test_extract_expression_options(tmp_path: Path) -> None:
    libavfilter = tmp_path / "libavfilter"
    libavfilter.mkdir()
    (libavfilter / "vf_drawbox.c").write_text(DRAWBOX)
    (libavfilter / "vf_null.c").write_text(
        'const FFFilter ff_vf_null = { .p.name = "null" };'
    )

    # unknown filter names (e.g. pad names like "default") are dropped
    assert extract_expression_options(tmp_path, {"drawbox", "null"}) == {
        "drawbox": ["w", "width", "x"]
    }
