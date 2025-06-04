import pytest
from pathlib import Path

@pytest.fixture
def get_data_dir():
    data_dir = Path(__file__).parent / "data"
    data_dir.mkdir(exist_ok=True)
    return data_dir
