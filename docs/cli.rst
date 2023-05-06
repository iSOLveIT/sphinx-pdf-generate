:pdf-title: Command Line Interface
:pdf-filename: CLI Tool
:pdf-revision: 0.0.1
:pdf-type: manual

.. _cli-tool:

Sphinx-PDF Generate CLI Tool
============================

Sphinx-PDF Generate provides a command-line interface tool you need to use in building the PDF documents.

You can run the command ``sphinx-pdf-generate -h`` to get help and usage information for the CLI tool.

.. code-block:: bash

    $ sphinx-pdf-generate -h

    usage: sphinx-pdf-generate [-h] [--version] sourcedir outdir

    Build PDF files for Sphinx HTML build files.

    positional arguments:
      sourcedir   source directory
      outdir      output directory for built documentation

    options:
      -h, --help  show this help message and exit
      --version   show program's version number and exit

    Sphinx's arguments:
      The following arguments are forwarded as-is to Sphinx. Please look at `sphinx --help` for more information.
        -b=builder, -a, -E, -d=path, -j=N, -c=path, -C, -D=setting=value, -t=tag, -A=name=value, -n, -v, -q, -Q, -w=file, -W, -T, -N, -P

Example
-------

For example, if you want to generate PDF documents for your documentation project, you can use the command ``sphinx-pdf-generate sourcedir outdir`` as below:

.. code-block:: bash

    $ sphinx-pdf-generate ./docs/source ./docs/_build/html

When you run the command above, the Sphinx-PDF Generate CLI tool passes the options and arguments specified to the Sphinx HTML builder.

The Sphinx HTML builder builds the HTML files for the documentation and generates a configuration file for Sphinx-PDF Generate.

The Sphinx-PDF Generate CLI tool then uses the information in the configuration file to generate the PDF documents for the documentation.