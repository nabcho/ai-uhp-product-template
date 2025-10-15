from fastapi.testclient import TestClient
from app.main import app

def test_root():
    client = TestClient(app)
    r = client.get("/")
    assert r.status_code == 200
