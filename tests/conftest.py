from selenium import webdriver
import pytest



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


