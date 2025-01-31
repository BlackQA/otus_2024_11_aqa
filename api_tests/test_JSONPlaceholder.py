import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert len(response.json()) == 100


def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_get_comments_for_post(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}/comments")
    assert response.status_code == 200
    comments = response.json()
    for comment in comments:
        assert comment["postId"] == post_id


@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_create_post(post_id):
    payload = {"userId": post_id, "title": "foo", "body": "bar"}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["userId"] == post_id
    assert response.json()["title"] == "foo"
    assert response.json()["body"] == "bar"


@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_update_post(post_id):
    payload = {"id": post_id, "title": "foo_updated"}
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == "foo_updated"


def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    assert response.json() == {}
