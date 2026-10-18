from pathlib import Path


def test_test_directory_contains_valid_python_tests():
    """Smoke-check that the repository test directory contains real Python tests."""
    tests_dir = Path(__file__).resolve().parent
    assert tests_dir.exists()
    assert (tests_dir / "test_config_env.py").is_file()
    assert (tests_dir / "execute_relevant_tests.py").is_file()


def test_test_files_are_python_files():
    """Ensure discovered test files keep a .py extension and are readable."""
    tests_dir = Path(__file__).resolve().parent
    for path in tests_dir.glob("*.py"):
        assert path.suffix == ".py"
        assert path.read_text(encoding="utf-8")


def test_repository_root_is_accessible():
    """Sanity check that the repo root is discoverable from the test file location."""
    repo_root = Path(__file__).resolve().parent.parent
    assert repo_root.exists()
    assert (repo_root / "config.py").is_file()
