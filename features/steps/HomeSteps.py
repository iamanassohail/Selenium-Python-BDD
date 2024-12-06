from features.pages.HomePage import HomePage as home_page
from behave import given


class HomeSteps:

    @given('I navigated to Login page')
    def step_impl(self):
        home_page.click_on_my_account_dropdown(self)
        home_page.click_on_login_link_button(self)