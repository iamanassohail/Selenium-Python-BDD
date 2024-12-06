from utilities import ConfigReader

class LoginLocators:
    username_textbox_id = "user-name"
    password_textbox_id = "password"
    login_button_id = "login-button"
    login_header_class = "login_logo"
    url = ConfigReader.read_configuration("SwagLabs", "url")
    login_username = ConfigReader.read_configuration("SwagLabs", "username")
    login_password = ConfigReader.read_configuration("SwagLabs", "password")