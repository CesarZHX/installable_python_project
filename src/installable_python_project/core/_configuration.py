from platformdirs import PlatformDirs

from ._initial_configuration import _APP_AUTHOR, _APP_NAME

_PLATFORM_DIRS: PlatformDirs = PlatformDirs(_APP_NAME, _APP_AUTHOR)


_USER_DATA_DIR_PATH: str = _PLATFORM_DIRS.user_data_dir
_USER_LOG_DIR_PATH: str = _PLATFORM_DIRS.user_log_dir
