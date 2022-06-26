from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_not_be_products_in_basket(self):
        self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT)

    def should_be_empty_basket_message(self):
        self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE)
