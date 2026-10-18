import os
from pathlib import Path

import pytest

from config import Config


def test_config_attributes_present():
    """Basic sanity checks for configuration attributes."""
    # Core attributes
    assert isinstance(Config.VANE_ROOT_ID, str) and len(Config.VANE_ROOT_ID) > 0
    assert isinstance(Config.BASE_DIR, Path)

    # Workspace directory should be a Path and exist (config.py creates it)
    assert hasattr(Config, "WORKSPACE_DIR")
    assert isinstance(Config.WORKSPACE_DIR, Path) or isinstance(Config.WORKSPACE_DIR, str)

    # Vector DB and LLM settings
    assert isinstance(Config.CHROMA_PERSIST_DIR, str) and "chroma_db" in Config.CHROMA_PERSIST_DIR
    assert isinstance(Config.EMBEDDING_MODEL, str)
    assert isinstance(Config.LLM_MODEL, str)

    # Numeric settings and ranges
    assert isinstance(Config.TEMPERATURE, float)
    assert isinstance(Config.MAX_TOKENS, int)
    assert isinstance(Config.API_TIMEOUT, float)
    assert isinstance(Config.MAX_SEARCH_RESULTS, int)

    # Confidence thresholds: 0.0 <= medium <= high <= 1.0
    assert 0.0 <= Config.CONFIDENCE_MEDIUM_THRESHOLD <= Config.CONFIDENCE_HIGH_THRESHOLD <= 1.0


def test_workspace_dir_writable(tmp_path, monkeypatch):
    """Verify that workspace directory is writable by creating a temporary marker file."""
    # Point the VANE_ROOT_ID to a temp location to avoid polluting repo workspace during tests
    monkeypatch.setenv("VANE_ROOT_ID", "TEST_VANE_ROOT_ID_FOR_CI")

    # Re-importing the config module in the same process won't re-run class body; import via importlib
    import importlib
    import sys

    # Remove config from sys.modules if present then reload to pick up monkeypatched env
    if "config" in sys.modules:
        del sys.modules["config"]
    cfg = importlib.import_module("config")

    workspace = Path(cfg.Config.WORKSPACE_DIR)
    workspace.mkdir(parents=True, exist_ok=True)

    marker = workspace / "ci_marker.txt"
    marker.write_text("ok")
    assert marker.exists()
    assert marker.read_text() == "ok"

    # cleanup
    marker.unlink()
