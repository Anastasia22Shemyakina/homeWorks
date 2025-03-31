import pytest
import requests

@pytest.mark.parametrize("city", ["new_york", "chicago"])
def test_brewery_by_city(city):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_city={city}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_brewery_by_name():
    response = requests.get("https://api.openbrewerydb.org/breweries/madtree-brewing-cincinnati")
    assert response.status_code == 200
    assert "MadTree Brewing" in response.text

def test_brewery_random():
    response = requests.get("https://api.openbrewerydb.org/breweries/random")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_brewery_types():
    response = requests.get("https://api.openbrewerydb.org/breweries/types")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.parametrize("state", ["california", "ohio"])
def test_brewery_by_state(state):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_state={state}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)