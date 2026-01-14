import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("","", "Username is required"),
        ("standard_user","", "Password is required"),
        ("", "secret_sauce", "Username is required"),
        ("wrong_user", "wrong_pass", "do not match"),
    ]
)

def test_login_negative_cases(page, username, password, expected_error):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)

    error = login_page.get_error_message()
    assert expected_error in error
    