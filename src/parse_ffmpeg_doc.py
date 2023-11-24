import os
import re

pattern = re.compile(r'(?P<body><h3 class="section"><a href="(.*?)">(?P<name>.*?)</a></h3>(.*?))<span', re.MULTILINE | re.DOTALL)


def extract_filter(html: str) -> list[tuple[str, str]]:
    return [(m.group("name"), m.group("body")) for m in pattern.finditer(html)]


def main() -> None:
    with open("ffmpeg-filters.html") as ifile:
        for name, body in extract_filter(ifile.read()):
            with open(f"source/{name}.html", "w") as ofile:
                ofile.write(body)
    return None


if __name__ == "__main__":
    os.makedirs("source", exist_ok=True)
    main()
