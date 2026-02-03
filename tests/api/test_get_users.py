import requests
import pytest

url = "https://jsonplaceholder.typicode.com"

@pytest.mark.api
def test_get_users():
    response = requests.get(f"{url}/users")

    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert "id" in data[0]
    assert "email" in data[0]


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user_by_id(user_id):
    response = requests.get(
        f"{url}/users/{user_id}"
    )

    assert response.status_code == 200