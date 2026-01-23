import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_user_can_login_successfully(Login_page, Inventory_page):
    Login_page.open()
    Login_page.login("standard_user", "secret_sauce")

    assert Inventory_page.is_loaded()
    