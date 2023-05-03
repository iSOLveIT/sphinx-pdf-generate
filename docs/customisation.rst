:pdf-filename: Customisation
:pdf-title: Customize Plugin
:pdf-revision: 0.0.1

.. _plugin-customisation:

Customisation
=============

Custom cover page
-----------------

You can create a custom cover page using the `jinja2 templating engine <https://jinja.palletsprojects.com/en/2.11.x/templates/>`_ or HTML and saving the content in a file with these file extensions ``.html.j2``, ``.html.jinja2``, ``.html``, or ``.htm``.

.. note::

    You should store the custom cover template file in the directory used as the value for :ref:`pdfgen_custom_template_path <custom_template_path>` option.

The plugin provides the following variables which you can use in your custom Jinja template:

* cover_title
* cover_subtitle
* cover_image
* author
* author_logo
* copyright
* disclaimer
* site_url
* revision
* project - (variable from **conf.py** file)
* version - (variable from **conf.py** file)
* release - (variable from **conf.py** file)
* and all the options you provided as the :ref:`local pdf options <local-options>` in a particular RST file.

Using `jinja2 <https://jinja.palletsprojects.com/en/2.11.x/templates/>`_ syntax, you can access all the data above.
Example: use `{{ author }}` to get the value for the :ref:`pdfgen_author` option:

.. _use-custom-template:

Using custom cover template
+++++++++++++++++++++++++++

You can specify the cover page to use for your PDF by following these steps:

**Step 1**

Set the :ref:`pdfgen_custom_template_path <custom_template_path>` option to the directory you want to store the cover template files at.

.. code-block:: python

    pdfgen_custom_template_path = "my_cover_templates_dir"

**Step 2**

Under the directory you set as ``pdfgen_custom_template_path``, create a custom template file. |br|
The custom template's filename can either be ``cover`` or any of the :ref:`document types <local-type>` you set with any of these file extensions ``.html.j2``, ``.html.jinja2``, ``.html``, or ``.htm``.

In the cover template file, write your preferred template syntax into it.

*Example of a cover template file using Jinja2 syntax:*

.. code-block:: jinja

    <article id="doc-cover">
        {% if cover_image is defined %}
            <div class="wrapper upper">
                <div class="logo" style="background-image: url('{{ cover_image | to_url }}');"></div>
            </div>
        {% else %}
            <div class="wrapper"></div>
        {% endif %}
        <div class="wrapper">
            <h1>{{ cover_title | e }}</h1>
            <h2>{{ cover_subtitle | e }}</h2>
            {% if revision %}
                <h3>Revision {{ revision | e }}</h3>
            {% endif %}
        </div>
        <div class="properties">
            <address>
                {% if author %}
                    <p id="author">{{ author | e }}</p>
                {% endif %}
                <a href="{{ site_url }}" id="project_logo" title="Resource Centre">
                    <img src="{{ author_logo }}" alt="Company Logo"
                    style="width:80px;height:30px"/>
                </a>
            </address>
        </div>
        <div class="reserved_rights">
            <address>
                {% if copyright %}
                    <p id="copyright">{{ copyright | e }}</p>
                {% endif %}
                {% if disclaimer %}
                    <p id="disclaimer">{{ disclaimer | e }}</p>
                {% endif %}
            </address>
        </div>
    </article>

**Step 3**

Save the file changes and rebuild your Sphinx project.

.. _use-custom-css-file:

Adjusting the output
--------------------

The resulting PDF can be customized easily by adding a custom stylesheet such as the following:

.. code-block:: css

    @page {
        size: a4 portrait;
        margin: 25mm 10mm 25mm 10mm;
        counter-increment: page;
        font-family: "Roboto","Helvetica Neue",Helvetica,Arial,sans-serif;
        white-space: pre;
        color: grey;
        @top-left {
            content: '© 2018 My Company';
        }
        @top-center {
            content: string(chapter);
        }
        @top-right {
            content: 'Page ' counter(page);
        }
    }

To implement the custom CSS, you need to create a ``pdf_custom.css`` file and save the custom CSS rules in it.

.. note::

    You should store the ``pdf_custom.css`` file under the directory you set as :ref:`pdfgen_custom_css_path <custom_css_path>`

The plugin provides the following CSS variables and named strings which you can use in your ``pdf_custom.css`` file:

* --title
* --subtitle
* --author
* --author-logo
* --copyright
* --type
* --site_url
* --revision
* --filename
* chapter

Using the ``var()`` CSS function, you can access all the CSS variables provided by the plugin.
E.g. use ``var(--author)`` to get the value for the :ref:`pdfgen_author` option.

