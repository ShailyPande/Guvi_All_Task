from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Pages.base_page import BasePage
import time


class LoginPage(BasePage):
    def __init__(self, driver,url):
        super().__init__(driver, url)
        self.driver = driver
        self.url = url

        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, '//button[@type="submit"]')
        self.invalid_message = (By.XPATH, '//div[@class="oxd-alert-content oxd-alert-content--error"]')
        self.dashboard = (By.XPATH, "//span[text()='Dashboard']")
        self.required_message_username = (By.XPATH,'//span[@class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message" and text()="Required"]')
        self.required_message_password = (By.XPATH,'//span[@class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message" and text()="Required"]')

    def enter_username(self, username):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.username_field)).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.password_field)).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.login_button)).click()





    def perform_login(self, username, password):
        self.launch_url()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(self.username_field))
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_user_message(self):
        required_usermessage_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.required_message_username))

        # Retrieve the text of the required message element
        required_username_message_text = required_usermessage_element.text
        return required_username_message_text


    def get_password_message(self):
        required_password_message_element = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.required_message_password))

        required_password_message_text = required_password_message_element.text
        return required_password_message_text

    def get_invalid_message(self):
        required_invalid_message_element = WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((self.invalid_message)))

        invalid_message_text = required_invalid_message_element.text
        return invalid_message_text

    def get_login_successfull(self):
        # Wait for the dashboard element to be present on the page
        dashboard_element = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(self.dashboard)
        )

        # Check if the dashboard element is displayed
        if dashboard_element.is_displayed():
            print("Login successful")
            return True
        else:
            print("Login failed")
            return False




