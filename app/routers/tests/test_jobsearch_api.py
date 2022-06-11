from fastapi.testclient import TestClient
import pytest

from app.models.job_search import JobSearchCreate
from app.testing import generate_random


ENDPOINT = "/search"


@pytest.fixture
def search_in_db(test_client: TestClient) -> dict:
    new_search = generate_random(JobSearchCreate)
    res = test_client.post(f"{ENDPOINT}/", json=new_search)
    return res.json()


def test_start_new_search(test_client: TestClient):
    # Generate a search
    new_search = generate_random(JobSearchCreate)

    # Post it
    res = test_client.post(f"{ENDPOINT}/", json=new_search)

    # Check that return value is DB representation
    res.raise_for_status()
    data = res.json()
    assert data["desired_title"] == new_search["desired_title"]
    assert data.get("id")
    assert data.get("created_on")
    assert data.get("updated_on")


def test_list_searches(test_client: TestClient, search_in_db: dict):
    # List searches
    res = test_client.get(f"{ENDPOINT}/")

    # Check that at least one expected id is included
    res.raise_for_status()
    data = res.json()
    assert len(data) > 0
    assert search_in_db["id"] in list(map(lambda x: x["id"], data))


def test_get_search(test_client: TestClient, search_in_db: dict):
    # Get a single known search
    res = test_client.get(f"{ENDPOINT}/{search_in_db['id']}")

    # Check that it's the one we know
    res.raise_for_status()
    data = res.json()
    assert data == search_in_db
