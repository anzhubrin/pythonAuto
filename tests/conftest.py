import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = "https://www.saucedemo.com"

    # headless mode
    # driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--headless')
    # browser.config.driver_options = driver_options

    # before test
    yield
    # after test
    browser.quit()
