from behave import *
from features.pages.AutoTestStore_LoginPage import LoginPage as login_page

class LoginSteps:
    @when("Login to the Website")
    def step_impl(self):
        login_page.enter_username(self)
        login_page.enter_password(self)
        login_page.click_login_button(self)