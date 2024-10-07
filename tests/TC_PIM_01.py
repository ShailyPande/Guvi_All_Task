import pytest
from Pages.forgot_password_page import ForgotPassword
import time
from Utils.config import BASE_URL


@pytest.mark.usefixtures("setup")
class TestForgotPasswordFunctionality:

    def test_forget_password(self,setup):
        self.driver = setup
        forgot_password = ForgotPassword(self.driver, BASE_URL)
        forgot_password.perform_forgot_password("Admin")

        forgot_password.reset_password_successfull()
        self.driver.close()