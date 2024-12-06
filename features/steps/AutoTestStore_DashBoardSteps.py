from behave import *
from features.pages.AutoTestStore_DashboardPage import DashboardPage as dashboard_page

class Dashboard:
    @given("Goto Automation Test Store")
    def step_impl(self):
        dashboard_page.goto_automation_test_store(self)
        dashboard_page.navigate_to_login_page(self)

    @step("Select the currency to euro")
    def step_impl(self):
        dashboard_page.click_on_currency_dropdown(self)
        dashboard_page.click_on_euro_currency_option(self)

    @step("From each section select all sales items and add it into the cart")
    def step_impl(self):
        dashboard_page.add_items_in_cart(self)

    @step("Change currancy to dollor")
    def step_impl(self):
        dashboard_page.click_on_currency_dropdown(self)
        dashboard_page.click_on_dollar_currency_option(self)