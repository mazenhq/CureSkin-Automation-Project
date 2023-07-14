from selenium.webdriver.common.by import By
from pages.base_page import Page

class header(Page):
    SEARCH_CLICK = (By.XPATH, "//a[@class='header__heading-link focus-inset']")


    def search_for_product(self):
        self.click(*self.SEARCH_CLICK)
