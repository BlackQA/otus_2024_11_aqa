import pytest
import requests

BASE_URL = "https://dog.ceo/api"


def test_get_random_breed_image():
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "status" in data
    assert data["status"] == "success"
    assert data["message"].endswith(".jpg")


@pytest.mark.parametrize("breed", ["hound", "bulldog", "doberman"])
def test_get_breed_image(breed):
    response = requests.get(f"{BASE_URL}/breed/{breed}/images/random")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "status" in data
    assert data["status"] == "success"
    assert data["message"].endswith(".jpg")


def test_get_all_breeds():
    response = requests.get(f"{BASE_URL}/breeds/list/all")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "status" in data
    assert data["status"] == "success"
    assert isinstance(data["message"], dict)


@pytest.mark.parametrize("sub_breed", ["hound", "bulldog", "doberman"])
def test_get_sub_breeds(sub_breed):
    response = requests.get(f"{BASE_URL}/breed/{sub_breed}/list")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "status" in data
    assert data["status"] == "success"
    assert isinstance(data["message"], list)


@pytest.mark.parametrize("breed", ["hound", "bulldog", "doberman"])
def test_get_three_breed_images(breed):
    response = requests.get(f"{BASE_URL}/breed/{breed}/images/random/3")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "success"
    assert "message" in data
    assert isinstance(data["message"], list)
    assert len(data["message"]) == 3
    for image_url in data["message"]:
        assert image_url.endswith(".jpg")
