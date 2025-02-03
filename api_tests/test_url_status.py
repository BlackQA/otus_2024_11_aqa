import pytest
import requests


def test_url_status(url_status):
    url, expected_status_code = url_status
    try:
        response = requests.get(url)
        assert response.status_code == expected_status_code
        print(f"URL: {url} returned status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request to {url} failed: {e}")
