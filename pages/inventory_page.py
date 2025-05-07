import allure
from allure_commons.types import Severity
from selene import browser, have


class InventoryPage:
    def __init__(self):
        self.choose_sorting = browser.element("//select[@data-test='product-sort-container']")
        self.az_sorting = browser.element("//option[@value='az']")
        self.za_sorting = browser.element("//option[@value='za']")
        self.low_to_high_price_sorting = browser.element("//option[@value='lohi']")
        self.high_to_low_price_sorting = browser.element("//option[@value='hilo']")

        self.check_sorting_xpath = browser.element("//*[@id='item_4_title_link']/div")

    @allure.step("Click sorting")
    def click_sorting_button(self):
        self.choose_sorting.click()
        return self

    @allure.step("Click az sorting")
    def click_sorting_az(self):
        self.az_sorting.click()
        return self

    @allure.step("Click za sorting")
    def click_sorting_za(self):
        self.za_sorting.click()
        return self

    @allure.step("Click low to high sorting")
    def click_sorting_low_to_high(self):
        self.low_to_high_price_sorting.click()
        return self

    @allure.step("Click high to low sorting")
    def click_sorting_high_to_low(self):
        self.high_to_low_price_sorting.click()
        return self

    @allure.step("Check az success sorting")
    def check_success_az_sorting(self):
        self.check_sorting_xpath.should(have.text("Sauce Labs Backpack"))
        return self

    @allure.step("Check za success sorting")
    def check_success_za_sorting(self):
        self.check_sorting_xpath.should(have.text("Test.allTheThings() T-Shirt (Red)"))
        return self

    @allure.step("Check low to high success sorting")
    def check_success_low_to_high_sorting(self):
        self.check_sorting_xpath.should(have.text("Sauce Labs Onesie"))
        return self

    @allure.step("Check high to low success sorting")
    def check_success_high_to_low_sorting(self):
        self.check_sorting_xpath.should(have.text("Sauce Labs Fleece Jacket"))
        return self