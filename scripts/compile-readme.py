import os
import shutil

import typer


def post_process(markdown_file: str, original_folder: str, new_folder: str) -> None:
    rel_path = (
        "https://raw.githubusercontent.com/livingbio/typed-ffmpeg/main/" + new_folder
    )

    # Move the folder
    if os.path.exists(original_folder):
        for filepath in os.listdir(original_folder):
            # Move the file, replace if it already exists
            old_path = os.path.join(original_folder, filepath)
            new_path = os.path.join(new_folder, filepath)
            if os.path.exists(new_path):
                os.remove(new_path)

            shutil.move(old_path, new_path)
            print(f"Moved {filepath} to {new_folder}")

    # Update paths in the Markdown file
    with open(markdown_file) as file:
        content = file.read()

    content = content.replace(original_folder, rel_path)

    with open(markdown_file, "w") as file:
        file.write(content)

    print("Image paths updated and folder moved.")


def main() -> None:
    os.remove("README.md")
    os.system("jupyter nbconvert --to markdown README.ipynb")
    assert os.path.exists("README.md")

    post_process("README.md", "README_files", "docs/media/README_files")


if __name__ == "__main__":
    typer.run(main)
