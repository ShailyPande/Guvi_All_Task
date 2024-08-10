from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Guvi_Instagram:
    def __init__(self,url):
        self.driver = None
        self.url = f"https://www.instagram.com/guviofficial/"  #define the instram page url

    def setup_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def find_followers_and_following(self):  #launch the given url
        self.driver.get(self.url)

        following = self.driver.find_element(By.XPATH, "//*[text()=' following']").text  #locate the element to get the following count 
        followers = self.driver.find_element(By.XPATH, "//*[text()=' followers']").text  #locate the element to get the followers count

        print(f" the number of following: {following}")  # print the number of following
        print(f" the number of followers: {followers}")  # print the number of followers

    def close_window(self):   # function to close the window
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
