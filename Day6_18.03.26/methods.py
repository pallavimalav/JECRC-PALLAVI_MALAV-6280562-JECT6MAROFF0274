from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()

driver.maximize_window()
sleep(3)

driver.get("https://testautomationpractice.blogspot.com/")

name = driver.find_element(By.ID, 'name')
name.clear()
name.send_keys('lavi-lavi')
sleep(1)

email = driver.find_element(By.XPATH, '//input[@placeholder="Enter EMail"]')
email.send_keys('email@yahoo.in')
sleep(3)

print(name.get_attribute('placeholder'))
print(email.get_attribute('value'))

male=driver.find_element(By.ID, 'male')
male.click()
# is displayed
print(male.is_displayed())
# is enabled : is only for buttons
print(male.is_enabled())


check = driver.find_element(By.XPATH,'//label[text()="Monday"]/preceding-sibling::input')
check.click()
print(check.is_selected())
# to print the inner text we use text
monday_checkbox = driver.find_element(By.XPATH,'//input[@id="monday"]/following-sibling::label')
print(monday_checkbox.text)
# is selected
# print(check.is_selected())


driver.quit()
