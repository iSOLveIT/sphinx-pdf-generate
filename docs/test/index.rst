:pdf-build: true
:pdf-title: Test Document
:pdf-subtitle: testcase-1a | testcase-1b | testcase-1c
:pdf-type: test
:pdf-filename: Test Case Document
:pdf-revision: 1.10
:pdf-toc_txt: false

==============
rst Cheatsheet
==============

The `rst Cheatsheet <https://github.com/ralsina/rst-cheatsheet>`_ covers a wide range of
rst markup. It and its contents are
`CC licensed <http://creativecommons.org/licenses/by/3.0/de/deed.en_GB>`_.

.. role:: small

Inline Markup
-------------

Inline markup allows words and phrases within text to have character styles (like italics and boldface) and functionality (like hyperlinks).

+----------------------------------------------------------+------------------------------------------------+
| ::                                                       |                                                |
|                                                          |                                                |
|    *emphasis*                                            | *emphasis*                                     |
+----------------------------------------------------------+------------------------------------------------+
| ::                                                       |                                                |
|                                                          |                                                |
|    **strong emphasis**                                   | **strong emphasis**                            |
+----------------------------------------------------------+------------------------------------------------+
| ::                                                       | The rendering and meaning of interpreted text  |
|                                                          | is domain- or application-dependent.           |
|    `interpreted text`                                    |                                                |
+----------------------------------------------------------+------------------------------------------------+
| ::                                                       |                                                |
|                                                          |                                                |
|    ``inline literal``                                    | ``inline literal``                             |
+----------------------------------------------------------+------------------------------------------------+
| ::                                                       |                                                |
|                                                          |                                                |
|    reference_                                            | reference_                                     |
+----------------------------------------------------------+------------------------------------------------+
| ::                                                       |                                                |
|                                                          |                                                |
|    `phrase reference`_                                   | `phrase reference`_                            |
+----------------------------------------------------------+------------------------------------------------+
| ::                                                       |                                                |
|                                                          |                                                |
|    anonymous__                                           | anonymous__                                    |
+----------------------------------------------------------+------------------------------------------------+
| ::                                                       |                                                |
|                                                          |                                                |
|    _`inline internal target`                             | _`inline internal target`                      |
+----------------------------------------------------------+------------------------------------------------+
| ::                                                       | The result is substituted in from the          |
|                                                          | substitution definition.                       |
|    |substitution reference|                              |                                                |
+----------------------------------------------------------+------------------------------------------------+
| ::                                                       |                                                |
|                                                          |                                                |
|    footnote reference [1]_                               | footnote reference [1]_                        |
+----------------------------------------------------------+------------------------------------------------+
| ::                                                       |                                                |
|                                                          |                                                |
|    citation reference [CIT2002]_                         | citation reference [CIT2002]_                  |
+----------------------------------------------------------+------------------------------------------------+
| ::                                                       |                                                |
|                                                          |                                                |
|    http://docutils.sf.net/                               | http://docutils.sf.net/                        |
+----------------------------------------------------------+------------------------------------------------+

__ http://docutils.sourceforge.net/docs/user/rst/quickref.html#hyperlink-targets

.. _reference: http://docutils.sourceforge.net/docs/user/rst/quickref.html#hyperlink-targets

.. _phrase reference: http://docutils.sourceforge.net/docs/user/rst/quickref.html#hyperlink-targets

Escaping with Backslashes
-------------------------

reStructuredText uses backslashes ("\\") to override the special meaning given to markup characters and get
the literal characters themselves. To get a literal backslash, use an escaped backslash ("\\\\"). For example:

+----------------------------------------------------------+------------------------------------------------+
| ::                                                       |                                                |
|                                                          |                                                |
|    *escape* ``with`` "\"                                 | *escape* ``with`` "\"                          |
+----------------------------------------------------------+------------------------------------------------+
| ::                                                       |                                                |
|                                                          |                                                |
|    \*escape* \``with`` "\\"                              | \*escape* \``with`` "\\"                       |
+----------------------------------------------------------+------------------------------------------------+

Lists
-----

