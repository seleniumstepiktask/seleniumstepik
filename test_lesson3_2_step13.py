from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


def registration(case):
    try:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        link = f"http://suninjuly.github.io/registration{case}.html"
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
        browser.quit()


class TestRegistration(unittest.TestCase):
    def test_registration_1(self):
        registration(1)

    def test_registration_2(self):
        registration(2)


if __name__ == '__main__':
    unittest.main()
