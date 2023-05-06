"""Main implementation."""

import argparse
import json
import os
from pathlib import Path
from typing import Dict

import colorama

from .build import SPHINX_BUILD_OPTIONS, get_builder, show
from .logging import get_logger
from .pdf_generate import PdfGeneratePlugin
from .version import __version__

GLOBAL_OPTIONS = {}.update(
    verbose=False,
    site_url="http://127.0.0.1:8000",
    debug=False,
    debug_target=None,
    author=None,
    author_logo=None,
    copyright=None,
    disclaimer=None,
    cover=True,
    cover_title=None,
    cover_subtitle=None,
    custom_template_path="_templates",
    theme_handler_path=None,
    plugin_handler_path=None,
    custom_css_path=None,
    toc=True,
    toc_numbering=True,
    toc_title="Table of Contents",
    toc_level=4,
    cover_images=None,
    theme_name="alabaster",
    templates_path=[],
)


def _get_build_args(args):
    build_args = []
    for arg, meta in SPHINX_BUILD_OPTIONS:
        val = getattr(args, arg)
        if not val:
            continue
        opt = f"-{arg}"
        if meta is None:
            build_args.extend([opt] * val)
        else:
            for v in val:
                build_args.extend([opt, v])

    build_args.extend([os.path.realpath(args.sourcedir), os.path.realpath(args.outdir)])
    return build_args


def get_parser():
    """Get the application's argument parser.

    Note: this also handles SPHINX_BUILD_OPTIONS, which later get forwarded to
    sphinx-build as-is.
    """

    class RawTextArgumentDefaultsHelpFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawTextHelpFormatter):
        pass

    parser = argparse.ArgumentParser(
        formatter_class=RawTextArgumentDefaultsHelpFormatter,
        description="Build PDF documents from Sphinx HTML build files.",
    )

    parser.add_argument("--version", action="version", version=f"sphinx-pdf-generate {__version__}")

    sphinx_arguments = ", ".join(f"-{arg}" if meta is None else f"-{arg}={meta}" for arg, meta in SPHINX_BUILD_OPTIONS)
    sphinx_parser = parser.add_argument_group(
        "Sphinx's arguments",
        (
            "The following arguments are forwarded as-is to Sphinx. Please look at "
            f"`sphinx-build --help` for more information.\n  {sphinx_arguments}"
        ),
    )

    for arg, meta in SPHINX_BUILD_OPTIONS:
        if meta is None:
            sphinx_parser.add_argument(f"-{arg}", action="count", help=argparse.SUPPRESS)
        else:
            sphinx_parser.add_argument(
                f"-{arg}",
                action="append",
                help=argparse.SUPPRESS,
                metavar=meta,
            )

    parser.add_argument("sourcedir", help="source directory")
    parser.add_argument("outdir", help="output directory for built documentation")
    return parser


def main() -> None:
    """Actual application logic."""
    colorama.init()
    log = get_logger("sphinx-pdf-generate")

    parser = get_parser()
    args = parser.parse_args()

    show(context="Starting PDF Build Process")

    srcdir = os.path.realpath(args.sourcedir)
    outdir = os.path.realpath(args.outdir)

    if not os.path.exists(srcdir):
        raise PDFGenerateException(f"The source directory {srcdir} does not exist.")
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    build_args = _get_build_args(args)
    builder = get_builder(build_args)

    if builder == 0:
        # Load configuration
        metadata_options_file = Path(outdir).joinpath("pdf_metadata.json")
        if not os.path.exists(metadata_options_file):
            raise PDFGenerateException(
                f"The The PDF metadata file, 'pdf_metadata.json', not found in the output directory. Check: {outdir}"
            )

        with open(metadata_options_file) as json_file:
            load_options: Dict[str, Dict] = json.load(json_file)

        global_config = load_options["GLOBAL_OPTIONS"] if "GLOBAL_OPTIONS" in load_options else GLOBAL_OPTIONS
        local_config = load_options.get("LOCAL_OPTIONS")

        if not local_config:
            raise PDFGenerateException(
                f"The PDF metadata file does not contain information about the local options. "
                f"Check the file for more information: {metadata_options_file}."
            )

        global_config.update(outdir=outdir, srcdir=srcdir)
        pdf_generator = PdfGeneratePlugin()
        pdf_generator.on_config(global_config)

        for html_pagename, html_metadata in local_config.items():
            html_page_path = Path(outdir).joinpath(f"{html_pagename}.html")
            html_page_content = html_page_path.read_text(encoding="utf-8")
            new_html_page_content = pdf_generator.convert_page_to_pdf(
                html_content=html_page_content, pagename=html_pagename, page_metadata=html_metadata
            )
            html_page_path.write_text(data=new_html_page_content, encoding="utf-8")

        show(context=f"Converting {pdf_generator.pdf_num_files} file(s) to PDF took {pdf_generator.total_time:.1f}s")

        if pdf_generator.num_errors > 0:
            show(context=f"{pdf_generator.num_errors} conversion errors occurred (see above)", error=True)
    else:
        show(context="Sphinx build was unsuccessful. No PDF files were generated.", error=True)


class PDFGenerateException(Exception):
    pass
