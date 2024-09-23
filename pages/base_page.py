from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class basepage:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def enter_text(self, locator, text, timeout=10):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    # def drop_down(self, locator, text, timeout=10,value):
    #     element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    #     select = Select(element)
    #     select.select_by_value(value)

    def get_current_url(self):
        return self.driver.current_url
