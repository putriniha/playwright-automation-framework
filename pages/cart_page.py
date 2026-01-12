class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = "#checkout"
        self.quantity_input = ".cart_quantity"
        self.remove_button = "#remove-sauce-labs-backpack"

    def proceed_to_checkout(self):
        self.page.click(self.checkout_button)

    # def update_quantity(self, qty):
    #     self.page.fill(self.quantity_input, qty)
    
    def remove_item(self):
        self.page.click(self.remove_button)
    
    def is_item_visible(self):
        return self.page.is_visible(self.remove_button)
