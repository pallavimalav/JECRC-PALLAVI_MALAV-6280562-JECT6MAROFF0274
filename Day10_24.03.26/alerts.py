# handling alerts with automation
# simple alert : only accepts
# confirmation alert : accept & dismiss
# prompt alert : accept, dismiss, and send keys


import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# from selenium.webdriver.common.action_chains import ActionChains
#
# folder = os.path.join(os.getcwd(),'alert')
# os.makedirs(folder,exist_ok=True)

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# action = ActionChains(driver)
driver.maximize_window()

sleep(3)

# simple alert
driver.find_element(By.XPATH,'//button[@onclick="jsAlert()"]').click()
sleep(3)
alert = driver.switch_to.alert
alert.accept()
sleep(3)

# confirmation alert
driver.find_element(By.XPATH,'//button[@onclick="jsConfirm()"]').click()
sleep(3)
alert = driver.switch_to.alert
# alert.accept()
alert.dismiss()
sleep(3)

# prompt alert
driver.find_element(By.XPATH,'//button[@onclick="jsPrompt()"]').click()
sleep(3)
alert = driver.switch_to.alert
alert.send_keys("mametaro")
# action.pause(3).perform()
sleep(3)
alert.accept()
# alert.dismiss()
sleep(3)

