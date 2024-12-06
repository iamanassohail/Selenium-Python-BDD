import time

from behave import given
from behave import when
from behave import then
from behave import step
from selenium import webdriver
from selenium.webdriver.common.by import By

Email = 'amotooriapril2023@gmail.com'
InputField_Email = (By.ID, "input-email")
InputField_Password = (By.ID, "input-password")
Password = '12345'
Button_Login = (By.XPATH, "//input[@value='Login']")
LinkButton_EditInfo = (By.XPATH, "Edit your account information")


@then('I should get a proper warning message')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//div[contains(@class,'alert alert-danger')]").is_displayed()


@when('I enter valid email and invalid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("amotooriapril2023@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys('invalid')


@when('I enter invalid email and invalid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("amotooriapril2023invalid@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys('invalid')


@when('I dont enter anything into email and password fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("amotooriapril2023invalid@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys('invalid')