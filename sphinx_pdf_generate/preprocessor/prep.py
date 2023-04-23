import re

from bs4 import BeautifulSoup

from .content import restructure_tabbed_content
from .links import rel_html_href, replace_asset_hrefs


def get_separate(soup: BeautifulSoup, base_url: str, site_url: str, outdir: str):
    """
    Function to restructure HTML content, so we can use it to generate separate PDFs.

    :param soup: HTML content
    :param base_url: File URI of PDF file destination. e.g.("file:///home/user-1/docs/sample")
    :param site_url: Documentation site URL
    :param outdir: Sphinx documentation build file directory. e.g. _build or build
    :return: Restructured HTML content
    """
    # Transforms all relative hrefs pointing to other html docs into full site URL hrefs
    for a in soup.find_all("a", href=True):
        a["href"] = rel_html_href(base_url, a["href"], site_url, outdir)

    soup = replace_asset_hrefs(soup, base_url)  # Replace hrefs and srcs in link and img tags respectively
    soup = restructure_tabbed_content(soup)  # Restructure tabbed content in HTML
    return soup


def get_content(soup: BeautifulSoup) -> BeautifulSoup:
    """
    Function to restructure HTML content by removing all unwanted parts and leaving only the content that will be
    used in converting the PDF.

    :param soup: HTML content
    :return: Restructured HTML content
    """
    content = soup.find("article", attrs={"class": "md-content__inner"})
    new_content = [content]
    soup.body.clear()
    soup.body.extend(new_content)
    # Check image alignment
    all_images = soup.find_all("img", attrs={"align": re.compile(r"left|right")})
    for img in all_images:
        # Modify <img> tags
        position = img["align"]
        img["style"] = f"float:{position};"
        del img["align"]
    # Check table alignment
    all_table_th = soup.find_all("th", attrs={"align": re.compile(r"left|right|center")})
    for th in all_table_th:
        # Modify <th> tags
        position = th["align"]
        th["style"] = f"text-align:{position};"
        del th["align"]
    all_table_td = soup.find_all("td", attrs={"align": re.compile(r"left|right|center")})
    for td in all_table_td:
        # Modify <td> tags
        position = td["align"]
        td["style"] = f"text-align:{position};"
        del td["align"]
    return soup
