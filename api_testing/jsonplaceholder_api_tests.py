import pytest
import requests
from pydantic import BaseModel

class PostModel(BaseModel):
    userId: int
    id: int
    title: str
    body: str

@pytest.mark.parametrize("post_id", [1, 5])
def test_get_post_by_id(base_url, post_id):
    response = requests.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == 200
    post = PostModel(**response.json())
    assert post.id == post_id

def test_get_all_posts(base_url):
    response = requests.get(f"{base_url}/posts")
    assert response.status_code == 200
    assert len(response.json()) == 100

def test_create_post(base_url):
    data = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(f"{base_url}/posts", json=data)
    assert response.status_code == 201
    post = PostModel(**response.json())
    assert post.title == "foo"

@pytest.mark.parametrize("user_id", [1, 2])
def test_get_posts_by_user(base_url, user_id):
    response = requests.get(f"{base_url}/posts", params={"userId": user_id})
    assert response.status_code == 200
    posts = response.json()
    assert all(p["userId"] == user_id for p in posts)

def test_get_single_user(base_url):
    response = requests.get(f"{base_url}/users/1")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == 1
    assert "username" in user
