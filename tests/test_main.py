"""
A simple starter test.

Run all tests with:
    pip install pytest
    pytest
"""

import os
import sys

# Make the "src" folder importable from here.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from utils.helpers import get_logger  # noqa: E402


def test_logger_is_created():
    """The logger should be created without errors."""
    log = get_logger("test")
    assert log is not None
    log.info("Test log message — the logger works!")
