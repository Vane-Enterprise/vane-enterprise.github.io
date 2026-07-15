# tests/test_config.py
import pytest
from config import Config

def test_config_initialization():
    """Test that Config initializes properly."""
    assert Config.VANE_ROOT_ID is not None
    assert Config.WORKSPACE_DIR is not None
