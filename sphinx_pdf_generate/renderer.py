import logging
import re
import sys
from importlib import import_module
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import Any, Dict, Optional

from bs4 import BeautifulSoup, Tag
from weasyprint import HTML

from . import cover, toc
from .options import Options
from .preprocessor import get_content
from .preprocessor import get_separate as prep_separate
from .styles import style_for_print
from .templates.filters.url import URLFilter
from .themes import generic as generic_theme


class Renderer:
    def __init__(self, options: Options, config: Dict[str, Any]):
        self._options = options
        self._config = config

        self.theme = self._load_theme_handler()
        self.user_plugin = self._load_user_plugin_handler()
        self.pgnum = 0
        self.pages = []

    def write_pdf(
        self,
        content: str,
        base_url: str,
        filename: str,
        pdf_metadata: Optional[Dict] = None,
    ):
        self.render_doc(content, base_url, pdf_metadata=pdf_metadata).write_pdf(filename)

    def render_doc(self, content: str, base_url: str, pdf_metadata: Dict = None):
        soup = BeautifulSoup(content, "html5lib")
        soup = get_content(soup)
        self.inject_pgnum(soup)

        style_tags: list[Tag] = style_for_print(self._options, pdf_metadata)
        style_tags[0].append(self.theme.get_stylesheet())  # Add theme CSS

        for style_tag in style_tags:
            soup.head.append(style_tag)

        soup = prep_separate(soup, base_url, self._options.site_url, self._config["outdir"])
        toc.make_toc(soup, self._options)
        cover.make_cover(soup, self._options, self._config, pdf_metadata=pdf_metadata)
        if self.user_plugin:
            self.user_plugin.main(soup=soup)

        # Enable Debugging
        not_as_uri = re.compile(r"^file:/{,2}")
        pattern = r"^{}".format(self._config["outdir"].rstrip("/"))
        check_site_dir = re.compile(pattern)
        if self._options.debug and self._options.debug_target is not None:
            # Debug a single PDF build file
            path_filter = URLFilter(self._options, self._config)
            debug_target_file = path_filter(pathname=str(self._options.debug_target))
            doc_src_path = path_filter(pathname=str(self._options.rst_src_path))

            if doc_src_path == debug_target_file:
                debug_folder_path = str(self._options.debug_dir()).replace("\\", "/")
                rel_url = not_as_uri.sub("", base_url)
                pdf_html_file = check_site_dir.sub(debug_folder_path, rel_url) + ".html"
                pdf_html_dir = Path(pdf_html_file).parent
                if not pdf_html_dir.is_dir():
                    pdf_html_dir.mkdir(parents=True, exist_ok=True)
                with open(pdf_html_file, "w", encoding="UTF-8") as f:
                    f.write(soup.prettify())
                html = HTML(string=str(soup)).render()
                return html
        elif self._options.debug and self._options.debug_target is None:
            # Debug every PDF build file
            debug_folder_path = str(self._options.debug_dir()).replace("\\", "/")
            rel_url = not_as_uri.sub("", base_url)
            pdf_html_file = check_site_dir.sub(debug_folder_path, rel_url) + ".html"
            pdf_html_dir = Path(pdf_html_file).parent
            if not pdf_html_dir.is_dir():
                pdf_html_dir.mkdir(parents=True, exist_ok=True)
            with open(pdf_html_file, "w", encoding="UTF-8") as f:
                f.write(soup.prettify())

        html = HTML(string=str(soup)).render()
        return html

    def add_link(self, content: str, file_name: str = None):
        return self.theme.modify_html(content, file_name)

    def inject_pgnum(self, soup):
        pgnum_counter = soup.new_tag("style")
        pgnum_counter.string = """
        @page :first {{
            counter-reset: __pgnum__ {};
        }}
        @page {{
            counter-increment: __pgnum__;
        }}
        """.format(
            self.pgnum
        )

        soup.head.append(pgnum_counter)

    @property
    def logger(self) -> logging:
        return self._options.logger

    def _load_theme_handler(self):
        theme = self._options.theme_name
        custom_theme_handler_path = self._options.theme_handler_path
        module_name = "." + (theme or "generic").replace("-", "_")

        if custom_theme_handler_path:
            try:
                spec = spec_from_file_location(module_name, Path.cwd().joinpath(custom_theme_handler_path))
                mod = module_from_spec(spec)
                spec.loader.exec_module(mod)
                return mod
            except FileNotFoundError as e:
                self.logger.error(
                    'Could not load theme handler {} from custom directory "{}": {}'.format(
                        theme, custom_theme_handler_path, e
                    ),
                    file=sys.stderr,
                )
                pass
        try:
            return import_module(module_name, "sphinx_pdf_generate.themes")
        except ImportError as e:
            self.logger.error(
                f"Could not load theme handler {theme} because it is not a supported theme by default: {e}",
                file=sys.stderr,
            )
            return generic_theme

    def _load_user_plugin_handler(self):
        custom_plugin_handler_path = self._options.user_plugin_handler_path
        module_name = ".user_plugin"

        if custom_plugin_handler_path:
            try:
                spec = spec_from_file_location(module_name, Path.cwd().joinpath(custom_plugin_handler_path))
                mod = module_from_spec(spec)
                spec.loader.exec_module(mod)
                return mod
            except FileNotFoundError as e:
                self.logger.error(
                    'Could not load the user plugin handler from custom directory "{}": {}'.format(
                        custom_plugin_handler_path, e
                    ),
                    file=sys.stderr,
                )
                pass
