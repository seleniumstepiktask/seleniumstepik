import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    y_element = browser.find_element(By.CSS_SELECTOR, "#answer")
    y_element.send_keys(y)

    check = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check.click()

    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()

    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()



finally:
    time.sleep(10)
    browser.quit()
