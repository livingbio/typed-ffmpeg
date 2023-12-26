import pathlib

import typer
from parse_c.cli import parse_filters
from parse_docs.cli import split_documents

app = typer.Typer()


@app.command()
def generate(outpath: pathlib.Path) -> None:
    filters = parse_filters()

    filter_doc_mapping = {}
    for doc in split_documents():
        for filter_name in doc.filter_names:
            filter_doc_mapping[filter_name] = doc

    for f in filters:
        if f.name not in filter_doc_mapping:
            print(f"WARNING: {f.name} has no document")
            continue


if __name__ == "__main__":
    app()
