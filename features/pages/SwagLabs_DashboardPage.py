from selenium.webdriver.common.by import By
from features.locators.SwagLab.DashboardLocators import DashboardLocators as dashboard_locators
from features.pages.BasePage import BasePage as base_page

class DashboardPage:

    def assert_user_on_dashboard(self):
        base_page.visibilty_of_element(self, By.CLASS_NAME, dashboard_locators.cart_icon_button_class, 10)

    def select_low_to_high_option(self):
        base_page.select_by_value(self, By.CLASS_NAME, dashboard_locators.filter_icon_button_class, dashboard_locators.low_to_high_option_value, 10)

    def get_price_list_of_all_items(self):
        elements = base_page.get_elements(self, By.CLASS_NAME, dashboard_locators.item_price_label_class, 10)
        item_price_list = []
        for element in elements:
            value = element.text[1:]
            value = float(value)
            item_price_list.append(value)

        base_page.get_accending_order(self, item_price_list)

    def add_two_items_in_cart(self):
        elements = base_page.get_elements(self, By.CLASS_NAME, dashboard_locators.item_cart_icon_button_class, 10)
        base_page.click_element_by_index(self, 0)
        base_page.click_element_by_index(self, 1)

    def click_on_cart_button(self):
        base_page.get_element(self, By.CLASS_NAME, dashboard_locators.cart_icon_button_class, 10)
        base_page.click_on_element(self)