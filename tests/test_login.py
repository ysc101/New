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


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.load(Config.BASE_URL)
    login_page.login(Config.USERNAME, Config.PASSWORD)

    # Assertion to verify successful login
    assert "ZPFMS" in driver.title


