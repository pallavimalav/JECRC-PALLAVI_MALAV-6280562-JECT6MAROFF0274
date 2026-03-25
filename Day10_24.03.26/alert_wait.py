import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# action = ActionChains(driver)
driver.maximize_window()

sleep(3)

# switching to alert using waits

wait = WebDriverWait(driver, 10)

driver.find_element(By.XPATH,'//button[@onclick="jsAlert()"]').click()

alert = wait.until(EC.alert_is_present())
sleep(3)
alert.accept()
sleep(3)

driver.quit()
