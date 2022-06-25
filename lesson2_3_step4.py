import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    btn_start = browser.find_element(By.CLASS_NAME, "btn")
    btn_start.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    y_element = browser.find_element(By.CSS_SELECTOR, "#answer")
    y_element.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()



finally:
    time.sleep(10)
    browser.quit()
