from features.locators.SwagLab.LoginLocators import LoginLocators as login_locators
from features.pages.BasePage import BasePage as base_page
from selenium.webdriver.common.by import By

class LoginPage:
    def goto_swaglabs(self):
        base_page.goto_url(self, login_locators.url)

    def assert_login_page_header(self):
        base_page.visibilty_of_element(self, By.CLASS_NAME, login_locators.login_header_class, 10)

    def enter_valid_username(self):
        base_page.get_element(self, By.ID, login_locators.username_textbox_id, 10)
        base_page.send_keys(self, login_locators.login_username)

    def enter_valid_password(self):
        base_page.get_element(self, By.ID, login_locators.password_textbox_id, 10)
        base_page.send_keys(self, login_locators.login_password)

    def click_login_button(self):
        base_page.get_element(self, By.ID, login_locators.login_button_id, 10)
        base_page.click_on_element(self)