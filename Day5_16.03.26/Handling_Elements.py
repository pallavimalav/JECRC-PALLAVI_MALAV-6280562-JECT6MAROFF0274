from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

name = driver.find_element(By.ID, 'name')
name.clear()
name.send_keys('lavi-lavi')
sleep(1)

email = driver.find_element(By.XPATH, '//input[@placeholder="Enter EMail"]')
email.send_keys('email@yahoo.in')
sleep(3)

print(name.get_attribute('placeholder'))
print(email.get_attribute('value'))

driver.quit()


