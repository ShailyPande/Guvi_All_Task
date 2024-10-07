import pytest
from Pages.admin_page import AdminPage
from Pages.login_page import LoginPage
import time
from Utils.config import BASE_URL

@pytest.mark.usefixtures("setup")
class TestAdminPageMenu:

    def test_admin_page_menu(self,setup):
        self.driver = setup
        login = LoginPage(self.driver, BASE_URL)
        login.perform_login("Admin", "admin123")

        admin_page_menu = AdminPage(self.driver, BASE_URL)
        admin_page_menu.click_Admin()
        if admin_page_menu.check_page_title():
            print("Page title is correct: OrangeHRM")
        else:
            print("Page title is incorrect!")

            menu_status = admin_page_menu.check_adminpage_all_menu_displayed()
            print(menu_status)



        self.driver.close()