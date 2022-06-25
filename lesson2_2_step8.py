import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    fn = browser.find_element(By.NAME, "firstname")
    fn.send_keys("Имя")

    ln = browser.find_element(By.NAME, "lastname")
    ln.send_keys("Фамилия")

    em = browser.find_element(By.NAME, "email")
    em.send_keys("Почта")

    input_path = os.path.join(os.path.dirname(__file__), "file.txt")
    file_input = browser.find_element(By.NAME, "file")
    file_input.send_keys(input_path)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
