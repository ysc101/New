# pages/login_page.py
from selenium.webdriver.common.by import By



class Vendor:
    def __init__(self, driver):
        self.driver = driver
        self.Master_Menu = (By.XPATH, "//a[text()='Master ']")
        self.Beneficiary_Creation_Menu=(By.XPATH,"//a[text()='Beneficiary Creation ']")


    def vendor(self, Master_Menu,Benficiary_Creation):
        self.driver.find_element(*self.Master_Menu).click()
        self.driver.find_element(self.Beneficiary_Creation_Menu).click()

