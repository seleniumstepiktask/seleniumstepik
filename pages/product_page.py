from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is still presented, but should disappear"

    def should_be_added_to_basket(self):
        self.should_be_message()
        self.should_be_price()

    def should_be_message(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE).text, "Wrong product added"

    def should_be_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(
            *ProductPageLocators.PRICE_MESSAGE).text, "Wrong product price"
