from pages.main_page import mainpage
from pages.header import header
from pages.search_results import searchresults


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = mainpage(self.driver)
        self.header = header(self.driver)
        self.search_results = searchresults(self.driver)



