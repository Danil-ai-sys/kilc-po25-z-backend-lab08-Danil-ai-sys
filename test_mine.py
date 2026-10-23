from fastapi.testclient import TestClient

from app.deps import get_storage
from app.main import app
from app.storage import Storage

client = TestClient(app)


def setup_function():
    store = Storage()
    app.dependency_overrides[get_storage] = lambda: store


def teardown_function():
    app.dependency_overrides.clear()


def test_message_from_another_room_returns_404():
    client.post("/rooms", json={"title": "general"})
    client.post("/rooms", json={"title": "homework"})

    client.post(
        "/rooms/1/messages",
        json={"author": "Aida", "text": "hello"},
    )

    response_from_wrong_room = client.get("/rooms/2/messages/1")
    response_from_correct_room = client.get("/rooms/1/messages/1")

    assert response_from_wrong_room.status_code == 404
    assert response_from_wrong_room.json()["code"] == "message_not_found"

    assert response_from_correct_room.status_code == 200
    assert response_from_correct_room.json()["id"] == 1