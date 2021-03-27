from selenium.webdriver.common.by import By

class HomePageLocators():
    CLOSE_NEWSLETTER_BTN = (By.XPATH, '//div [@class="popup-window-close-button"][@popup-window-id="3"]')
    ZALOGUJ_BTN = (By.XPATH, '//*[@id="layoutPortletElement_359"]/header/div/div[3]/ul/li[2]/a/span')

class LoginPageLocators():
    REGISTER_BTN = (By.XPATH, '//*[@class="sign-in-form-table"]/tbody/tr[7]/td[2]/a[2]')

class RegistrationPageLocators():
    NAME_INPUT = (By.CSS_SELECTOR, '#Name_51')
    SURNAME_INPUT = (By.NAME, 'Surname_51')

