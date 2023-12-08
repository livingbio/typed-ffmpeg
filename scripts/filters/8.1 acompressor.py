import subprocess
from typing import Literal


class FFmpegAudioCompressor:
    def __init__(
        self,
        level_in: float = 1.0,
        mode: Literal["upward", "downward"] = "downward",
        threshold: float = 0.125,
        ratio: float = 2.0,
        attack: float = 20.0,
        release: float = 250.0,
        makeup: float = 1.0,
        knee: float = 2.82843,
        link: Literal["average", "maximum"] = "average",
        detection: Literal["peak", "rms"] = "rms",
        mix: float = 1.0,
    ):
        self.level_in = level_in
        self.mode = mode
        self.threshold = threshold
        self.ratio = ratio
        self.attack = attack
        self.release = release
        self.makeup = makeup
        self.knee = knee
        self.link = link
        self.detection = detection
        self.mix = mix

    def compress(self, input_file: str, output_file: str):
        args = [
            "ffmpeg",
            "-i",
            input_file,
            "-filter_complex",
            f"acompressor=level_in={self.level_in}:mode={self.mode}:"
            f"threshold={self.threshold}:ratio={self.ratio}:"
            f"attack={self.attack}:release={self.release}:"
            f"makeup={self.makeup}:knee={self.knee}:"
            f"link={self.link}:detection={self.detection}:"
            f"mix={self.mix}",
            "-y",  # Overwrite output file if it exists
            output_file,
        ]

        subprocess.run(args, check=True)


# Example usage
compressor = FFmpegAudioCompressor(threshold=0.2, attack=50, release=500, mix=0.5)

compressor.compress("input.mp3", "compressed_output.mp3")
