from features.locators.HomeLocators import HomeLocators as home_locators
from features.pages.BasePage import BasePage as base_page
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self):
        self.Dropdown_Account_Xpath = "//span[text()='My Account']"

    def click_on_my_account_dropdown(self):
        base_page.get_element(self, By.XPATH, home_locators.Dropdown_Account_Xpath,10)
        base_page.click_on_element(self)

    def click_on_login_link_button(self):
        base_page.get_element(self, By.LINK_TEXT, home_locators.login_link_text, 10)
        base_page.click_on_element(self)
