from installable_python_project.core._configuration import (
    _USER_DATA_DIR_PATH,
    _USER_LOG_DIR_PATH,
)


def test_configuration() -> None:
    assert _USER_DATA_DIR_PATH and _USER_LOG_DIR_PATH
