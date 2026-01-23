import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_user_can_login_successfully(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.is_loaded()
    