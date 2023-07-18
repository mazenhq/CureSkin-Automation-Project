from selenium.webdriver.common.by import By
from pages.base_page import Page

class searchresults(Page):
    SEARCH_RESULTS = (By.CSS_SELECTOR, 'img.header__heading-logo.small-hide')
    POP_UP_BTN = (By.XPATH, "//button[@class='popup-close']")
    def verify_found_results_text(self):
        self.wait_for_element_click(*self.POP_UP_BTN)
        try:
            self.driver.find_element(*self.SEARCH_RESULTS)
            assert True
        except:
            assert False, f"Expected element not found"


        #assert self.driver.find_element(*self.SEARCH_RESULTS), f"Expected Results text not found"
