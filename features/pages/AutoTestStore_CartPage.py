from features.pages.BasePage import BasePage as base_page
from features.locators.AutomationLoginTest.CartLocators import CartLocator as cart_locators
from selenium.webdriver.common.by import By


class CartPage:
    def goto_cart_page(self):
        base_page.get_element(self, By.XPATH, cart_locators.cart_nav_button_xpath, 10)
        base_page.click_on_element(self)

    def calculate_total_amount(self):
        base_page.get_element(self, By.XPATH, cart_locators.cart_table_xpath, 10)
        cart_rows = base_page.get_elements_from_parent_element(self, By.TAG_NAME, "tr")
        cart_rows.pop(0)
        total_amount = 0.00
        for row in cart_rows:
            price_col = base_page.get_child_elements(self, row, By.TAG_NAME, "td")
            quantity_ele = base_page.get_child_element(self, price_col[4], By.TAG_NAME, "input")
            total_item_price = price_col[5].text[:-1]
            quantity = int(quantity_ele.get_attribute("value"))
            price = float(price_col[3].text[:-1])
            total_price = price * quantity
            base_page.assert_values(self, total_item_price, total_price)
            total_amount += price

    def make_total_amount_less_then_200_euro(self):
        total_price = float(base_page.get_element(self, By.XPATH, cart_locators.total_amount_span_xpath, 10).text[:-1].replace(",", ""))
        while total_price > 200:
            base_page.get_element(self, By.XPATH, cart_locators.cart_table_xpath, 10)
            cart_rows = base_page.get_elements_from_parent_element(self, By.TAG_NAME, "tr")
            cart_row_cols = base_page.get_child_elements(self, cart_rows[1], By.TAG_NAME, "td")
            delete_button = base_page.get_child_element(self, cart_row_cols[6], By.TAG_NAME, "a")
            delete_button.click()
            total_price = float(base_page.get_element(self, By.XPATH, cart_locators.total_amount_span_xpath, 10).text[:-1].replace(",",
                                                                                                                   ""))

    def make_total_amount_less_then_200_dollor(self):
        total_price = float(base_page.get_element(self, By.XPATH, cart_locators.total_amount_span_xpath, 10).text[1:].replace(",", ""))
        while total_price > 200:
            base_page.get_element(self, By.XPATH, cart_locators.cart_table_xpath, 10)
            cart_rows = base_page.get_elements_from_parent_element(self, By.TAG_NAME, "tr")
            cart_row_cols = base_page.get_child_elements(self, cart_rows[1], By.TAG_NAME, "td")
            delete_button = base_page.get_child_element(self, cart_row_cols[6], By.TAG_NAME, "a")
            delete_button.click()
            total_price = float(base_page.get_element(self, By.XPATH, cart_locators.total_amount_span_xpath, 10).text[1:].replace(",",""))

    def make_total_amount_200(self):
        total_price = float(base_page.get_element(self, By.XPATH, cart_locators.total_amount_span_xpath, 10).text[:-1].replace(",", ""))
        while total_price > 200:
            base_page.get_element(self, By.XPATH, cart_locators.cart_table_xpath, 10)
            cart_rows = base_page.get_elements_from_parent_element(self, By.TAG_NAME, "tr")
            cart_row_cols = base_page.get_child_elements(self, cart_rows[1], By.TAG_NAME, "td")
            delete_button = base_page.get_child_element(self, cart_row_cols[6], By.TAG_NAME, "a")
            delete_button.click()
            total_price = float(base_page.get_element(self, By.XPATH, cart_locators.total_amount_span_xpath, 10).text[:-1].replace(",",""))
