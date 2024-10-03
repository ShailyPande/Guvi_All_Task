import pytest
from Pages.admin_page import AdminPage
from Pages.login_page import LoginPage
import time
from Utils.config import BASE_URL

@pytest.mark.usefixtures("setup")
class TestAdminPageMenu:

    def test_admin_page_headers(self,setup):
        self.driver = setup
        login = LoginPage(self.driver, BASE_URL)
        login.perform_login("Admin", "admin123")

        admin_page_menu = AdminPage(self.driver, BASE_URL)
        admin_page_menu.click_Admin()

        assert admin_page_menu.check_adminpage_all_menu_displayed(), "Not all side menu options are displayed"

        self.driver.close()