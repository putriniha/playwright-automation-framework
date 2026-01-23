class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_button = "#add-to-cart-sauce-labs-backpack"
        self.cart_icon = ".shopping_cart_link"
    
    def is_loaded(self):
        return "inventory" in self.page.url
    
    def add_item_to_cart(self):
        self.page.click(self.add_to_cart_button)
        
    def go_to_cart(self):
        self.page.click(self.cart_icon)
        
    def get_confirmation_text(self):
        return self.page.text_content(".complete-header")
    
    