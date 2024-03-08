import os
import pathlib
import tempfile

source_folder = pathlib.Path(__file__).parent.parent.parent.parent.parent / "ffmpeg"

target_folder = pathlib.Path(__file__).parent / "ffmpeg"
target_folder.mkdir(exist_ok=True)


def pre_compile_file(file: pathlib.Path) -> pathlib.Path:
    os.chdir(source_folder)

    assert file.exists(), f"{file} does not exist"
    print(f"precompile {file}")
    target = pathlib.Path(tempfile.mktemp(suffix=file.suffix))

    os.system(f"gcc -E -I. {file} > {target}")
    return target


def precompile() -> None:
    os.chdir(source_folder)

    if not os.path.exists("config_components.h"):
        os.system("./configure")

    with open("config_components.h") as f:
        text = f.read()

    text = text.replace(" 0", " 1")

    with open("config_components.h", "w") as f:
        f.write(text)

    for file in source_folder.glob("**/*.[cm]"):
        p = file.relative_to(source_folder)
        target_path = (target_folder / p).resolve()
        target_path.parent.mkdir(parents=True, exist_ok=True)

        compiled_file = pre_compile_file(file)
        compiled_file.rename(target_path)