You can also use the ``string()`` function to access the value of a named string.
E.g. use ``string(chapter)`` to get the value for a chapter.

The custom CSS is appended to the Sphinx stylesheets so, you can choose to override rules by using the ``!important`` CSS keyword or not.

Changing the orientation of a page
++++++++++++++++++++++++++++++++++

The plugin allows you to change the orientation of a page to fit the content on that page.

For example, if you have a table on a page, and it is too wide to fit the current orientation used by the page, 
you can change the page orientation of the individual page by doing the following:

* Wrap the RST content in a raw HTML ``div`` element. The ``div`` element should have its ``class`` attribute set to ``"rotated-page"``. Example:
    .. code-block:: rst

        .. raw:: html

            <div class="rotated-page">

        PLACE CONTENT HERE

        .. raw:: html

            </div>
* Create a ``pdf_custom.css`` file and set these CSS variables under the ``:root {}`` CSS rule:
    * ``--base-page-orientation`` - default page orientation to use and
    * ``--rotated-page-orientation`` - page orientation to use for rotated pages. |br| E.g. ``:root {--base-page-orientation: a4 portrait; --rotated-page-orientation: a4 landscape;}``

.. raw:: html

    <div class="rotated-page">

Example
*******

In this example, we are going to change the page orientation for `this subsection <example>`_.

.. note::

    Download the generated pdf to see the result.

.. table::
    :widths: auto

    +---------------------------------------------------------------------------------------+
    | GPIO Table                                                                            |
    +==================+=============+===========+==========================================+
    | **Header / Pin** | **Symbol**  | **Type**  | **Description**                          |
    +------------------+-------------+-----------+------------------------------------------+
    | Header1 - 1      |   GND       | Power     | Module / System GND                      |
    +------------------+-------------+-----------+------------------------------------------+
    | Header1 - 2      |   IO3       |  I/O      | GPIO – Capabilities are Module Dependent |
    +------------------+-------------+-----------+------------------------------------------+
    | Header1 - 3      |   IO2       |  I/O      | GPIO – Capabilities are Module Dependent |
    +------------------+-------------+-----------+------------------------------------------+
    | Header1 - 4      |   IO1       |  I/O      | GPIO – Capabilities are Module Dependent |
    +------------------+-------------+-----------+------------------------------------------+
    | Header1 - 5      | 3V3 OUT     | Power     | 3.3V Power Output for User               |
    +------------------+-------------+-----------+------------------------------------------+
    | Header2 - 1      |  RESET      |   I       | System Reset, Active Low                 |
    +------------------+-------------+-----------+------------------------------------------+

.. raw:: html

    </div>

In the example above, the `example section <example>`_ is wrapped inside a ``div`` like below:

.. code-block:: rst

    .. raw:: html

        <div class="rotated-page">

    Example
    *******

    In this example, we are going to change the page orientation for `this subsection <example>`_.

    .. note::

        Download the generated pdf to see the result.

    .. table::
        :widths: auto

        +---------------------------------------------------------------------------------------+
        | GPIO Table                                                                            |
        +==================+=============+===========+==========================================+
        | **Header / Pin** | **Symbol**  | **Type**  | **Description**                          |
        +------------------+-------------+-----------+------------------------------------------+
        | Header1 - 1      |   GND       | Power     | Module / System GND                      |
        +------------------+-------------+-----------+------------------------------------------+
        | Header1 - 2      |   IO3       |  I/O      | GPIO – Capabilities are Module Dependent |
        +------------------+-------------+-----------+------------------------------------------+
        | Header1 - 3      |   IO2       |  I/O      | GPIO – Capabilities are Module Dependent |
        +------------------+-------------+-----------+------------------------------------------+
        | Header1 - 4      |   IO1       |  I/O      | GPIO – Capabilities are Module Dependent |
        +------------------+-------------+-----------+------------------------------------------+
        | Header1 - 5      | 3V3 OUT     | Power     | 3.3V Power Output for User               |
        +------------------+-------------+-----------+------------------------------------------+
        | Header2 - 1      |  RESET      |   I       | System Reset, Active Low                 |
        +------------------+-------------+-----------+------------------------------------------+

    .. raw:: html

        </div>

and the ``pdf_custom.css`` file contains this code:

.. code-block:: css

    :root {
        --base-page-orientation: a4 portrait;
        --rotated-page-orientation: a4 landscape;
    }


.. note::

    You can write your own custom CSS to handle page orientation but you must use the **named page** CSS approach like below:
    
    .. code-block:: css

        /* Named page ↓ */
        @page rotated {
          size: A3 landscape;
        }

        .rotated-page {
          page: rotated;
          page-break-before: always;
          page-break-after: always;
        }
