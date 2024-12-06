from behave import *
from features.pages.SwagLabs_CartPage import CartPage as cart_page

class CartSteps:
    @then("assert the quantity and total items in cart with prices")
    def step_impl(self):
        cart_page.verify_count_of_items(self)
