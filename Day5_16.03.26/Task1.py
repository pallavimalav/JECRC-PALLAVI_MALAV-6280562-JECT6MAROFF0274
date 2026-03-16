# Task 1

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()

print("Page Title:", driver.title)

time.sleep(3)

username = driver.find_element(By.NAME, "username")
username.clear()

username.send_keys("Admin")

password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

time.sleep(5)

current_url = driver.current_url
print("Current URL:", current_url)

if "dashboard" in current_url:
    print("Successful Login")

driver.quit()