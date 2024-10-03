from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Pages.base_page import BasePage
import time


class ForgotPassword(BasePage):

    def __init__(self,driver,url):
        super().__init__(driver, url)
        self.driver=driver
        self.url = url
        self.forgot_your_password_link = (By.XPATH,"//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")
        self.username_reset_password_popup = (By.XPATH,"//input[@class='oxd-input oxd-input--active']")
        self.reset_password_button = (By.XPATH,"//button[@class='oxd-button oxd-button--large oxd-button--secondary orangehrm-forgot-password-button orangehrm-forgot-password-button--reset']")
        self.cancel_reset_password_button = (By.XPATH, "oxd-button oxd-button--large oxd-button--ghost orangehrm-forgot-password-button orangehrm-forgot-password-button--cancel")
        self.reset_password_successfully_message = (By.XPATH,"//h6[text()='Reset Password link sent successfully']")
        self.login_button = (By.XPATH, '//button[@type="submit"]')

    def click_forgot_password_link(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.forgot_your_password_link))
        self.click_element(self.forgot_your_password_link,20)

    def enter_username_on_popup(self, username):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.username_reset_password_popup)).send_keys(username)


    def click_resetPassword_button(self):
        WebDriverWait(self.driver,20).until((EC.element_to_be_clickable(self.reset_password_button))).click()


    def perform_forgot_password(self,username):
        self.launch_url(20)
        self.click_forgot_password_link()
        self.enter_username_on_popup(username)
        time.sleep(20)
        self.click_resetPassword_button()


    # def click_cancel_button(self):
    #     WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.cancel_reset_password_button)).click()



    def reset_password_successfull(self):


        try:
            reset_password_successfully_message = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.reset_password_successfully_message))
            if reset_password_successfully_message.is_displayed():
                return "Password Reset done successfuly"

        except TimeoutException:


            return "Unknown error occurred during login"





