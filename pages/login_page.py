import allure
from allure_commons.types import Severity
from selene import browser, have


class LoginPage:
    def __init__(self):
        self.user_name = browser.element("#user-name")
        self.password = browser.element("#password")
        self.login_button = browser.element("#login-button")
        self.success_login_xpath = browser.element("//span[@class='title']")
        self.no_success_login_xpath = browser.element("//h3[@data-test='error']")

    @allure.tag("web")
    @allure.severity(Severity.NORMAL)
    @allure.step("Open Login page")
    def open_login_page(self):
        browser.open("https://www.saucedemo.com")
        return self

    @allure.step("Fill username")
    def fill_user_name(self, value):
        self.user_name.type(value)
        return self

    @allure.step("Fill password")
    def fill_password(self, value):
        self.password.type(value)
        return self

    @allure.step("Click login button")
    def click_login_button(self):
        self.login_button.click()
        return self

    @allure.step("Check success login")
    def check_success_login(self):
        self.check_success_login.should(have.text("Products"))
        return self

    @allure.step("Check no success login")
    def check_no_success_login(self):
        self.no_success_login_xpath.should(have.text("Epic sadface: Sorry, this user has been locked out."))
        return self