import random
import string


class LoginLocators:

    login_textbox_id = "input-email"
    password_textbox_id = "input-password"
    login_email = "amotooriapril2023@gmail.com"
    login_password = "12345"
    login_button_xpath = "//input[@value='Login']"
    login_successfully_text = "Edit your account information"

    def generate_random_email(self):
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        domains = ['example.com', 'gmail.com', 'yahoo.com', 'hotmail.com']
        domain = random.choice(domains)
        email = f"{username}@{domain}"
        return email