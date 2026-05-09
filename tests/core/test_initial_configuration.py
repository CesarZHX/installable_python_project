from installable_python_project.core._initial_configuration import (
    _APP_AUTHOR,
    _APP_NAME,
)


def test_initial_configuration() -> None:
    assert _APP_NAME and _APP_AUTHOR
