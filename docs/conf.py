# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

from sphinx_pdf_generate.version import __version__

sys.path.append(os.path.abspath("../"))

project = "Sphinx-Pdf-Generate"
copyright = "2023, iSOLveIT"
author = "iSOLveIT"
version = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_immaterial",
    "sphinx_design",
    "sphinx_pdf_generate",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "research.md"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_immaterial"
html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
    },
    "site_url": "https://isolveit.github.io/sphinx-pdf-generate",
    "repo_url": "https://github.com/iSOLveIT/sphinx-pdf-generate",
    "repo_name": "Sphinx-PDF Generate",
    "repo_type": "github",
    "edit_uri": "blob/main/docs",
    "globaltoc_collapse": True,
    "features": [
        "navigation.sections",
        "navigation.top",
        "search.share",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "deep-purple",
            "accent": "deep-purple",
            "toggle": {
                "icon": "material/weather-night",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "deep-purple",
            "accent": "deep-purple",
            "toggle": {
                "icon": "material/weather-sunny",
                "name": "Switch to light mode",
            },
        },
    ],
}
html_logo = "_static/SPDF-logo.png"
html_favicon = "_static/SPDF-logo.png"
html_title = "Home"
html_sidebars = {"**": ["globaltoc.html", "localtoc.html", "searchbox.html"]}
html_static_path = ["_static"]

rst_epilog = """
.. |br| raw:: html 

   <br>

.. _github-issues: https://github.com/iSOLveIT/sphinx-pdf-generate/issues

.. |github-issues| replace:: GitHub issues

.. _weasyprint-linux: https://weasyprint.readthedocs.io/en/latest/install.html#linux

.. |weasyprint-linux| replace:: Linux

.. _weasyprint-macos: https://weasyprint.readthedocs.io/en/latest/install.html#macos

.. |weasyprint-macos| replace:: MacOS

.. _weasyprint-windows: https://weasyprint.readthedocs.io/en/latest/install.html#windows

.. |weasyprint-windows| replace:: Windows

.. _sphinx-material: https://github.com/bashtage/sphinx-material/

.. |sphinx-material| replace:: Sphinx-Material

.. _sphinx-immaterial: https://github.com/jbms/sphinx-immaterial/

.. |sphinx-immaterial| replace:: Sphinx-Immaterial

.. _contributing: https://isolveit.github.io/sphinx-pdf-generate/contribute.html

.. |contributing| replace:: Contribution Guidelines

"""  # noqa: W291

# Sphinx-PDF-Generate configurations
pdfgen_verbose = False
pdfgen_site_url = "https://isolveit.github.io/sphinx-pdf-generate/"
# pdfgen_debug = True
# pdfgen_debug_target = "index.rst"
pdfgen_author = "iSOLveIT"
pdfgen_author_logo = "_static/SPDF-logo.png"
pdfgen_copyright = copyright
pdfgen_disclaimer = "Disclaimer: Content can change at anytime and best to refer to website for latest information."
pdfgen_cover = True
# pdfgen_cover_title = ""
# pdfgen_cover_subtitle = ""
pdfgen_custom_template_path = ""
pdfgen_custom_css_path = ""
# pdfgen_plugin_handler_path = "custom_code.py"
pdfgen_toc = True
pdfgen_toc_numbering = True
pdfgen_toc_title = "Contents"
pdfgen_toc_level = 6
pdfgen_cover_images = {}
