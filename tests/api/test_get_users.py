import requests
import pytest

url = "https://jsonplaceholder.typicode.com"

@pytest.mark.api
def test_get_users():
    response = requests.get(f"{url}/users")
    assert response.status_code == 200
    assert len(response.json()) > 0
