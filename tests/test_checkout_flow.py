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

    cart_page.proceed_to_checkout()

    checkout_page.fill_information("Putri", "QA", "12345")

    confirmation = checkout_complete_page.get_confirmation_text()
    assert "Thank you for your order!" in confirmation
