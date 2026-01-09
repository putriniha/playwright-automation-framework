from pages.login_page import LoginPage

def test_login_empty_fields(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("", "")

    error = login_page.get_error_message()

    assert error, "Error message should not be empty"
    assert "username" in error.lower()
    assert "required" in error.lower()

