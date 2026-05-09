from installable_python_project.core.paths import USER_DATA_DIR


def test_user_data_dir_exists() -> None:
    assert USER_DATA_DIR.exists()
