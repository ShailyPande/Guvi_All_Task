from pages.PIM_page import PIM_Page
from tests.TC_Login_01 import TestValidLogin
import pytest



@pytest.mark.usefixtures("setup")
class Test_Add_Employee_PIM_Page:

    def test_add_employee(self):
        login_test = TestValidLogin()
        login_test.test_valid_login()


        add_employee_pim_page = PIM_Page(self.driver)
        add_employee_pim_page.PIM_elemnet_click()
        add_employee_pim_page.PIM_page_add_detail("Shaily","K","P","1234")
        add_employee_pim_page.save_button_click()







