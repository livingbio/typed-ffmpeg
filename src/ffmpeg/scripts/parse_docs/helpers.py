import html2text
from bs4 import BeautifulSoup

from .schema import FilterDocument


def convert_html_to_markdown(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    # Convert <dt> and <dd> tags to a more Markdown-friendly format
    for dl in soup.find_all("dl"):
        for tag in dl.find_all(["dt", "dd"]):
            if tag.name == "dt":
                tag.insert_before(soup.new_tag("p"))
                tag.string = "**" + tag.text + "**"
            elif tag.name == "dd":
                tag.insert_before(soup.new_tag("p"))
                tag.string = tag.text + "\n\n"

    # Use html2text for other conversions
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.bypass_tables = False

    # Convert the HTML to Markdown
    updated_html = str(soup)
    markdown = converter.handle(updated_html)

    markdown = markdown.replace("\\", "").replace("\\", "\\\\")

    return markdown


def parse_filter_document(body: str) -> FilterDocument:
    soup = BeautifulSoup(body, "html.parser")
    h3 = soup.find("h3")
    title = h3.text
    index, filter_namestr = title.split(" ", 1)
    filter_names = map(lambda i: i.strip(), filter_namestr.split(","))
    ref = h3.a["href"].replace("#toc-", "").replace("-1", "")

    # check cross reference
    refs: set[str] = set()
    for a in soup.find_all("a"):
        href = a.get("href")
        if href.startswith("#") and not href.startswith("#toc-"):
            refs.add(href[1:])

    return FilterDocument(
        section_index=index,
        hash=ref,
        title=title,
        body=body,
        filter_names=tuple(filter_names),
    )


def parse_paremeters(soup: BeautifulSoup) -> dict[str, str]:
    parameters = []
    current_params = []

    element: BeautifulSoup
    for element in soup.find_all(["dt", "dd"], recursive=False):
        if element.name == "dt" and element.samp:
            current_params.append(element.samp.get_text())
        elif element.name == "dd" and current_params:
            description = str(element)
            for param in current_params:
                param = param.strip().replace(" ", ",")
                for p in param.split(","):
                    p = p.strip()
                    parameters.append({"name": p, "description": description})
            current_params = []

    return {k["name"]: k["description"] for k in parameters}
