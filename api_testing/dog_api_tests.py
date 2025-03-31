import pytest
import requests

def test_all_breeds_list():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    assert response.status_code == 200
    assert response.json()["status"] == "success"

@pytest.mark.parametrize("breed", ["retriever", "pug"])
def test_random_image_by_breed(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_random_image():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_sub_breed_list():
    response = requests.get("https://dog.ceo/api/breed/hound/list")
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_image_count():
    response = requests.get("https://dog.ceo/api/breed/hound/images")
    assert response.status_code == 200
    assert isinstance(response.json()["message"], list)