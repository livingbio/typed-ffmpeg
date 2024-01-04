import os
import pathlib

source_folder = pathlib.Path(__file__).parent / "ffmpeg"
source_folder.mkdir(exist_ok=True)


def precompile(folder: pathlib.Path):
    os.chdir(folder)

    if not os.path.exists("config_components.h"):
        os.system("./configure")

    with open("config_components.h") as f:
        text = f.read()

    text = text.replace(" 0", " 1")

    with open("config_components.h", "w") as f:
        f.write(text)

    for file in folder.glob("libavfilter/*.[cm]"):
        print(f"precompile {file}")
        os.system(f"gcc -E -I. {file} > {(source_folder / file.name).resolve()}")
