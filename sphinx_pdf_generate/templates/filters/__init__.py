from typing import Any, Dict

from sphinx_pdf_generate.options import Options


class _FilterBase:
    def __init__(self, options: Options, config: Dict[str, Any]):
        self.__options = options
        self.__config = config

    @property
    def options(self) -> Options:
        return self.__options

    @property
    def config(self) -> Dict[str, Any]:
        return self.__config

    def __call__(self, *args: Any) -> Exception:
        raise Exception("must be overridden")
