import pytest
from Pages.login_page import LoginPage
import time
from Utils.config import BASE_URL


@pytest.mark.usefixtures("setup")
class TestLoginAllScenarios:


    def test_login_with_valid_user_valid_password(self,setup):
        self.driver = setup
        login = LoginPage(self.driver,BASE_URL)
        login.perform_login("Admin","admin123" )
        login_message = login.get_message()

        assert login_message == "Login successful"
        time.sleep(10)
        print("Quitting driver")
        self.driver.close()



    def test_login_with_empty_username_valid_password(self,setup):
        self.driver = setup
        login = LoginPage(self.driver, BASE_URL)
        login.perform_login(" ", "admin123")

        login_message = login.get_message()

        assert login_message == "Required field error:  user name field is required"
        time.sleep(10)
        print("Quitting driver")
        self.driver.close()


    def  test_login_with_valid_username_empty_password(self,setup):
        self.driver = setup
        login = LoginPage(self.driver,BASE_URL)

        login.perform_login("Admin", " ")

        login_message = login.get_message()

        assert login_message == "Required field error:  password field is required"
        time.sleep(10)
        print("Quitting driver")
        self.driver.close()

    def test_login_with_invalid_username_valid_password(self,setup):
        self.driver = setup
        login = LoginPage(self.driver,BASE_URL)
        login.perform_login("Admin123", "admin123")

        login_message = login.get_message()

        assert login_message == "Invalid credentials: Please check your username and password"
        time.sleep(10)
        print("Quitting driver")
        self.driver.close()

    def test_login_with_valid_username_invalid_password(self,setup):
        self.driver = setup
        login = LoginPage(self.driver,BASE_URL)
        login.perform_login("Admin", "admin1234")

        login_message = login.get_message()
        print("Quitting driver")
        self.driver.close()


        assert login_message == "Invalid credentials: Please check your username and password"
        time.sleep(10)








