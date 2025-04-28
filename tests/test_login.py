from time import sleep
import allure
from pages.login_page import LoginPage


def test_standard_login():
    login_page = LoginPage()

    login_page.open_login_page()
    login_page.fill_user_name("standard_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.success_login_xpath()


def test_locked_out_user():
    login_page = LoginPage()

    login_page.open_login_page()
    login_page.fill_user_name("locked_out_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.check_no_success_login()


def test_problem_user():
    login_page = LoginPage()

    login_page.open_login_page()
    login_page.fill_user_name("problem_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.success_login_xpath()


def test_performance_glitch_user():
    login_page = LoginPage()

    login_page.open_login_page()
    login_page.fill_user_name("performance_glitch_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    sleep(5)
    login_page.success_login_xpath()

def test_error_user():
    login_page = LoginPage()

    login_page.open_login_page()
    login_page.fill_user_name("error_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.success_login_xpath()

def test_visual_user():
    login_page = LoginPage()

    login_page.open_login_page()
    login_page.fill_user_name("visual_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.success_login_xpath()