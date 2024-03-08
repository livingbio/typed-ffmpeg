import os
import pathlib

source_folder = pathlib.Path(__file__).parent / "ffmpeg"
source_folder.mkdir(exist_ok=True)


def pre_compile_file(file: pathlib.Path, target: pathlib.Path) -> None:
    print(f"precompile {file}")
    os.system(f"gcc -E -I. {file} > {target}")


def precompile(folder: pathlib.Path) -> None:
    os.chdir(folder)

    if not os.path.exists("config_components.h"):
        os.system("./configure")

    with open("config_components.h") as f:
        text = f.read()

    text = text.replace(" 0", " 1")

    with open("config_components.h", "w") as f:
        f.write(text)

    for file in folder.glob("**/*.[cm]"):
        p = file.relative_to(folder)
        compiled_path = (source_folder / p).resolve()
        compiled_path.parent.mkdir(parents=True, exist_ok=True)
        pre_compile_file(file, compiled_path)
