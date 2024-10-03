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
        self.error_message = (By.XPATH, '//div[@class="oxd-alert-content oxd-alert-content--error"]')
        self.dashboard = (By.XPATH, "//span[text()='Dashboard']")
        self.required_message_username = (By.XPATH,'//span[@class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message" and text()="Required"]')
        self.required_message_password = (By.XPATH,'(//span[text()="Required"]')

    def enter_username(self, username):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.username_field)).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.password_field)).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.login_button)).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.dashboard))


    def perform_login(self, username, password):
        self.launch_url()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(self.username_field))
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_message(self):
        try:
            # Check if login is successful by looking for the dashboard element
            WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(self.dashboard))
            return "Login successful"
        except TimeoutException:
            pass  # If the dashboard isn't found, continue to check for errors

        try:
            # Check if the "Required" message is displayed for empty username field
            required_message_username = WebDriverWait(self.driver, 40).until(
                EC.visibility_of_element_located(self.required_message_username))
            if required_message_username.is_displayed():
                return "Required field error:  user name field is required"
        except TimeoutException:
            pass  # If no 'Required' message, continue to check for invalid credential errors


        try:
            # Check if the "Required" message is displayed for empty password fields
            required_message_password = WebDriverWait(self.driver, 40).until(
                EC.visibility_of_element_located(self.required_message_password))
            if required_message_password.is_displayed():
                return "Required field error:  password field is required"
        except TimeoutException:
            pass


        try:
            error_message= WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(self.error_message))
            if error_message.is_displayed():
                return "Invalid credentials: Please check your username and password"
        except TimeoutException:
            pass

        return "Unknown error occurred during login"


