import logging
from pathlib import Path
from typing import Any, Dict, Optional

from .templates.filters.url import URLFilter
from .templates.template import Template


class Options:
    def __init__(self, config: Dict[str, Any], logger: logging):
        self.verbose: bool = config["verbose"]
        self.debug: bool = config["debug"]
        self.debug_target: Optional[str] = config["debug_target"]
        self.srcdir: Path = Path(config["srcdir"])
        self.outdir: Path = Path(config["outdir"])
        self._src_path: Optional[Path] = None
        self._dest_path: Optional[Path] = None

        self.site_url: str = config["site_url"]
        self.theme_name: str = config["theme_name"]

        # Author, Copyright, Disclaimer
        self._author: Optional[str] = config["author"]
        self._copyright: Optional[str] = config["copyright"]
        self._disclaimer: Optional[str] = config["disclaimer"]

        # Individual document type cover
        self._cover_images: Optional[Dict] = config["cover_images"]

        # Cover
        self.cover: bool = config["cover"]
        self._cover_title: Optional[str] = config["cover_title"]
        self._cover_subtitle: Optional[str] = config["cover_subtitle"]

        # path to custom template 'cover.html' and 'custom.css'
        self.custom_template_path: str = config["custom_template_path"]
        self.custom_css_path: Optional[str] = config["custom_css_path"]

        # TOC and Chapter heading
        self.toc: bool = config["toc"]
        self.toc_title: str = config["toc_title"]
        self.toc_level: int = config["toc_level"]
        self.toc_ordering: bool = config["toc_numbering"]

        # H1 Title of the document
        self._body_title: str = ""

        # Template handler(Jinja2 wrapper)
        self._template = Template(self, config)

        # Author Logo
        logo_path_filter = URLFilter(self, config)
        self.author_logo: Optional[str] = config["author_logo"]
        if isinstance(self.author_logo, str):
            self.author_logo = logo_path_filter(self.author_logo)

        # Custom Theme and User Plugin
        self.theme_handler_path: Optional[str] = config["theme_handler_path"]
        self.user_plugin_handler_path: Optional[str] = config["plugin_handler_path"]

        # for system
        self._logger = logger

    @property
    def body_title(self) -> str:
        return self._body_title

    @body_title.setter
    def body_title(self, text):
        self._body_title = text

    @property
    def author(self) -> str:
        return self._author

    @property
    def copyright(self) -> str:
        return self._copyright

    @property
    def disclaimer(self) -> str:
        return self._disclaimer

    @property
    def cover_title(self) -> str:
        return self._cover_title

    @property
    def cover_subtitle(self) -> str:
        return self._cover_subtitle

    @property
    def cover_images(self) -> Dict:
        return self._cover_images

    @property
    def logger(self) -> logging:
        return self._logger

    @property
    def template(self) -> Template:
        return self._template

    @property
    def rst_src_path(self) -> Path:
        return self._src_path

    @rst_src_path.setter
    def rst_src_path(self, input_path):
        self._src_path = input_path

    @property
    def out_dest_path(self) -> Path:
        return self._dest_path

    @out_dest_path.setter
    def out_dest_path(self, input_path):
        self._dest_path = input_path

    def debug_dir(self) -> Path:
        if self.debug:
            docs_out_dir = Path(self.outdir).parent.resolve()
            debug_folder_path = docs_out_dir.joinpath("pdf_html_debug")
            if not debug_folder_path.is_dir():
                debug_folder_path.mkdir(parents=True, exist_ok=True)
            return debug_folder_path
