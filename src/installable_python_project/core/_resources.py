from importlib.resources import files
from importlib.resources.abc import Traversable

_ROOT_PACKAGE: Traversable = files("installable_python_project")
_ASSETS_PACKAGE: Traversable = _ROOT_PACKAGE / "assets"


_INITIAL_CONFIGURATION_FILE: Traversable = _ASSETS_PACKAGE / "config.ini"
_INITIAL_CONFIGURATION_FILE_PATH: str = str(_INITIAL_CONFIGURATION_FILE)
