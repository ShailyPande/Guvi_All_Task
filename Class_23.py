from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

# Launch the below URL
driver.get("https://jqueryui.com/droppable/")

# Maximize the window
driver.maximize_window()

# Switch to frame where elments are present
driver.switch_to.frame(0)

# locate the drage and drop elements
drag = driver.find_element(By.XPATH,"//div[@id='draggable']")
drop = driver.find_element(By.XPATH,"//div[@id='droppable']")

actions = ActionChains(driver)

# drop the dragged elment
actions.drag_and_drop(drag,drop).perform()

time.sleep(5)

driver.quit()
