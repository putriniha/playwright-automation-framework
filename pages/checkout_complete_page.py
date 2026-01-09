class CheckoutCompletePage:
    def __init__(self, page):
        self.page = page
        self.complete_header = ".complete-header"

    def get_confirmation_text(self):
        return self.page.text_content(self.complete_header)
