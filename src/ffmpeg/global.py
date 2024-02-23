from .dag.nodes import InputNode
from .schema import _to_tuple
from .streams.av import AVStream


def input(
    filename: str,
    *,
    loglevel: str,
    v: str,
    report: bool,
    max_alloc: str,
    cpuflags: str,
    cpucount: str,
    hide_banner: bool,
    y: bool,
    n: bool,
    ignore_unknown: bool,
    copy_unknown: bool,
    recast_media: bool,
    benchmark: bool,
    benchmark_all: bool,
    progress: str,
    stdin: bool,
    timelimit: str,
    dump: bool,
    hex: bool,
    vsync: str,
    frame_drop_threshold: float,
    adrift_threshold: str,
    copyts: bool,
    start_at_zero: bool,
    copytb: int,
    dts_delta_threshold: float,
    dts_error_threshold: float,
    xerror: bool,
    abort_on: str,
    filter_threads: str,
    filter_complex: str,
    filter_complex_threads: int,
    lavfi: str,
    filter_complex_script: str,
    auto_conversion_filters: bool,
    stats: bool,
    stats_period: str,
    debug_ts: bool,
    max_error_rate: float,
    psnr: bool,
    vstats: bool,
    vstats_file: str,
    vstats_version: int,
    qphist: bool,
    init_hw_device: str,
    filter_hw_device: str,
    **kwargs: int | str | bool | float
) -> AVStream:
    """
    Input file URL (ffmpeg `-i` option)

    Args:
        filename: Input file URL
        loglevel: set logging level
        v: set logging level
        report: generate a report
        max_alloc: set maximum size of a single allocated block
        cpuflags: force specific cpu flags
        cpucount: force specific cpu count
        hide_banner: do not show program banner
        y: overwrite output files
        n: never overwrite output files
        ignore_unknown: Ignore unknown stream types
        copy_unknown: Copy unknown stream types
        recast_media: allow recasting stream type in order to force a decoder of different media type
        benchmark: add timings for benchmarking
        benchmark_all: add timings for each task
        progress: write program-readable progress information
        stdin: enable or disable interaction on standard input
        timelimit: set max runtime in seconds in CPU user time
        dump: dump each input packet
        hex: when dumping packets, also dump the payload
        vsync: set video sync method globally; deprecated, use -fps_mode
        frame_drop_threshold: frame drop threshold
        adrift_threshold: deprecated, does nothing
        copyts: copy timestamps
        start_at_zero: shift input timestamps to start at 0 when using copyts
        copytb: copy input stream time base when stream copying
        dts_delta_threshold: timestamp discontinuity delta threshold
        dts_error_threshold: timestamp error delta threshold
        xerror: exit on error
        abort_on: abort on the specified condition flags
        filter_threads: number of non-complex filter threads
        filter_complex: create a complex filtergraph
        filter_complex_threads: number of threads for -filter_complex
        lavfi: create a complex filtergraph
        filter_complex_script: read complex filtergraph description from a file
        auto_conversion_filters: enable automatic conversion filters globally
        stats: print progress report during encoding
        stats_period: set the period at which ffmpeg updates stats and -progress output
        debug_ts: print timestamp debugging info
        max_error_rate: ratio of decoding errors (0.0: no errors, 1.0: 100% errors) above which ffmpeg returns an error instead of success.
        psnr: calculate PSNR of compressed frames (deprecated, use -flags +psnr)
        vstats: dump video coding statistics to file
        vstats_file: dump video coding statistics to file
        vstats_version: Version of the vstats format to use.
        qphist: deprecated, does nothing
        init_hw_device: initialise hardware device
        filter_hw_device: set hardware device used when filtering
        **kwargs: Additional options

    Returns:
        Input stream

    Examples:
    ```py
    >>> input("input.mp4")
    <AVStream: input.mp4>
    ```
    """
    vv: dict[str, int | float | str | bool] = {
        "loglevel": loglevel,
        "v": v,
        "report": report,
        "max_alloc": max_alloc,
        "cpuflags": cpuflags,
        "cpucount": cpucount,
        "hide_banner": hide_banner,
        "y": y,
        "n": n,
        "ignore_unknown": ignore_unknown,
        "copy_unknown": copy_unknown,
        "recast_media": recast_media,
        "benchmark": benchmark,
        "benchmark_all": benchmark_all,
        "progress": progress,
        "stdin": stdin,
        "timelimit": timelimit,
        "dump": dump,
        "hex": hex,
        "vsync": vsync,
        "frame_drop_threshold": frame_drop_threshold,
        "adrift_threshold": adrift_threshold,
        "copyts": copyts,
        "start_at_zero": start_at_zero,
        "copytb": copytb,
        "dts_delta_threshold": dts_delta_threshold,
        "dts_error_threshold": dts_error_threshold,
        "xerror": xerror,
        "abort_on": abort_on,
        "filter_threads": filter_threads,
        "filter_complex": filter_complex,
        "filter_complex_threads": filter_complex_threads,
        "lavfi": lavfi,
        "filter_complex_script": filter_complex_script,
        "auto_conversion_filters": auto_conversion_filters,
        "stats": stats,
        "stats_period": stats_period,
        "debug_ts": debug_ts,
        "max_error_rate": max_error_rate,
        "psnr": psnr,
        "vstats": vstats,
        "vstats_file": vstats_file,
        "vstats_version": vstats_version,
        "qphist": qphist,
        "init_hw_device": init_hw_device,
        "filter_hw_device": filter_hw_device,
    }
    return InputNode(
        filename=filename,
        kwargs=_to_tuple(vv | kwargs),
    ).stream()
