from selenium import webdriver
import pytest



@pytest.fixture(scope="function")
def setup(request):
    """
      Setup Selenium WebDriver for class-level tests.
      Initializes the driver, maximizes the browser window, and quits after tests.
      """
    driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    # print("Quitting driver")
    # driver.quit()

