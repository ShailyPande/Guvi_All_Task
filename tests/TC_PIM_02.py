from pages.PIM_page import PIM_Page
import pytest
from tests.TC_Login_01 import TestValidLogin


@pytest.mark.usefixtures("setup")
class Test_Edit_Existing_Employee_PIM_Page:

    def test_edit_existing_employee(self):
        login_test = TestValidLogin()
        login_test.test_valid_login()

        edit_employee_pim_page = PIM_Page(self.driver)
        edit_employee_pim_page.PIM_elemnet_click()
        edit_employee_pim_page.update_details("shaily","Kumari"," ", "1234")
        edit_employee_pim_page.personal_details_page_save_button()

