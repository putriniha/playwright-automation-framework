import requests
import pytest

url = "https://jsonplaceholder.typicode.com"

@pytest.mark.api
def test_get_invalid_user():
    response = requests.get(
        f"{url}/users/9999"
    )

    assert response.status_code == 404

@pytest.mark.api
def test_create_user_invalid_payload():
    payload = {}

    response = requests.post(
        f"{url}/users",
        json=payload
    )

    assert response.status_code == 201  # No validation
    
@pytest.mark.api
def test_invalid_endpoint():
    response = requests.get(
        f"{url}/userrs"
    )

    assert response.status_code == 404



