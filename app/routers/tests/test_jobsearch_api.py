from fastapi.testclient import TestClient


ENDPOINT = "/search"


def test_start_new_search(test_client: TestClient):
    new_search = {
        "desired_title": "Senior Title Inflator",
        "desired_salary": {
            "lower_bound": 10000000,
        },
    }
    req = test_client.post(f"{ENDPOINT}/", json=new_search)

    req.raise_for_status()
    assert req.json()["desired_title"] == "Senior Title Inflator"


def test_list_searches(test_client: TestClient):
    searches = test_client.get(f"{ENDPOINT}/")
