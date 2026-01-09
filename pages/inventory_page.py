class InventoryPage:
    def __init__(self, page):
        self.page = page

        # locators
        self.inventory_list = page.locator(".inventory_list")

    def is_loaded(self):
        return self.inventory_list.is_visible()