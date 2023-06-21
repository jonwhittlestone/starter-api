from starlette.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    print(response)
    assert response.status_code == 200
