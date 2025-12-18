import copy
import pytest

from src import app as app_module
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    # snapshot activities and restore after each test to keep tests isolated
    original = copy.deepcopy(app_module.activities)
    client = TestClient(app_module.app)
    try:
        yield client
    finally:
        app_module.activities.clear()
        app_module.activities.update(original)