+----------------------------------------------------------+------------------------------------------------------+
| ::                                                       |                                                      |
|                                                          |                                                      |
|    - This is item 1. A blank line before the first       |    - This is item 1. A blank line before the first   |
|      and last items is required.                         |      and last items is required.                     |
|    - This is item 2                                      |    - This is item 2                                  |
|                                                          |                                                      |
|    - Item 3: blank lines between items are optional.     |    - Item 3: blank lines between items are optional. |
|    - Item 4: Bullets are "-", "*" or "+".                |    - Item 4: Bullets are "-", "*" or "+".            |
|      Continuing text must be aligned after the bullet    |      Continuing text must be aligned after the bullet|
|      and whitespace.                                     |      and whitespace.                                 |
|    - This list item contains nested items                |    - This list item contains nested items            |
|                                                          |                                                      |
|      - Nested items must be indented to the same         |      - Nested items must be indented to the same     |
|        level                                             |        level                                         |
+----------------------------------------------------------+------------------------------------------------------+
| ::                                                       |                                                      |
|                                                          |                                                      |
|    3. This is the first item                             |    3. This is the first item                         |
|    4. This is the second item                            |    4. This is the second item                        |
|    5. Enumerators are arabic numbers,                    |    5. Enumerators are arabic numbers,                |
|       single letters, or roman numerals                  |       single letters, or roman numerals              |
|    6. List items should be sequentially                  |    6. List items should be sequentially              |
|       numbered, but need not start at 1                  |       numbered, but need not start at 1              |
|       (although not all formatters will                  |       (although not all formatters will              |
|       honour the first index).                           |       honour the first index).                       |
|    #. This item is auto-enumerated                       |    #. This item is auto-enumerated                   |
+----------------------------------------------------------+------------------------------------------------------+
| ::                                                       |                                                      |
|                                                          |                                                      |
|    what                                                  |    what                                              |
|      Definition lists associate a term with              |      Definition lists associate a term with          |
|      a definition.                                       |      a definition.                                   |
|                                                          |                                                      |
|    how                                                   |    how                                               |
|      The term is a one-line phrase, and the              |      The term is a one-line phrase, and the          |
|      definition is one or more paragraphs or             |      definition is one or more paragraphs or         |
|      body elements, indented relative to the             |      body elements, indented relative to the         |
|      term. Blank lines are not allowed                   |      term. Blank lines are not allowed               |
|      between term and definition.                        |      between term and definition.                    |
+----------------------------------------------------------+------------------------------------------------------+
| ::                                                       |                                                      |
|                                                          |                                                      |
|    :Authors:                                             |    :Authors:                                         |
|        Tony J. (Tibs) Ibbs,                              |        Tony J. (Tibs) Ibbs,                          |
|        David Goodger                                     |        David Goodger                                 |
|                                                          |                                                      |
|    :Version: 1.0 of 2001/08/08                           |    :Version: 1.0 of 2001/08/08                       |
|    :Dedication: To my father.                            |    :Dedication: To my father.                        |
+----------------------------------------------------------+------------------------------------------------------+
| ::                                                       |                                                      |
|                                                          |                                                      |
|    -a            command-line option "a"                 |    -a            command-line option "a"             |
|    -b file       options can have arguments              |    -b file       options can have arguments          |
|                  and long descriptions                   |                  and long descriptions               |
|    --long        options can be long also                |    --long        options can be long also            |
|    --input=file  long options can also have              |    --input=file  long options can also have          |
|                  arguments                               |                  arguments                           |
|    /V            DOS/VMS-style options too               |    /V            DOS/VMS-style options too           |
+----------------------------------------------------------+------------------------------------------------------+

.. raw:: pdf

   Spacer 0 72

Section Structure
-----------------

