from behave import given
from behave import when
from behave import then
from behave import step
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I navigate to Register Page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")
    context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    context.driver.find_element(By.LINK_TEXT, "Register").click()


@when('I enter details into mandatory fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("Anas")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Sohail")
    context.driver.find_element(By.ID, "input-email").send_keys("anas.sohail2004@gmail.com")
    context.driver.find_element(By.ID, "input-telephone").send_keys("03102035407")
    context.driver.find_element(By.ID, "input-password").send_keys("12345")
    context.driver.find_element(By.ID, "input-confirm").send_keys("12345")


@when('I click on Continue button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@value='Continue']").click()


@then('Account should get created')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//h1[text()='Your Account Has Been Created!']").is_displayed()


@when('I enter details into all fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("Anas")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Sohail")
    context.driver.find_element(By.ID, "input-email").send_keys("anas.sohail2005@gmail.com")
    context.driver.find_element(By.ID, "input-telephone").send_keys("03102035407")
    context.driver.find_element(By.ID, "input-password").send_keys("12345")
    context.driver.find_element(By.ID, "input-confirm").send_keys("12345")


@when('I enter details into all fields except email field')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("Anas")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Sohail")
    context.driver.find_element(By.ID, "input-telephone").send_keys("03102035407")
    context.driver.find_element(By.ID, "input-password").send_keys("12345")
    context.driver.find_element(By.ID, "input-confirm").send_keys("12345")


@when('I enter existing accounts email into email field')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("anas.sohail2000@outlook.com")


@then('Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//div[text()='Warning: E-Mail Address is already registered!']").is_displayed()


@when('I dont enter anything into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("")
    context.driver.find_element(By.ID, "input-lastname").send_keys("")
    context.driver.find_element(By.ID, "input-email").send_keys("")
    context.driver.find_element(By.ID, "input-telephone").send_keys("")
    context.driver.find_element(By.ID, "input-password").send_keys("")
    context.driver.find_element(By.ID, "input-confirm").send_keys("")


@then('Proper warning messages for every mandatory fields should be displayed')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//div[text()='Warning: You must agree to the Privacy Policy!']").is_displayed()
    assert context.driver.find_element(By.XPATH, "//div[text()='First Name must be between 1 and 32 characters!']").is_displayed()
    assert context.driver.find_element(By.XPATH, "//div[text()='Last Name must be between 1 and 32 characters!']").is_displayed()
    assert context.driver.find_element(By.XPATH, "//div[text()='E-Mail Address does not appear to be valid!']").is_displayed()
    assert context.driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div[1]").is_displayed()
    assert context.driver.find_element(By.XPATH, "//div[text()='Password must be between 4 and 20 characters!']").is_displayed()


@step("I select Privacy Policy option")
def step_impl(context):
    context.driver.find_element(By.NAME, "agree").click()
