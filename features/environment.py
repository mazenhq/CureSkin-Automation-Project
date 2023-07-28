import logging
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions



####Allure command:####
# To generate JSON
#behave -f allure_behave.formatter:AllureFormatter -o .\Mazen_results\ .\features\tests\Cure_search.feature

# To generate Allure Report
# allure serve <path to folder that has JSON results>




def browser_init(context, test_name):
    """
    :param context: Behave context
    """

    ######## GOOGLE CHROME #######################
    # driver_path = ChromeDriverManager().install()
    # service = ChromeService(driver_path)
    # context.driver = webdriver.Chrome(service=service)
    ####################################################

    ######### FIREFOX ##############
    # driver_path = GeckoDriverManager().install()
    # service = FirefoxService(driver_path)
    # context.driver = webdriver.Firefox(service=service)
    #################################

    #########HEADLESS MODE #########################
    # driver_path = ChromeDriverManager().install()
    # service = ChromeService(driver_path)
    # options = ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(service=service, options=options)
    ##################################################

    ########BROWSERSTACK############
    desired_cap = DesiredCapabilities.CHROME.copy()
    #desired_cap = {
    #    'browser': 'Chrome',
    #    'os_version': '11',
    #    'os': 'Windows',
    #    'name': test_name
    #}

    bs_user = 'syedahmed_Sqh8ir'
    bs_key = '6GnpHaXrpW1xwNhBpTNY'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, options=ChromeOptions())
    #########################################################################

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logging.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
