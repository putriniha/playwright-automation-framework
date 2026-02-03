import requests
import pytest

url = "https://jsonplaceholder.typicode.com"

@pytest.mark.api
def test_update_user():
    
    payload = {
        "name": "Putri Updated"
    }

    response = requests.put(
        f"{url}/users/1",
        json=payload
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Putri Updated"
