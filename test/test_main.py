from fastapi.testclient import TestClient
from itertools import combinations
from . import (
    app,
    mocked_data,
    remove_same_source_and_target,
    remove_duplicated_in_data,
    format_distance_to_int,
)

client = TestClient(app)


def test_graph_creation():
    response = client.post("/create_graph", json=mocked_data.valid_graph)
    assert response.status_code == 201
    assert type(response.json()["id"]) == int
    assert response.json()["id"] > 0


def test_graph_creation_invalid_data():
    response = client.post("/create_graph", json=mocked_data.invalid_graph)

    formated_data = remove_same_source_and_target(
        remove_duplicated_in_data(mocked_data.invalid_graph["data"])
    )
    assert response.status_code == 201
    assert type(response.json()["id"]) == int
    assert response.json()["id"] > 0
    assert format_distance_to_int(response.json()["data"]) == formated_data


def test_get_graph():
    created_graph = client.post("/create_graph", json=mocked_data.valid_graph)
    created_graph_id = created_graph.json()["id"]
    response = client.get(f"/graph/{created_graph_id}")
    assert response.status_code == 200
    assert response.json()["id"] == created_graph.json()["id"]
    assert response.json()["data"] == created_graph.json()["data"]


def test_get_graph_not_found():
    response = client.get("/graph/0")
    assert response.status_code == 404
    assert response.json()["detail"] == "Graph not found"


def test_get_all_routes_no_maxstops():
    created_graph = client.post(
        "/create_graph", json=mocked_data.valid_graph_all_routes_no_maxstops
    )
    created_graph_id = created_graph.json()["id"]
    response = client.post(f"/routes/{created_graph_id}/from/A/to/C")
    assert response.status_code == 200
    assert response.json() == mocked_data.valid_graph_all_routes_response_no_maxstops
