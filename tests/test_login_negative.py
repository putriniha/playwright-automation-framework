from pages.login_page import LoginPage

def test_login_invalid_credentials(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("wrong_user", "wrong_password")

    error = login_page.get_error_message()
    assert "Username and password do not match" in error

