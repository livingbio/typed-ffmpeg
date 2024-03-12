# NOTE: this file is auto-generated, do not modify
from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..nodes import FilterableStream, OutputNode, OutputStream


class OutputArgs(ABC):
    @abstractmethod
    def _output_node(self, *streams: FilterableStream, filename: str | Path, **kwargs: Any) -> OutputNode:
        ...

    def output(
        self,
        *streams: "FilterableStream",
        filename: str | Path,
        f: str = None,
        c: str = None,
        codec: str = None,
        pre: str = None,
        map: str = None,
        map_metadata: str = None,
        map_chapters: int = None,
        t: str | float | None = None,
        to: str | float | None = None,
        fs: int = None,
        ss: str | float | None = None,
        timestamp: str = None,
        metadata: str = None,
        program: str = None,
        stream_group: str = None,
        dframes: int = None,
        target: str = None,
        shortest: bool = None,
        shortest_buf_duration: float = None,
        bitexact: bool = None,
        apad: str = None,
        copyinkf: bool = None,
        copypriorss: int = None,
        frames: int = None,
        tag: str = None,
        q: str = None,
        qscale: str = None,
        profile: str = None,
        filter: str = None,
        filter_script: str = None,
        attach: str = None,
        disposition: str = None,
        thread_queue_size: int = None,
        bits_per_raw_sample: int = None,
        stats_enc_pre: str = None,
        stats_enc_post: str = None,
        stats_mux_pre: str = None,
        stats_enc_pre_fmt: str = None,
        stats_enc_post_fmt: str = None,
        stats_mux_pre_fmt: str = None,
        vframes: int = None,
        r: str = None,
        fpsmax: str = None,
        s: str = None,
        aspect: str = None,
        pix_fmt: str = None,
        vn: bool = None,
        rc_override: str = None,
        vcodec: str = None,
        timecode: str = None,
        _pass: int = None,
        passlogfile: str = None,
        vf: str = None,
        intra_matrix: str = None,
        inter_matrix: str = None,
        chroma_intra_matrix: str = None,
        vtag: str = None,
        fps_mode: str = None,
        force_fps: bool = None,
        streamid: str = None,
        force_key_frames: str = None,
        b: str = None,
        autoscale: bool = None,
        fix_sub_duration_heartbeat: bool = None,
        aframes: int = None,
        aq: str = None,
        ar: int = None,
        ac: int = None,
        an: bool = None,
        acodec: str = None,
        ab: str = None,
        atag: str = None,
        sample_fmt: str = None,
        channel_layout: str = None,
        ch_layout: str = None,
        af: str = None,
        sn: bool = None,
        scodec: str = None,
        stag: str = None,
        muxdelay: float = None,
        muxpreload: float = None,
        sdp_file: str = None,
        time_base: str = None,
        enc_time_base: str = None,
        bsf: str = None,
        apre: str = None,
        vpre: str = None,
        spre: str = None,
        fpre: str = None,
        max_muxing_queue_size: int = None,
        muxing_queue_data_threshold: int = None,
        dcodec: str = None,
        dn: bool = None,
        top: int = None,
        **kwargs: Any,
    ) -> OutputStream:
        """
        Output file URL

        Args:
            *streams: the streams to output
            filename: the filename to output to
            f: force container format (auto-detected otherwise)
            c: select encoder/decoder ('copy' to copy stream without reencoding)
            codec: alias for -c (select encoder/decoder)
            pre: preset name
            map: set input stream mapping
            map_metadata: set metadata information of outfile from infile
            map_chapters: set chapters mapping
            t: stop transcoding after specified duration
            to: stop transcoding after specified time is reached
            fs: set the limit file size in bytes
            ss: start transcoding at specified time
            timestamp: set the recording timestamp ('now' to set the current time)
            metadata: add metadata
            program: add program with specified streams
            stream_group: add stream group with specified streams and group type-specific arguments
            dframes: set the number of data frames to output
            target: specify target file type (\"vcd\", \"svcd\", \"dvd\", \"dv\" or \"dv50\
        "with optional prefixes \"pal-\", \"ntsc-\" or \"film-\")
            shortest: finish encoding within shortest input
            shortest_buf_duration: maximum buffering duration (in seconds) for the -shortest option
            bitexact: bitexact mode
            apad: audio pad
            copyinkf: copy initial non-keyframes
            copypriorss: copy or discard frames before start time
            frames: set the number of frames to output
            tag: force codec tag/fourcc
            q: use fixed quality scale (VBR)
            qscale: use fixed quality scale (VBR)
            profile: set profile
            filter: apply specified filters to audio/video
            filter_script: deprecated, use -/filter
            attach: add an attachment to the output file
            disposition: disposition
            thread_queue_size: set the maximum number of queued packets from the demuxer
            bits_per_raw_sample: set the number of bits per raw sample
            stats_enc_pre: write encoding stats before encoding
            stats_enc_post: write encoding stats after encoding
            stats_mux_pre: write packets stats before muxing
            stats_enc_pre_fmt: format of the stats written with -stats_enc_pre
            stats_enc_post_fmt: format of the stats written with -stats_enc_post
            stats_mux_pre_fmt: format of the stats written with -stats_mux_pre
            vframes: set the number of video frames to output
            r: override input framerate/convert to given output framerate (Hz value, fraction or abbreviation)
            fpsmax: set max frame rate (Hz value, fraction or abbreviation)
            s: set frame size (WxH or abbreviation)
            aspect: set aspect ratio (4:3, 16:9 or 1.3333, 1.7777)
            pix_fmt: set pixel format
            vn: disable video
            rc_override: rate control override for specific intervals
            vcodec: alias for -c:v (select encoder/decoder for video streams)
            timecode: set initial TimeCode value.
            _pass: select the pass number (1 to 3)
            passlogfile: select two pass log file name prefix
            vf: alias for -filter:v (apply filters to video streams)
            intra_matrix: specify intra matrix coeffs
            inter_matrix: specify inter matrix coeffs
            chroma_intra_matrix: specify intra matrix coeffs
            vtag: force video tag/fourcc
            fps_mode: set framerate mode for matching video streams; overrides vsync
            force_fps: force the selected framerate, disable the best supported framerate selection
            streamid: set the value of an outfile streamid
            force_key_frames: force key frames at specified timestamps
            b: video bitrate (please use -b:v)
            autoscale: automatically insert a scale filter at the end of the filter graph
            fix_sub_duration_heartbeat: set this video output stream to be a heartbeat stream for fix_sub_duration, according to which subtitles should be split at random access points
            aframes: set the number of audio frames to output
            aq: set audio quality (codec-specific)
            ar: set audio sampling rate (in Hz)
            ac: set number of audio channels
            an: disable audio
            acodec: alias for -c:a (select encoder/decoder for audio streams)
            ab: alias for -b:a (select bitrate for audio streams)
            atag: force audio tag/fourcc
            sample_fmt: set sample format
            channel_layout: set channel layout
            ch_layout: set channel layout
            af: alias for -filter:a (apply filters to audio streams)
            sn: disable subtitle
            scodec: alias for -c:s (select encoder/decoder for subtitle streams)
            stag: force subtitle tag/fourcc
            muxdelay: set the maximum demux-decode delay
            muxpreload: set the initial demux-decode delay
            sdp_file: specify a file in which to print sdp information
            time_base: set the desired time base hint for output stream (1:24, 1:48000 or 0.04166, 2.0833e-5)
            enc_time_base: set the desired time base for the encoder (1:24, 1:48000 or 0.04166, 2.0833e-5). two special values are defined - 0 = use frame rate (video) or sample rate (audio),-1 = match source time base
            bsf: A comma-separated list of bitstream filters
            apre: set the audio options to the indicated preset
            vpre: set the video options to the indicated preset
            spre: set the subtitle options to the indicated preset
            fpre: set options from indicated preset file
            max_muxing_queue_size: maximum number of packets that can be buffered while waiting for all streams to initialize
            muxing_queue_data_threshold: set the threshold after which max_muxing_queue_size is taken into account
            dcodec: alias for -c:d (select encoder/decoder for data streams)
            dn: disable data
            top: deprecated, use the setfield video filter
            **kwargs: the arguments for the output

        Returns:
            the output stream
        """

        options = {
            k: v
            for k, v in {
                "f": f,
                "c": c,
                "codec": codec,
                "pre": pre,
                "map": map,
                "map_metadata": map_metadata,
                "map_chapters": map_chapters,
                "t": t,
                "to": to,
                "fs": fs,
                "ss": ss,
                "timestamp": timestamp,
                "metadata": metadata,
                "program": program,
                "stream_group": stream_group,
                "dframes": dframes,
                "target": target,
                "shortest": shortest,
                "shortest_buf_duration": shortest_buf_duration,
                "bitexact": bitexact,
                "apad": apad,
                "copyinkf": copyinkf,
                "copypriorss": copypriorss,
                "frames": frames,
                "tag": tag,
                "q": q,
                "qscale": qscale,
                "profile": profile,
                "filter": filter,
                "filter_script": filter_script,
                "attach": attach,
                "disposition": disposition,
                "thread_queue_size": thread_queue_size,
                "bits_per_raw_sample": bits_per_raw_sample,
                "stats_enc_pre": stats_enc_pre,
                "stats_enc_post": stats_enc_post,
                "stats_mux_pre": stats_mux_pre,
                "stats_enc_pre_fmt": stats_enc_pre_fmt,
                "stats_enc_post_fmt": stats_enc_post_fmt,
                "stats_mux_pre_fmt": stats_mux_pre_fmt,
                "vframes": vframes,
                "r": r,
                "fpsmax": fpsmax,
                "s": s,
                "aspect": aspect,
                "pix_fmt": pix_fmt,
                "vn": vn,
                "rc_override": rc_override,
                "vcodec": vcodec,
                "timecode": timecode,
                "pass": _pass,
                "passlogfile": passlogfile,
                "vf": vf,
                "intra_matrix": intra_matrix,
                "inter_matrix": inter_matrix,
                "chroma_intra_matrix": chroma_intra_matrix,
                "vtag": vtag,
                "fps_mode": fps_mode,
                "force_fps": force_fps,
                "streamid": streamid,
                "force_key_frames": force_key_frames,
                "b": b,
                "autoscale": autoscale,
                "fix_sub_duration_heartbeat": fix_sub_duration_heartbeat,
                "aframes": aframes,
                "aq": aq,
                "ar": ar,
                "ac": ac,
                "an": an,
                "acodec": acodec,
                "ab": ab,
                "atag": atag,
                "sample_fmt": sample_fmt,
                "channel_layout": channel_layout,
                "ch_layout": ch_layout,
                "af": af,
                "sn": sn,
                "scodec": scodec,
                "stag": stag,
                "muxdelay": muxdelay,
                "muxpreload": muxpreload,
                "sdp_file": sdp_file,
                "time_base": time_base,
                "enc_time_base": enc_time_base,
                "bsf": bsf,
                "apre": apre,
                "vpre": vpre,
                "spre": spre,
                "fpre": fpre,
                "max_muxing_queue_size": max_muxing_queue_size,
                "muxing_queue_data_threshold": muxing_queue_data_threshold,
                "dcodec": dcodec,
                "dn": dn,
                "top": top,
            }.items()
            if v is not None
        }

        return self._output_node(*streams, filename=filename, **options, **kwargs).stream()
