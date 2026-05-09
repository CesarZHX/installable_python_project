from sys import stderr

from loguru import logger

from ._configuration import _USER_LOG_DIR_PATH

_TIME: str = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>"
_LEVEL: str = "<level>{level: <8}</level>"
_LOCATION: str = "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"
_MESSAGE: str = "{extra} - <level>{message}</level>"
_LOGGER_FORMAT: str = " | ".join((_TIME, _LEVEL, _LOCATION, _MESSAGE))
_SINK: str = f"{_USER_LOG_DIR_PATH}/{{time:YYYY-MM-DD}}.log"


logger.remove()


logger.add(stderr, format=_LOGGER_FORMAT, enqueue=True)
logger.add(
    _SINK,
    rotation="1 day",
    retention="30 days",
    compression="zip",
    enqueue=True,
    backtrace=False,
    diagnose=True,
    format=_LOGGER_FORMAT,
)
