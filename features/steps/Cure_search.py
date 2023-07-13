from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open cureskin page')
def open_cureskin(context):
    #context.driver.get('https://shop.cureskin.com/search?q=cure')
    context.app.main_page.open_main_page()

@when('Click on the home page')
def click_search_icon(context):
    #context.driver.find_element(By.CSS_SELECTOR, 'img.header__heading-logo.small-hide').click()
    context.app.header.search_for_product()
    sleep(4)


@then('verify result for homepage is shown')
def verify_found_results_text(context):
    #context.driver.find_element(By.CSS_SELECTOR, 'img.header__heading-logo.small-hide')
    context.app.search_results.verify_found_results_text()


