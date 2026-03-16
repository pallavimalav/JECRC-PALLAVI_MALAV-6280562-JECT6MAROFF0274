# Task 2

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/radio-button")

driver.maximize_window()

time.sleep(2)

print("Page Title:", driver.title)

yes_radio = driver.find_element(By.XPATH, "//label[@for='yesRadio']")

yes_radio.click()

time.sleep(2)

result = driver.find_element(By.CLASS_NAME, "text-success")
print("Result Message:", result.text)

class_attr = yes_radio.get_attribute("class")
id_attr = yes_radio.get_attribute("for")

print("Class Attribute:", class_attr)
print("ID Attribute:", id_attr)

print("Current URL:", driver.current_url)

driver.quit()