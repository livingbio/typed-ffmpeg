import html2text
from bs4 import BeautifulSoup


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

    return markdown
