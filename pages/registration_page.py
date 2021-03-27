from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators
from selenium.webdriver.common.keys import Keys

class RegistrationPage(BasePage):

    def _verify_page(self):
        print("Weryfikacja RegistartionPage")
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT))

    def fill_name(self, name):
        element = self.driver.find_element(*RegistrationPageLocators.NAME_INPUT)
        element.send_keys(name)

    def fill_surname(self, surname):
        element = self.driver.find_element(*RegistrationPageLocators.SURNAME_INPUT)
        element.send_keys(surname)
