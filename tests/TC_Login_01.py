# pages/login_page.py
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import pytest


@pytest.mark.usefixtures("setup")
class TestValidLogin:
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")
        assert login_page.is_login_successful(), "Login failed, but it should have succeeded"


