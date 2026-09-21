import os
import sys
from pathlib import Path
import pytest

# Add src to PYTHONPATH so tests can import maya
src_path = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(src_path))

@pytest.fixture(autouse=True)
def setup_test_env():
    """Setup test environment variables."""
    os.environ["MAYA_ENV"] = "test"
    os.environ["MAYA_DEBUG"] = "true"
    yield
    # Teardown can happen here
