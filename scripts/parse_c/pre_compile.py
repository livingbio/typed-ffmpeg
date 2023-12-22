import os
import pathlib

source_folder = pathlib.Path(__file__).parent / "ffmpeg"
source_folder.mkdir(exist_ok=True)


def precompile(folder: pathlib.Path):
    os.chdir(folder)

    if not os.path.exists("config_components.h"):
        os.system("./configure")

    for file in folder.glob("libavfilter/*.c"):
        print(f"precompile {file}")
        os.system(f"gcc -E -I. {file} -o {(source_folder / file.name).resolve()}")
