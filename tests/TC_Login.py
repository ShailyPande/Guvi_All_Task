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
        login.get_login_successfull()
        # print(login.get_login_successfull())
        time.sleep(10)
        print("Quitting driver")
        self.driver.close()



    def test_login_with_empty_username_valid_password(self,setup):
        self.driver = setup
        login = LoginPage(self.driver, BASE_URL)
        login.perform_login(" ", "admin123")
        login.get_user_message()
        print(login.get_user_message())
        assert login.get_user_message() =="Required"
        time.sleep(10)
        print("Quitting driver")
        self.driver.close()


    def  test_login_with_valid_username_empty_password(self,setup):
        self.driver = setup
        login = LoginPage(self.driver,BASE_URL)

        login.perform_login("Admin", " ")
        login.get_password_message()
        print(login.get_password_message())
        assert login.get_password_message() == "Required"
        time.sleep(10)
        print("Quitting driver")
        self.driver.close()

    def test_login_with_invalid_username_valid_password(self,setup):
        self.driver = setup
        login = LoginPage(self.driver,BASE_URL)
        login.perform_login("Admin123", "admin123")
        login.get_invalid_message()
        assert login.get_invalid_message() == "Invalid credentials"
        time.sleep(10)
        print("Quitting driver")
        self.driver.close()

    def test_login_with_valid_username_invalid_password(self,setup):
        self.driver = setup
        login = LoginPage(self.driver,BASE_URL)
        login.perform_login("Admin", "admin1234")
        login.get_invalid_message()
        assert login.get_invalid_message() == "Invalid credentials"
        time.sleep(10)
        print("Quitting driver")
        self.driver.close()









