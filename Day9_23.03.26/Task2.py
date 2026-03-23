# Task 2
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get("https://www.myntra.com/")
driver.maximize_window()

wait= WebDriverWait(driver, 10)

action = ActionChains(driver)

category = wait.until(EC.element_to_be_clickable((By.XPATH,'(//div[@class="desktop-navLink"])[2]')))
sleep(2)

action.move_to_element(category).perform()
sleep(1)

collection = wait.until(EC.element_to_be_clickable((By.XPATH,'//li[@data-reactid="212"]')))
collection.click()
sleep(2)

for i in range(0,5):
    action.send_keys(Keys.PAGE_DOWN).perform()
    sleep(2)

print("Task Completed!")

driver.quit()
sleep(3)

