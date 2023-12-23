{
    .name          = "tblend",
    .description   = NULL_IF_CONFIG_SMALL("Blend successive frames."),
    .priv_size     = sizeof(BlendContext),
    .priv_class    = &tblend_class,
    .init          = init,
    .uninit        = uninit,
    FILTER_INPUTS(tblend_inputs),
    FILTER_OUTPUTS(blend_outputs),
    FILTER_PIXFMTS_ARRAY(pix_fmts),
    .flags         = AVFILTER_FLAG_SUPPORT_TIMELINE_INTERNAL | AVFILTER_FLAG_SLICE_THREADS,
    .process_command = process_command,
}
