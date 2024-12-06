import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities import ConfigReader


class BasePage:
    browser = None

    def define_driver(self):
        global driver
        browser = ConfigReader.read_configuration("basic info", "browser")
        if browser.__eq__("chrome"):
            driver = webdriver.Chrome()

        driver.maximize_window()
        # driver.get(ConfigReader.read_configuration("basic info", "url"))

    def quit_driver(self):
        driver.quit()

    def click_on_element(self):
        try:
            element.click()
        except:
            raise

    def get_element(self, locator_type, locator_value, wait_time):
        global element
        try:
            WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((locator_type, locator_value)))
            WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((locator_type, locator_value)))
            element = driver.find_element(locator_type, locator_value)
            return element
        except:
            raise

    def get_elements_from_parent_element(self, locator_type, locator_value):
        global elements
        try:
            elements = element.find_elements(locator_type, locator_value)
            return elements
        except:
            raise

    def get_child_elements(self, ele, locator_type, locator_value):
        global elements
        try:
            elements = ele.find_elements(locator_type, locator_value)
            return elements
        except:
            raise

    # def get_elements_from_parent_element(self, locator_type, locator_value, ele):
    #     global elements
    #     try:
    #         elements = ele.find_elements(locator_type, locator_value)
    #         return elements
    #     except:
    #         raise


    def send_keys(self, keys):
        try:
            element.send_keys(keys)
        except:
            raise

    def presence_of_element(self, locator_type, locator_value, wait_time):
        try:
            WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((locator_type, locator_value)))
            return True
        except:
            return False

    def child_element_available(self, ele, locator_type, locator_value, wait_time):
        try:
            ele.find_element(locator_type, locator_value)
            return True
        except:
            return False

    def visibilty_of_element(self, locator_type, locator_value, wait_time):
        try:
            WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((locator_type, locator_value)))
            return True
        except:
            return False

    def assert_text_of_element(self, expected_text):
        try:
            assert element.text.__eq__(expected_text)
        except:
            raise

    def assert_values(self, actual, expected):
        try:
            assert actual.__eq__(expected)
        except:
            raise

    def goto_url(self, url):
        try:
            driver.get(url)
        except:
            raise

    def select_by_value(self, locator_type, locator_value, select_value, wait_time):
        try:
            WebDriverWait(driver, wait_time).until(EC.visibility_of_element_located((locator_type, locator_value)))
            select = Select(driver.find_element(locator_type, locator_value))
            select.select_by_value(select_value)
        except:
            raise

    def get_elements(self, locator_type, locator_value, wait_time):
        global elements
        try:
            WebDriverWait(driver, wait_time).until(EC.presence_of_all_elements_located((locator_type, locator_value)))
            WebDriverWait(driver, wait_time).until(EC.visibility_of_all_elements_located((locator_type, locator_value)))
            elements = driver.find_elements(locator_type, locator_value)
            return elements
        except:
            raise

    def get_accending_order(self, list):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                raise
        return

    def click_element_by_index(self, index):
        try:
            elements.__getitem__(index).click()
        except:
            raise

    def get_child_element(self, ele, locator_type, locator_value):
        global element
        try:
            element = ele.find_element(locator_type, locator_value)
            return element
        except:
            raise