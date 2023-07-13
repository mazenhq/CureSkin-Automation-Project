from Pages.header import Header
from Pages.amazon_main import MainPage
from Pages.verify_signin import VerifySignin


class Application:

    def __init__(self, driver):
        self.driver = driver