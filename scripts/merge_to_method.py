import pathlib
import re

BASE_PATH = pathlib.Path(__file__).parent


def main() -> None:

    with (BASE_PATH / "_stream.py").open() as ifile:
        base = ifile.read()

    for path in sorted((BASE_PATH / "./filters").iterdir(), key=lambda x: x.stem):
        print(f"Processing {path}")
        with path.open() as ifile:
            body = ifile.read()

            # remove the from xx import xxx lines
            body = "\n".join([i for i in body.split("\n") if not i.startswith("from")])

            # convert "steam: Stream" to "self"
            body = body.replace("stream: Stream", "self")
            body = body.replace("stream,", "self,")

            # convert "-> Stream" -> '-> "Stream"'
            body = body.replace("-> Stream", '-> "Stream"')

            # convert "[\w]+.__name__", to `"[\w]+"`
            body = re.sub(r"([\w]+).__name__", r'"\1"', body)

            # add a tab to each line
            body = "\n".join(["    " + i for i in body.split("\n")])

            base += f"\n\n{body}"

    with open(BASE_PATH / "../src/stream.py", "w") as ofile:
        ofile.write(base)


if __name__ == "__main__":
    main()
