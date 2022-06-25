from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    fn = browser.find_element(By.CSS_SELECTOR, ".first[required]")
    fn.send_keys("Имя")

    ln = browser.find_element(By.CSS_SELECTOR, ".second[required]")
    ln.send_keys("Фамилия")

    em = browser.find_element(By.CSS_SELECTOR, ".third[required]")
    em.send_keys("Почта")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
