from selene import browser, have


def test_standard_login():
    browser.open("/")

    browser.element("#user-name").type("standard_user")
    browser.element("#password").type("secret_sauce")
    browser.element("#login-button").click()

    browser.element("//span[@class='title']").should(have.text("Products"))