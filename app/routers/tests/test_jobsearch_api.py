from fastapi.testclient import TestClient


ENDPOINT = "/search"


def test_start_new_search(test_client: TestClient):
    new_search = {
        "desired_title": "Senior Title Inflator",
        "desired_salary": 10000000,
    }
    res = test_client.post(f"{ENDPOINT}/", json=new_search)

    res.raise_for_status()
    data = res.json()
    assert data["desired_title"] == "Senior Title Inflator"
    assert data.get("id")
    assert data.get("created_on")
    assert data.get("updated_on")


def test_list_searches(test_client: TestClient):
    # TODO: Add some specific test searches
    res = test_client.get(f"{ENDPOINT}/")

    res.raise_for_status()
    data = res.json()
    # TODO: Assert specific searches are here
    assert len(data) > 0


# TODO: Test get search
