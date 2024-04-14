from app.main import app
from fastapi.testclient import TestClient
import pytest


@pytest.fixture
def client():
    client = TestClient(app)
    return client
