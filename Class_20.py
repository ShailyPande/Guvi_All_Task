#1-Case Using Python Selenium and the URL https://www.cowin.gov.in/ you have to-
#Click on the Create "FAQ" and "Partner" anchor tag present on Home page and open two new window
#Now you have to fetch the opened Window /Frame ID and dispaly the same on the console
#Kindly close the two window and come back on home page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC

class cowin_site:
    def __init__(self,home_page):
        self.driver = None
        self.home_page_url = home_page
        self.home_window = None


    #launch the home page url and capture the home page window handle
    def driver_setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.home_page_url)
        self.home_window = self.driver.current_window_handle


    #Get the window handle of all the window
    def all_pages_window_handle(self):
        self.all_pages = self.driver.window_handles


    #Launch the FAQ page
    def faq_page(self):
        self.faq_link = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"(//a[contains(@href,'/faq')])")))
        self.faq_link.click()
        self.all_pages_window_handle()


    #Fetch the FAQ windlow frame ID
    def faq_window_handle(self):
        self.driver.switch_to.window(self.all_pages[0])
        self.faq_window = self.driver.current_window_handle
        print(f"The FAQ window handle is: {self.faq_window}")
        time.sleep(5)


    #Launch the Partner page
    def partner_page(self):
        self.partner_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(@href, '/our-partner')])")))
        self.partner_link.click()
        self.all_pages_window_handle()


    # Fetch the Partner windlow frame ID
    def partner_window_handle(self):
        self.driver.switch_to.window(self.all_pages[1])
        self.partner_window = self.driver.current_window_handle
        print(f"The Partner page frame ID is: {self.partner_window}")


    def return_to_home(self):
        for handle in self.all_pages:
            if handle != self.home_window:
                self.driver.switch_to.window(handle)
                self.driver.close()
        self.driver.switch_to.window(self.home_window)  # Switch back to the home page window
        print("Returned to the home page window.")


    #Close the window
    def close_window(self):
        self.driver.quit()



if __name__ == "__main__":
    test = cowin_site("https://www.cowin.gov.in/")
    test.driver_setup()
    test.faq_page()
    test.faq_window_handle()
    test.partner_page()
    test.partner_window_handle()
    #test.close_partner_window()
    #test.close_faq_window()
    test.return_to_home()
    test.close_window()

#2 Case-Using Python Selenium visit URL https://labour.gov.in/ and do the following tasks given below-
#1. Goto the Menu whose name is "Documents" and Download the Monthly Progress Report.
#2. Goto the Menu whose name is "Media" where you will find a sub menu whose name is "Photo Gallery" Your task is to download the 10 photos from the webpage
#and store them in a folder Kindly create the folder using Python only.


import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
import os


class labour_gov:
    def __init__(self, home_page):
        self.driver = None
        self.home_page_url = home_page

    def setup_chrome_option(self, download_dir=None):
        chrome_options = Options()
        chrome_options.add_argument("--incognito")  # Open Chrome in incognito mode
        chrome_options.add_experimental_option("prefs", {
            "plugins.always_open_pdf_externally": True,
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,  # Disable prompt for download
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        return chrome_options

    def driver_setup(self, chrome_options=None):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(self.home_page_url)
        self.driver.maximize_window()

    def Documents(self):
        self.action = ActionChains(self.driver)
        self.document_menu = self.driver.find_element(By.XPATH, '//*[@id="nav"]/li[7]/a')
        self.action.move_to_element(self.document_menu).perform()

    def Download_menu(self):
        self.download_menu_option = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()= 'Monthly Progress Report']")))
        self.download_menu_option.click()
        time.sleep(5)

    def Media(self):
        action = ActionChains(self.driver)
        self.media_menu = self.driver.find_element(By.XPATH, '//a[@href="/press-releases"][@title="labour"]')
        self.action.move_to_element(self.media_menu).perform()

    def Photo_Gallery(self):
        self.photo_gallery_menu_option = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href = '/photo-gallery']")))
        self.photo_gallery_menu_option.click()
        self.photo_gallery_menu_option = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "(//a[normalize-space()='Photo Gallery'])[2]")))
        href = self.photo_gallery_menu_option.get_attribute('href')
        # Wait for the page to load
        self.driver.get(href)
        time.sleep(5)
        window_after = self.driver.window_handles[-1]
        image_elements = self.driver.find_elements(By.XPATH, "//table//img")
        time.sleep(2)
        return image_elements

    def setup_download_directory(self):
        download_dir = os.path.join(os.getcwd(), "PhotoGallery")
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        return image_elements

    def extract_image_url(self, image_elements):
        self.image_urls = [element.get_attribute('src') for element in image_elements[:10]]

    def download_image(self, image_urls=None, download_dir=None):
        for i, url in enumerate(image_urls, 1):
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    with open(os.path.join(download_dir, f"image_{i}.jpg"), "wb") as f:
                        f.write(response.content)
                        print(f"Downloaded image {i}")
                else:
                    print(f"Failed to download image {i}")
            except Exception as e:
                print(f"Error occurred while downloading image {i}: {str(e)}")

    def close_window(self):
        self.driver.quit()


if __name__ == "__main__":
    test = labour_gov("https://labour.gov.in/")
    chrome_options = test.setup_chrome_option()
    test.driver_setup(chrome_options=chrome_options)
    test.Documents()
    test.Download_menu()
    test.Media()
    image_elements = test.Photo_Gallery()
    download_dir = test.setup_download_directory()
    image_urls = test.extract_image_url(image_elements)
    test.download_image(image_urls, download_dir)
    test.close_window()



