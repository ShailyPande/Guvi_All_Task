import pytest
from Pages.admin_page import AdminPage
from Pages.login_page import LoginPage
import time
from Utils.config import BASE_URL

@pytest.mark.usefixtures("setup")
class TestAdminPageHeaders:

    def test_adminpage_headers(self,setup):
        self.driver = setup
        login = LoginPage(self.driver, BASE_URL)
        login.perform_login("Admin", "admin123")

        admin_page_header = AdminPage(self.driver, BASE_URL)
        admin_page_header.click_Admin()
        admin_page_header.check_page_title()
        assert admin_page_header.check_adminpage_all_headers_displayed(), "Not all admin page headers are displayed"

        self.driver.close()