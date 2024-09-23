from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import basepage
from selenium.webdriver.support.ui import Select

class Personal_Detail_Page(basepage):

    def __init__(self, driver):
        super().__init__(driver)
        self.success_message_locator = (By.CSS_SELECTOR, "Successfully Saved")
        self.employee_personal_details_page_first_name = (By.XPATH, "//input[@class='oxd-input oxd-input--active orangehrm-firstname']")
        self.employee_personal_details_page_middle_name = (By.XPATH, "//input[@class='oxd-input oxd-input--active orangehrm-middlename']")
        self.employee_personal_page_details_last_name = (By.XPATH, "//input[@class='oxd-input oxd-input--active orangehrm-middlename']")
        self.personal_details_page_employee_id = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input')
        self.personal_details_page_other_id = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input')
        self.personal_details_page_driver_license_number = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[4]")
        #self.personal_details_page_first_save_button = (By.XPATH, "(//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'])[1]')")
        self.personal_details_page_nationality = (By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[1]")
        self.personal_details_page_marital_status = (By.XPATH,"(//div[@class='oxd-select-text oxd-select-text--active'])[2]")
        self.personal_details_page_male_gender = (By.XPATH, "//input[@type='radio' and @value='1']")
        self.personal_details_page_female_gender = (By.XPATH, "//input[@type='radio' and @value='2']")
        self.personal_details_page_License_Expiry_Date = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]")
        self.personal_details_page_date_of_birth = (By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[2]")
        self.personal_detail_page_blood_type = (By.XPATH, "(//div[@class ='oxd-select-wrapper'])[3]")

    def employee_list_page(self):
        self.click_element(self.employee_List_menu_locator)
        WebDriverWait(self.driver, 10).until(lambda driver: '/viewEmployeeList' in driver.current_url)

    def scroll_click_employee_by_id(self, employee_id, arguments=None, arugments=None, true=None):
        self.editing_employee_element_locator = (
        By.XPATH, f"//div[@class='oxd-table-body']//div[text()='{employee_id}']")
        self.driver.execute_script("arugments[0].scrollIntoView(true);", self.editing_employee_element_locator)
        self.editing_employee_element_locator.click()

    def clickonedit(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID, self.btnEditDetails_id))).click()


    def UpdateFirstName(self,firstname):
        self.driver.find_element(By.XPATH,self.employee_personal_details_page_first_name).clear()
        self.driver.find_element(By.XPATH,self.employee_personal_details_page_first_name).send_keys(firstname)

    def UpdateMiddleName(self, midname):
        self.driver.find_element(By.XPATH,self.employee_personal_details_page_middle_name).clear()
        self.driver.find_element(By.XPATH,self.employee_personal_details_page_middle_name).send_keys(midname)

    def UpdateLastName(self, lastname):
        self.driver.find_element(By.XPATH,self.employee_personal_page_details_last_name).clear()
        self.driver.find_element(By.XPATH,self.employee_personal_page_details_last_name).send_keys(lastname)

    def UpdateEmployeeID(self, empID):
         self.driver.find_element(By.XPATH,self.personal_details_page_employee_id).clear()
         self.driver.find_element(By.XPATH,self.personal_details_page_employee_id).send_keys(empID)

    def UpdateOtherID(self, otherID):
         self.driver.find_element(By.XPATH,self.personal_details_page_other_id).clear()
         self.driver.find_element(By.XPATH,self.personal_details_page_other_id).send_keys(otherID)

    def UpdateDriverLicenceNr(self, DLNumber):
        self.driver.find_element(By.XPATH,self.personal_details_page_driver_license_number).clear()
        self.driver.find_element(By.XPATH,self.personal_details_page_driver_license_number).send_keys(DLNumber)


    def UpdateLicenceExpireDate(self, ExpDate):
         self.driver.find_element(By.XPATH,self.personal_details_page_License_Expiry_Date).clear()
         self.driver.find_element(By.XPATH,self.personal_details_page_License_Expiry_Date).send_keys(ExpDate)


    def UpdateNationality(self,option):
        self.nationality_dropdown = Select(self.driver.find_element_by_id(self.personal_details_page_nationality))
        self.nationality_dropdown.select_by_visible_text(option)


    def UpdateMaritalStatus(self, Status):
        self.maritalstatus_dropdown = Select(self.driver.find_element_by_id(self.personal_details_page_marital_status))
        self.maritalstatus_dropdown.select_by_visible_text(Status)


    def UpdateDob(self, DOBDate):
        self.driver.find_element(By.XPATH,self.personal_details_page_date_of_birth).clear()
        self.driver.find_element(By.XPATH,self.personal_details_page_date_of_birth).send_keys(DOBDate)


    def UpdateGender(self, gender):
        if gender.lower() == "male":
            self.driver.find_element(By.XPATH,self.personal_details_page_male_gender).click()
        elif gender.lower() == "female":
            self.driver.find_element(By.XPATH,self.personal_details_page_female_gender).click()
        else:
            self.driver.find_element_by_id(self.personal_details_page_male_gender).click()
    


    def personal_details_page_save_button(self):
        self.click_element(self.personal_details_save_button, 10)
        success_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.success_message_locator))

        assert success_message.text == "Successfully Saved"




