from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

time.sleep(3)

#Login in page
user_name = driver.find_element(By.ID,"user-name")
password = driver.find_element(By.ID,"password")
login_btn = driver.find_element(By.ID,"login-button")

user_name.send_keys("standard_user")
password.send_keys("secret_sauce")
login_btn.click()

time.sleep(3)

#title of the web page
title_of_page= driver.title
print(title_of_page)

#current url of the web page
current_url_of_page = driver.current_url
print(current_url_of_page)

#Extract contents of the webpage and save it in a Text file whose name willbe "Webpage_task_txt_11.txt"
page_source = driver.page_source
with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(page_source)

# Close the browser
driver.quit()
