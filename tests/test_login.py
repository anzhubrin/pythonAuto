from time import sleep

from selene import browser, have


def test_standard_login():
    browser.open("/")
    browser.element("#user-name").type("standard_user")
    browser.element("#password").type("secret_sauce")
    browser.element("#login-button").click()
    browser.element("//span[@class='title']").should(have.text("Products"))


def test_locked_out_user():
    browser.open("/")
    browser.element("#user-name").type("locked_out_user")
    browser.element("#password").type("secret_sauce")
    browser.element("#login-button").click()
    browser.element("//h3[@data-test='error']").should(have.text("Epic sadface: Sorry, this user has been locked out."))


def test_problem_user():
    browser.open("/")
    browser.element("#user-name").type("problem_user")
    browser.element("#password").type("secret_sauce")
    browser.element("#login-button").click()
    browser.element("//span[@class='title']").should(have.text("Products"))


def test_performance_glitch_user():
    browser.open("/")
    browser.element("#user-name").type("performance_glitch_user")
    browser.element("#password").type("secret_sauce")
    browser.element("#login-button").click()
    sleep(5)
    browser.element("//span[@class='title']").should(have.text("Products"))

def test_error_user():
    browser.open("/")
    browser.element("#user-name").type("error_user")
    browser.element("#password").type("secret_sauce")
    browser.element("#login-button").click()
    browser.element("//span[@class='title']").should(have.text("Products"))

def test_visual_user():
    browser.open("/")
    browser.element("#user-name").type("error_user")
    browser.element("#password").type("secret_sauce")
    browser.element("#login-button").click()
    browser.element("//span[@class='title']").should(have.text("Products"))