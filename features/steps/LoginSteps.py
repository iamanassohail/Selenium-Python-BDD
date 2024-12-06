from behave import when
from behave import then
from features.pages.LoginPage import LoginPage as login_page


class LoginSteps:
    @when('I enter invalid email and valid password into the fields')
    def step_impl(self):
        login_page.enter_invalid_email(self)
        login_page.enter_password(self)

    @when('I enter valid email address and valid password into the fields')
    def step_impl(self):
        login_page.enter_valid_email(self)
        login_page.enter_password(self)

    @when('I click on Login button')
    def step_impl(self):
        login_page.click_login_button_on_login_page(self)

    @then('I should get logged in')
    def step_impl(self):
        login_page.assert_login_in_successfully(self)