"""Logic for interacting with sphinx-build."""

import shlex
import subprocess
import sys
from typing import List, Optional, Union

from colorama import Fore, Style

SPHINX_BUILD_OPTIONS = (
    ("b", "builder"),
    ("a", None),
    ("E", None),
    ("d", "path"),
    ("j", "N"),
    ("c", "path"),
    ("C", None),
    ("D", "setting=value"),
    ("t", "tag"),
    ("A", "name=value"),
    ("n", None),
    ("v", None),
    ("q", None),
    ("Q", None),
    ("w", "file"),
    ("W", None),
    ("T", None),
    ("N", None),
    ("P", None),
)


def _log(text: str, *, colour: str) -> None:
    print(f"{Fore.GREEN}[sphinx-pdf-generate] {colour}{text}{Style.RESET_ALL}")


def show(*, context: Optional[str] = None, command: Union[list, tuple, None] = None, error: Optional[bool] = None):
    """Show context and command-to-be-executed, with nice formatting and colors."""
    if context is not None:
        _log(context, colour=Fore.CYAN)
    if command is not None:
        assert isinstance(command, (list, tuple))
        _log("> " + " ".join(shlex.quote(s) for s in command), colour=Fore.BLUE)
    if error is not None:
        _log(context, colour=Fore.RED)


def get_builder(sphinx_args: List[str]) -> int:
    """Prepare the function that calls sphinx."""
    sphinx_command = [sys.executable, "-m", "sphinx"] + sphinx_args

    def build() -> int:
        """Generate the documentation using ``sphinx``."""

        try:
            remove_dir_command = ["rm", "-fr", sphinx_args[-1]]
            subprocess.run(remove_dir_command, check=True)
            show(command=["sphinx-build"] + sphinx_args)
            sphinx_build = subprocess.run(sphinx_command, check=True)
            return sphinx_build.returncode
        except subprocess.CalledProcessError as e:
            print(f"Command exited with exit code: {e.returncode}")
            return e.returncode

    return build()
