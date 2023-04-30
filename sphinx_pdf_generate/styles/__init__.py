import html
import re
from pathlib import Path
from typing import Any, Dict, Optional

from bs4 import Tag

from ..options import Options


def _css_escape(text: Optional[str]) -> str:
    """@see https://developer.mozilla.org/en-US/docs/Web/CSS/string"""

    if not text:
        return ""

    text = html.unescape(str(text))

    # -- probably not needed.
    # text = text.encode('unicode-escape').decode('ascii').replace('\\u', '\\')

    return text.replace("'", "\\27")


def style_for_print(options: Options, pdf_metadata: Optional[Dict[str, Any]] = None) -> list[Tag]:
    base_path = Path(Path(__file__).parent).resolve()
    pdf_metadata = {} if pdf_metadata is None else pdf_metadata

    css_string = """
    :root {{
        --author: '{}';
        --author-logo: url('{}');
        --copyright: '{}';
        --title: '{}';
        --subtitle: '{}';
        --type: '{}';
        --revision: '{}';
        --filename: '{}';
        --site-url: '{}';
        --base-page-orientation: a4 portrait;
        --rotated-page-orientation: a4 landscape;

    }}""".format(
        _css_escape(options.author),
        _css_escape(options.author_logo),
        _css_escape(options.copyright),
        _css_escape(pdf_metadata.get("title", options.body_title or options.cover_title)),
        _css_escape(pdf_metadata.get("subtitle", options.cover_subtitle)),
        _css_escape(pdf_metadata.get("type", "document")),
        _css_escape(pdf_metadata.get("revision", "")),
        _css_escape(pdf_metadata.get("filename", "")),
        _css_escape(re.sub(r"http://|https://", "", options.site_url)),
    )
    css_tag = Tag(name="style", attrs={"class": "plugin-default-css"})
    css_tag.append(css_string)
    css_files = ["_paging.css"]

    if options.toc:
        css_files.append("toc.css")

    if options.cover:
        css_files.append("cover.css")

    docs_src_dir = Path(options.srcdir).resolve()
    custom_css_path = Path(options.custom_css_path) if options.custom_css_path is not None else Path()
    # Add plugin custom CSS
    if options.custom_css_path is not None:
        if not custom_css_path.is_absolute():
            custom_css_path = docs_src_dir.joinpath(options.custom_css_path)
        if custom_css_path.is_dir():
            css_files.append("pdf_custom.css")

    css_styles_list: list[Tag] = []
    for css_file in css_files:
        filename = base_path.joinpath(css_file) if css_file != "pdf_custom.css" else custom_css_path.joinpath(css_file)
        if filename.is_file():
            with open(filename, encoding="UTF-8") as f:
                css_rules = f.read()
                if css_file in ["_styles.css", "_paging.css"]:
                    css_tag.append(css_rules)
                else:
                    style_tag = Tag(
                        name="style",
                        attrs={"class": "plugin-{}".format(css_file.replace(".", "-"))},
                    )
                    style_tag.append(css_rules)
                    css_styles_list.append(style_tag)

    css_styles_list.insert(0, css_tag)  # Insert default CSS tag at the start
    return css_styles_list
