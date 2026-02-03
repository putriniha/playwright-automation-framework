import requests
import pytest

url = "https://jsonplaceholder.typicode.com"

@pytest.mark.api
def test_delete_user():
        
    response = requests.delete(
        f"{url}/users/1"
    )

    assert response.status_code == 200
