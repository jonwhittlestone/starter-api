from starlette.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_root():
    response = client.get("/health")
    print(response)
    assert response.status_code == 200

# def test_create_album(test_app, monkeypatch):
#     test_data = {"name": "something", 
#                  "artist": "yazz", 
#                  "year": 1981}

#     def mock_post(db_session, payload):
#         return test_data

#     monkeypatch.setattr(crud, "post", mock_post)

#     response = test_app.post("/notes/", content=json.dumps(test_data),)
#     assert response.status_code == 201
#     assert response.json() == test_data
