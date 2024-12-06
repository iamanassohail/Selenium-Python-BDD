from utilities import ConfigReader

class LoginLocators:
    username = ConfigReader.read_configuration("AutomationTestStore", "username")
    password = ConfigReader.read_configuration("AutomationTestStore", "password")
    username_textbox_id = "loginFrm_loginname"
    password_textbox_id = "loginFrm_password"
    login_button_xpath = "//button[@title='Login']"