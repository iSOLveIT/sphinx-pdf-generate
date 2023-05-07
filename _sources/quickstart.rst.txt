:pdf-title: Quickstart
:pdf-filename: Quickstart
:pdf-revision: 0.0.1
:pdf-type: manual

.. _quickstart:

Quickstart
==========

Eager to get started? This page gives a good introduction to the Sphinx-PDF Generate plugin.
Follow :ref:`Installation <install>` to set up a project and install Sphinx-PDF Generate first.

A Minimal Sphinx Docs
---------------------

To set up a Sphinx project, you need to do the following:

1. Install the Sphinx package in your Python virtual environment using the command:
    .. code-block:: bash

        $ pip install sphinx
2. Setup the Sphinx project by running the following command (choosing the default config options) under a **docs/** folder:
    .. code-block:: bash

        $ sphinx-quickstart
3. Inside the docs folder, you should have the following file structure.
    .. code-block:: bash

        ├── docs
            ├── _build
            ├── _static
            ├── _templates
            ├── conf.py
            ├── index.rst
            ├── make.bat
            ├── Makefile
4. In the **conf.py** file under your **docs** folder, you can set the values for the following options:
    .. code-block:: python

        extensions = ["sphinx_pdf_generate",]

        # Sphinx-PDF-Generate global options
        pdfgen_site_url = "https://example.com"
        pdfgen_author = "Sphinx-PDF Generate"
        pdfgen_copyright = "2023, Sphinx-PDF Generate"
        pdfgen_disclaimer = "Disclaimer: Content can change at anytime and best to refer to website for latest information."
        pdfgen_cover = True
        pdfgen_cover_title = "Sphinx-PDF Generate"
        pdfgen_toc = True
        pdfgen_toc_numbering = True
        pdfgen_toc_title = "Table of Contents"
        pdfgen_toc_level = 4

    .. note::

        The configuration options above are used as default values when the local options are not set in the individual RST documents. You can refer to the :ref:`Options <plugin-options>` page for detailed information about the configuration options.
5. Use the Sphinx-PDF Generate CLI tool to build the documentation project by running the following command in a terminal inside the **docs** folder:
    .. code-block:: bash

        $ sphinx-pdf-generate . _build/html
6. After the documentation build is complete, the **_build/html** folder should now have a PDF file for every RST document you decided to build.
7. When you open your documentation build files in the browser, the PDF document should be added as shown in the image below:
    .. image:: _static/img/image_1.png
        :align: center
        :width: 100%
        :alt: options.html file with PDF attachment

**So what did the above steps do?**

1. First, we installed the ``sphinx`` extension and created a Sphinx project.
2. Next, we configured our Sphinx project to use the ``sphinx_pdf_generate`` based on the recommended :ref:`configuration options <plugin-options>`.
3. We then used the Sphinx-PDF Generate CLI tool to build the HTML files and generate the PDF documents for the documentation.
4. Finally, we viewed the output of our documentation in our web browser.

