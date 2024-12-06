from features.pages.BasePage import BasePage as base_page
from features.locators.AutomationLoginTest.LoginLocators import LoginLocators as login_locators
from selenium.webdriver.common.by import By

class LoginPage:
    def enter_username(self):
        base_page.get_element(self, By.ID, login_locators.username_textbox_id, 10)
        base_page.send_keys(self, login_locators.username)

    def enter_password(self):
        base_page.get_element(self, By.ID, login_locators.password_textbox_id, 10)
        base_page.send_keys(self, login_locators.password)

    def click_login_button(self):
        base_page.get_element(self, By.XPATH, login_locators.login_button_xpath, 10)
        base_page.click_on_element(self)