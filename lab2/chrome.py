# Wiktor Rostkowski
import unittest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


navigate_url = "https://www.google.pl"


class GoogleSearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(navigate_url)
        self.driver.implicitly_wait(5)
        self.logger = logging.getLogger('selenium')
        self.logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        self.logger.addHandler(ch)


    def tearDown(self):
        self.driver.quit()

    def test_google_search(self):
        #  Wejdź na stronę Google
        # Potwierdzenie plików cookies
        cookies = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div')
        if cookies.is_displayed():
            cookies.click()
        self.logger.info("Pliki Cookies zaakceptowane")



        # Wpisz zapytanie do wyszukiwarki
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium Tutorial")
        self.logger.info("Wyszukiwarka otwarta i wpisana przykładowa wartość")


        # Naciśnij Enter
        search_box.send_keys(Keys.RETURN)
        self.logger.info("Zatwierdzenie wyniku wyszukiwania")


        # Sprawdź, czy wyniki zawierają oczekiwane słowo kluczowe
        results = self.driver.find_elements(By.CSS_SELECTOR,'h3')
        keyword = "Selenium"
        keyword_found = False
        self.logger.info("Sprawdzenie czy wyszukiwarka znalazła treści podobne do naszego słowa kluczowego")

        for result in results:
            if keyword.lower() in result.text.lower():
                keyword_found = True
                break

        # Czy Treść o Selenium się pojawiła?
        self.assertTrue(keyword_found, f"Expected keyword '{keyword}' not found in any search result.")

        sleep(5)
        self.logger.info("Zakończenie testu, zamknięcie przeglądarki")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
