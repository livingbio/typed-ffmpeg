import pathlib
import re
import urllib.request

import typer

from .schema import FilterDocument, parse_filter_document

app = typer.Typer()

document_path = pathlib.Path(__file__).parent / "source"
document_path.mkdir(exist_ok=True)


@app.command()
def download_ffmpeg_filter_documents() -> None:
    # download ffmpeg filter documents
    url = "https://ffmpeg.org/ffmpeg-filters.html"
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode("utf-8")

    with (document_path / "ffmpeg-filters.html").open("w") as ofile:
        ofile.write(text)


# @app.command()
# def code_gen() -> None:
#     filters = []
#     for f in settings.schemas_path.glob("*.json"):
#         filter = Filter.load(f)
#         filters.append(filter)

#     code = generate_class(filters)

#     with (settings.source_path / "stream.py").open("w") as ofile:
#         ofile.write(code)


# @app.command()
# def generate_schema(path: pathlib.Path) -> None:
#     info = FilterDocument.load(path)

#     if all((settings.schemas_path / f"{filter_name}.json").exists() for filter_name in info.filter_names):
#         return None

#     filters = parse_schema(info)

#     for filter in filters:
#         filter.save()


@app.command()
def split_documents() -> None:
    # split documents into individual files for easier processing

    section_pattern = re.compile(
        r'(?P<body><h3 class="section"><a href="(.*?)">(?P<name>.*?)</a></h3>(.*?))<span',
        re.MULTILINE | re.DOTALL,
    )

    def extract_filter(html: str) -> list[tuple[str, str]]:
        return [(m.group("name"), m.group("body")) for m in section_pattern.finditer(html)]

    infos: list[FilterDocument] = []
    with (document_path / "ffmpeg-filters.html").open() as ifile:
        for name, body in extract_filter(ifile.read()):
            info = parse_filter_document(body)

            if not info.section_index.startswith("8.") and not info.section_index.startswith("11."):
                continue

            print(f"Processing {info.title}...")
            info.save()
            infos.append(info)

    for info in infos:
        # if len(info.refs) >= 1:
        #     print(f"WARNING: {name} has multiple references: {info.refs}")

        for ref in info.refs:
            if not ref.exists():
                print(f"WARNING: {info.title} has missing reference: {ref}")

    return None


if __name__ == "__main__":
    app()
