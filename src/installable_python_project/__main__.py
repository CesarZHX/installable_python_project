from retry import retry

from .core.logger import logger
from .core.paths import USER_DATA_DIR


@retry(tries=3, delay=1, backoff=2, max_delay=2)
def main() -> None:
    logger.info("App started.")
    logger.info(f"User data directory: '{USER_DATA_DIR}'.")


if __name__ == "__main__":
    main()
