class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = "#checkout"

    def proceed_to_checkout(self):
        self.page.click(self.checkout_button)
