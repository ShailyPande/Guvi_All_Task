from selenium import webdriver
import pytest
from pages.login_page import LoginPage



@pytest.fixture(scope="class")
def setup(request):
    """
      Setup Selenium WebDriver for class-level tests.
      Initializes the driver, maximizes the browser window, and quits after tests.
      """
    driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.


    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    request.cls.driver = driver

    # Yield control back to the test
    yield driver

    # Quit the driver after the test
    driver.quit()


# @pytest.fixture(scope="class")
# def login(request, setup):
#     """
#     Fixture to log into the application.
#     Assumes the setup_driver fixture is used to initialize the driver.
#     """
#     login_page = LoginPage(request.cls.driver)  # Pass the driver to the login page object
#     login_page.enter_username("Admin")  # Replace with valid username
#     login_page.enter_password("admin123")  # Replace with valid password
#     login_page.click_login()
#
#     # Check if login was successful (optional)
#     assert "dashboard" in request.cls.driver.current_url  # Assuming dashboard URL contains 'dashboard'
#
#     # Login is done, continue with the test
#     yield request.cls.driver