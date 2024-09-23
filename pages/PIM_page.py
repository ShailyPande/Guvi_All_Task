from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import basepage

class PIM_Page(basepage):

    def __init__(self, driver):
        super().__init__(driver)  # Call the basepage
        self.add_button_locator = (By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']")
        self.PIM_element_locator = (By.XPATH, '//a[@href="/web/index.php/pim/viewPimModule"]')
        self.first_name_locator = (By.XPATH,"//input[@name='firstName']")
        self.middle_name_locator = (By.XPATH, "//input[@name='middleName']")
        self.last_name_locator = (By.XPATH, "//input[@name='lastName']")
        self.employee_id_locator= (By.XPATH,"(//input[contains(@class, 'oxd-input oxd-input--active')])[1]")
        self.save_button_locator = (By.XPATH, "//button[contains(@type, 'submit')]")
        self.cancel_button_locator = (By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--ghost']")
        self.success_message_locator = (By.CSS_SELECTOR, "Successfully Saved")
        self.employee_List_menu_locator = (By.XPATH,"//a[text()= 'Employee List']")
        self.delete_confirmation_popup = (By.XPATH,'//div[@class ="oxd-sheet oxd-sheet--rounded oxd-sheet--white oxd-dialog-sheet oxd-dialog-sheet--shadow oxd-dialog-sheet--gutters orangehrm-dialog-popup"]')
        self.delete_popup_No_button = (By.XPATH,'//button[text()=" No, Cancel "]')
        self.delete_popup_Yes_button = (By.XPATH, '//button[text()=" Yes, Delete "]')
        self.delete_message_locator = (By.CSS_SELECTOR, "Successfully Deleted")



    def PIM_elemnet_click(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.PIM_element_locator)).click()


    def add_button_clcik(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.add_button_locator)).click()


    def PIM_page_add_detail(self,first_name,middle_name,last_name,employee):
        expected_url_part = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee"
        WebDriverWait(self.driver, 10).until(lambda d: expected_url_part in d.current_url)

        self.enter_text(self.first_name_locator,first_name,10)
        self.enter_text(self.middle_name_locator,middle_name,10)
        self.enter_text(self.last_name_locator, last_name, 10)
        #self.employee_id_locator.clear()
        self.enter_text(self.employee_id_locator,employee,10)


    def PIM(self,first_name,middle_name,last_name,employee):
        self.PIM_element_click()
        self.add_button_clcik()
        self.PIM_page_add_detail(first_name,middle_name,last_name,employee)


    def save_button_click(self):

        self.click_element(self.save_button_locator)
        # Wait for the success message to appear
        success_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.success_message_locator))

        assert success_message.text == "Successfully Saved"

        # Wait for the page to redirect to 'Personal Details' section
        WebDriverWait(self.driver, 10).until(lambda driver: '/viewPersonalDetails' in driver.current_url)
        assert '/viewPersonalDetails' in self.driver.current_url, "the user details saved successfully"


    def cancel_button_click(self):

        self.click_element(self.cancel_button_locator)
        WebDriverWait(self.driver, 10).until(lambda driver: '/viewEmployeeList' in driver.current_url)
        assert '/viewEmployeeList' in self.driver.current_url, "the user cancel to add data "


    def employee_list_page(self):
        self.click_element(self.employee_List_menu_locator)
        WebDriverWait(self.driver, 10).until(lambda driver: '/viewEmployeeList' in driver.current_url)


    def scroll_click_employee_by_id(self, employee_id, arguments=None, true=None):
        self.editing_employee_element_locator = (By.XPATH, f"//div[@class='oxd-table-body']//div[text()='{employee_id}']")
        self.driver.execute_script("arugments[0].scrollIntoView(true);",self.editing_employee_element_locator)
        self.editing_employee_element_locator.click()


    def update_details(self,first_name,middle_name,last_name,other_id):
        self.enter_text(self.employee_personal_details_page_first_name,first_name,10)
        self.enter_text(self.employee_personal_details_page_middle_name,middle_name,10)
        self.enter_text( self.employee_personal_page_details_last_name, middle_name, 10)
        self.enter_text(self.personal_details_other_id, other_id, 10)
        self.enter_text(self.personal_details_driver_license_number, other_id, 10)


    
    def personal_details_page_save_button(self):
        self.click_element(self.personal_details_save_button, 10)
        success_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.success_message_locator))

        assert success_message.text == "Successfully Saved"

    def scroll_delete_employee_data(self, employee_id, arguments=None, true=None):
        self.editing_employee_element_locator = (By.XPATH, f"//div[@class='oxd-table-body']//div[text()='{employee_id}']")
        self.driver.execute_script("arugments[0].scrollIntoView(true);",self.editing_employee_element_locator)

    def delete_click_existing_employee(self,employee_id):
        self.delete_button_locator = (By.XPATH, f"//div[@class ='oxd-table-cell oxd-padding-cell']//div[text()='{employee_id}']")
        self.click_element(self.delete_button_locator,10)


    def delete_confirmation(self):
        self.click_element(self.delete_confirmation_popup,10)


    def click_No_popup(self):
        self.click_element(self.delete_popup_No_button,10)


    def click_yes_popup(self):
        self.click_element(self.delete_popup_Yes_button,10)


    def delete_successfull_message(self):
        success_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.success_delete_message_locator))

        assert success_message.text == "Successfully Deleted"


