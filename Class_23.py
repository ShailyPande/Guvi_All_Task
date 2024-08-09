from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()

driver.switch_to.frame(0)
drag = driver.find_element(By.XPATH,"//div[@id='draggable']")
drop = driver.find_element(By.XPATH,"//div[@id='droppable']")

actions = ActionChains(driver)

actions.drag_and_drop(drag,drop).perform()

time.sleep(5)

driver.quit()