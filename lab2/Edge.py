# Wiktor Rostkowski
import logging
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

navigate_url = "https://www.wina-bachus.pl"

class SklepTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
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

    def accept_age_warning(self):
        agewarning = self.driver.find_element(By.ID, 'ageWarningButton')
        if agewarning.is_displayed():
            agewarning.click()

    def test_shop_search(self):
        self.logger.info("Otwieranie serwisu wina-bachus.pl")

        # Akceptacja wieku 18 lat
        self.accept_age_warning()

        # Ustawienie ciasteczka za pomocą JavaScript
        self.driver.execute_script("document.getElementById('ageWarningButton').click();")

        # Poczekaj na ukrycie elementu z komunikatem wiekowym
        self.driver.implicitly_wait(20)
        age_banner_bg = self.driver.find_element(By.CLASS_NAME, 'age-banner-bg')
        if age_banner_bg.is_displayed():
            self.logger.info("Komunikat wiekowy nadal widoczny.")
        else:
            self.logger.info("Komunikat wiekowy ukryty.")

        # Potwierdzenie plików cookies
        cookies = self.driver.find_element(By.ID, 'cookieButton')
        if cookies.is_displayed():
            cookies.click()

        # Klikniecie przycisku wyszukiwarki
        self.driver.find_element(By.XPATH, '/html/body/main/header/div[2]/div/div[1]/div[3]/div/div[1]/a/i').click()
        self.logger.info("Wyszukiwarka otwarta")

        # Wpisanie w pole wyszukaj frazy tanie wino
        self.driver.find_element(By.CLASS_NAME, 'ui-autocomplete-input').send_keys("PINTIA Vega Sicilia")
        # Zatwierdzenie wyszukiwania
        self.driver.find_element(By.XPATH, '/html/body/main/header/div[2]/div/div[1]/div[2]/div[2]/form/button/i').click()
        self.logger.info("Nowa strona z wyszukiwaniem")

        # Ponowne zamknięcie komunikatu wiekowego na nowej stronie
        self.accept_age_warning()

        # Kliknięcie w produkt
        self.driver.find_element(By.XPATH, '/html/body/main/section/div/div/section/section/div[3]/div/div[1]/article[2]/div/a').click()
        sleep(5)
        self.logger.info("Zakończenie testu, zamknięcie przeglądarki")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
