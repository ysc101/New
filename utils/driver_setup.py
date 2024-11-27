# utils/driver_setup.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.config import Config

def get_driver():
    service = Service(Config.DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(50)
    driver.maximize_window()
    return driver
