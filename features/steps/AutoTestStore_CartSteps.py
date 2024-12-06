from behave import *
from features.pages.AutoTestStore_CartPage import CartPage as cart_page

class CartSteps:
    @Then("Go to the AutoTestStore cart then assert the items count and amount")
    def step_impl(self):
        cart_page.goto_cart_page(self)
        cart_page.calculate_total_amount(self)


    @when("Delete items until amount less then 200 Euro")
    def step_impl(self):
        cart_page.make_total_amount_less_then_200_euro(self)

    @step("Delete items until amount less then 200 Dollar")
    def step_impl(self):
        cart_page.make_total_amount_less_then_200_dollor(self)