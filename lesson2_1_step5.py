import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    y_element = browser.find_element(By.CSS_SELECTOR, "#answer")
    y_element.send_keys(y)

    check = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    check.click()

    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio.click()

    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()



finally:
    time.sleep(10)
    browser.quit()
