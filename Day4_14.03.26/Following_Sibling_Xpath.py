from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

# 1. Navigate to Amazon
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)

# //div[@class="group1.1"]/following-sibling::div

driver.quit()