from fastapi.testclient import TestClient
import pytest

from app.models.position import PositionCreate
from app.testing import generate_random


ENDPOINT = "/positions"


@pytest.fixture
def position_in_db(test_client: TestClient) -> dict:
    new_position = generate_random(PositionCreate)
    res = test_client.post(f"{ENDPOINT}/", json=new_position)
    return res.json()


def test_create_new_position(test_client: TestClient):
    # Generate a position
    new_position = generate_random(PositionCreate)

    # Post it
    res = test_client.post(f"{ENDPOINT}/", json=new_position)

    # Check that return value is DB representation
    res.raise_for_status()
    data = res.json()
    assert data["title"] == new_position["title"]
    assert data.get("id")
    assert data.get("created_on")
    assert data.get("updated_on")


def test_list_positions(test_client: TestClient, position_in_db: dict):
    # List positions
    res = test_client.get(f"{ENDPOINT}/")

    # Check that at least one expected id is included
    res.raise_for_status()
    data = res.json()
    assert len(data) > 0
    assert position_in_db["id"] in list(map(lambda x: x["id"], data))


def test_get_position(test_client: TestClient, position_in_db: dict):
    # Get a single known position
    res = test_client.get(f"{ENDPOINT}/{position_in_db['id']}")

    # Check that it's the one we know
    res.raise_for_status()
    data = res.json()
    assert data == position_in_db


def test_delete_position(test_client: TestClient, position_in_db: dict):
    # Delete the single known position
    test_client.delete(f"{ENDPOINT}/{position_in_db['id']}")

    # Test that it's gone
    with pytest.raises(Exception):  # TODO: Test specific HTTPError here
        res = test_client.get(f"{ENDPOINT}/{position_in_db['id']}")
