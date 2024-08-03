from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

time.sleep(5)

cookies_before_login = driver.get_cookies()
print("cookies before login:")

for cookie in cookies_before_login:
    print(cookie)


user_name = driver.find_element(By.ID,"user-name")
password = driver.find_element(By.ID,"password")
login_btn = driver.find_element(By.ID,"login-button")

user_name.send_keys("standard_user")
password.send_keys("secret_sauce")
login_btn.click()

time.sleep(3)

cookies_after_login = driver.get_cookies()
print("cookies after login:")

for cookie in cookies_after_login:
    print(cookie)

hamburger_menu = driver.find_element(By.ID,"react-burger-menu-btn")
hamburger_menu.click()

time.sleep(3)

logout_btn = driver.find_element(By.ID,"logout_sidebar_link")
logout_btn.click()

driver.quit()