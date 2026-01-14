import pytest 

def test_user_can_checkout_successfully(
    login_page,
    inventory_page,
    cart_page,
    checkout_page,
    checkout_complete_page
):
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart()

    # cart_page.update_quantity(2)

    assert cart_page.is_item_visible()
    
    cart_page.proceed_to_checkout()

    checkout_page.fill_information("Putri", "QA", "12345")

    confirmation = checkout_complete_page.get_confirmation_text()
    assert "Thank you for your order!" in confirmation

@pytest.mark.parametrize(
    "first_name, last_name, postal_code",
    [
        ("Test", "User", "12345"),
        ("Putri", "QA", "12345"),
    ]
)

def test_checkout_with_various_user_info(
    login_page,
    inventory_page,
    cart_page,
    checkout_page,
    checkout_complete_page,
    first_name,
    last_name,
    postal_code
):
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart()

    assert cart_page.is_item_visible()
    
    cart_page.proceed_to_checkout()

    checkout_page.fill_information(first_name, last_name, postal_code)

    confirmation = checkout_complete_page.get_confirmation_text()
    assert "Thank you for your order!" in confirmation