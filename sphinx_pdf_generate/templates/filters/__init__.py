from typing import Any, Dict

from sphinx.application import Sphinx


class _FilterBase:
    def __init__(self, options: object, config: Dict[str, Any]):
        self.__options = options
        self.__config = config

    @property
    def options(self):
        return self.__options

    @property
    def config(self):
        return self.__config

    def __call__(self, *args):
        raise "must be overridden"
