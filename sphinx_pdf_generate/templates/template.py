# import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import jinja2

from .filters.datetime import strftime, strptime
from .filters.url import URLFilter


class Template:

    """Pickups key-value from `mkdocs.yml`"""

    __KEYS = [
        "author",
        "author_logo",
        "copyright",
        "disclaimer",
        "cover_title",
        "cover_subtitle",
        "site_url",
        "project",
        "version",
        "release",
    ]

    def __init__(self, options: object, config: Dict[str, Any]):
        self._options = options
        self._config = config

        self._keywords = None
        self._jinja_env = None

    @property
    def _env(self) -> jinja2.Environment:
        def generate():
            base_path = Path(Path(__file__).parent).resolve()
            template_paths = []
            docs_src_dir = Path(self._options.srcdir).resolve()
            # Include the template path specified under the `pdfgen_custom_template_path` configuration under conf.py
            custom_template_path = Path(self._options.custom_template_path)
            if not custom_template_path.is_absolute():
                custom_template_path = docs_src_dir.joinpath(self._options.custom_template_path)
            if custom_template_path.is_dir():
                template_paths.append(custom_template_path)

            # Include all templates path listed under the Sphinx `templates_path` configuration under conf.py
            sphinx_templates_paths: List[str] = self._config["templates_path"]
            for _templates_path in sphinx_templates_paths:
                sphinx_template_path = Path(_templates_path)
                if not sphinx_template_path.is_absolute():
                    sphinx_template_path = docs_src_dir.joinpath(sphinx_template_path)
                if sphinx_template_path.is_dir():
                    template_paths.append(sphinx_template_path)

            template_paths.append(base_path.joinpath("."))  # Include the extensions default templates folder path

            template_paths = list(set(template_paths))
            file_loader = jinja2.FileSystemLoader(template_paths)
            logging_undefined = jinja2.make_logging_undefined(logger=self._options.logger, base=jinja2.Undefined)
            env = jinja2.Environment(
                loader=file_loader,
                undefined=logging_undefined,
                lstrip_blocks=True,
                trim_blocks=True,
                autoescape=True,
            )

            env.filters["strptime"] = strptime
            env.filters["strftime"] = strftime
            env.filters["to_url"] = URLFilter(self._options, self._config)

            return env

        if not self._jinja_env:
            self._jinja_env = generate()
        return self._jinja_env

    @property
    def keywords(self) -> dict:
        """Keywords to pass when rendering the template."""

        import html

        def unescape_html_in_list(values: list) -> list:
            new_values = []
            for v in values:
                if isinstance(v, str):
                    new_values.append(html.unescape(v))
                elif isinstance(v, list):
                    new_values.append(unescape_html_in_list(v))
                elif isinstance(v, dict):
                    unescape_html(v)
                    new_values.append(v)
                else:
                    new_values.append(v)
            return new_values

        def unescape_html(variables: dict):
            for k, v in variables.items():
                if isinstance(v, str):
                    variables[k] = html.unescape(v)
                elif isinstance(v, list):
                    variables[k] = unescape_html_in_list(v)
                elif isinstance(v, dict):
                    unescape_html(v)

        def build_keywords():
            keywords = {}

            for key in self.__KEYS:
                if hasattr(self._options, key):
                    keywords[key] = getattr(self._options, key)
                elif key in self._config:
                    keywords[key] = self._config[key]

            unescape_html(keywords)

            keywords["now"] = datetime.now()

            if self._options.verbose:
                from pprint import pformat

                self._options.logger.info("Template variables:")
                for line in pformat(keywords).split("\n"):
                    self._options.logger.info("  " + line)

            return keywords

        if not self._keywords:
            self._keywords = build_keywords()

        return self._keywords

    def select(self, names: [str], parent=None, globals=None) -> jinja2.Template:
        """Find and load a template by names of given."""

        real_names = []
        for name in names:
            for ext in [".html.j2", ".html.jinja2", ".html", ".htm"]:
                real_names.append(name + ext)

        return self._env.select_template(real_names, parent=parent, globals=globals)
