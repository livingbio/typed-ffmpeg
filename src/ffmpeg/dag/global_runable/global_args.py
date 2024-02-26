from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..nodes import GlobalNode, GlobalStream, OutputStream


class GlobalArgs(ABC):
    @abstractmethod
    def _global_node(self, *streams: OutputStream, **kwargs: Any) -> GlobalNode:
        ...

    def global_args(
        self,
        *,
        loglevel: str = None,
        v: str = None,
        report: bool = None,
        max_alloc: str = None,
        cpuflags: str = None,
        cpucount: str = None,
        hide_banner: bool = None,
        y: bool = None,
        n: bool = None,
        ignore_unknown: bool = None,
        copy_unknown: bool = None,
        recast_media: bool = None,
        benchmark: bool = None,
        benchmark_all: bool = None,
        progress: str = None,
        stdin: bool = None,
        timelimit: str = None,
        dump: bool = None,
        hex: bool = None,
        vsync: str = None,
        frame_drop_threshold: float = None,
        adrift_threshold: str = None,
        copyts: bool = None,
        start_at_zero: bool = None,
        copytb: int = None,
        dts_delta_threshold: float = None,
        dts_error_threshold: float = None,
        xerror: bool = None,
        abort_on: str = None,
        filter_threads: str = None,
        filter_complex: str = None,
        filter_complex_threads: int = None,
        lavfi: str = None,
        filter_complex_script: str = None,
        auto_conversion_filters: bool = None,
        stats: bool = None,
        stats_period: str = None,
        debug_ts: bool = None,
        max_error_rate: float = None,
        psnr: bool = None,
        vstats: bool = None,
        vstats_file: str = None,
        vstats_version: int = None,
        qphist: bool = None,
        init_hw_device: str = None,
        filter_hw_device: str = None,
        **kwargs: int | str | bool | float,
    ) -> GlobalStream:
        """
        Set global options.

        Args:
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
            GlobalStream: GlobalStream instance
        """
        vv: dict[str, int | float | str | bool] = {
            k: v
            for k, v in {
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
            }.items()
            if v is not None
        }
        return self._global_node(**(vv | kwargs)).stream()
