from behave import given
from behave import when
from behave import then
from behave import step
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I got navigated to Home Page')
def step_impl(context):
    assert context.driver.title.__eq__("Your Store")


@when('I enter valid product into the Search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("HP")


@when('I click on Search button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@id='search']//button").click()


@then('Valid product should get displayed in Search results')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()


@when('I entered invalid product into the Search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("Honda")


@then('Proper message should be displayed in Search results')
def step_impl(context):
    expected_text = "There is no product that matches the search criteria."

    assert context.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)


@when('I dont enter anything into Search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("")
