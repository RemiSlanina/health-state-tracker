import pytest
from app.api import app
from starlette.testclient import TestClient

# ****************** HELPER FUNCTIONS ******************
@pytest.fixture
def json_entry():
    return {
        "energy_level": 4,
        "pain_level": 4,
        "sensory_load": 5,
        "food_tolerance": "avocado tolerated",
        "note": "noise"
    }
@pytest.fixture
def invalid_json_entry():
    return {
        "energy_level": 99,
        "pain_level": 400,
        "sensory_load": -5556,
        "food_tolerance": "avocado tolerated",
        "note": "noise"
    }

def test_get_entries_api():
    client = TestClient(app)
    response = client.get("/entries")
    assert response.status_code == 200

def test_get_entry_api(json_entry):
    client = TestClient(app)
    create_response = client.post("/entries", json=json_entry)
    created = create_response.json()
    entry_id = created["id"]
    response = client.get(f"/entries/{entry_id}")
    assert response.status_code == 200
    assert create_response.status_code == 200
    print(create_response.json())

def test_create_entry_api(json_entry):
    client = TestClient(app)
    response = client.post(
        "/entries", json=json_entry )
    assert response.status_code == 200
    assert response.json()["note"] == "noise"
    assert response.json()["energy_level"] == 4
    assert response.json()["pain_level"] == 4
    assert response.json()["sensory_load"] == 5
    assert response.json()["food_tolerance"] == "avocado tolerated"

def test_get_missing_entry_api():
    client = TestClient(app)
    response = client.get("/entries/999999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Entry not found."}

def test_delete_missing_entry_api():
    client = TestClient(app)
    response = client.delete("/entries/999999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Entry not found."}

def test_update_missing_entry_api(json_entry):
    client = TestClient(app)
    response = client.put("/entries/999999", json=json_entry)
    assert response.status_code == 404
    assert response.json() == {"detail": "Entry not found."}

def test_create_entry_invalid_args_api(invalid_json_entry):
    client = TestClient(app)
    response = client.post("/entries", json=invalid_json_entry)
    assert response.status_code == 422

def test_update_entry_invalid_args_api(json_entry, invalid_json_entry):
    client = TestClient(app)
    create_response = client.post("/entries", json=json_entry)
    # unpack json and included id
    created = create_response.json()
    entry_id = created["id"]
    response = client.put(f"/entries/{entry_id}", json=invalid_json_entry)
    assert response.status_code == 422


