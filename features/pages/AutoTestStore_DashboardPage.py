from features.pages.BasePage import BasePage as base_page
from features.locators.AutomationLoginTest.DashboardLocators import DashboardLocators as dashboard_locators, \
    DashboardLocators
from selenium.webdriver.common.by import By

class DashboardPage:
    def goto_automation_test_store(self):
        base_page.goto_url(self, dashboard_locators.url)

    def navigate_to_login_page(self):
        base_page.get_element(self, By.ID, dashboard_locators.lgon_register_button_id, 10)
        base_page.click_on_element(self)

    def click_on_currency_dropdown(self):
        base_page.get_element(self, By.CLASS_NAME, dashboard_locators.currency_dropdown_class, 10)
        base_page.click_on_element(self)

    def click_on_euro_currency_option(self):
        base_page.get_element(self, By.XPATH, dashboard_locators.euro_option_xpath, 10)
        base_page.click_on_element(self)

    def click_on_dollar_currency_option(self):
        base_page.get_element(self, By.XPATH, dashboard_locators.dollar_option_xpath, 10)
        base_page.click_on_element(self)
        
    def add_items_in_cart(self):
        category_list = base_page.get_elements(self, By.XPATH, dashboard_locators.catagory_menu_nav_xpath, 10)
        category_list.pop(0)
        count = len(category_list)
        for i in range(count):
            category_list = base_page.get_elements(self, By.XPATH, dashboard_locators.catagory_menu_nav_xpath, 10)
            category_list.pop(0)
            category_list[i].click()
            item_list = base_page.get_elements(self, By.XPATH, dashboard_locators.items_cart_xpath, 10)
            for item in item_list:
                check_sale = base_page.child_element_available(self, item, By.CLASS_NAME, dashboard_locators.sale_tag_span_class, 10)
                if check_sale == True:
                    check_cart = base_page.child_element_available(self, item, By.CLASS_NAME, dashboard_locators.add_to_cart_button_class, 10)
                    if check_cart == True:
                        cart = base_page.get_child_element(self, item, By.CLASS_NAME, dashboard_locators.add_to_cart_button_class)
                        base_page.click_on_element(self)
                        price_label = base_page.get_child_element(self, item, By.CLASS_NAME, dashboard_locators.new_price_dev_class)
                        dashboard_locators.item_count += 1
                        dashboard_locators.total_amount += float(price_label.text[:-1])