import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from ..main import app


@pytest.mark.anyio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200


def test_create_album(client: TestClient):
    client = TestClient(app)  #
    test_data = {"name": "Blood Sugar Sex Magik", "artist": "RHCP", "year": "1991"}
    response = client.post("/api/v1/albums", json=test_data)
    data = response.json()
    assert response.status_code == 201

    assert data["name"] == test_data.get("name")
    assert data["artist"] == test_data.get("artist")
