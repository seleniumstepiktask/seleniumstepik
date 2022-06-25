import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    y_element = browser.find_element(By.CSS_SELECTOR, "#answer")
    y_element.send_keys(y)

    check = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", check)
    check.click()

    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio.click()

    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
