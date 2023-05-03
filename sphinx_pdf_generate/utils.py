import os
import re
from typing import Any, Dict, List, Optional, Tuple, Union

from bs4 import BeautifulSoup, PageElement

PDF_LOCAL_OPTIONS: List[Tuple[str, Union[bool, str, None]]] = [
    ("pdf-build", True),
    ("pdf-title", None),
    ("pdf-subtitle", []),
    ("pdf-type", "document"),
    ("pdf-filename", None),
    ("pdf-revision", None),
]


def get_pdf_metadata(pdf_metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Function for parsing RST file metadata. The metadata includes the ff.:

    - pdf-build: default to True
    - pdf-title: default to None
    - pdf-subtitle: default to empty list []. If a value is provided then the list must be separated by the ``|`` symbol
    - pdf-type: default to "document"
    - pdf-filename: default to None
    - pdf-revision: default to None
    - pdf-toc_txt: default to False

    :param pdf_metadata: A dictionary object containing the metadata of a page.
    :return: Dictionary object containing parsed metadata.
    """

    pdf_metadata = {} if pdf_metadata is None else pdf_metadata
    pdf_meta: Dict[str, Any] = {}

    for option, default_value in PDF_LOCAL_OPTIONS:
        option_value = default_value
        if option in pdf_metadata:
            option_value = pdf_metadata.get(option)
            if option == "pdf-build":
                option_value = option_value.lower() != "false"
            elif option == "pdf-toc_txt":
                option_value = option_value.lower() == "true"
            elif option == "pdf-subtitle":
                option_value = [item.strip() for item in option_value.split("|")]

        pdf_meta.update([(option.replace("pdf-", "", 1), option_value)])
    return pdf_meta


def secure_filename(filename):
    r"""Pass it a filename, and it will return a secure version of it.  This
    filename can then safely be stored on a regular file system and passed
    to :func:`os.path.join`.  The filename returned is an ASCII only string
    for maximum portability.

    On Windows systems the function also makes sure that the file is not
    named after one of the special device files.

    >>> secure_filename("My cool movie.mov")
    'My_cool_movie.mov'
    >>> secure_filename("../../../etc/passwd")
    'etc_passwd'
    >>> secure_filename(u'i contain cool \xfcml\xe4uts.txt')
    'i_contain_cool_umlauts.txt'

    The function might return an empty filename.  It's your responsibility
    to ensure that the filename is unique and that you generate random
    filename if the function returned an empty one.

    :param filename: the filename to secure
    """
    _filename_ascii_strip_re = re.compile(r"[^A-Za-z0-9_.-]")
    _windows_device_files = (
        "CON",
        "AUX",
        "COM1",
        "COM2",
        "COM3",
        "COM4",
        "LPT1",
        "LPT2",
        "LPT3",
        "PRN",
        "NUL",
    )

    for sep in os.path.sep, os.path.altsep:
        if sep:
            filename = filename.replace(sep, " ")
    filename = str(_filename_ascii_strip_re.sub("", "_".join(filename.split()))).strip("._")

    # on nt a couple of special files are present in each folder.  We
    # have to ensure that the target file is not such a filename.  In
    # this case we prepend an underline
    if os.name == "nt" and filename and filename.split(".")[0].upper() in _windows_device_files:
        filename = "_" + filename

    return filename


def h1_title_tag(content: Union[str, PageElement], pdf_title: str) -> Optional[str]:
    soup = content
    if isinstance(soup, str):
        soup = BeautifulSoup(soup, "html5lib")
    title = soup.find("h1", attrs={"id": re.compile(r"[\w\-]+")})
    if title is None:
        return pdf_title
    title = re.sub(r"^[\d.]+ ", "", title.text)
    return title.rstrip("¶")
