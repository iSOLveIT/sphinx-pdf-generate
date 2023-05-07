:pdf-title: Sphinx-PDF Generate
:pdf-filename: Introduction
:pdf-revision: 0.0.1
:pdf-type: manual

.. Sphinx-Pdf-Generate documentation master file, created by
   sphinx-quickstart on Thu Mar 23 05:16:16 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. only:: html

   .. image:: https://img.shields.io/pypi/dm/sphinx-pdf-generate.svg
       :target: https://pypi.python.org/pypi/sphinx-pdf-generate
       :alt: Downloads
   .. image:: https://img.shields.io/pypi/l/sphinx-pdf-generate.svg
       :target: https://pypi.python.org/pypi/sphinx-pdf-generate
       :alt: License
   .. image:: https://img.shields.io/pypi/pyversions/sphinx-pdf-generate.svg
       :target: https://pypi.python.org/pypi/sphinx-pdf-generate
       :alt: Supported versions
   .. image:: https://github.com/iSOLveIT/sphinx-pdf-generate/actions/workflows/main.yaml/badge.svg
       :target: https://github.com/iSOLveIT/sphnx-pdf-generate/actions/main.yaml
       :alt: GitHub Docs CI Action status
   .. image:: https://github.com/iSOLveIT/sphinx-pdf-generate/actions/workflows/ci.yaml/badge.svg
       :target: https://github.com/iSOLveIT/sphinx-pdf-generate/actions
       :alt: GitHub CI Action status
   .. image:: https://img.shields.io/pypi/v/sphinx-pdf-generate.svg
       :target: https://pypi.python.org/pypi/sphinx-pdf-generate
       :alt: PyPI Package latest release
   .. image:: https://img.shields.io/badge/code%20style-black-000000.svg
       :target: https://github.com/psf/black
       :alt: black code style

.. _getting-started:

.. image:: _static/SPDF-logo.png
   :alt: Sphinx-PDF Generate Logo
   :align: center
   :width: 95%

Sphinx PDF Generate
===================

*A Sphinx extension to generate individual PDF files for each documentation page.*

Sphinx-PDF-Generate extension generates separate PDF files from each HTML page derived from your Sphinx RST files page
in your Sphinx documentation using `WeasyPrint <http://weasyprint.org/>`_.

The extension supports many advanced features such as table of contents, customisable cover page
, support for CSS paged media module `CSS paged media module <https://developer.mozilla.org/en-US/docs/Web/CSS/@page>`_
, and using Sphinx page metadata to generate cover page.

Requirements
------------

1. This package requires Sphinx version 5.0 or higher.
2. Python 3.8 or higher
3. WeasyPrint depends on cairo, Pango and GDK-PixBuf which need to be installed separately. Please follow the installation instructions for your platform carefully:
    - |weasyprint-linux|_
    - |weasyprint-macos|_
    - |weasyprint-windows|_
4. Explicit support for your Sphinx theme is probably required using custom CSS. As of now, the supported themes are |sphinx-material|_ and |sphinx-immaterial|_.
   A generic version will just generate the PDF files and put the download link into a ``<link>`` tag.

:pagebreak:`True`

Install the package with pip
----------------------------

.. note::

    We recommend you install the extension in a Python virtualenv.

.. code-block:: bash

    pip install sphinx-pdf-generate

You can refer to the :ref:`Installation <install>` page for information.

Activate Extension
------------------

You can activate the extension in your **conf.py** file by adding the following:

.. code-block:: python

    extensions = ["sphinx_pdf_generate"]

You can then set the appropriate extension configuration. Visit the :ref:`options <plugin-options>` page to read more.

Usage
-----
You can generate PDF documents for your documentation project by using the command ``sphinx-pdf-generate sourcedir outdir`` as below:

.. code-block:: bash

    $ sphinx-pdf-generate docs/source docs/_build/html

After the documentation build is complete, you should now see the following message at the end of your build output:

.. code-block:: bash

    [sphinx-pdf-generate] Converting 7 file(s) to PDF took 12.1s

In your ``OUTPUTDIR`` e.g.(``docs/_build/html``) you should now have a PDF file for every RST document you decided to build.

You can refer to the :ref:`Quickstart <quickstart>` page for a good introduction to Sphinx-PDF Generate.

:pagebreak:`True`

Contributing
------------

From reporting a bug to submitting a pull request: every contribution is appreciated and welcome. Report bugs, ask questions and request features using |github-issues|_.

If you want to contribute to the code of this project, please read the :ref:`contribute`.

Special thanks
--------------

Many thanks to `Terry Zhao <https://github.com/zhaoterryy>`_ the author of the `MkDocs PDF Export Plugin <https://github.com/zhaoterryy/mkdocs-pdf-export-plugin>`_ and `Jonathan  Stoppani <https://github.com/GaretJax>`_ the author of the `Sphinx-Autobuild Plugin <https://github.com/executablebooks/sphinx-autobuild>`_.

Their projects inspired the creation of this plugin. We've used some of their code in this project.

.. toctree::
   :maxdepth: 2
   :hidden:

   Installation <install>
   Quickstart <quickstart>
   Options <options>
   CLI Tool <cli>
   Customisation <customisation>
   Contributions <contribute>
   Changelog & License <changelog>
