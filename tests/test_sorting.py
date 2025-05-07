from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_sorting_a_z():
    login_page = LoginPage()
    inventory_page = InventoryPage()

    login_page.open_login_page()
    login_page.fill_user_name("standard_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.success_login_xpath()

    inventory_page.click_sorting_button()
    inventory_page.high_to_low_price_sorting()
    inventory_page.check_success_az_sorting()

def test_sorting_z_a():
    login_page = LoginPage()
    inventory_page = InventoryPage()

    login_page.open_login_page()
    login_page.fill_user_name("standard_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.success_login_xpath()

    inventory_page.click_sorting_button()
    inventory_page.click_sorting_za()
    inventory_page.check_success_za_sorting()

def test_sorting_low_to_high():
    login_page = LoginPage()
    inventory_page = InventoryPage()

    login_page.open_login_page()
    login_page.fill_user_name("standard_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.success_login_xpath()

    inventory_page.click_sorting_button()
    inventory_page.low_to_high_price_sorting()
    inventory_page.click_sorting_low_to_high()

def test_sorting_high_to_low():
    login_page = LoginPage()
    inventory_page = InventoryPage()

    login_page.open_login_page()
    login_page.fill_user_name("standard_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.success_login_xpath()

    inventory_page.click_sorting_button()
    inventory_page.click_sorting_high_to_low()
    inventory_page.check_success_high_to_low_sorting()
