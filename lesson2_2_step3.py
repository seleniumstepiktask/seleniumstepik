import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    a_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    a = a_element.text
    b_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    b = b_element.text
    y = str(int(a) + int(b))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
