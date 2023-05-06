import json
import logging
from pathlib import Path
from timeit import default_timer as timer
from typing import Any, Dict

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util import docutils

from sphinx_pdf_generate.logging import get_logger
from sphinx_pdf_generate.options import Options
from sphinx_pdf_generate.renderer import Renderer
from sphinx_pdf_generate.templates.filters.url import URLFilter
from sphinx_pdf_generate.utils import get_pdf_metadata, h1_title_tag, secure_filename
from sphinx_pdf_generate.version import __version__


def setup(app: Sphinx) -> Dict[str, Any]:
    ########################################################################
    # CONFIG_VALUES
    ######################################################################
    # Define config values
    app.add_config_value("pdfgen_verbose", False, "html", types=[bool])
    app.add_config_value("pdfgen_site_url", "http://127.0.0.1:8000", "html", types=[str])
    app.add_config_value("pdfgen_debug", False, "html", types=[bool])
    app.add_config_value("pdfgen_debug_target", "", "html", types=[str])
    app.add_config_value("pdfgen_author", None, "html", types=[str])
    app.add_config_value("pdfgen_author_logo", None, "html", types=[str])
    app.add_config_value("pdfgen_copyright", None, "html", types=[str])
    app.add_config_value("pdfgen_disclaimer", None, "html", types=[str])
    app.add_config_value("pdfgen_cover", True, "html", types=[bool])
    app.add_config_value("pdfgen_cover_title", None, "html", types=[str])
    app.add_config_value("pdfgen_cover_subtitle", None, "html", types=[str])
    app.add_config_value("pdfgen_custom_template_path", "_templates", "html", types=[str])
    app.add_config_value("pdfgen_theme_handler_path", None, "html", types=[str])
    app.add_config_value("pdfgen_plugin_handler_path", None, "html", types=[str])
    app.add_config_value("pdfgen_custom_css_path", None, "html", types=[str])
    app.add_config_value("pdfgen_toc", True, "html", types=[bool])
    app.add_config_value("pdfgen_toc_numbering", True, "html", types=[bool])
    app.add_config_value("pdfgen_toc_title", "Table of Contents", "html", types=[str])
    app.add_config_value("pdfgen_toc_level", 4, "html", types=[int])
    app.add_config_value("pdfgen_cover_images", None, "html", types=[dict])

    ######################################################################
    # ROLES
    ######################################################################
    app.add_role("pagebreak", page_break_role)
    ########################################################################
    # EVENTS
    ########################################################################
    # Make connections to events
    app.connect("builder-inited", builder_inited)
    app.connect("html-page-context", generate_sources_to_convert)
    app.connect("build-finished", build_finished)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


# ----- SPHINX-EVENTS FUNCTIONS ----- #
def builder_inited(app: Sphinx) -> None:
    if not hasattr(app.env, "sphinx_pdfgen_data"):
        # Used to store the data about of HTML files that needs to be converted.
        app.env.sphinx_pdfgen_data = {}


def generate_sources_to_convert(
    app: Sphinx, pagename: str, templatename: str, context: Dict, doctree: docutils.nodes.Node
):
    project_metadata: Dict[str, str] = app.env.metadata.get(pagename)  # Get metadata of a page
    app.env.sphinx_pdfgen_data.update([(pagename, project_metadata)])


def page_break_role(name, rawtext, text, lineno, inliner, options={}, content=[]):  # noqa B006
    """Sphinx role to insert a page break in the HTML output."""
    return [nodes.raw("", '<p class="page-break" style="margin: 0"></p>', format="html")], []


def build_finished(app: Sphinx, exception: Exception):
    global_options = {}
    global_options.update(
        verbose=app.config.pdfgen_verbose,
        site_url=app.config.pdfgen_site_url,
        debug=app.config.pdfgen_debug,
        debug_target=None if len(app.config.pdfgen_debug_target) == 0 else app.config.pdfgen_debug_target,
        author=app.config.author if not app.config.pdfgen_author else app.config.pdfgen_author,
        author_logo=app.config.html_logo if not app.config.pdfgen_author_logo else app.config.pdfgen_author_logo,
        copyright=app.config.copyright if not app.config.pdfgen_copyright else app.config.pdfgen_copyright,
        disclaimer=app.config.pdfgen_disclaimer,
        cover=app.config.pdfgen_cover,
        cover_title=app.config.pdfgen_cover_title if app.config.pdfgen_cover_title else app.config.project,
        cover_subtitle=app.config.pdfgen_cover_subtitle,
        custom_template_path=app.config.pdfgen_custom_template_path,
        theme_handler_path=app.config.pdfgen_theme_handler_path,
        plugin_handler_path=app.config.pdfgen_plugin_handler_path,
        custom_css_path=app.config.pdfgen_custom_css_path,
        toc=app.config.pdfgen_toc,
        toc_numbering=app.config.pdfgen_toc_numbering,
        toc_title=app.config.pdfgen_toc_title,
        toc_level=app.config.pdfgen_toc_level,
        cover_images=app.config.pdfgen_cover_images,
        theme_name=app.config.html_theme,
        templates_path=app.config.templates_path,
    )

    local_options = app.env.sphinx_pdfgen_data
    pdf_metadata = {"GLOBAL_OPTIONS": global_options, "LOCAL_OPTIONS": local_options}

    path_to_save_metadata = Path(app.outdir).joinpath("pdf_metadata.json")
    with open(path_to_save_metadata, "w") as json_file:
        json.dump(pdf_metadata, json_file, indent=4)


