# NOTE: this file is auto-generated, do not modify
"""
Global arguments.
"""



from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any


from ...types import Binary, Boolean, Color, Dictionary, Double, Duration, Flags, Float, Func, Image_size, Int, Int64, Pix_fmt, Rational, Sample_fmt, String, Time, Video_rate
from ...utils.frozendict import merge


if TYPE_CHECKING:
    from ..nodes import GlobalNode, GlobalStream, OutputStream

class GlobalArgs(ABC):
    """
    Abstract base class for providing global FFmpeg command-line arguments.

    This class defines an interface for setting global options that apply to the entire
    FFmpeg command. These options control the general behavior of FFmpeg such as
    logging levels, overwrite behavior, thread usage, and hardware acceleration.

    Implementers must define the _global_node abstract method to apply these arguments
    to actual FFmpeg command execution.
    """

    @abstractmethod
    def _global_node(self, *streams: OutputStream, **kwargs: Any) -> GlobalNode:
        ...

    def global_args(
        self,
        *,loglevel: Func = None,v: Func = None,report: Func = None,max_alloc: Func = None,cpuflags: Func = None,cpucount: Func = None,f: Func = None,c: Func = None,codec: Func = None,pre: Func = None,map: Func = None,map_channel: Func = None,map_metadata: Func = None,map_chapters: Func = None,t: Func = None,to: Func = None,fs: Func = None,ss: Func = None,sseof: Func = None,seek_timestamp: Func = None,isync: Func = None,itsoffset: Func = None,itsscale: Func = None,timestamp: Func = None,metadata: Func = None,program: Func = None,dframes: Func = None,progress: Func = None,timelimit: Func = None,dump: Func = None,readrate: Func = None,readrate_initial_burst: Func = None,target: Func = None,vsync: Func = None,frame_drop_threshold: Func = None,adrift_threshold: Func = None,copytb: Func = None,shortest_buf_duration: Func = None,apad: Func = None,dts_delta_threshold: Func = None,dts_error_threshold: Func = None,abort_on: Func = None,copypriorss: Func = None,frames: Func = None,tag: Func = None,q: Func = None,qscale: Func = None,profile: Func = None,filter: Func = None,filter_threads: Func = None,filter_script: Func = None,reinit_filter: Func = None,filter_complex: Func = None,filter_complex_threads: Func = None,lavfi: Func = None,filter_complex_script: Func = None,stats_period: Func = None,attach: Func = None,dump_attachment: Func = None,stream_loop: Func = None,max_error_rate: Func = None,discard: Func = None,disposition: Func = None,thread_queue_size: Func = None,bits_per_raw_sample: Func = None,stats_enc_pre: Func = None,stats_enc_post: Func = None,stats_mux_pre: Func = None,stats_enc_pre_fmt: Func = None,stats_enc_post_fmt: Func = None,stats_mux_pre_fmt: Func = None,vframes: Func = None,r: Func = None,fpsmax: Func = None,s: Func = None,aspect: Func = None,pix_fmt: Func = None,display_rotation: Func = None,rc_override: Func = None,vcodec: Func = None,timecode: Func = None,_pass: Func = None,passlogfile: Func = None,vstats: Func = None,vstats_file: Func = None,vstats_version: Func = None,vf: Func = None,intra_matrix: Func = None,inter_matrix: Func = None,chroma_intra_matrix: Func = None,top: Func = None,vtag: Func = None,qphist: Func = None,fps_mode: Func = None,streamid: Func = None,force_key_frames: Func = None,b: Func = None,hwaccel: Func = None,hwaccel_device: Func = None,hwaccel_output_format: Func = None,aframes: Func = None,aq: Func = None,ar: Func = None,ac: Func = None,acodec: Func = None,ab: Func = None,atag: Func = None,sample_fmt: Func = None,channel_layout: Func = None,ch_layout: Func = None,af: Func = None,guess_layout_max: Func = None,scodec: Func = None,stag: Func = None,canvas_size: Func = None,muxdelay: Func = None,muxpreload: Func = None,sdp_file: Func = None,time_base: Func = None,enc_time_base: Func = None,bsf: Func = None,absf: Func = None,vbsf: Func = None,apre: Func = None,vpre: Func = None,spre: Func = None,fpre: Func = None,max_muxing_queue_size: Func = None,muxing_queue_data_threshold: Func = None,init_hw_device: Func = None,filter_hw_device: Func = None,extra_options: dict[str, Any] | None = None,
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
            f: force format
            c: codec name
            codec: codec name
            pre: preset name
            map: set input stream mapping
            map_channel: map an audio channel from one stream to another (deprecated)
            map_metadata: set metadata information of outfile from infile
            map_chapters: set chapters mapping
            t: record or transcode \"duration\" seconds of audio/video
            to: record or transcode stop time
            fs: set the limit file size in bytes
            ss: set the start time offset
            sseof: set the start time offset relative to EOF
            seek_timestamp: enable/disable seeking by timestamp with -ss
            isync: Indicate the input index for sync reference
            itsoffset: set the input ts offset
            itsscale: set the input ts scale
            timestamp: set the recording timestamp ('now' to set the current time)
            metadata: add metadata
            program: add program with specified streams
            dframes: set the number of data frames to output
            progress: write program-readable progress information
            timelimit: set max runtime in seconds in CPU user time
            dump: dump each input packet
            readrate: read input at specified rate
            readrate_initial_burst: The initial amount of input to burst read before imposing any readrate
            target: specify target file type (\"vcd\", \"svcd\", \"dvd\", \"dv\" or \"dv50\
        "with optional prefixes \"pal-\", \"ntsc-\" or \"film-\")
            vsync: set video sync method globally; deprecated, use -fps_mode
            frame_drop_threshold: frame drop threshold
            adrift_threshold: deprecated, does nothing
            copytb: copy input stream time base when stream copying
            shortest_buf_duration: maximum buffering duration (in seconds) for the -shortest option
            apad: audio pad
            dts_delta_threshold: timestamp discontinuity delta threshold
            dts_error_threshold: timestamp error delta threshold
            abort_on: abort on the specified condition flags
            copypriorss: copy or discard frames before start time
            frames: set the number of frames to output
            tag: force codec tag/fourcc
            q: use fixed quality scale (VBR)
            qscale: use fixed quality scale (VBR)
            profile: set profile
            filter: set stream filtergraph
            filter_threads: number of non-complex filter threads
            filter_script: read stream filtergraph description from a file
            reinit_filter: reinit filtergraph on input parameter changes
            filter_complex: create a complex filtergraph
            filter_complex_threads: number of threads for -filter_complex
            lavfi: create a complex filtergraph
            filter_complex_script: read complex filtergraph description from a file
            stats_period: set the period at which ffmpeg updates stats and -progress output
            attach: add an attachment to the output file
            dump_attachment: extract an attachment into a file
            stream_loop: set number of times input stream shall be looped
            max_error_rate: ratio of decoding errors (0.0: no errors, 1.0: 100% errors) above which ffmpeg returns an error instead of success.
            discard: discard
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
            r: set frame rate (Hz value, fraction or abbreviation)
            fpsmax: set max frame rate (Hz value, fraction or abbreviation)
            s: set frame size (WxH or abbreviation)
            aspect: set aspect ratio (4:3, 16:9 or 1.3333, 1.7777)
            pix_fmt: set pixel format
            display_rotation: set pure counter-clockwise rotation in degrees for stream(s)
            rc_override: rate control override for specific intervals
            vcodec: force video codec ('copy' to copy stream)
            timecode: set initial TimeCode value.
            _pass: select the pass number (1 to 3)
            passlogfile: select two pass log file name prefix
            vstats: dump video coding statistics to file
            vstats_file: dump video coding statistics to file
            vstats_version: Version of the vstats format to use.
            vf: set video filters
            intra_matrix: specify intra matrix coeffs
            inter_matrix: specify inter matrix coeffs
            chroma_intra_matrix: specify intra matrix coeffs
            top: deprecated, use the setfield video filter
            vtag: force video tag/fourcc
            qphist: deprecated, does nothing
            fps_mode: set framerate mode for matching video streams; overrides vsync
            streamid: set the value of an outfile streamid
            force_key_frames: force key frames at specified timestamps
            b: video bitrate (please use -b:v)
            hwaccel: use HW accelerated decoding
            hwaccel_device: select a device for HW acceleration
            hwaccel_output_format: select output format used with HW accelerated decoding
            aframes: set the number of audio frames to output
            aq: set audio quality (codec-specific)
            ar: set audio sampling rate (in Hz)
            ac: set number of audio channels
            acodec: force audio codec ('copy' to copy stream)
            ab: audio bitrate (please use -b:a)
            atag: force audio tag/fourcc
            sample_fmt: set sample format
            channel_layout: set channel layout
            ch_layout: set channel layout
            af: set audio filters
            guess_layout_max: set the maximum number of channels to try to guess the channel layout
            scodec: force subtitle codec ('copy' to copy stream)
            stag: force subtitle tag/fourcc
            canvas_size: set canvas size (WxH or abbreviation)
            muxdelay: set the maximum demux-decode delay
            muxpreload: set the initial demux-decode delay
            sdp_file: specify a file in which to print sdp information
            time_base: set the desired time base hint for output stream (1:24, 1:48000 or 0.04166, 2.0833e-5)
            enc_time_base: set the desired time base for the encoder (1:24, 1:48000 or 0.04166, 2.0833e-5). two special values are defined - 0 = use frame rate (video) or sample rate (audio),-1 = match source time base
            bsf: A comma-separated list of bitstream filters
            absf: deprecated
            vbsf: deprecated
            apre: set the audio options to the indicated preset
            vpre: set the video options to the indicated preset
            spre: set the subtitle options to the indicated preset
            fpre: set options from indicated preset file
            max_muxing_queue_size: maximum number of packets that can be buffered while waiting for all streams to initialize
            muxing_queue_data_threshold: set the threshold after which max_muxing_queue_size is taken into account
            init_hw_device: initialise hardware device
            filter_hw_device: set hardware device used when filtering
            extra_options: Additional options

        Returns:
            GlobalStream: GlobalStream instance
        """

        return self._global_node(**merge(
            {






















                "loglevel": loglevel,

                "v": v,

                "report": report,

                "max_alloc": max_alloc,

                "cpuflags": cpuflags,

                "cpucount": cpucount,




                "f": f,






                "c": c,

                "codec": codec,

                "pre": pre,

                "map": map,

                "map_channel": map_channel,

                "map_metadata": map_metadata,

                "map_chapters": map_chapters,

                "t": t,

                "to": to,

                "fs": fs,

                "ss": ss,

                "sseof": sseof,

                "seek_timestamp": seek_timestamp,


                "isync": isync,

                "itsoffset": itsoffset,

                "itsscale": itsscale,

                "timestamp": timestamp,

                "metadata": metadata,

                "program": program,

                "dframes": dframes,



                "progress": progress,


                "timelimit": timelimit,




                "readrate": readrate,

                "readrate_initial_burst": readrate_initial_burst,

                "target": target,

                "vsync": vsync,

                "frame_drop_threshold": frame_drop_threshold,

                "adrift_threshold": adrift_threshold,



                "copytb": copytb,


                "shortest_buf_duration": shortest_buf_duration,


                "apad": apad,

                "dts_delta_threshold": dts_delta_threshold,

                "dts_error_threshold": dts_error_threshold,


                "abort_on": abort_on,


                "copypriorss": copypriorss,

                "frames": frames,

                "tag": tag,

                "q": q,

                "qscale": qscale,

                "profile": profile,

                "filter": filter,

                "filter_threads": filter_threads,

                "filter_script": filter_script,

                "reinit_filter": reinit_filter,

                "filter_complex": filter_complex,

                "filter_complex_threads": filter_complex_threads,

                "lavfi": lavfi,

                "filter_complex_script": filter_complex_script,



                "stats_period": stats_period,

                "attach": attach,

                "dump_attachment": dump_attachment,

                "stream_loop": stream_loop,


                "max_error_rate": max_error_rate,

                "discard": discard,

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

                "display_rotation": display_rotation,




                "rc_override": rc_override,

                "vcodec": vcodec,

                "timecode": timecode,

                "pass": _pass,

                "passlogfile": passlogfile,


                "vstats": vstats,

                "vstats_file": vstats_file,

                "vstats_version": vstats_version,

                "vf": vf,

                "intra_matrix": intra_matrix,

                "inter_matrix": inter_matrix,

                "chroma_intra_matrix": chroma_intra_matrix,

                "top": top,

                "vtag": vtag,

                "qphist": qphist,

                "fps_mode": fps_mode,


                "streamid": streamid,

                "force_key_frames": force_key_frames,

                "b": b,

                "hwaccel": hwaccel,

                "hwaccel_device": hwaccel_device,

                "hwaccel_output_format": hwaccel_output_format,





                "aframes": aframes,

                "aq": aq,

                "ar": ar,

                "ac": ac,


                "acodec": acodec,

                "ab": ab,

                "atag": atag,

                "sample_fmt": sample_fmt,

                "channel_layout": channel_layout,

                "ch_layout": ch_layout,

                "af": af,

                "guess_layout_max": guess_layout_max,


                "scodec": scodec,

                "stag": stag,


                "canvas_size": canvas_size,

                "muxdelay": muxdelay,

                "muxpreload": muxpreload,

                "sdp_file": sdp_file,

                "time_base": time_base,

                "enc_time_base": enc_time_base,

                "bsf": bsf,

                "absf": absf,

                "vbsf": vbsf,

                "apre": apre,

                "vpre": vpre,

                "spre": spre,

                "fpre": fpre,

                "max_muxing_queue_size": max_muxing_queue_size,

                "muxing_queue_data_threshold": muxing_queue_data_threshold,



                "init_hw_device": init_hw_device,

                "filter_hw_device": filter_hw_device,


            }, extra_options)
        ).stream()
