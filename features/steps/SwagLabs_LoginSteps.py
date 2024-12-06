from behave import *
from features.pages.SwagLabs_LoginPage import LoginPage as login_page

@given("Go to Url")
def step_impl(self):
    login_page.goto_swaglabs(self)

@when("enter valid username")
def step_impl(self):
    login_page.enter_valid_username(self)

@step("enter valid password")
def step_impl(self):
    login_page.enter_valid_password(self)


@step("click sign in")
def step_impl(self):
    login_page.click_login_button(self)


@given("go to Dashboard")
def step_impl(self):
    login_page.goto_swaglabs(self)
    login_page.enter_valid_username(self)
    login_page.enter_valid_password(self)
    login_page.click_login_button(self)