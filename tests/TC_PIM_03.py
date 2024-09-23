from pages.PIM_page import PIM_Page
import pytest
from tests.TC_Login_01 import TestValidLogin


@pytest.mark.usefixtures("setup")
class Test_Delete_Existing_Employee:

    def test_delete_exiting_employee_data(self):
        login_test = TestValidLogin()
        login_test.test_valid_login()

        delete_existing_employee = PIM_Page(self.driver)
        delete_existing_employee.PIM_elemnet_click()
        delete_existing_employee.scroll_delete_employee_data(self,822)
        delete_existing_employee.delete_click_existing_employee(822)
        delete_existing_employee.delete_confirmation()
        delete_existing_employee.click_yes_popup()
        delete_existing_employee.delete_successfull_message()
