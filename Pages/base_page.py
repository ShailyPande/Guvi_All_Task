from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:

    def __init__(self, driver,url):
        self.driver = driver
        self.url=url

    def click_element(self, locator, timeout=20):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()



    def launch_url(self,timeout=20):
        self.driver.get(self.url)
        self.driver.maximize_window()
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(self.url))


    def enter_text(self, locator, text, timeout=10):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)


    def get_current_url(self):
        return self.driver.current_url

    def get_page_title(self):
        return self.driver.title

    def verify_page_title(self,expected_title):
        return self.get_page_title() == expected_title


    def get_text(self, locator, timeout=20):
        element = self.find_element(locator, timeout)
        return element.text

    def contains_text(self, locator, content, timeout=20):
        element = self.get_text(locator, timeout)
        return content in element

    def attribute(self, locator, attr_name, timeout=2):
        element = self.find_element(locator, timeout)
        return element.get_attribute(attr_name)