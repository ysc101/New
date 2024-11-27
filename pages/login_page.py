# pages/login_page.py
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "txtUser")
        self.password_field = (By.ID, "txtPass")
        self.login_button = (By.ID, "btnLogin")

    def load(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
