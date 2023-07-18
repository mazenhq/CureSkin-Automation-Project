from pages.base_page import Page
from selenium.webdriver.common.by import By
class mainpage(Page):

    def open_main_page(self):
        self.open_url('https://shop.cureskin.com/search?q=cure')
