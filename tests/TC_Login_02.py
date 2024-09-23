# pages/login_page.py
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import pytest


@pytest.mark.usefixtures("setup")
class TestInValidLogin:

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("Admin1", "admin123")
        assert not login_page.is_login_successful(), "Login suc ceeded, but it should have failed"