from typing import Any, Dict


class _FilterBase:
    def __init__(self, options: object, config: Dict[str, Any]):
        self.__options = options
        self.__config = config

    @property
    def options(self) -> object:
        return self.__options

    @property
    def config(self) -> Dict[str, Any]:
        return self.__config

    def __call__(self, *args: Any) -> Exception:
        raise Exception("must be overridden")
