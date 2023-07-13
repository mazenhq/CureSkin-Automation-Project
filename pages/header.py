from selenium.webdriver.common.by import By
from pages.base_page import Page

class header(Page):
    SEARCH_CLICK = (By.CSS_SELECTOR, '.header__search')
    SEARCH_FILED = (By.ID, 'Search-In-Modal')

    def search_for_product(self):
        self.click(*self.SEARCH_CLICK)
        self.input_text('cure', *self.SEARCH_FILED)