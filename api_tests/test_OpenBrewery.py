import pytest
import requests

BASE_URL = "https://api.openbrewerydb.org"

breweries = [
    pytest.param("5128df48-79fc-4f0f-8b52-d06be54d0cec", id="Brewery 1"),
    pytest.param("e432899b-7f58-455f-9c7b-9a6e2130a1e0", id="Brewery 2"),
    pytest.param("6d14b220-8926-4521-8d19-b98a2d6ec3db", id="Brewery 3"),
    pytest.param("ef970757-fe42-416f-931d-722451f1f59c", id="Brewery 4"),
    pytest.param("9c5a66c8-cc13-416f-a5d9-0a769c87d318", id="Brewery 5"),
]


def test_get_breweries():
    response = requests.get(f"{BASE_URL}/breweries")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


@pytest.mark.parametrize("brewery_id", breweries)
def test_get_single_brewery(brewery_id):
    response = requests.get(f"{BASE_URL}/breweries/{brewery_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == brewery_id


@pytest.mark.parametrize("brewery_type", ["micro", "regional", "brewpub"])
def test_get_breweries_by_type(brewery_type):
    response = requests.get(f"{BASE_URL}/breweries", params={"by_type": brewery_type})
    assert response.status_code == 200
    data = response.json()
    for brewery in data:
        assert brewery["brewery_type"] == brewery_type


@pytest.mark.parametrize("page", [1, 2, 3])
def test_get_breweries_pagination(page):
    response = requests.get(f"{BASE_URL}/breweries", params={"page": page})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


@pytest.mark.parametrize("per_page", [10, 20, 50])
def test_get_breweries_per_page(per_page):
    response = requests.get(f"{BASE_URL}/breweries", params={"per_page": per_page})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= per_page
