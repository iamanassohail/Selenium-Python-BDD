from features.pages.BasePage import BasePage as base_page
from features.locators.SwagLab.CartLocators import CartLocators as cart_locators
from selenium.webdriver.common.by import By

class CartPage:
    def verify_count_of_items(self):
        base_page.get_element(self, By.CLASS_NAME, cart_locators.item_cart_icon_count_badge_class, 10)
        base_page.assert_text_of_element(self, "2")