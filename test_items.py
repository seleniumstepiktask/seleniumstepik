import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


def test_cart(browser):
    browser.get(link)
    # time.sleep(30)
    cart = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert cart.is_displayed()
