from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Pages.base_page import BasePage
import time


class AdminPage(BasePage):


    def __init__(self, driver,url):
        super().__init__(driver, url)
        self.url = url
        self.driver = driver
        #Admin Page Headers
        self.User_Management_locator = (By.XPATH,'//li[@class="oxd-topbar-body-nav-tab --parent --visited"]')
        self.Job_locator = (By.XPATH,'//li[@class="oxd-topbar-body-nav-tab --parent"]//span[text()="Job "]')
        self.Organization_locator = (By.XPATH,'//li[@class="oxd-topbar-body-nav-tab --parent"]//span[text()="Organization "]')
        self.Qualification_locator = (By.XPATH, '// li[ @class ="oxd-topbar-body-nav-tab --parent"] // span[text()="Qualifications "]')
        self.Nationalities_locator = (By.XPATH, '//li[@class="oxd-topbar-body-nav-tab"]//a[text()="Nationalities"]')
        self.Corporate_Banding_locator = (By.XPATH, '//li[@class="oxd-topbar-body-nav-tab"]//a[text()="Corporate Branding"]')
        self.Configuration_locator = (By.XPATH, '//li[@class="oxd-topbar-body-nav-tab --parent"]//span[text()="Configuration "]')
        #Admin Page side Menu
        self.Admin_locator = (By.XPATH, '//a[@href="/web/index.php/admin/viewAdminModule"]')
        self.PIM_element = (By.XPATH,'//a[@href="/web/index.php/pim/viewPimModule"]')
        self.Leave_element = (By.XPATH,'//a[@href="/web/index.php/leave/viewLeaveModule"]')
        self.Time_element = (By.XPATH,'//a[@href="/web/index.php/time/viewTimeModule"]')
        self.Recruitment_element = ((By.XPATH,'//a[@href="/web/index.php/recruitment/viewRecruitmentModule"]'))
        self.MyInfo_element = ((By.XPATH, '//a[@href="/web/index.php/pim/viewMyDetails"]'))
        self.Performance_element = ((By.XPATH, '//a[@href="/web/index.php/performance/viewPerformanceModule"]'))
        self.Dashboard_element = ((By.XPATH, '//a[@href="/web/index.php/dashboard/index"]'))
        self.Directory_element = ((By.XPATH, '//a[@href="/web/index.php/directory/viewDirectory"]'))
        self.Maintenance_element = ((By.XPATH, '//a[@href="/web/index.php/maintenance/viewMaintenanceModule"]'))
        self.Claim_element = ((By.XPATH, '//a[@href="/web/index.php/claim/viewClaimModule"]'))
        self.Buzz_element = ((By.XPATH, '//a[@href="/web/index.php/buzz/viewBuzz"]'))


    def click_Admin(self):
        self.Admin = WebDriverWait(self.driver,20).until(EC.presence_of_element_located(self.Admin_locator))
        self.Admin.click()


    def check_page_title(self):
        return self.verify_page_title("OrangeHRM")


    def check_adminpage_all_headers_displayed(self):

        try:
            WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.User_Management_locator))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.Job_locator))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.Organization_locator))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.Qualification_locator))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.Nationalities_locator))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.Corporate_Banding_locator))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.Configuration_locator))

            return  "All admin page headers are displayed."

        except TimeoutException:
            return False


    def check_adminpage_all_menu_displayed(self):


        try:
            WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.Admin_locator))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.PIM_element))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.Leave_element))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.Time_element))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.Recruitment_element))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.MyInfo_element))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.Performance_element))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.Dashboard_element))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.Directory_element))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.Maintenance_element))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.Claim_element))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.Buzz_element))

            return "All admin page menu are displayed."

        except TimeoutException:
            return False















