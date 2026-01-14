import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        "problem_user",
        "performance_glitch_user",
        "error_user",
        "visual_user",
    ]
)

def test_login_multiple_users(page, inventory_page, username):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, "secret_sauce")
    
    inventory_page = InventoryPage(page)
    assert inventory_page.is_loaded()
    