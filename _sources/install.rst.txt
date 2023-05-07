:pdf-title: Installation
:pdf-filename: Installation and Activation
:pdf-revision: 0.0.1
:pdf-type: manual

.. _install:

Installation
============

Python Version
--------------
We recommend using the latest version of Python. Sphinx-PDF Generate supports Python 3.7 and newer.

Virtual environments
--------------------
Use a virtual environment to manage the dependencies for your project, both in development and production.

Python comes bundled with the `venv <https://docs.python.org/3/library/venv.html#module-venv>`_ module to create virtual environments.

Create an environment
+++++++++++++++++++++
Create a project folder and a ``venv`` folder within:

.. tab-set::

    .. tab-item:: macOS/Linux
        :sync: unix

        .. code-block:: bash

            $ mkdir myproject
            $ cd myproject
            $ python3 -m venv .venv

    .. tab-item:: Windows (PowerShell)
        :sync: win

        .. code-block:: posh

            > mkdir myproject
            > cd myproject
            > python -m venv .venv

Activate the environment
++++++++++++++++++++++++
Before you work on your project, activate the corresponding environment:

.. tab-set::

    .. tab-item:: macOS/Linux
        :sync: unix

        .. code-block:: bash

            $ .venv/bin/activate

    .. tab-item:: Windows (PowerShell)
        :sync: win

        .. code-block:: posh

            > .venv\Scripts\activate

:pagebreak:`True`

Install Sphinx-PDF Generate
---------------------------
Within the activated environment, use the following command to install Sphinx-PDF Generate:

.. tab-set::

    .. tab-item:: Using pip

        .. code-block:: bash

           $ pip install sphinx-pdf-generate

    .. tab-item:: From source

        .. code-block:: bash

           $ git clone https://github.com/iSOLveIT/sphinx-pdf-generate
           $ cd sphinx-pdf-generate
           $ pip install .

Activate Sphinx-PDF Generate
----------------------------

Add **sphinx_pdf_generate** to the extensions list.

.. code-block:: python

   extensions = ["sphinx_pdf_generate",]

You can refer to the :ref:`Quickstart <quickstart>` page for a good introduction to Sphinx-PDF Generate. |br|
Also, you can refer to the :ref:`Options <plugin-options>` page for information about the configuration options for Sphinx-PDF Generate.