# ----- PDF-GENERATE-PLUGIN CLASS ----- #
class PdfGeneratePlugin:
    def __init__(self):
        self._options = None
        self._config = None
        self._logger = get_logger("sphinx-pdf-generate")
        self._logger.setLevel(logging.INFO)
        self.renderer = None
        self.generate_txt = None
        self.combined = False
        self.pdf_num_files = 0
        self.txt_num_files = 0
        self.num_errors = 0
        self.total_time = 0

    def on_config(self, config):
        self._config = config

        if self._config.get("debug"):
            self._logger.info("PDF debug option is enabled.")
        if self._config.get("debug_target"):
            self._logger.info("Debug Target File: {}".format(self._config.get("debug_target")))

        self._options = Options(self._config, self._logger)

        from weasyprint.logger import LOGGER

        if self._options.verbose:
            LOGGER.setLevel(logging.DEBUG)
            self._logger.setLevel(logging.DEBUG)
        else:
            LOGGER.setLevel(logging.ERROR)

        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        LOGGER.addHandler(handler)

        self.renderer = Renderer(options=self._options, config=self._config)
        return

    def convert_page_to_pdf(self, html_content: str, pagename: str, page_metadata: Dict[str, str]):
        start = timer()

        abs_dest_path = Path(self._config["outdir"]).joinpath(f"{pagename}.html")
        src_path = Path(f"{pagename}.rst")

        self._options.rst_src_path = Path(self._config["srcdir"]).joinpath(src_path)

        dest_path = abs_dest_path.parent
        if not dest_path.is_dir():
            dest_path.mkdir(parents=True, exist_ok=True)
        self._options.out_dest_path = dest_path

        page_metadata = page_metadata if page_metadata is not None else {}
        pdf_meta: Dict[str, Any] = get_pdf_metadata(page_metadata)
        build_pdf_document = pdf_meta.get("build")

        if self._options.debug and self._options.debug_target is not None:
            # Debugging only the debug target file
            path_filter = URLFilter(self._options, self._config)
            debug_target_file = path_filter(pathname=str(self._options.debug_target))
            doc_src_path = path_filter(pathname=str(self._options.rst_src_path))
            if doc_src_path == debug_target_file:
                build_pdf_document = True
            else:
                build_pdf_document = False

        if build_pdf_document and Path(self._config["srcdir"]).joinpath(src_path).exists():
            self._options.body_title = h1_title_tag(html_content, pdf_meta.get("title"))

            file_name = pdf_meta.get("filename") or pdf_meta.get("title") or self._options.body_title or None
            if file_name is None:
                file_name = str(pagename).split("/")[-1]
                self._logger.error(
                    f"You must set the filename metadata in {pagename}.rst so we can use in the PDF document. "
                    f"The source filename is used as fallback."
                )

            # Generate a secure filename
            file_name = secure_filename(file_name)
            base_url = dest_path.joinpath(file_name).as_uri()
            pdf_file = file_name + ".pdf"

            try:
                self._logger.info(f"Converting {src_path} to {pdf_file}")
                self.renderer.write_pdf(
                    html_content,
                    base_url,
                    dest_path.joinpath(pdf_file),
                    pdf_metadata=pdf_meta,
                )

                html_content = self.renderer.add_link(html_content, pdf_file)
                self.pdf_num_files += 1
            except Exception as e:
                self.num_errors += 1
                raise PDFGenerateException(f"Error converting {src_path}. Reason: {e}")
        else:
            self._logger.info(f"Skipped: PDF conversion for {src_path}")

        end = timer()
        self.total_time += end - start
        return html_content


class PDFGenerateException(Exception):
    pass
