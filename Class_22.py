from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Guvi_Instagram:
    def __init__(self,url):
        self.driver = None
        self.url = f"https://www.instagram.com/guviofficial/"

    def setup_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def find_followers_and_following(self):
        self.driver.get(self.url)

        following = self.driver.find_element(By.XPATH, "//*[text()=' following']").text
        followers = self.driver.find_element(By.XPATH, "//*[text()=' followers']").text

        print(f" the number of following: {following}")
        print(f" the number of followers: {followers}")

    def close_window(self):
        self.driver.quit()

    def run(self):
        self.setup_driver()
        try:
            self.find_followers_and_following()
        finally:
            self.close_window()

if __name__ == "__main__":
    guvi = Guvi_Instagram("guviofficial")
    guvi.run()
