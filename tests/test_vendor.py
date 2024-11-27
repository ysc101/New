# tests/test_login.py
import pytest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from utils.config import Config
from pages.vendor_page import Vendor


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.close()

def test_vendor(driver):
    vendor_page=Vendor(driver)
    vendor_page.Master_Menu
    vendor_page.Beneficiary_Creation_Menu
