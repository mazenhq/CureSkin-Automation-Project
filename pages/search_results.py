from selenium.webdriver.common.by import By
from pages.base_page import Page

class searchresults(Page):
    SEARCH_RESULTS = (By.CSS_SELECTOR, 'img.header__heading-logo.small-hide')
    def verify_found_results_text(self):
        self.driver.find_element(*self.SEARCH_RESULTS)
