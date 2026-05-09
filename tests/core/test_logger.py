from installable_python_project.core.logger import logger


def test_logger() -> None:
    assert logger.debug("Logger is working.") is None
