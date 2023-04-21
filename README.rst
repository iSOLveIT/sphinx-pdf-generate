.. _github-issues: https://github.com/iSOLveIT/sphinx-pdf-generate/issues

.. |github-issues| replace:: GitHub issues

.. _weasyprint-linux: https://weasyprint.readthedocs.io/en/latest/install.html#linux

.. |weasyprint-linux| replace:: Linux

.. _weasyprint-macos: https://weasyprint.readthedocs.io/en/latest/install.html#os-x

.. |weasyprint-macos| replace:: MacOS

.. _weasyprint-windows: https://weasyprint.readthedocs.io/en/latest/install.html#windows

.. |weasyprint-windows| replace:: Windows

.. _sphinx-material: https://github.com/bashtage/sphinx-material/

.. |sphinx-material| replace:: Sphinx-Material

.. _sphinx-immaterial: https://github.com/jbms/sphinx-immaterial/

.. |sphinx-immaterial| replace:: Sphinx-Immaterial

.. _contributing: https://isolveit.github.io/sphinx-pdf-generate/contribute.html

.. |contributing| replace:: Contribution Guidelines

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

Installation
------------

.. note::

    Recommended to install the extension in a Python virtualenv.

Install the package with pip
++++++++++++++++++++++++++++

**Linux & MacOS**

.. code-block:: bash

    python -m pip install -e "git+https://github.com/iSOLveIT/sphinx-pdf-generate/#egg=sphinx-pdf-generate"


**Windows**

.. code-block:: PowerShell

    python -m pip install -e "git+https://github.com/iSOLveIT/sphinx-pdf-generate/#egg=sphinx-pdf-generate"


Install from source repository
++++++++++++++++++++++++++++++

.. code-block:: bash

    cd [YOUR_PROJECT_DIRECTORY]
    git clone https://github.com/iSOLveIT/sphinx-pdf-generate
    cd sphinx-pdf-generate
    pip install -e .


Activate Extension
------------------

You can activate the extension in your **conf.py** file by adding the following:

.. code-block:: python

    extensions = ["sphinx_pdf_generate"]

You can then set the appropriate extension configuration. Visit the `configuration page <https://isolveit.github.io/sphinx-pdf-generate/configuration.html>`_ on our documentation website to read more.

Testing
-------

When building your repository with the ``sphinx-build`` command, you should now see the following message at the end of your build output:

    Converting 17 files to PDF took 15.6s

In your ``OUTPUTDIR`` e.g.``_build/html`` you should now have a PDF file for every HTML page.

Options
-------

Aside the extension configuration, you can also control how the generated PDF file should look like.
You can do so by using what we call the **local options** in your RST file.

For more information on the local options, visit the `local options page <https://isolveit.github.io/sphinx-pdf-generate/options.html>`_ on our documentation website.

Contributing
------------

From reporting a bug to submitting a pull request: every contribution is appreciated and welcome. Report bugs, ask questions and request features using |github-issues|_.

If you want to contribute to the code of this project, please read the |contributing|_.

Special thanks
--------------

Many thanks to `Terry Zhao <https://github.com/zhaoterryy>`_ the author of the `MkDocs PDF Export Plugin <https://github.com/zhaoterryy/mkdocs-pdf-export-plugin>`_ and `Jonathan  Stoppani <https://github.com/GaretJax>`_ the author of the `Sphinx-Autobuild Plugin <https://github.com/executablebooks/sphinx-autobuild>`_.

Their projects inspired the creation of this plugin. We've used some of their code in this project.

