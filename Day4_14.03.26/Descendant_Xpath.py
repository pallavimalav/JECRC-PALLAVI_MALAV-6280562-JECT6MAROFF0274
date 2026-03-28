from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

# 1. Navigate to Amazon
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)

# //div[@id="nav-main"]/descendant::span[text()="All"]

# Descendant XPath
All = driver.find_element(By.XPATH,'//div[@id="nav-main"]/descendant::span[text()="All"]')
print(All)
print('All-option found')

driver.quit()


