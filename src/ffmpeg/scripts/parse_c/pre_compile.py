import os
import pathlib

source_folder = pathlib.Path(__file__).parent.parent.parent.parent.parent / "ffmpeg"

target_folder = pathlib.Path(__file__).parent / "ffmpeg"
target_folder.mkdir(exist_ok=True)


def precompile() -> None:
    print("precompile")
    os.chdir(source_folder)

    if not os.path.exists("config_components.h"):
        assert os.system("./configure")

    with open("config_components.h") as f:
        text = f.read()

    text = text.replace(" 0", " 1")

    with open("config_components.h", "w") as f:
        f.write(text)

    for file in source_folder.glob("**/*.[cm]"):
        print(f"precompile {file}")
        p = file.relative_to(source_folder)
        target_path = (target_folder / p).resolve()

        if target_path.exists():
            continue

        target_path.parent.mkdir(parents=True, exist_ok=True)
        os.system(f"gcc -E -I. {file} > {target_path}") == 0
