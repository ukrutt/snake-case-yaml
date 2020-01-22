"""Common fixtures."""

import os

import pytest


@pytest.fixture
def test_root():
    """Switch out of the project root.

    This way we don't stomp on log and CSV output files during testing.
    """
    start_dir = os.getcwd()
    os.chdir("tests/test_root/")
    yield
    # Teardown comes after yield
    os.chdir(start_dir)
