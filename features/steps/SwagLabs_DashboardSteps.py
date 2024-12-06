from features.pages.SwagLabs_DashboardPage import DashboardPage as dashboard_page
from behave import *


class DashboardSteps:
    @then("assert user land to the dashboard")
    def step_impl(self):
        dashboard_page.assert_user_on_dashboard(self)

    @when("open the filter dropdown")
    def step_impl(self):
        dashboard_page.select_low_to_high_option(self)

    @when("select the prize low to high")
    def step_impl(self):
        dashboard_page.select_low_to_high_option(self)

    @then("verify items are sort in low to high")
    def step_impl(self):
        dashboard_page.get_price_list_of_all_items(self)

    @when("add lowest two items in the cart")
    def step_impl(self):
        dashboard_page.add_two_items_in_cart(self)

    @step("go to the cart")
    def step_impl(self):
        dashboard_page.click_on_cart_button(self)