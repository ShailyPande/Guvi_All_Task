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

    def setup_chrome_option(self,download_dir= None):
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

    def driver_setup(self,chrome_options= None):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(self.home_page_url)
        self.driver.maximize_window()

    def Documents(self):
        self.action = ActionChains(self.driver)
        self.document_menu = self.driver.find_element(By.XPATH, '//*[@id="nav"]/li[7]/a')
        self.action.move_to_element(self.document_menu).perform()

    def Download_menu(self):
        self.download_menu_option = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH,"//a[normalize-space()= 'Monthly Progress Report']")))
        self.download_menu_option.click()
        time.sleep(5)

    def Media(self):
        action = ActionChains(self.driver)
        self.media_menu = self.driver.find_element(By.XPATH, '//a[@href="/press-releases"][@title="labour"]')
        self.action.move_to_element(self.media_menu).perform()

    def Photo_Gallery(self):
        self.photo_gallery_menu_option = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH,"//a[@href = '/photo-gallery']")))
        self.photo_gallery_menu_option.click()
        self.photo_gallery_menu_option = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "(//a[normalize-space()='Photo Gallery'])[2]")))
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

    def extract_image_url(self,image_elements):
        self.image_urls = [element.get_attribute('src') for element in image_elements[:10]]

    def download_image(self,image_urls = None,download_dir=None):
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
    test.driver_setup(chrome_options = chrome_options)
    test.Documents()
    test.Download_menu()
    test.Media()
    image_elements = test.Photo_Gallery()
    download_dir= test.setup_download_directory()
    image_urls = test.extract_image_url(image_elements)
    test.download_image(image_urls,download_dir)
    test.close_window()





