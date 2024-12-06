from features.locators.LoginLocators import LoginLocators as login_locators
from features.pages.BasePage import BasePage as base_page
from selenium.webdriver.common.by import By


class LoginPage:
    def enter_valid_email(self):
        base_page.get_element(self, By.ID, login_locators.login_textbox_id, 10)
        base_page.send_keys(self, login_locators.login_email)

    def enter_invalid_email(self):
        base_page.get_element(self, By.ID, login_locators.login_textbox_id, 10)
        base_page.send_keys(self, login_locators.generate_random_email(self))

    def enter_password(self):
        base_page.get_element(self, By.ID, login_locators.password_textbox_id, 10)
        base_page.send_keys(self, login_locators.login_password)

    def click_login_button_on_login_page(self):
        base_page.get_element(self, By.XPATH, login_locators.login_button_xpath, 10)
        base_page.click_on_element(self)

    def assert_login_in_successfully(self):
        base_page.get_element(self, By.LINK_TEXT, login_locators.login_successfully_text, 10)
        base_page.assert_text_of_element(self, login_locators.login_successfully_text)