+----------------------------------------------------------+--------------------------------------------------------+
| ::                                                       |                                                        |
|                                                          |                                                        |
|    Title                                                 |                                                        |
|    =====                                                 |   Title                                                |
|                                                          |                                                        |
|    Titles are underlined (or over- and underlined) with  |   Titles are underlined (or over- and underlined) with |
|    a nonalphanumeric character at least as long as the   |   a nonalphanumeric character at least as long as the  |
|    text.                                                 |   text.                                                |
|                                                          |                                                        |
|    A lone top-level section is lifted up to be the       |   A lone top-level section is lifted up to be the      |
|    document's title.                                     |   document's title.                                    |
|                                                          |                                                        |
|    Any non-alphanumeric character can be used, but       |   Any non-alphanumeric character can be used, but      |
|    Python convention is:                                 |   Python convention is:                                |
|                                                          |                                                        |
|    * ``#`` with overline, for parts                      |   * ``#`` with overline, for parts                     |
|    * ``*`` with overline, for chapters                   |   * ``*`` with overline, for chapters                  |
|    * ``=``, for sections                                 |   * ``=``, for sections                                |
|    * ``-``, for subsections                              |   * ``-``, for subsections                             |
|    * ``^``, for subsubsections                           |   * ``^``, for subsubsections                          |
|    * ``"``, for paragraphs                               |   * ``"``, for paragraphs                              |
+----------------------------------------------------------+--------------------------------------------------------+

Blocks
------

+---------------------------------------------------------------+------------------------------------------------------+
| ::                                                            |                                                      |
|                                                               |                                                      |
|    This is a paragraph.                                       | This is a paragraph.                                 |
|                                                               |                                                      |
|    Paragraphs line up at their left edges, and are            | Paragraphs line up at their left                     |
|    normally separated by blank lines.                         | edges, and are normally separated                    |
|                                                               | by blank lines.                                      |
+---------------------------------------------------------------+------------------------------------------------------+
| ::                                                            |                                                      |
|                                                               |                                                      |
|    A paragraph containing only two colons indicates           |    A paragraph containing only two colons            |
|    the following indented or quoted text is a literal         |    indicates that the following indented             |
|    block or quoted text is a literal block.                   |    or quoted text is a literal block.                |
|                                                               |                                                      |
|    ::                                                         |    ::                                                |
|                                                               |                                                      |
|      Whitespace, newlines, blank lines, and  all kinds of     |      Whitespace, newlines, blank lines, and          |
|      markup (like *this* or \this) is preserved here.         |      all kinds of markup (like *this* or             |
|                                                               |      \this) is preserved by literal blocks.          |
|    You can also tack the ``::`` at the end of a               |                                                      |
|    paragraph::                                                |    You can also tack the ``::`` at the end of a      |
|                                                               |    paragraph::                                       |
|       It's very convenient to use this form.                  |                                                      |
|                                                               |      It's very convenient to use this form.          |
|    Per-line quoting can also be used for unindented           |                                                      |
|    blocks::                                                   |    Per-line quoting can also be used for             |
|                                                               |    unindented blocks::                               |
|    > Useful for quotes from email and                         |                                                      |
|    > for Haskell literate programming.                        |    > Useful for quotes from email and                |
|                                                               |    > for Haskell literate programming.               |
+---------------------------------------------------------------+------------------------------------------------------+
| ::                                                            |                                                      |
|                                                               |                                                      |
|    | Line blocks are useful for addresses,                    |    | Line blocks are useful for addresses,           |
|    | verse, and adornment-free lists.                         |    | verse, and adornment-free lists.                |
|    |                                                          |    |                                                 |
|    | Each new line begins with a                              |    | Each new line begins with a                     |
|    | vertical bar ("|").                                      |    | vertical bar ("|").                             |
|    |     Line breaks and initial indents                      |    |     Line breaks and initial indents             |
|    |     are preserved.                                       |    |     are preserved.                              |
|    | Continuation lines are wrapped                           |    | Continuation lines are wrapped                  |
|      portions of long lines; they begin                       |      portions of long lines; they begin              |
|      with spaces in place of vertical bars.                   |      with spaces in place of vertical bars.          |
+---------------------------------------------------------------+------------------------------------------------------+
| ::                                                            |                                                      |
|                                                               |                                                      |
|   Block quotes are just:                                      |   Block quotes are just:                             |
|                                                               |                                                      |
|       Indented paragraphs,                                    |       Indented paragraphs,                           |
|                                                               |                                                      |
|           and they may nest.                                  |           and they may nest.                         |
+---------------------------------------------------------------+------------------------------------------------------+
| ::                                                            |                                                      |
|                                                               |                                                      |
|   Doctest blocks are interactive                              |   Doctest blocks are interactive                     |
|   Python sessions. They begin with                            |   Python sessions. They begin with                   |
|   "``>>>``" and end with a blank line.                        |   "``>>>``" and end with a blank line.               |
|                                                               |                                                      |
|   >>> print "This is a doctest block."                        |   >>> print "This is a doctest block."               |
|   This is a doctest block.                                    |   This is a doctest block.                           |
+---------------------------------------------------------------+------------------------------------------------------+
| ::                                                            |                                                      |
|                                                               |                                                      |
|   A transition marker is a horizontal line                    |   A transition marker is a horizontal line           |
|   of 4 or more repeated punctuation                           |   of 4 or more repeated punctuation                  |
|   characters.                                                 |   characters.                                        |
|                                                               |                                                      |
|   ------------                                                |                                                      |
|                                                               |                                                      |
|   A transition should not begin or end a                      |   +-----------+                                      |
|   section or document, nor should two                         |   |           |                                      |
|   transitions be immediately adjacent.                        |   +-----------+                                      |
|                                                               |                                                      |
|                                                               |                                                      |
|                                                               |   A transition should not begin or end a             |
|                                                               |   section or document, nor should two                |
|                                                               |   transitions be immediately adjacent.               |
+---------------------------------------------------------------+------------------------------------------------------+

