import pytest
from app.api import app
from starlette.testclient import TestClient


def test_get_entries_api():
    client = TestClient(app)
    response = client.get("/entries")
    assert response.status_code == 200

def test_get_entry_api():
    client = TestClient(app)
    create_response = client.post("/entries", json={
        "energy_level": 4,
        "pain_level": 4,
        "sensory_load": 5,
        "food_tolerance": "avocado tolerated",
        "note": "noise"
    },)
    # unpack json and included id
    created = create_response.json()
    entry_id = created["id"]
    # fetch the entry that got created and test it:
    response = client.get(f"/entries/{entry_id}")
    assert response.status_code == 200
    assert create_response.status_code == 200
    print(create_response.json())

def test_create_entry_api():
    client = TestClient(app)
    response = client.post(
        "/entries", json={
        "energy_level": 4,
        "pain_level": 4,
        "sensory_load": 5,
        "food_tolerance": "avocado tolerated",
        "note": "noise"
        },
    )
    assert response.status_code == 200
    assert response.json()["note"] == "noise"
    assert response.json()["energy_level"] == 4
    assert response.json()["pain_level"] == 4
    assert response.json()["sensory_load"] == 5
    assert response.json()["food_tolerance"] == "avocado tolerated"
    # print(response.json())
    # print(response.request.method)
    # print(response.request.url)
    # print(response.request.headers)
    # print(response.request.content)

