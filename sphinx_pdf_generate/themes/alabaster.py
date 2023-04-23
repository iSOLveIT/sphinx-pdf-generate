from typing import Optional


def get_stylesheet() -> Optional[str]:
    return None


def modify_html(html: str, href: str) -> str:
    a_tag = f'<a class="pdf-icon" href="{href}" download title="Download PDF"></a>'

    # insert into HTML
    insert_point = '<div class="document">'
    html = html.replace(insert_point, insert_point + a_tag)
    return html