.. raw:: pdf

   PageBreak

Tables
------

There are two syntaxes for tables in reStructuredText. Grid tables are complete but cumbersome to create. Simple
tables are easy to create but limited (no row spans, etc.).

+---------------------------------------------------------------+------------------------------------------------------+
| ::                                                            |                                                      |
|                                                               |                                                      |
|                                                               |                                                      |
|   +------------+------------+-----------+                     |   +------------+------------+-----------+            |
|   | Header 1   | Header 2   | Header 3  |                     |   | Header 1   | Header 2   | Header 3  |            |
|   +============+============+===========+                     |   +============+============+===========+            |
|   | body row 1 | column 2   | column 3  |                     |   | body row 1 | column 2   | column 3  |            |
|   +------------+------------+-----------+                     |   +------------+------------+-----------+            |
|   | body row 2 | Cells may span columns.|                     |   | body row 2 | Cells may span columns.|            |
|   +------------+------------+-----------+                     |   +------------+------------+-----------+            |
|   | body row 3 | Cells may  | - Cells   |                     |   | body row 3 | Cells may  | - Cells   |            |
|   +------------+ span rows. | - contain |                     |   +------------+ span rows. | - contain |            |
|   | body row 4 |            | - blocks. |                     |   | body row 4 |            | - blocks. |            |
|   +------------+------------+-----------+                     |   +------------+------------+-----------+            |
+---------------------------------------------------------------+------------------------------------------------------+
| ::                                                            |                                                      |
|                                                               |                                                      |
|                                                               |                                                      |
|   =====  =====  ======                                        |   =====  =====  ======                               |
|      Inputs     Output                                        |      Inputs     Output                               |
|   ------------  ------                                        |   ------------  ------                               |
|     A      B    A or B                                        |     A      B    A or B                               |
|   =====  =====  ======                                        |   =====  =====  ======                               |
|   False  False  False                                         |   False  False  False                                |
|   True   False  True                                          |   True   False  True                                 |
|   False  True   True                                          |   False  True   True                                 |
|   True   True   True                                          |   True   True   True                                 |
|   =====  =====  ======                                        |   =====  =====  ======                               |
+---------------------------------------------------------------+------------------------------------------------------+


Credits
-------

+---------------------------------------+-------------------------------------------------------+
| CP Font from LiquiType:               | http://www.liquitype.com/workshop/type_design/cp-mono |
+---------------------------------------+-------------------------------------------------------+
| Magnetic Balls V2 image by fdecomite: | http://www.flickr.com/photos/fdecomite/2926556794/    |
+---------------------------------------+-------------------------------------------------------+
| Sponsored by Net Managers             | http://www.netmanagers.com.ar                         |
+---------------------------------------+-------------------------------------------------------+
| Typeset using rst2pdf                 | http://rst2pdf.googlecode.com                         |
+---------------------------------------+-------------------------------------------------------+
