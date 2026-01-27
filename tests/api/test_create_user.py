import requests
import pytest

@pytest.mark.api
def test_create_user():
    url = "https://jsonplaceholder.typicode.com"

    payload = {
        "name": "Putri",
        "username": "putri123",
        "email": "putri@test.com",
    }

    response = requests.post(
        f"{url}/users", 
        json=payload
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Putri"
